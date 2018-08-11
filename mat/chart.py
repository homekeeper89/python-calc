from tkinter import *;
class chart:
    def __init__(self, window, row, column, output_entry):
        self.window = window;
        self.pad = Frame(window);
        self.row = row;
        self.column = column;
        self.outentry= output_entry;
        self.pad.grid(row = self.row, column = self.column,sticky = W);

    def make_button(self):
        char_lst = ['LINE', 'SCATTER']
        r , c = 0,0
        for k, v in enumerate(char_lst):
            def inner(index = k):
                self.show(index)
            Button(self.pad, text = v, width =10, command = inner).grid(row = r, column = c)
            c +=1;

    def show(self, index): # 버튼만 보여주는 메서드
        button_pad = Frame(self.window)
        button_pad.grid(row =3, column =0, sticky = N);
        if index == 0:
            cr = {'black' : 'k', 'green':'g', 'red':'r'};
            ls = {'solid' : '-', 'dashed' : '--', 'dashed dot' : '-.'};
            marker = {'point' : '.', 'circle' : 'o', 'triangle_up' : '^'};
            category = [cr, ls, marker];
            r = 0;
            c = 0;
            record_lst = [];
            for i in range(len(category)):
                for key,value in category[i].items():
                    def inner(k = key, v = value, index =i):
                        print(i)
                        del record_lst[i:i+1];
                        record_lst.insert(i,{k,v});
                        self.button_action(k,record_lst);
                    Button(button_pad,text = i, width = 10, command = inner).grid(row = r, column=c);
                    c += 1;
                if c > 2:
                    c = 0;
                    r += 1;

    def button_action(self,key,lst):
        #str = "plt.plot([10, 20, 30, 40], [1, 4, 9, 16], c= '%s', ls='%s', marker='%s')" %(lst[0][key],lst[1][key], lst[2][key]);
        print(lst);
        self.outentry.delete(0, END);
        self.outentry.insert(END, "Test");
