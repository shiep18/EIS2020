import wzq
import jzq
import tkinter as tk
import tkinter.messagebox
import pickle
import pymysql
import cv2
import os

window = tk.Tk()
window.title('智能下棋手')
window.geometry("%dx%d" %(324,474))
b = tk.PhotoImage(file="b.gif")
w = tk.PhotoImage(file="w.gif")
j = tk.PhotoImage(file="j.gif")
imgLabel = tk.Label(window,image=b)
imgLabel.pack(side=tk.LEFT)

def start_jzq():
    window_jzq = tk.Toplevel(window)
    window_jzq.geometry("%dx%d" %(587,490))
    window_jzq.title('井字棋')
    imgLabel = tk.Label(window_jzq,image=j)
    imgLabel.pack(side=tk.RIGHT)
    def quit_game():
        window_jzq.destroy()
    btn_login = tk.Button(window_jzq, text='人机对战',command=jzq.jzq_pve, bg = '#ffffcc', font=('华文行楷',16))
    btn_login.place(x=245, y=80)

    btn_login = tk.Button(window_jzq, text='人人对战',command=jzq.jzq_pvp, bg = '#ffffcc', font=('华文行楷',16))
    btn_login.place(x=245, y=140)

    btn_login = tk.Button(window_jzq, text='退出游戏',command=quit_game, bg = '#ffffcc', font=('华文行楷',16))
    btn_login.place(x=245, y=200)

def start_wzq():
    window_wzq = tk.Toplevel(window)
    window_wzq.geometry("%dx%d" %(450, 450))
    window_wzq.title('五子棋')
    imgLabel = tk.Label(window_wzq,image=w)
    imgLabel.pack(side=tk.RIGHT)
    def quit_game():
        window_wzq.destroy()
    btn_login = tk.Button(window_wzq, text='人机对战',command=wzq.wzq_pve, bg = '#99cc00', font=('华文行楷',16))
    btn_login.place(x=175, y=250)

    btn_login = tk.Button(window_wzq, text='人人对战',command=wzq.wzq_pvp, bg = '#99cc00', font=('华文行楷',16))
    btn_login.place(x=175, y=310)

    btn_login = tk.Button(window_wzq, text='退出游戏',command=quit_game, bg = '#99cc00', font=('华文行楷',16))
    btn_login.place(x=175, y=370)
    
btn_login = tk.Button(window, text='五子棋',height = 1,width = 19 ,command=start_wzq, bg = '#ffcc66', font=('华文行楷',16))
btn_login.place(x=60, y=310)

btn_login = tk.Button(window, text='井字棋',height = 1,width = 19 ,command=start_jzq, bg = '#ffcc66', font=('华文行楷',16))
btn_login.place(x=60, y=240)

window.mainloop()


