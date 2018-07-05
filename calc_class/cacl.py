from tkinter import *;

window = Tk();
window.title("kke")
display = Entry(width = 45, bg = "light blue");
display.grid(row = 1, column = 0);

savedis = Entry(width = 45, bg = "light green");
savedis.grid(row = 2, column =0);

def cmd():
    text = display.get();
    
    savedis.insert(END,text);
op = Frame(window);
op.grid(row =3, column =0);
Button(op, text = "click", width = 5, command = cmd).grid(row = 3, column = 3);
oper = Frame(window);
oper.grid(row = 1, column = 4, stick = E);
op_list = ["0","1","2","3","4","5","6","7","8","9"];
def click(x):
    display.insert(END, x);
r = 3;
c = 3;
for i in op_list:
    def kk(x = i):
        click(x);
    Button(oper, text =  i, width = 5, command = kk).grid(row = r, column = c)
    c += 1;
    if c > 5:
        c = 3;
        r += 1;

window.mainloop();
