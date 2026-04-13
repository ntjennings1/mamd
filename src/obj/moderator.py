import tkinter as tk

class Moderator(tk.Frame):
	def __init__(self, root, dashboard, loop):
		super().__init__(root)
		self.root = root
		self.dashboard = dashboard
		self.loop = loop

		self.width = 200
		self.height = 600

		self.content = None
		self.options = ['Select an option ...']
		self.oselctor = None

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

	def get_options(self):
		return self.options

	def set_option(self, options):
		self.optins = options 

	def add_options(self, options):
		self.get_options().append(option)

	def get_oselector(self):
		return self.oselector

	def set_oselector(self, oselector):
		self.oselector = oselector

	def throw_exec(self, mes):
		if (mes == 'cust'):
			print('[ERR] Error customizing moderator.')

	def place(self, row, col):
		self.grid(row=row, column=col)

	async def customize(self):
		try:
			self.set_content(tk.Frame(self,
										width=400,
										height=400,
										bg='gray'))
			self.get_content().grid(row=0, column=0)
		except Exception as ex:
			print(ex)
			self.throw_exec('cust')
