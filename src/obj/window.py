import os
import sys
import time
import asyncio
import tkinter as tk

from obj.helper import Helper
from obj.controller import Controller
from obj.viewer import Viewer

class Window():
    def __init__(self, dashboard, loop):
        self.dashboard = dashboard
        self.loop = loop
        self.helper = None

        self.root = tk.Tk()
        self.width = ''
        self.height = ''

    def get_dashboard(self):
        return self.dashboard

    def set_dashboard(self, dashboard):
        self.dashboard = dashboard

    def get_loop(self):
        return self.loop

    def set_loop(self, loop):
        self.loop = loop

    def get_helper(self):
        return self.helper

    def set_helper(self, helper):
        self.helper = helper

    def get_root(self):
        return self.root

    def set_root(self, root):
        self.root = root

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height

    async def customize(self):
        print('c')

    async def bootui(self):
        print('[!] Welcome to MAMD')
        #await self.customize()
        while True:
            self.get_root().update()
            await asyncio.sleep(.1)