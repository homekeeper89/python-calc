from tkinter import *;

class display():
    def __init__(self, window, row,col):
        self.window = window;
        self.row = row;
        self.col = col;
        self.tpfr = Frame(window);
        self.tpfr.grid(row = self.row, column = self.col, sticky = N);

    def make_Entry(self, row, col, width, color):
        display = Entry(self.tpfr, width = width, bg=color)
        display.grid(row = row, column = col);
