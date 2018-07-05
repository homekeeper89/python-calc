from tkinter import *;

class button:
    def __init__(self, window, output, row, column, sticky):
        self.window = window;
        self.row = row;
        self.column = column;
        self.sticky = sticky;
        self.output = output;
        self.frame = Frame(window).grid(row = self.row, column = self.column,
        sticky = self.sticky);

    def make_button(self, btn_lst, boolen):
        if boolen == False:
            return ;
        r  = 10
        c = 10
        for btn in btn_lst:
            def cmd(x = btn):
                self.click(x)
            Button(self.frame, text = btn, width = 5, command = cmd).grid(
            row = r, column = c)
            c += 1;
            if c > 12:
                c = 10;
                r += 1;

    def click(self, x):
        print(self.output.row);
        self.output.entry.insert(x);
