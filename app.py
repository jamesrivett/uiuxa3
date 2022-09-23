import tkinter as tk
from view import View

class MyApplication(tk.Tk):
    """Hello World Main Application"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Hello Tkinter")
        self.geometry("800x600")
        self.resizable(width=False, height=False)

        View(self).grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        self.columnconfigure(0, weight=1)