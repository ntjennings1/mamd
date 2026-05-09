import os
import asyncio
import subprocess
import time

class Model():
	def __init__(self, dashboard, loop):
		self.dashboard = dashboard
		self.loop = loop
		self.model = None

		self.path = ''
		self.name = ''
		self.type = ''
		self.biases = []
		self.weights = []
		self.ins = []
		self.outs = []

	def get_dashboard(self):
		return self.dashboard

	def set_dashboard(self, dashboard):
		self.dashboard = dashboard

	def get_loop(self):
		return self.loop

	def set_loop(self, loop):
		self.loop = loop

	def get_model(self):
		return self.model

	def set_model(self, model):
		self.model = model

	def get_path(self):
		return self.path

	def set_path(self, path):
		self.path = path

	def get_name(self):
		return self.name

	def set_name(self, name):
		self.name = name

	def get_type(self):
		return self.type

	def set_type(self, type):
		self.type = type

	def get_biases(self):
		return self.biases

	def set_biases(self, biases):
		self.biases = biases

	def add_bias(self, bias):
		self.get_biases().append(bias)

	def get_weights(self):
		return self.weights

	def set_weights(self, weights):
		self.weights = weights

	def add_weight(self, weight):
		self.get_weights().append(weight)

	def throw_exec(self, mes):
		if (mes == 'eval'):
			print('[ERR] Error evaluating chosen file.')

	async def perform(self):
		try:
			import numpy as np
			import onnx
			import onnxruntime as ort

			# Create session options and enable profiling
			opts = ort.SessionOptions()
			opts.enable_profiling = True
			opts.profile_file_prefix = f'{self.get_dashboard().get_odir()}/{self.get_name()}'

			# Create session (CUDA if available)
			session = ort.InferenceSession(
				self.get_path(),
				sess_options=opts,
				providers=["CUDAExecutionProvider", "CPUExecutionProvider"]
			)

			# Build dummy input
			inp = session.get_inputs()[0]
			shape = [d if isinstance(d, int) else 1 for d in inp.shape]
			dummy = np.random.rand(*shape).astype(np.float32)

			# Run once so profiling has something to record
			session.run(None, {inp.name: dummy})

			# End profiling and get the file path
			profile_file = session.end_profiling()
		except Exception as ex:
			print(ex)

	async def graph(self):
		try:
			import numpy as np
			import onnx
			import pydot
			from onnx.tools.net_drawer import GetPydotGraph, GetOpNodeProducer

			pydot_graph = GetPydotGraph(
				self.get_model().graph,
				name=self.get_model().graph.name,
				rankdir="TB",
				node_producer=GetOpNodeProducer("docstring")
			)
			pydot_graph.write_svg(f"{self.get_dashboard().get_odir()}/{self.get_name()}.svg")

		except Exception as ex:
			print(ex)

	async def describe(self):
		try:
			import numpy as np
			import onnx
			from onnx import shape_inference, helper
			from collections import Counter

			for init in self.get_model().graph.initializer:
				arr = onnx.numpy_helper.to_array(init)
				if ('bias' in init.name):
					self.add_bias(init)
				elif ('weight' in init.name):
					self.add_weight(init)
				print(init.name, arr.shape, arr.dtype, arr.size, arr.nbytes)

			ops = Counter(node.op_type for node in self.get_model().graph.node)
			print(ops)

			# Text graph layout
			inferred = shape_inference.infer_shapes(self.get_model())
			t = helper.printable_graph(inferred.graph)
			with open(f'{self.get_dashboard().get_odir()}/{self.get_name()}.txt', "w", encoding='utf-8') as f:
				f.write(t)
				f.write('\n\n')
				f.write(str(inferred))
		except Exception as ex:
			print(ex)

	async def init(self):
		try:
			import onnx
			self.set_model(onnx.load(self.get_path()))

			project_dir = os.path.dirname(os.path.dirname(self.get_dashboard().get_dir()))
			out_dir = os.path.join(project_dir, "out")
			if os.path.isdir(out_dir):
				import shutil
				tmp = out_dir
				shutil.rmtree(out_dir)
				self.get_dashboard().set_odir(tmp)
				os.makedirs(self.get_dashboard().get_odir(), exist_ok=True)
			else:
				self.get_dashboard().set_odir(out_dir)
				os.makedirs(self.get_dashboard().get_odir(), exist_ok=True)
		except Exception as ex:
			print(ex)

	async def eval(self):
		try:
			async def prove(name):
				tmp = name.split('.')
				if (len(tmp) > 2):
					return
				else:
					self.set_name(tmp[0])
					self.set_type(tmp[1])

					await self.get_dashboard().get_window().get_emoter().reset()
					await self.get_dashboard().get_window().get_emoter().emote('aps')

			tmp = self.get_path().split('/')
			sz = len(tmp)
			chosen = tmp[sz-1]
			await prove(chosen)
			await self.init()

		except Exception as ex:
			print(ex)
			self.throw_exec('eval')