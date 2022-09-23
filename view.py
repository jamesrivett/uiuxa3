import tkinter as tk
from tkinter import ttk

class View(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        PRICE_largepizza = "15.99"
        PRICE_mediumpizza = "12.99"
        PRICE_smallpizza = "10.99"

        LABEL_largepizza = ttk.Label(self, text='Large Pizza | ' + PRICE_largepizza)
        LABEL_largepizza.grid(row=0, column=0, sticky=tk.W)
        BUTTON_addToCart_largepizza = ttk.Button(self, text="Add to Cart", command=self.addToCart)
        BUTTON_addToCart_largepizza.grid(row=0, column=1, sticky=tk.E) 

        LABEL_mediumpizza = ttk.Label(self, text='Medium Pizza | ' + PRICE_mediumpizza)
        LABEL_mediumpizza.grid(row=1, column=0, sticky=tk.W)
        BUTTON_addToCart_mediumpizza = ttk.Button(self, text="Add to Cart", command=self.addToCart)
        BUTTON_addToCart_mediumpizza.grid(row=1, column=1, sticky=tk.E) 

        LABEL_smallpizza = ttk.Label(self, text='Small Pizza | ' + PRICE_smallpizza)
        LABEL_smallpizza.grid(row=2, column=0, sticky=tk.W)
        BUTTON_addToCart_smallpizza = ttk.Button(self, text="Add to Cart", command=self.addToCart)
        BUTTON_addToCart_smallpizza.grid(row=2, column=1, sticky=tk.E) 

    def addToCart(self):
        pass