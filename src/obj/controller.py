import tkinter as tk

class Controller(tk.Frame):
	def __init__(self, root, dashboard, loop):
		super().__init__(root)
		self.root = root
		self.dashboard = dashboard
		self.loop = loop

		self.width = 200
		self.height = 600

		self.buttons = []
		self.stop_button = None
		self.reset_button = None
		self.train_button = None
		self.test_button = None

	def get_root(self):
		return self.root

	def set_root(self, root):
		self.root = root

	def get_dashboard(self):
		return self.dashboard

	def set_dashboard(self, dashboard):
		self.dashboard = dashboard

	def get_loop(self):
		return self.loop

	def set_loop(self, loop):
		self.loop = loop

	def get_width(self):
		return self.width

	def set_width(self, width):
		self.width = width

	def get_height(self):
		return self.height

	def set_height(self, height):
		self.height = height

	def get_tbutton(self):
		return self.train_button

	def set_tbutton(self, tbutton):
		self.train_button = tbutton

	def get_tsbutton(self):
		return self.test_button

	def set_tsbutton(self, tbutton):
		self.test_button = tbutton

	def get_sbutton(self):
		return self.stop_button

	def set_sbutton(self, sbutton):
		self.stop_button = sbutton

	def get_rbutton(self):
		return self.reset_button

	def set_rbutton(self, rbutton):
		self.reset_button = rbutton

	def throw_exec(self, mes):
		if (mes == 'cust'):
			print('[ERR] Error customizing controller elements.')
		elif (mes == 'place'):
			print('[ERR] Error placing controller.')
		elif (mes == 'test'):
			print('[ERR] Error performing test sequence.')
		elif (mes == 'train'):
			print('[ERR] Error performing train sequence.')
		elif (mes == 'reset'):
			print('[ERR] Error resetting controller.')

	async def reset(self):
		try:
			self.get_dashboard().set_mode('')
			self.get_tbutton().config(bg='chartreuse3',
										state=tk.NORMAL)
			self.get_tsbutton().config(bg='gold',
										state=tk.NORMAL)
			self.get_rbutton().config(bg='gray80',
										state=tk.DISABLED)
			self.get_sbutton().config(bg='gray80',
										state=tk.DISABLED)
			await self.get_dashboard().get_window().get_viewer().reset()
			await self.get_dashboard().get_window().get_emoter().reset()
			await self.get_dashboard().reset()
		except Exception as ex:
			print(ex)
			self.throw_exec('reset')

	async def train(self):
		try:
			await self.get_dashboard().get_window().config('train')
		except Exception as ex:
			print(ex)
			self.throw_exec('train')

	async def test(self):
		try:
			await self.get_dashboard().get_window().config('test')

		except Exception as ex:
			print(ex)
			self.throw_exec('test')

	async def config(self, which):
		try:
			if (which == 'test'):
				self.get_tbutton().config(bg='gray80',
											state=tk.DISABLED)
				self.get_tsbutton().config(state=tk.DISABLED)
				self.get_rbutton().config(bg='SteelBlue1',
											state=tk.NORMAL)
				'''self.get_sbutton().config(bg='brown2',
											state=tk.NORMAL)'''
			if (which == 'train'):
				self.get_tbutton().config(state=tk.DISABLED)
				self.get_tsbutton().config(bg='gray80',
											state=tk.DISABLED)
				self.get_rbutton().config(bg='SteelBlue1',
											state=tk.NORMAL)
				'''self.get_sbutton().config(bg='brown2',
											state=tk.NORMAL)'''

		except Exception as ex:
			print(ex)
			self.throw_exec('test')	

	def place(self, row, col):
		try:
			self.grid(row=row, column=col)
		except Exception as ex:
			print(ex)
			self.throw_exec('place')

	async def customize(self):
		try:
			self.set_tbutton(tk.Button(self,
										width=7,
										height=2,
										state='normal',
										text='Train',
										bg='chartreuse3',
										fg='black',
										activebackground='chartreuse3',
										activeforeground='black',
										highlightbackground='black',
										highlightcolor='black',
										highlightthickness=1,
										relief='solid',
										borderwidth=1,
										command=lambda:self.get_loop().create_task(self.train())))
			self.get_tbutton().grid(row=0, column=0)
			self.set_tsbutton(tk.Button(self,
										width=7,
										height=2,
										state='normal',
										text='Test',
										bg='gold',
										fg='black',
										activebackground='gold',
										activeforeground='black',
										highlightbackground='black',
										highlightcolor='black',
										highlightthickness=1,
										relief='solid',
										borderwidth=1,
										command=lambda:self.get_loop().create_task(self.test())))
			self.get_tsbutton().grid(row=0, column=1)
			self.set_rbutton(tk.Button(self,
										width=7,
										height=2,
										state='disabled',
										text='Reset',
										bg='gray80',
										fg='black',
										activebackground='SteelBlue1',
										activeforeground='black',
										highlightbackground='black',
										highlightcolor='black',
										highlightthickness=1,
										relief='solid',
										borderwidth=1,
										command=lambda:self.get_loop().create_task(self.reset())))
			self.get_rbutton().grid(row=0, column=2)
			self.set_sbutton(tk.Button(self,
										width=7,
										height=2,
										state='disabled',
										text='Stop',
										bg='gray80',
										fg='black',
										activebackground='brown1',
										activeforeground='black',
										highlightbackground='black',
										highlightcolor='black',
										highlightthickness=1,
										relief='solid',
										borderwidth=1,
										command=lambda:self.get_loop().create_task(self.reset())))
			self.get_sbutton().grid(row=0, column=3)
		except Exception as ex:
			print(ex)
			self.throw_exec('cust')
