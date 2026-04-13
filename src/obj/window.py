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
        self.root = tk.Tk()
        self.controller = None
        self.viewer = None
        self.emoter = None
        self.helper = None

        self.width = ''
        self.height = ''
        self.screen_wdith = self.get_root().winfo_screenwidth()
        self.screen_height = self.get_root().winfo_screenheight()

        self.buttons = []
        self.close_button = None
        self.help_button = None
        self.train_button = None
        self.test_button = None
        self.stop_button = None
        self.reset_button = None

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

    def get_controller(self):
        return self.controller

    def set_controller(self, controller):
        self.controller = controller

    def get_viewer(self):
        return self.viewer

    def set_viewer(self, viewer):
        self.viewer = viewer

    def get_emoter(self):
        return self.emoter

    def set_emoter(self, emoter):
        self.emoter = emoter

    def get_helper(self):
        return self.helper

    def set_helper(self, helper):
        self.helper = helper

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height

    def get_buttons(self):
        return self.buttons

    def set_buttons(self, buttons):
        self.buttons = buttons

    def add_button(self, button):
        self.get_buttons().append(button)

    async def customize(self):
        print('c')

    async def fill(self):
        try:
            self.set_controller(Controller(self.get_root(), self.get_dashboard(), self.get_loop()))
        except Exception as ex:
            print('ex')

    async def bootui(self):
        try:
            print('[!] Welcome to MAMD')
            #await self.fill()
            #await self.customize()
            while True:
                self.get_root().update()
                await asyncio.sleep(.1)
        except Exception as ex:
            print(ex)