import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

class Viewer(tk.Frame):
	def __init__(self, root, dashboard, loop):
		super().__init__(root)
		self.root = root
		self.dashboard = dashboard
		self.loop = loop

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

	def place(self, row, col):
		self.grid(row=row, column=col)

	async def customize(self):
		try:
			self.set_rview(scrolledtext.ScrolledText(self,
										wrap='word',
										width=75,
										height=5,
										bg='gray'))
			self.get_rview().grid(row=0, column=0)
		except Exception as ex:
			print(ex)
			self.throw_exec('cust')