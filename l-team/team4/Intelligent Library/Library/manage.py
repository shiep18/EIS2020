import tkinter as tk
import tkinter.messagebox as tkm
import pymysql
import os
import wave2pinyin as w2p
import recordsound as rs
from xpinyin import Pinyin
import threading
import baidusound as bs
import datetime
from MyQR import myqr
from pyzbar import pyzbar
from PIL import Image,ImageTk
global photo4

def say():
    global speak
    bs.speak(speak)


def manage_interface():
    global photo4
    window_manage_interface = tk.Toplevel()
    window_manage_interface.geometry('600x400')
    window_manage_interface.title('管理界面')

    img = Image.open('picture\\qiantai.jpg')
    photo4 = ImageTk.PhotoImage(img)
    tk.Label(window_manage_interface,image=photo4).place(x=200,y=100)

    conn = pymysql.connect('localhost', 'root', '', 'library')
    cursor = conn.cursor()

    def manage_add_book():
        #global order
        window_add = tk.Tk()
        window_add.geometry("600x400")
        window_add.title('添加书')

        tk.Label(window_add, text='书名', font=('Arial', 14)).place(x=10, y=90)
        tk.Label(window_add, text='位置', font=('Arial', 14)).place(x=10, y=130)
        tk.Label(window_add, text='位置请按楼层-书架号-书架层数的格式', font=('Arial', 14)).place(x=10, y=170)
        tk.Label(window_add, text='如第3层11号书架的第4层，为03-11-04', font=('Arial', 14)).place(x=10, y=210)

        var_usr_name = tk.StringVar()
        entry_usr_name = tk.Entry(window_add, textvariable=var_usr_name, font=('Arial', 14))
        entry_usr_name.place(x=120,y=90)

        var_usr_name = tk.StringVar()
        entry_usr_name1 = tk.Entry(window_add, textvariable=var_usr_name, font=('Arial', 14))
        entry_usr_name1.place(x=120,y=130)

        def getinfo():
            conn = pymysql.connect('localhost', 'root', '', 'library')
            cursor = conn.cursor()   
            global speak
            a=entry_usr_name.get()
            b=entry_usr_name1.get()
            res="'"+ a + "'" + "," + "'"+ b + "'" + "," + "1" + "," + "1"
            sql = "INSERT INTO books(bookname,place,state1,state2) VALUES (" + res + ")"
            try:
                cursor.execute(sql)
                conn.commit()
                speak="新书添加成功"
                threading.Thread(target=say).start()
            except:
                conn.rollback()
                conn.close()

            window_add.destroy()
            #window.destroy()

        login = tk.Button(window_add, text='确定', command=getinfo)
        login.place(x=300, y=300)

    def manage_user():
        window_manage_user = tk.Toplevel(window_manage_interface)
        window_manage_user.geometry('600x400')
        window_manage_user.title('现有用户')
        conn = pymysql.connect('localhost', 'root', '', 'library')
        cursor = conn.cursor()

        tk.Label(window_manage_user, text='学号', font=('Arial', 14)).place(x=50, y=100,)
        tk.Label(window_manage_user, text='姓名', font=('Arial', 14)).place(x=200, y=100,)

        sql="SELECT * FROM user"
        cursor.execute(sql)
        results = cursor.fetchall()
        i=1
        for row in results:
            tk.Label(window_manage_user, text=row[0], font=('Arial', 14)).place(x=50, y=100+40*i,)
            tk.Label(window_manage_user, text=row[1], font=('Arial', 14)).place(x=200, y=100+40*i,)
            i=i+1
        
        def back():
            window_manage_user.destroy()

        btn = tk.Button(window_manage_user, text='退出', command=back)
        btn.place(x=500, y=300)
    
    def manage_book():
        window_manage_book = tk.Toplevel(window_manage_interface)
        window_manage_book.geometry('700x600')
        window_manage_book.title('已有图书')
        conn = pymysql.connect('localhost', 'root', '', 'library')
        cursor = conn.cursor()

        tk.Label(window_manage_book, text='书名', font=('Arial', 14)).place(x=50, y=100,)
        tk.Label(window_manage_book, text='位置', font=('Arial', 14)).place(x=150, y=100,)
        tk.Label(window_manage_book, text='是否外借(0是/1否)', font=('Arial', 14)).place(x=250, y=100,)
        tk.Label(window_manage_book, text='是否丢失(0是/1否)', font=('Arial', 14)).place(x=450, y=100,)

        sql="SELECT * FROM books"
        cursor.execute(sql)
        results = cursor.fetchall()
        i=1
        for row in results:
            tk.Label(window_manage_book, text=row[0], font=('Arial', 14)).place(x=50, y=100+40*i,)
            tk.Label(window_manage_book, text=row[1], font=('Arial', 14)).place(x=150, y=100+40*i,)
            tk.Label(window_manage_book, text=str(row[2]), font=('Arial', 14)).place(x=350, y=100+40*i,)
            tk.Label(window_manage_book, text=str(row[3]), font=('Arial', 14)).place(x=500, y=100+40*i,)
            i=i+1

        def back():
            window_manage_book.destroy()

        btn = tk.Button(window_manage_book, text='退出', command=back)
        btn.place(x=550, y=550)

    def manage_borrow():
        window_manage_borrow = tk.Toplevel(window_manage_interface)
        window_manage_borrow.geometry('600x400')
        window_manage_borrow.title('已借图书')
        conn = pymysql.connect('localhost', 'root', '', 'library')
        cursor = conn.cursor()

        tk.Label(window_manage_borrow, text='书名', font=('Arial', 14)).place(x=50, y=100,)
        tk.Label(window_manage_borrow, text='姓名', font=('Arial', 14)).place(x=150, y=100,)
        #tk.Label(window_manage_borrow, text='是否归还(1是/0否)', font=('Arial', 14)).place(x=250, y=100,)
    
        sql="SELECT * FROM borrowed_books"
        cursor.execute(sql)
        results = cursor.fetchall()
        i=1
        for row in results:
            tk.Label(window_manage_borrow, text=row[0], font=('Arial', 14)).place(x=50, y=100+40*i,)
            tk.Label(window_manage_borrow, text=row[1], font=('Arial', 14)).place(x=150, y=100+40*i,)
            #tk.Label(window_manage_borrow, text=str(row[2]), font=('Arial', 14)).place(x=250, y=100+40*i,)
            i=i+1

        def back():
            window_manage_borrow.destroy()

        btn = tk.Button(window_manage_borrow, text='退出', command=back)
        btn.place(x=550, y=350)

    def manage_lost():
        window_manage_lost = tk.Toplevel(window_manage_interface)
        window_manage_lost.geometry('600x400')
        window_manage_lost.title('丢失图书')
        conn = pymysql.connect('localhost', 'root', '', 'library')
        cursor = conn.cursor()

        tk.Label(window_manage_lost, text='书名', font=('Arial', 14)).place(x=50, y=100,)
    
        sql="SELECT * FROM  lost_books"
        cursor.execute(sql)
        results = cursor.fetchall()
        i=1
        for row in results:
            tk.Label(window_manage_lost, text=row[0], font=('Arial', 14)).place(x=50, y=100+40*i,)
            i=i+1

        def back():
            window_manage_lost.destroy()

        btn = tk.Button(window_manage_lost, text='退出', command=back)
        btn.place(x=500, y=350)


    btn = tk.Button(window_manage_interface, text='查询用户', command=manage_user)
    btn.place(x=50, y=100)
    btn = tk.Button(window_manage_interface, text='查询借书情况', command=manage_borrow)
    btn.place(x=50, y=150)
    btn = tk.Button(window_manage_interface, text='查询书籍丢失情况', command=manage_lost)
    btn.place(x=50, y=200)
    btn = tk.Button(window_manage_interface, text='查询现有书籍', command=manage_book)
    btn.place(x=50, y=250)
    btn = tk.Button(window_manage_interface, text='添加新书', command=manage_add_book)
    btn.place(x=50, y=300)

def manage_login():
    window_manage = tk.Tk()
    window_manage.geometry('600x400')
    window_manage.title('管理员登录')
    conn = pymysql.connect('localhost', 'root', '', 'library')
    cursor = conn.cursor()
    
    tk.Label(window_manage, text='密码', font=('Arial', 14)).place(x=100, y=150,)
    var_usr_name = tk.StringVar()
    entry_usr_name = tk.Entry(window_manage, textvariable=var_usr_name, font=('Arial', 14),show='*')
    entry_usr_name.place(x=150,y=150)

    def manage_sign_in():
        a=entry_usr_name.get()
        sql = "SELECT * FROM manage"
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            if a in row:
                tkm.showinfo('提示', '登录成功！')
                window_manage.destroy()
                manage_interface()
            else :
                tk.Label(window_manage,fg='red', text='密码错误', font=('Arial', 14)).place(x=100, y=100,)

    btn = tk.Button(window_manage, text='登录', command=manage_sign_in)
    btn.place(x=150, y=200) 

