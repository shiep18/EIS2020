import serial
import tkinter as tk
top = tk.Tk()

ser=serial.Serial("COM12")
ser.write(" ".encode())

def ALL():
    c = "1"
    ser.write(c.encode())
def ZHUAN():
    c = "2"
    ser.write(c.encode())
def F():
    c = "3"
    ser.write(c.encode())
def B():
    c = "4"
    ser.write(c.encode())
def L():
    c = "5"
    ser.write(c.encode())
def R():
    c = "6"
    ser.write(c.encode())
def ORIGIN():
    c = "7"
    ser.write(c.encode())
def POSITION():
    c = "8"
    ser.write(c.encode())
def STOP():
    c = "9"
    ser.write(c.encode())
def ZPOSITION():
    c =input("请指定机器人的坐标，格式为0,x,y:")
    ser.write(c.encode())


top.title("Remote Control")
btn=tk.Button(top,text="搜索",bg="yellow",command = ALL)
btn.place(x=30,y=135)
btn=tk.Button(top,text="转向",bg="yellow",command = ZHUAN)
btn.place(x=95,y=135)
btn=tk.Button(top,text="暂停",bg="yellow",command = STOP)
btn.place(x=155,y=135)
btn=tk.Button(top,text="前",bg="yellow",command = F)
btn.place(x=100,y=50)
btn=tk.Button(top,text="后",bg="yellow",command = B)
btn.place(x=100,y=100)
btn=tk.Button(top,text="左",bg="yellow",command = L)
btn.place(x=50,y=75)
btn=tk.Button(top,text="右",bg="yellow",command = R)
btn.place(x=150,y=75)
btn=tk.Button(top,text="回到起点",bg="green",command = ORIGIN)
btn.place(x=20,y=170)
btn=tk.Button(top,text="现在位置",bg="green",command = POSITION)
btn.place(x=85,y=170)
btn=tk.Button(top,text="指定位置",bg="green",command = ZPOSITION)
btn.place(x=150,y=170)
tk.Label(top,text='高尔夫球捡球机器人遥控器',font=('Arial',10)).place(x=38,y=15)
top.mainloop()


