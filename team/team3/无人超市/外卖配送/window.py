import tkinter as tk
import tkinter.messagebox
import pickle
import pymysql
import cv2
import os
#from MXMqtt import MXMqtt
#MQTTHOST = "mqtt.16302.com"
#MQTTPORT = 1883
#mqtt = MXMqtt(MQTTHOST,MQTTPORT)
window = tk.Tk()
window.title('美团外卖')
window.geometry("%dx%d" %(500,700))
a = tk.PhotoImage(file="1.gif")
b = tk.PhotoImage(file="2.gif")
imgLabel = tk.Label(window,image=a)
imgLabel.pack(side=tk.LEFT)
def send():
    import 外卖配送
def start():
    window1 = tk.Toplevel(window)
    window1.geometry("%dx%d" %(500,700))
    window1.title('无人超市外卖')
    imgLabel = tk.Label(window1,image=b)
    imgLabel.pack(side=tk.RIGHT)

    tk.Label(window1, text='商品名', font=('Arial', 14)).place(x=30, y=180)
    tk.Label(window1, text='单价', font=('Arial', 14)).place(x=300, y=180)
    tk.Label(window1, text='件数', font=('Arial', 14)).place(x=380, y=180)
    
    tk.Label(window1, text='欧莱雅男士洁面乳', font=('Arial', 14)).place(x=30, y=220)
    tk.Label(window1, text='39元', font=('Arial', 14)).place(x=300, y=220)
    var = tk.StringVar()
    entry = tk.Entry(window1, textvariable=var ,width = 5,font=('Arial', 14))
    entry.place(x=380,y=220)

    tk.Label(window1, text='九制陈皮', font=('Arial', 14)).place(x=30, y=260)
    tk.Label(window1, text='29元', font=('Arial', 14)).place(x=300, y=260)
    var = tk.StringVar()
    entry = tk.Entry(window1, textvariable=var ,width = 5,font=('Arial', 14))
    entry.place(x=380,y=260)

    tk.Label(window1, text='农夫山泉', font=('Arial', 14)).place(x=30, y=300)
    tk.Label(window1, text='2元', font=('Arial', 14)).place(x=300, y=300)
    var = tk.StringVar()
    entry = tk.Entry(window1, textvariable=var ,width = 5,font=('Arial', 14))
    entry.place(x=380,y=300)
    
    tk.Label(window1, text='《追风筝的人》', font=('Arial', 14)).place(x=30, y=340)
    tk.Label(window1, text='29元', font=('Arial', 14)).place(x=300, y=340)
    var = tk.StringVar()
    entry = tk.Entry(window1, textvariable=var ,width = 5,font=('Arial', 14))
    entry.place(x=380,y=340)

    tk.Label(window1, text='《阿波罗是如何飞到月球的》', font=('Arial', 14)).place(x=30, y=380)
    tk.Label(window1, text='69元', font=('Arial', 14)).place(x=300, y=380)
    var = tk.StringVar()
    entry = tk.Entry(window1, textvariable=var ,width = 5,font=('Arial', 14))
    entry.place(x=380,y=380)
    
    tk.Label(window1, text='德生牌收音机PL-380', font=('Arial', 14)).place(x=30, y=420)
    tk.Label(window1, text='399元', font=('Arial', 14)).place(x=300, y=420)
    var = tk.StringVar()
    entry = tk.Entry(window1, textvariable=var ,width = 5,font=('Arial', 14))
    entry.place(x=380,y=420)
    
    tk.Label(window1, text='清扬洗发露200g', font=('Arial', 14)).place(x=30, y=460)
    tk.Label(window1, text='28元', font=('Arial', 14)).place(x=300, y=460)
    var = tk.StringVar()
    entry = tk.Entry(window1, textvariable=var ,width = 5,font=('Arial', 14))
    entry.place(x=380,y=460)
    
    tk.Label(window1, text='《生死疲劳》', font=('Arial', 14)).place(x=30, y=500)
    tk.Label(window1, text='39元', font=('Arial', 14)).place(x=300, y=500)
    var = tk.StringVar()
    entry = tk.Entry(window1, textvariable=var ,width = 5,font=('Arial', 14))
    entry.place(x=380,y=500)

    btn_login = tk.Button(window1, text='立即下单',width = 14 ,command=send, font=('黑体',20))
    btn_login.place(x=145, y=600)
    
btn_login = tk.Button(window, text='立即下单',width = 14 ,command=start, bg = '#fed731', font=('黑体',20))
btn_login.place(x=145, y=490)


window.mainloop()


