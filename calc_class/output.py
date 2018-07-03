from tkinter import *;

class output:
    def __init__(self, window, width, height, background):
        self.window = window;
        self.width = width;
        self.height = height;
        self.wrap = WORD;
        self.background = background;
        self.Text = Text(window, width = self.width, height = self.height,
        wrap = self.wrap, background = self.background).grid(row = 4,
        column  = 0, columnspan = 2, sticky = W)
