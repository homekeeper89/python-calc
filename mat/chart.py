from tkinter import *;
class chart:
    def __init__(self, window, row, column):
        self.window = window;
        self.pad = Frame(window);
        self.row = row;
        self.column = column;
        self.pad.grid(row = self.row, column = self.column,sticky = W);

    def make_button(self):
        char_lst = ['LINE', 'SCATTER']
        r , c = 0,0
        for k, v in enumerate(char_lst):
            def inner(index = k):
                self.show(index)
            Button(self.pad, text = v, width =10, command = inner).grid(row = r, column = c)
            c +=1;

    def show(self, index):
        button_pad = Frame(self.window)
        button_pad.grid(row =3, column =0, sticky = N);
        print("show show", index)
        if index == 0:
            cr = {'black' : 'k', 'green':'g', 'red':'r'};
            ls = {'solid' : '-', 'dashed' : '--', 'dashed dot' : '-.'};
            marker = {'point' : '.', 'circle' : 'o', 'triangle_up' : '^'};
            category = [cr, ls, marker];
            r = 0;
            c = 0;
            for i in range(len(category)):
                for key,value in category[i].items():
                    Button(button_pad,text = key, width = 10).grid(row = r, column=c);
                    c += 1;
                if c > 2:
                    c = 0;
                    r += 1;
