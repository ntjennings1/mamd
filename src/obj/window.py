import os
import sys
import time
import asyncio
import tkinter as tk

from obj.helper import Helper
from obj.moderator import Moderator
from obj.controller import Controller
from obj.emoter import Emoter
from obj.viewer import Viewer

class Window():
	def __init__(self, dashboard, loop):
		self.dashboard = dashboard
		self.loop = loop
		self.root = tk.Tk()
		self.moderator = None
		self.controller = None
		self.emoter = None
		self.viewer = None
		self.helper = None

		self.dir = os.path.dirname(os.path.abspath(__file__))
		self.fu_logo = None
		self.fu_path = ''
		self.gr_logo = None
		self.gr_path = ''
		self.p_logo = None
		self.p_path = ''
		self.a_logo = None
		self.a_path = ''
		self.width = ''
		self.height = ''
		self.screen_width = self.get_root().winfo_screenwidth()
		self.screen_height = self.get_root().winfo_screenheight()

		self.buttons = []
		self.close_button = None
		self.help_button = None

		self.running = False
		self.ptask = None

	def get_dashboard(self):
		return self.dashboard

	def set_dashboard(self, dashboard):
		self.dashboard = dashboard

	def get_loop(self):
		return self.loop

	def set_loop(self, loop):
		self.loop = loop

	def get_root(self):
		return self.root

	def set_root(self, root):
		self.root = root

	def get_moderator(self):
		return self.moderator

	def set_moderator(self, moderator):
		self.moderator = moderator

	def get_controller(self):
		return self.controller

	def set_controller(self, controller):
		self.controller = controller

	def get_emoter(self):
		return self.emoter

	def set_emoter(self, emoter):
		self.emoter = emoter

	def get_viewer(self):
		return self.viewer

	def set_viewer(self, viewer):
		self.viewer = viewer

	def get_helper(self):
		return self.helper

	def set_helper(self, helper):
		self.helper = helper

	def get_dir(self):
		return self.dir

	def set_dir(self, dir):
		self.dir = dir

	def get_fulogo(self):
		return self.fu_logo

	def set_fulogo(self, fulogo):
		self.fu_logo = fulogo

	def get_fupath(self):
		return self.fu_path

	def set_fupath(self, fupath):
		self.fu_path = fupath

	def get_grlogo(self):
		return self.gr_logo

	def set_grlogo(self, grlogo):
		self.gr_logo = grlogo

	def get_grpath(self):
		return self.gr_path

	def set_grpath(self, grpath):
		self.gr_path = grpath

	def get_plogo(self):
		return self.p_logo

	def set_plogo(self, plogo):
		self.p_logo = plogo

	def get_ppath(self):
		return self.p_path

	def set_ppath(self, ppath):
		self.p_path = ppath

	def get_alogo(self):
		return self.a_logo

	def set_alogo(self, alogo):
		self.a_logo = alogo

	def get_apath(self):
		return self.a_path

	def set_apath(self, apath):
		self.a_path = apath

	def get_width(self):
		return self.width

	def set_width(self, width):
		self.width = width

	def get_height(self):
		return self.height

	def set_height(self, height):
		self.height = height

	def get_swidth(self):
		return self.screen_width

	def set_switdth(self, swidth):
		self.screen_width = swidth

	def get_sheight(self):
		return self.screen_height

	def set_sheight(self, sheight):
		self.screen_height = sheight

	def get_buttons(self):
		return self.buttons

	def set_buttons(self, buttons):
		self.buttons = buttons

	def add_button(self, button):
		self.get_buttons().append(button)

	def get_cbutton(self):
		return self.close_button

	def set_cbutton(self, cbutton):
		self.close_button = cbutton

	def get_hbutton(self):
		return self.help_button

	def set_hbutton(self, hbutton):
		self.help_button = hbutton

	def get_running(self):
		return self.running

	def set_running(self, running):
		self.running = running

	def get_ptask(self):
		return self.ptask

	def set_ptask(self, ptask):
		self.ptask = ptask

	def throw_exec(self, mes):
		if (mes == 'boot'):
			print('[ERR] Error booting window.')
		elif (mes == 'pump'):
			print('[ERR] Error running UI pump.')
		elif (mes == 'center'):
			print('[ERR] Error finding screen center.')
		elif (mes == 'config'):
			print('[ERR] Error configuring UI.')
		elif (mes == 'fill'):
			print('[ERR] Error filling UI elements.')

	def center(self):
		try:
			center_x = (int(self.get_swidth()) / 2) - (int(self.get_width()) / 2)
			center_y = (int(self.get_sheight()) / 2) - (int(self.get_height()) / 2)

			return center_x,center_y
		except Exception as ex:
			print(ex)
			self.throw_exec('center')

	async def customize(self):
		try:
			from PIL import Image, ImageTk

			src_dir = os.path.dirname(self.get_dir())
			im_dir = os.path.join(src_dir, "images")
			self.set_fupath(os.path.join(im_dir, "file_upload.png"))
			self.set_grpath(os.path.join(im_dir, "route.png"))
			self.set_ppath(os.path.join(im_dir, "data_dist.png"))
			self.set_apath(os.path.join(im_dir, "settings.png"))

			ful = Image.open(self.get_fupath()).convert("RGBA")
			w, h = ful.size
			scale = 0.25
			resized = ful.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
			fu = ImageTk.PhotoImage(resized)
			self.set_fulogo(fu)

			grl = Image.open(self.get_grpath()).convert("RGBA")
			w, h = grl.size
			scale = 0.15
			gresized = grl.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
			gr = ImageTk.PhotoImage(gresized)
			self.set_grlogo(gr)

			pl = Image.open(self.get_ppath()).convert("RGBA")
			w, h = pl.size
			scale = 0.15
			presized = pl.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
			p = ImageTk.PhotoImage(presized)
			self.set_plogo(p)

			al = Image.open(self.get_apath()).convert("RGBA")
			w, h = al.size
			scale = 0.15
			aresized = al.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
			a = ImageTk.PhotoImage(aresized)
			self.set_alogo(a)

			await self.get_moderator().customize()
			self.get_moderator().place(0,0)
			self.get_moderator().grid_configure(padx=50, pady=50)

			await self.get_controller().customize()
			self.get_controller().place(1,0)
			self.get_controller().grid_configure(pady=(0,50))

			await self.get_emoter().customize()
			self.get_emoter().place(0,1)
			self.get_emoter().grid_configure(padx=(0,50))

			await self.get_viewer().customize()
			self.get_viewer().place(1,1)
			self.get_viewer().grid_configure(padx=(0,50))
			self.get_viewer().grid_configure(pady=(0,50))

		except Exception as ex:
			print(ex)
			self.throw_exec('cust')

	async def fill(self):
		try:
			self.set_moderator(Moderator(self.get_root(), self.get_dashboard(), self.get_loop()))
			self.set_controller(Controller(self.get_root(), self.get_dashboard(), self.get_loop()))
			self.set_emoter(Emoter(self.get_root(), self.get_dashboard(), self.get_loop()))
			self.set_viewer(Viewer(self.get_root(), self.get_dashboard(), self.get_loop()))
		except Exception as ex:
			print(ex)
			self.throw_exec('fill')

	async def config(self, which):
		try:
			if (which == 'land'):
				#self.get_root().overrideredirect(True)
				#self.get_root().resizable(False, False)
				self.get_root().attributes('-topmost', True)
			elif (which == 'test'):
				self.get_dashboard().set_mode('test')
				await self.get_viewer().config('test')
				await self.get_controller().config('test')
				await self.get_emoter().emote('fu')
			elif (which == 'train'):
				self.get_dashboard().set_mode('train')
				await self.get_viewer().config('train')
				await self.get_controller().config('train')
		except Exception as ex:
			print(ex)
			self.throw_exec('config')

	async def pump(self):
		while self.get_running():
			try:
				self.get_root().update_idletasks()
				self.get_root().update()
			except tk.TclError:
				print(ex)
				return
			except Exception as ex:
				print(ex)
				self.throw_exec('pump')
			await asyncio.sleep(0.001)

	async def bootui(self):
		try:
			def on_close():
				print('[!] MAMD Shutdown.')
				if self.get_ptask():
					self.set_running(False)
					self.get_ptask().cancel()
					self.set_ptask(None)
					self.get_root().destroy()
				os._exit(0)

			print('[!] Welcome to MAMD')
			self.set_running(True)

			await self.fill()
			await self.customize()
			await self.config('land')
			self.get_root().title('MAMD')
			self.get_root().protocol("WM_DELETE_WINDOW", on_close)

			self.set_ptask(self.get_loop().create_task(self.pump()))

		except Exception as ex:
			print(ex)
			self.throw_exec('boot')