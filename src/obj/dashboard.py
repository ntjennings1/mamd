import os
from obj.window import Window
from obj.model import Model

class Dashboard():
	def __init__(self, scenario, loop):
		self.scenario = scenario
		self.loop = loop
		self.window = Window(self, loop)
		self.model = Model(self, loop)

		self.dir = os.path.dirname(os.path.abspath(__file__))
		self.odir = None
		self.mode = ''

	def get_scenario(self):
		return self.scenario

	def set_scenario(self, scenario):
		self.scenario = scenario

	def get_loop(self):
		return self.loop

	def set_loop(self, loop):
		self.loop = loop

	def get_window(self):
		return self.window

	def set_window(self, window):
		self.window = window

	def get_model(self):
		return self.model

	def set_model(self, model):
		self.model = model

	def get_dir(self):
		return self.dir

	def set_dir(self, dir):
		self.dir = dir

	def get_odir(self):
		return self.odir

	def set_odir(self, odir):
		self.odir = odir

	def get_mode(self):
		return self.mode

	def set_mode(self, mode):
		self.mode = mode

	def throw_exec(self, mes):

		if (mes == 'boot'):
			print('[ERR] Error booting dashboard ui.')

	async def reset(self):
		self.set_model(Model(self, self.get_loop()))
		self.set_mode('')

	async def bootui(self):
		try:
			await self.get_window().bootui()
		except Exception as ex:
			print(ex)
			self.throw_exec('boot')
		except KeyboardInterrupt:
			print('[!] Dashboard Shutdown.')