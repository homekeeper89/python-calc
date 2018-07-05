from tkinter import *

class display:
    def __init__(self, window, text, row, column, sticky = "N"):
        self.window = window;
        self.text = text;
        self.row = row;
        self.column = column;
        self.sticky = sticky;
        self.lavel = Label(self.window, text = self.text).grid(
        row = 0,
        column = 0, sticky = self.sticky);
        self.entry = Entry(self.window, width = 20, bg = "light green").grid(
        row = self.row, column = self.column, sticky = W);

    def insert(self, x):
        self.entry.insert(x);
