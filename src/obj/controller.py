import tkinter as tk

class Controller(tk.Frame):
    def __init__(self, root, dashboard, loop):
        super().__init__(root)
        self.root = root
        self.dashboard = dashboard
        self.loop = loop

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
