from tkinter import *;
import matplotlib.pylab as plt

window = Tk();
window.title("Maplotlib Calculaor");

top_row = Frame(window);
top_row.grid(row = 0, column = 0, columnspan=2, sticky = N);
display = Entry(top_row, width = 45, bg = "light green")
display.grid(row = 0, column = 0);

button_pad = Frame(window);
button_pad.grid(row = 2, column = 0, sticky = W);
color = {'black' : 'k', 'green':'g', 'red':'r'};
ls = {'solid' : '-', 'dashed' : '--', 'dashed dot' : '-.'};
marker = {'point' : '.', 'circle' : 'o', 'triangle_up' : '^'};
def save(key, value):
    if key == 0: # color
        display.delete(0, END);
        str = "plt.plot([10, 20, 30, 40], [1, 4, 9, 16], c="+value+", ls='--', marker='o')"
        display.insert(END, str);
    if key == 1 : # line style
        display.delete(0, END);
        str = "plt.plot([10, 20, 30, 40], [1, 4, 9, 16], c='b', ls=" + value+", marker='o')"
        display.insert(END, str);
    if key == 2 : # marker
        display.delete(0, END);
        str = "plt.plot([10, 20, 30, 40], [1, 4, 9, 16], c='b', ls='--', marker='"+value+")"
        display.insert(END, str);

lst = [color, ls, marker];
r = 0;
c = 0;
for i in range(len(lst)):
    for key,value in lst[i].items():
        def par(k = i, v = value):
            save(k, v);
        Button(button_pad,text = key, width = 5, command = par).grid(row = r, column=c);
        c += 1;
    if c > 2:
        c = 0;
        r += 1;
def cmd():
    print(display.get())
    #plt.plot([10, 20, 30, 40], [1, 4, 9, 16])
    #plt.show()
Button(text = "click", width = 5, command = cmd).grid(row=1,column=1);
window.mainloop();
