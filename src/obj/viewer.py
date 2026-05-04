import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

class Viewer(tk.Frame):
	def __init__(self, root, dashboard, loop):
		super().__init__(root)
		self.root = root
		self.dashboard = dashboard
		self.loop = loop

		self.width = 0
		self.height = 0
		self.reports = []
		self.rview = None

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

	def get_reports(self):
		return self.reports

	def set_reports(self, reports):
		self.reports = reports

	def add_report(self, report):
		self.get_reports().append(report)

	def get_rview(self):
		return self.rview

	def set_rview(self, rview):
		self.rview = rview

	def throw_exec(self, mes):
		if (mes == 'cust'):
			print('[ERR] Error customizing viewer.')
		elif (mes == 'place'):
			print('[ERR] Error placing viewer.')
		elif (mes == 'line'):
			print('[ERR] Error adding line to viewer.')
		elif (mes == 'clear'):
			print('[ERR] Error clearing viewer content.')

	async def reset(self):
		await self.clear_lines()
		await self.add_line('[-->] Select a mode.')


	async def clear_lines(self):
		try:
			self.get_rview().config(state=tk.NORMAL)
			self.get_rview().delete('1.0', tk.END)
			self.get_rview().config(state=tk.DISABLED)
		except Exception as ex:
			print(ex)
			self.throw_exec('clear')

	async def add_line(self, line):
		try:
			self.get_rview().config(state=tk.NORMAL)
			self.get_rview().insert(tk.END, line + '\n')
			self.get_rview().config(state=tk.DISABLED)
		except Exception as ex:
			print(ex)
			self.throw_exec('line')

	async def config(self, which):
		if (which == 'test'):
			await self.clear_lines()
			await self.add_line('[-->] Test Mode.')
			await self.add_line('')
			await self.add_line('Start by selecting a model to analyze and test.')
		elif (which == 'train'):
			await self.clear_lines()
			await self.add_line('[-->] Train Mode.')
			await self.add_line('')
			await self.add_line('Start by selecting your datasets.')

	def place(self, row, col):
		try:
			self.grid(row=row, column=col)
		except Exception as ex:
			print(ex)
			self.throw_exec('place')

	async def customize(self):
		try:
			self.set_width(65)
			self.set_height(4)
			self.set_rview(scrolledtext.ScrolledText(self,
										wrap='word',
										width=self.get_width(),
										height=self.get_height(),
										bg='gray80',
										state='disabled'))
			self.get_rview().grid(row=0, column=0)
			await self.add_line('[-->] Select a mode.')
		except Exception as ex:
			print(ex)
			self.throw_exec('cust')