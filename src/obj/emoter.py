import tkinter as tk
from tkinter import filedialog

class Emoter(tk.Frame):
	def __init__(self, root, dashboard, loop):
		super().__init__(root)
		self.root = root
		self.dashboard = dashboard

		self.loop = loop

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
							print("Selected:", filepath)
					except Exception as ex:
						print(ex)
						self.throw_exec('file')

				self.set_lsection(tk.Label(self,  bg="gray80", image=self.get_dashboard().get_window().get_fulogo()))
				self.get_lsection().bind("<Button-1>", fu)
				self.get_lsection().grid(row=0, column=0)
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
			self.set_content(tk.Frame(self,
										width=600,
										height=400,
										bg='gray80'))
			self.get_content().grid(row=0, column=0)
		except Exception as ex:
			print(ex)
			self.throw_exec('cust')
