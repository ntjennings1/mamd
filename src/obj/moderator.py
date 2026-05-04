import tkinter as tk
from tkinter import ttk

class Moderator(tk.Frame):
	def __init__(self, root, dashboard, loop, **kwargs):
		super().__init__(root, **kwargs)
		self.root = root
		self.dashboard = dashboard
		self.loop = loop

		self.width = 0
		self.height = 0
		self.options = ['Select an option ...']
		self.oselector = None

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
			self.set_width(400)
			self.set_height(400)
			self.config(width=self.get_width(),
						height=self.get_height(),
						bg='gray80')
			self.grid_propagate(False)
			self.grid_columnconfigure(0, weight=1)

			self.set_oselector(ttk.Combobox(self,
											values=self.get_options(),
											state='readonly'))
			self.get_oselector().grid(row=0, column=0, sticky='ew')

		except Exception as ex:
			print(ex)
			self.throw_exec('cust')
