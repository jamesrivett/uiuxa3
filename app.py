import tkinter as tk
from view import View

class MyApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Restaurant GUI")
        self.resizable(width=True, height=False)

        View(self).grid(sticky=(tk.E + tk.W + tk.N + tk.S))