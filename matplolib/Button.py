class button:
    def __init__(self, window, row, column, display):
        self.window = window
        self.pad = Frame(window);
        self.pad.grid(row = row, column = column, sticky = W);
        color = {'black' : 'k', 'green':'g', 'red':'r'};
        ls = {'solid' : '-', 'dashed' : '--', 'dashed dot' : '-.'};
        marker = {'point' : '.', 'circle' : 'o', 'triangle_up' : '^'};
        lst = [color, ls, marker];
        r = 0;
        c = 0;
        for i in range(len(lst)):
            for key,value in lst[i].items():
                def par(k = i, v = value):
                    save(k, v);
                Button(button_pad,text = key, width = 10, command = par).grid(row = r, column=c);
                c += 1;
            if c > 2:
                c = 0;
                r += 1;
    def save(self, key, value):
        if key == 0: # color
            display.delete(0, END);
            savePara(key, value);
            str = "plt.plot([10, 20, 30, 40], [1, 4, 9, 16], c= '%s', ls='%s', marker='%s')" %(par_lst[0], par_lst[1], par_lst[2])
            display.insert(END, str);
        if key == 1 : # line style
            display.delete(0, END);
            savePara(key, value);
            str = "plt.plot([10, 20, 30, 40], [1, 4, 9, 16], c= '%s', ls='%s', marker='%s')" %(par_lst[0], par_lst[1], par_lst[2])
            display.insert(END, str);
        if key == 2 : # marker
            display.delete(0, END);
            savePara(key, value);
            str = "plt.plot([10, 20, 30, 40], [1, 4, 9, 16], c= '%s', ls='%s', marker='%s')" %(par_lst[0], par_lst[1], par_lst[2])
            display.insert(END, str);

    par_lst = ['b', '--', 'o'];
    def savePara(key, val):
        if par_lst[key] != None:
            par_lst[key] = val;
        else:
            par_lst.insert(key, val);
