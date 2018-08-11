from tkinter import *;

window = Tk();
window.title("test");
window.geometry("300x300")

top_row = Frame(window);
top_row.grid(row = 0, column = 0, columnspan=2, sticky = N);
display = Entry(top_row, width = 100, bg = "light green")
display.grid(row = 0, column = 0);

two_row = Frame(window);
two_row.grid(row = 1, column = 0, columnspan=2, sticky = N);
displays = Entry(two_row, width = 100, bg = "red")
displays.grid(row = 0, column = 0);

three_row = Frame(window);
three_row.grid(row = 3, column = 0, columnspan=2, sticky = N);
displayss = Entry(three_row, width = 100, bg = "blue")
displayss.grid(row = 1, column = 0);


window.mainloop();
