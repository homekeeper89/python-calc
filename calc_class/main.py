from tkinter import *;
from display import *;
from output import *;
from button import *;

window = Tk();
window.title("왜 안되냐");

my_lavel = display(window, "위치 고정인가", 2, 0);
my_out = output(window, 75,6,"light blue");
my_by = button(window, my_lavel, 20, 10, S)
lst = ["0,", "1", "2", "3", "4", "5"]
my_by.make_button(lst, True);
window.mainloop();
