from tkinter import *;
from chart import *;
from display import *;

window = Tk();
window.title("Maplotlib Calc");
window.geometry("500x400");
# 결과들을 보여주는 아웃풋
output = display(window, 0, 0);
out_entry = output.make_Entry(0,0,70,"light green")
# class를 생성할시엔 무조건 frame row, col을 받게끔 해야함
chart = chart(window,2,0,out_entry); # 버튼을 만들기 위함
chart.make_button();
window.mainloop();
