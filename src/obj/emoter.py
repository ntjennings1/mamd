import tkinter as tk
from tkinter import filedialog

class Emoter(tk.Frame):
	def __init__(self, root, dashboard, loop):
		super().__init__(root)
		self.root = root
		self.dashboard = dashboard
		self.loop = loop

		self.width = 0
		self.height = 0
		self.content = None
		self.logo_section = None
		self.section_label = None

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

	def get_content(self):
		return self.content

	def set_content(self, content):
		self.content = content

	def get_lsection(self):
		return self.logo_section

	def set_lsection(self, lsection):
		self.logo_section = lsection

	def get_slabel(self):
		return self.section_label

	def set_slabel(self, slabel):
		self.section_label = slabel

	def throw_exec(self, mes):
		if (mes == 'cust'):
			print('[ERR] Error customizing emoter.')
		elif (mes == 'place'):
			print('[ERR] Error placing emoter.')
		elif (mes == 'emote'):
			print('[ERR] Error emoting.')
		elif (mes == 'file'):
			print('[ERR] Error fetching model.')
		elif (mes == 'res'):
			print('[ERR] Error resetting emoter.')

	async def reset(self):
		try:
			if (self.get_lsection() != None):
				self.get_lsection().grid_forget()
				self.get_lsection().destroy()
				self.set_lsection(None)

			if (self.get_slabel() != None):
				self.get_slabel().grid_forget()
				self.get_slabel().destroy()
				self.set_slabel(None)

		except Exception as ex:
			print(ex)
			self.throw_exec('res')

	async def emote(self, which):
		try:
			
			if (which == 'fu'):
				def fu(event):
					try:
						filepath = filedialog.askopenfilename(
							title="Select a model",
							filetypes=[("All Files", ".onnx")]
						)
						if filepath:
							self.get_dashboard().get_model().set_path(filepath)
							self.get_loop().create_task(self.get_dashboard().get_model().eval())
					except Exception as ex:
						print(ex)
						self.throw_exec('file')

				self.set_lsection(tk.Label(self.get_content(),  bg="gray80", image=self.get_dashboard().get_window().get_fulogo()))
				self.get_lsection().bind("<Button-1>", fu)
				self.get_lsection().grid(row=0, column=0)

				self.set_slabel(tk.Label(self.get_content(), bg='gray80', text='Click to select a file'))
				self.get_slabel().grid(row=1, column=0)

			elif (which == 'aps'):
				self.set_lsection(tk.Frame(self.get_content(),
											bg='gray80'))
				self.get_lsection().grid(row=0, column=0)

				gr_label = tk.Label(self.get_lsection(), bg='gray80', image=self.get_dashboard().get_window().get_grlogo())
				gr_label.grid(row=0, column=0)

				p_label = tk.Label(self.get_lsection(), bg='gray80', image=self.get_dashboard().get_window().get_plogo())
				p_label.grid(row=0, column=1)
				p_label.grid_configure(padx=(50,50))

				a_label = tk.Label(self.get_lsection(), bg='gray80', image=self.get_dashboard().get_window().get_alogo())
				a_label.grid(row=0, column=2)

		except Exception as ex:
			print(ex)
			self.throw_exec('emote')

	def place(self, row, col):
		try:
			self.grid(row=row, column=col)
		except Exception as ex:
			print(ex)
			self.throw_exec('place')

	async def customize(self):
		try:
			self.set_width(600)
			self.set_height(400)
			self.config(width=self.get_width(),
						height=self.get_height(),
						bg='gray80')
			self.grid_propagate(False)

			self.set_content(tk.Frame(self,
										width=self.get_width(),
										height=self.get_height(),
										bg='gray80'))
			self.get_content().grid(row=0, column=1)
			self.get_content().grid_propagate(False)
			self.get_content().grid_columnconfigure(0, weight=1)
			self.get_content().grid_rowconfigure(0, weight=1)

		except Exception as ex:
			print(ex)
			self.throw_exec('cust')
