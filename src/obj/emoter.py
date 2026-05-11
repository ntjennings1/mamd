import os
import asyncio
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

		self.buffer = None
		self.arc = None
		self.angle = None
		self.content = None
		self.section_label = None
		self.logo_section = None
		self.button_section = None
		self.back_button = None
		self.help_button = None

		self.gr_section = None
		self.gr_img = None
		self.gr_edit = None
		self.gr_id = None
		self.scale = 1.0
		self.zoom_step = 1.1
		self.pan_start = None

		self.waiting = False
		self.buffer_task = None

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

	def get_buffer(self):
		return self.buffer

	def set_buffer(self, buffer):
		self.buffer = buffer

	def get_arc(self):
		return self.arc

	def set_arc(self, arc):
		self.arc = arc

	def get_angle(self):
		return self.angle

	def set_angle(self, angle):
		self.angle = angle

	def get_content(self):
		return self.content

	def set_content(self, content):
		self.content = content

	def get_slabel(self):
		return self.section_label

	def set_slabel(self, slabel):
		self.section_label = slabel

	def get_lsection(self):
		return self.logo_section

	def set_lsection(self, lsection):
		self.logo_section = lsection

	def get_bsection(self):
		return self.button_section

	def set_bsection(self, bsection):
		self.button_section = bsection

	def get_bbutton(self):
		return self.back_button

	def set_bbutton(self, bbutton):
		self.back_button = bbutton

	def get_hbutton(self):
		return self.help_button

	def set_hbutton(self, hbutton):
		self.help_button = hbutton

	def get_grsection(self):
		return self.gr_section

	def set_grsection(self, grsection):
		self.gr_section = grsection

	def get_grimg(self):
		return self.gr_img

	def set_grimg(self, grimg):
		self.gr_img = grimg

	def get_gredit(self):
		return self.gr_edit

	def set_gredit(self, gredit):
		self.gr_edit = gredit

	def get_grid(self):
		return self.gr_id

	def set_grid(self, grid):
		self.gr_id = grid

	def get_scale(self):
		return self.scale

	def set_scale(self, scale):
		self.scale = scale

	def get_zstep(self):
		return self.zoom_step

	def set_zstep(self, zstep):
		self.zoom_step = zstep

	def get_pstart(self):
		return self.pan_start

	def set_pstart(self, pstart):
		self.pan_start = pstart

	def get_waiting(self):
		return self.waiting

	def set_waiting(self, waiting):
		self.waiting = waiting

	def get_btask(self):
		return self.buffer_task

	def set_btask(self, btask):
		self.buffer_task = btask

	def throw_exec(self, mes):
		if (mes == 'cust'):
			print('[ERR] Error customizing emoter.')
		elif (mes == 'place'):
			print('[ERR] Error placing emoter.')
		elif (mes == 'emote'):
			print('[ERR] Error emoting.')
		elif (mes == 'file'):
			print('[ERR] Error fetching model.')
		elif (mes == 'gr'):
			print('[ERR] Error displaying visual graph.')
		elif (mes == 'ani'):
			print('[ERR] Error animating buffer.')
		elif (mes == 'stop'):
			print('[ERR] Error stoping animation.')
		elif (mes == 'clear'):
			print('[ERR] Error clearing emoter.')
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

	async def clear(self):
		try:
			if (self.get_content().winfo_children()):
				for widget in self.get_content().winfo_children():
					widget.grid_forget()
		except Exception as ex:
			print(ex)
			self.throw_exec('clear')

	async def stop_a(self):
		try:
			if self.get_btask():
				self.get_btask().cancel()
				self.set_btask(None)
		except Exception as ex:
			print(ex)
			self.throw_exec('stop')

	async def animate(self):
		try:
			speed = 5
			while self.get_waiting():
				self.set_angle((self.get_angle() + speed) % 360)
				self.get_buffer().itemconfig(self.get_arc(), start=self.get_angle())
				await asyncio.sleep(0.016)

		except Exception as ex:
			print(ex)
			self.throw_exec('ani')
 
	async def edis(self, which):
		try:
			if (which == 'gr'):

				self.get_bbutton().grid(row=0, column=0, sticky="w")
				self.get_hbutton().grid(row=0, column=2, sticky="e")
				self.get_content().grid_columnconfigure(0, weight=1)
				self.get_content().grid_columnconfigure(1, weight=1)
				self.get_content().grid_columnconfigure(2, weight=1)
				self.get_content().grid_rowconfigure(0, weight=0)
				self.get_content().grid_rowconfigure(1, weight=1)

				self.get_buffer().grid(row=1, column=1)

				self.set_slabel(tk.Label(self.get_content(), bg='gray80', text='Scroll to zoom.'))
				self.get_slabel().grid(row=2, column=1)
		except Exception as ex:
			print(ex)

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
							self.nav_wrap('gr')
					except Exception as ex:
						print(ex)
						self.throw_exec('file')

				self.set_lsection(tk.Label(self.get_content(),  bg="gray80", image=self.get_dashboard().get_window().get_fulogo()))
				self.get_lsection().bind("<Button-1>", fu)
				self.get_lsection().grid(row=0, column=0)

				self.set_slabel(tk.Label(self.get_content(), bg='gray80', text='Click to select a file'))
				self.get_slabel().grid(row=1, column=0)

			elif (which == 'aps'):
				await self.get_dashboard().get_window().get_viewer().clear_lines()
				await self.get_dashboard().get_window().get_viewer().add_line(f'[-->] {self.get_dashboard().get_model().get_name()} chosen ...')
				await self.get_dashboard().get_window().get_viewer().add_line('')
				await self.get_dashboard().get_window().get_viewer().add_line(f'Select an analytics path above.')

				def gr(event):
					self.set_waiting(True)
					self.set_btask(asyncio.create_task(self.animate()))
					self.get_loop().create_task(self.get_dashboard().get_model().graph())
				def p(event):
					self.get_loop().create_task(self.get_dashboard().get_model().perform())
				def a(event):
					self.get_loop().create_task(self.get_dashboard().get_model().describe())

				self.set_lsection(tk.Frame(self.get_content(),
											bg='gray80'))
				self.get_lsection().grid(row=0, column=0)

				gr_label = tk.Label(self.get_lsection(), bg='gray80', image=self.get_dashboard().get_window().get_grlogo())
				gr_label.bind("<Button-1>", gr)
				gr_label.grid(row=0, column=0)

				p_label = tk.Label(self.get_lsection(), bg='gray80', image=self.get_dashboard().get_window().get_plogo())
				p_label.grid(row=0, column=1)
				p_label.bind("<Button-1>", p)
				p_label.grid_configure(padx=(50,50))

				a_label = tk.Label(self.get_lsection(), bg='gray80', image=self.get_dashboard().get_window().get_alogo())
				a_label.bind("<Button-1>", a)
				a_label.grid(row=0, column=2)

				self.set_slabel(tk.Label(self.get_content(), bg='gray80', text='Click to select a path.'))
				self.get_slabel().grid(row=1, column=0)

		except Exception as ex:
			print(ex)
			self.throw_exec('emote')

	async def nav(self, place):
		if (place == 'aps'):
			await self.clear()
			self.set_waiting(False)
			await self.stop_a()
			self.get_content().grid_columnconfigure(0, weight=1)
			self.get_content().grid_columnconfigure(1, weight=0)
			self.get_content().grid_columnconfigure(2, weight=0)
			self.get_content().grid_rowconfigure(0, weight=1)
			self.get_content().grid_rowconfigure(1, weight=0)
			await self.emote('aps')
		elif (place == 'gr'):
			await self.clear()
			await self.get_dashboard().get_model().eval()

	def nav_wrap(self, which):
		self.get_loop().create_task(self.nav(which))

	def place(self, row, col):
		try:
			self.grid(row=row, column=col)
		except Exception as ex:
			print(ex)
			self.throw_exec('place')

	async def customize(self):
		try:
			from PIL import Image, ImageTk

			def _on_zoom(event):
				try:
					if event.num == 5 or event.delta < 0:
						self.set_scale( self.get_scale() / self.get_zstep() )
					else:
						self.set_scale( self.get_scale() * self.get_zstep() )

					_redraw()
				except Exception as ex:
					print(ex)

			def _on_resize(event):
				try:
					_redraw()
				except Exception as ex:
					print(ex)

			def _redraw():
				try:
					w = int(self.get_grimg().width * self.get_scale())
					h = int(self.get_grimg().height * self.get_scale())

					resized = self.get_grimg().resize((w, h), Image.LANCZOS)
					self.set_gredit(ImageTk.PhotoImage(resized))

					self.get_grsection().delete(self.get_grid())
					self.set_grid(self.get_grsection().create_image(0, 0, anchor="nw", image=self.get_gredit()))

					# Update scroll region
					self.get_grsection().config(scrollregion=(0, 0, w, h))
				except Exception as ex:
					print(ex)

			def _start_pan(event):
	  			self.pan_start = (event.x, event.y)

			def _do_pan(event):
				if self.get_pstart() is None:
					return

				dx = event.x - self.get_pstart()[0]
				dy = event.y - self.get_pstart()[1]

				self.get_grsection().move(self.get_grid(), dx, dy)
				self.pan_start = (event.x, event.y)

			def _end_pan(event):
				self.pan_start = None

			self.set_width(600)
			self.set_height(400)
			self.config(width=self.get_width(),
						height=self.get_height(),
						bg='gray80')
			self.grid_propagate(False)

			# Frames
			self.set_content(tk.Frame(self,
										width=self.get_width(),
										height=self.get_height(),
										bg='gray80'))
			self.get_content().grid(row=0, column=1)
			self.get_content().grid_propagate(False)
			self.get_content().grid_columnconfigure(0, weight=1)
			self.get_content().grid_rowconfigure(0, weight=1)

			self.set_bsection(tk.Frame(self.get_content(),
										width=self.get_width(),
										height=self.get_height(),
										bg='gray80'))

			# Buttons
			self.set_bbutton(tk.Button(self.get_content(),
									width=4,
									state='normal',
									text="<<<",
									bg='darkorange',
									fg='black',
									activebackground='darkorange',
									activeforeground='black',
									command=lambda:self.nav_wrap('aps')))

			self.set_hbutton(tk.Button(self.get_content(),
									width=4,
									state='normal',
									text="???",
									bg='gold2',
									fg='black',
									activebackground='gold2',
									activeforeground='black',
									command=lambda:self.nav_wrap('help')))

			# Buffer
			thickness = 5
			size = 100
			speed = 5
			pad = thickness // 2
			arc_len = 90
			self.set_angle(0)
			bounds = (pad, pad, size - pad, size - pad)
			self.set_buffer(tk.Canvas(self.get_content(),
										width=size,
										height=size,
										bg='gray80',
										highlightthickness=0))
			self.set_arc(self.get_buffer().create_arc(
				bounds,
				start=self.get_angle(),
				extent=arc_len,
				style="arc",
				outline="red",
				width=thickness
			))

			# Zoomer
			self.set_grsection(tk.Canvas(self.get_content(), bg='gray80'))
			self.get_grsection().bind("<MouseWheel>", _on_zoom)
			self.get_grsection().bind("<Configure>", _on_resize)
			self.get_grsection().bind("<Button-1>", _start_pan)
			self.get_grsection().bind("<B1-Motion>", _do_pan)
			self.get_grsection().bind("<ButtonRelease-1>", _end_pan)

		except Exception as ex:
			print(ex)
			self.throw_exec('cust')
