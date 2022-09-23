from functools import total_ordering
import tkinter as tk
from tkinter import ttk

class View(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.PRICE_largepizza = tk.DoubleVar(value=15.99)
        self.PRICE_mediumpizza = tk.DoubleVar(value=12.99)
        self.PRICE_smallpizza = tk.DoubleVar(value=10.99)

        LABEL_largepizza = ttk.Label(self, text='Large Pizza | ' + str(self.PRICE_largepizza.get()))
        LABEL_largepizza.grid(row=0, column=0, sticky=tk.W)
        BUTTON_addToCart_largepizza = ttk.Button(self, text="Add to Cart", command=lambda: self.addToCart(self.PRICE_largepizza.get()))
        BUTTON_addToCart_largepizza.grid(row=0, column=1, sticky=tk.E) 

        LABEL_mediumpizza = ttk.Label(self, text='Medium Pizza | ' + str(self.PRICE_mediumpizza.get()))
        LABEL_mediumpizza.grid(row=1, column=0, sticky=tk.W)
        BUTTON_addToCart_mediumpizza = ttk.Button(self, text="Add to Cart", command=lambda: self.addToCart(self.PRICE_mediumpizza.get()))
        BUTTON_addToCart_mediumpizza.grid(row=1, column=1, sticky=tk.E) 

        LABEL_smallpizza = ttk.Label(self, text='Small Pizza | ' + str(self.PRICE_smallpizza.get()))
        LABEL_smallpizza.grid(row=2, column=0, sticky=tk.W)
        BUTTON_addToCart_smallpizza = ttk.Button(self, text="Add to Cart", command=lambda: self.addToCart(self.PRICE_smallpizza.get()))
        BUTTON_addToCart_smallpizza.grid(row=2, column=1, sticky=tk.E) 
        
        self.total = tk.DoubleVar(value=0.00)
        LABEL_total = ttk.Label(self, textvariable=self.total)
        LABEL_total.grid(row=3, column=2, sticky=tk.S)

    def addToCart(self, price):
        val = self.total.get()
        newval = val + price
        self.total.set(newval)