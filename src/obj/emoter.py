import tkinter as tk

class Emoter(tk.Frame):
	def __init__(self, root, dashboard, loop):
		super().__init__(root)
		self.root = root
		self.dashboard = dashboard
		self.loop = loop

		self.content = None

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

	def get_content(self):
		return self.content

	def set_content(self, content):
		self.content = content

	def throw_exec(self, mes):
		if (mes == 'cust'):
			print('[ERR] Error customizing emoter.')

	def place(self, row, col):
		self.grid(row=row, column=col)

	async def customize(self):
		try:
			self.set_content(tk.Frame(self,
										width=600,
										height=400,
										bg='gray'))
			self.get_content().grid(row=0, column=0)
		except Exception as ex:
			print(ex)
			self.throw_exec('cust')
