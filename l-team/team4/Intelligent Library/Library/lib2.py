import tkinter as tk
import tkinter.messagebox as tkm
import pymysql
import threading
import baidusound as bs
import QRcode as qr
import manage
from PIL import Image,ImageTk

conn = pymysql.connect('localhost', 'root', '', 'library')
cursor = conn.cursor()

window = tk.Tk()
window.title('library')
window.geometry("600x400")
img = Image.open('picture\\library.jpg')
photo = ImageTk.PhotoImage(img)
tk.Label(window,image=photo).place(x=200,y=100)
tk.Label(window,fg='blue',text='欢迎来到上海电力大学图书馆',font=('Arial', 14)).place(x=150,y=40)

global order
order=""

def getuserinfo(number):
    info = ["0", "0", "0"]
    conn = pymysql.connect('localhost', 'root', '', 'library')
    cursor = conn.cursor()
    sql = "SELECT * FROM user WHERE number = '%d'" % int(number)
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        info[0] = row[1]  #姓名
        info[1] = row[2]  #密码
    return info

def get_ones_borrowed_book(name):
    i=0
    conn = pymysql.connect('localhost', 'root', '', 'library')
    cursor = conn.cursor()
    sql = "SELECT * FROM borrowed_books WHERE borrower = '%s'" % name
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        i+=1
    return i


def getbooksplace(name):
    conn = pymysql.connect('localhost', 'root', '', 'library')
    cursor = conn.cursor()
    sql = "SELECT * FROM books WHERE bookname = '%s'" % name
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        place = row[1]
    place = place.split("-")
    goal = "您找的书在第" + str(int(place[0])) + "层，" + str(int(
        place[1])) + "号书架的第" + str(int(place[2])) + "层"
    return goal


def scan(bookname):
    conn = pymysql.connect('localhost', 'root', '', 'library')
    cursor = conn.cursor()
    #首先检测是否在lost内
    sql = "SELECT * FROM lost_books"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        if bookname == row[0]:
            return False
    #不在lost内就查询当前二维码
    if qr.scanqr(bookname):
        return True
    #未找到目标书籍则加入lost库
    sql1 = "update books set state2= 1 where bookname=\'" + bookname + "\'"
    sql2 = "INSERT INTO lost_books(bookname) VALUES (\'" + bookname + "\')"
    try:
        cursor.execute(sql1)
        conn.commit()
        cursor.execute(sql2)
        conn.commit()
        return False
    except:
        conn.rollback()
        conn.close()


def getbook():
    length = 0
    i = 0
    conn = pymysql.connect('localhost', 'root', '', 'library')
    cursor = conn.cursor()
    sql = "SELECT * FROM books"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        length += 1
    books = ['0' for index in range(length)]
    for row in results:
        books[i] = row[0]
        i += 1
    return books



def get_borrowed_book():
    length = 0
    i = 0

    conn = pymysql.connect('localhost', 'root', '', 'library')
    cursor = conn.cursor()
    sql = "SELECT * FROM borrowed_books"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        length += 1
    books = ['0' for index in range(length)]
    for row in results:
        books[i] = row[0]
        i += 1
    return books


def borrow():
    global order
    bs.record()
    order = bs.w2p()


def say():
    global speak
    bs.speak(speak)


def user():
    global photo1
    window_user = tk.Toplevel(window)
    window_user.geometry('600x400')
    window_user.title('用户界面')
    img = Image.open('picture\\jiehuan.jpg')
    photo1 = ImageTk.PhotoImage(img)
    tk.Label(window_user,image=photo1).place(x=200,y=100)

    btn_login = tk.Button(window_user, text='借书', command=borrow_book)
    btn_login.place(x=50, y=100)

    btn_login = tk.Button(window_user, text='还书', command=back_book)
    btn_login.place(x=50, y=200)

    



def register():
    window_register = tk.Toplevel(window)
    window_register.geometry('600x400')
    window_register.title('注册')

    # tk.Label(window_register, text='年级', font=('Arial', 14)).place(x=10, y=90)
    # tk.Label(window_register, text='班级', font=('Arial', 14)).place(x=10, y=130)
    tk.Label(window_register, text='学号', font=('Arial', 14)).place(x=10, y=90)
    tk.Label(window_register, text='用户名', font=('Arial', 14)).place(x=10,y=130)
    tk.Label(window_register, text='密码', font=('Arial', 14)).place(x=10, y=170)
    tk.Label(window_register, text='确认密码', font=('Arial', 14)).place(x=10, y=210)

    var_usr_name = tk.StringVar()
    entry_usr_name = tk.Entry(window_register,
                              textvariable=var_usr_name,
                              font=('Arial', 14))
    entry_usr_name.place(x=120, y=90)

    var_usr_name = tk.StringVar()
    entry_usr_name1 = tk.Entry(window_register,
                               textvariable=var_usr_name,
                               font=('Arial', 14))
    entry_usr_name1.place(x=120, y=130)

    var_usr_name = tk.StringVar()
    entry_usr_name2 = tk.Entry(window_register,
                               textvariable=var_usr_name,
                               font=('Arial', 14),
                               show='*')
    entry_usr_name2.place(x=120, y=170)

    var_usr_name = tk.StringVar()
    entry_usr_name3 = tk.Entry(window_register,
                               textvariable=var_usr_name,
                               font=('Arial', 14),
                               show='*')
    entry_usr_name3.place(x=120, y=210)

    # var_usr_name = tk.StringVar()
    # entry_usr_name4 = tk.Entry(window_register, textvariable=var_usr_name, font=('Arial', 14),show='*')
    # entry_usr_name4.place(x=120,y=250)

    # var_usr_name = tk.StringVar()
    # entry_usr_name5 = tk.Entry(window_register, textvariable=var_usr_name, font=('Arial', 14),show='*')
    # entry_usr_name5.place(x=120,y=290)

    def password_check():
        e = entry_usr_name2.get()
        h = entry_usr_name3.get()
        if e == h:
            getinfo()
        else:
            tk.Label(window_register,
                     fg='red',
                     text='请确保两次输入密码一致',
                     font=('Arial', 14)).place(x=10, y=10)

    def getinfo():
        conn = pymysql.connect('localhost', 'root', '', 'library')
        cursor = conn.cursor()

        a = entry_usr_name.get()
        b = entry_usr_name1.get()
        c = entry_usr_name2.get()

        g = a + ",\'" + b + "\'," + c
        sql = "INSERT INTO user(number,name,password) VALUES (" + g + ")"
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()
            conn.close()

        window_register.destroy()

    login = tk.Button(window_register, text='确定', command=password_check)
    login.place(x=200, y=330)


def sign_in():
    window_login = tk.Toplevel(window)
    window_login.geometry('600x400')
    window_login.title('登录')

    tk.Label(window_login, text='学号', font=('Arial', 14)).place(x=10, y=90)
    tk.Label(window_login, text='密码', font=('Arial', 14)).place(x=10, y=130)

    var_usr_name = tk.StringVar()
    entry_usr_name = tk.Entry(window_login,
                              textvariable=var_usr_name,
                              font=('Arial', 14))
    entry_usr_name.place(x=120, y=90)

    var_usr_name = tk.StringVar()
    entry_usr_name1 = tk.Entry(window_login,
                               textvariable=var_usr_name,
                               font=('Arial', 14),
                               show='*')
    entry_usr_name1.place(x=120, y=130)

    def usr_panduan():
        global name
        number_inputed = entry_usr_name.get()
        password_inputed = entry_usr_name1.get()
        password_got = getuserinfo(number_inputed)[1]
        if password_got == password_inputed:
            tkm.showinfo('提示', '登录成功！')
            window_login.destroy()
            name = getuserinfo(number_inputed)[0]
            #window.destroy()
            user()
            #tk.Label(window_login, text='登陆成功', font=('Arial', 14)).place(x=10, y=150)
        else:
            tk.Label(window_login, text='用户名或密码错误',
                     font=('Arial', 14)).place(x=10, y=150)
        #window_login.destroy()

    log = tk.Button(window_login, text='登录', command=usr_panduan)
    log.place(x=200, y=300)


def borrow_book():
    global order, name, photo2
    window_borrow = tk.Toplevel()
    window_borrow.geometry("600x400")
    window_borrow.title('借书')

    img = Image.open('picture\\jieshu.jpg')
    photo2 = ImageTk.PhotoImage(img)
    tk.Label(window_borrow,image=photo2).place(x=400,y=100)

    tk.Label(window_borrow, text='请在开始录音后后，说出要添加的书名',
             font=('Arial', 14)).place(x=50, y=50)
    tk.Label(window_borrow, text='若未正确读取，请再次点击开始录音',
             font=('Arial', 14)).place(x=50, y=100)
    tk.Label(window_borrow, text='正确识别书名后，点击确定',
             font=('Arial', 14)).place(x=50, y=150)

    def waitorder():
        global order
        
        yuyin=threading.Thread(target=borrow)
        yuyin.start()
        yuyin.join()
        tk.Label(window_borrow, text='您是否要找'+order+'      ',font=('Arial', 14)).place(x=50, y=200)

    def getinfo():
        global speak
        conn = pymysql.connect('localhost', 'root', '', 'library')
        cursor = conn.cursor()
        a = order
        #判断是否收录
        if a != "":
            books = getbook()
            if a in books:
                #判断是否已借出
                books = get_borrowed_book()
                if a not in books:
                    #扫描二维码，判断书是否在书架上
                    if scan(a):
                        res = "'" + a + "'" + "," + "'" + name + "'" + "," "0" + "," + "1"
                        sql1 = "update books set state1=" + '0' + ',state2=' + '1' + " where bookname=\'" + a + "\'"
                        sql2 = "INSERT INTO borrowed_books(bookname,borrower,state1,state2) VALUES (" + res + ")"
                        try:
                            speak = "请按照提示位置去取书"
                            threading.Thread(target=say).start()
                            place = getbooksplace(a)
                            tkm.showinfo('提示', place)
                            cursor.execute(sql1)
                            conn.commit()
                            cursor.execute(sql2)
                            conn.commit()
                            tk.Label(window_borrow, text='                                                  ', font=('Arial', 14)).place(x=50, y=200)
                            #os.remove('test\\'+a+'.jpg')
                        except:
                            conn.rollback()
                            conn.close()
                    else:
                        tkm.showinfo('提示', a + "丢失，请等待管理员找回")
                else:
                    tkm.showinfo('提示', a + "已借出，请换本书吧")
            else:
                tkm.showinfo('提示', a + "未收录")

        #window_borrow.destroy()
        #window.destroy()
    def exxit():
        window_borrow.destroy()

    def judgenumber():
        global name,order
        if get_ones_borrowed_book(name)<=2:
            waitorder()
            tk.Label(window_borrow, text='           ', font=('Arial', 14)).place(x=100, y=250)
        else:
            tk.Label(window_borrow, text='借书已达上限', font=('Arial', 14)).place(x=100, y=250)
            order=""

    login = tk.Button(window_borrow, text='开始录音', command=judgenumber)
    login.place(x=200, y=300)
    login = tk.Button(window_borrow, text='确定', command=getinfo)
    login.place(x=300, y=300)
    login = tk.Button(window_borrow, text='退出', command=exxit)
    login.place(x=400, y=300)


def back_book():
    global photo3
    conn = pymysql.connect('localhost', 'root', '', 'library')
    cursor = conn.cursor()
    global order, name
    length = 0
    y_place = 2
    number = 0
    window_back = tk.Toplevel()
    window_back.geometry('600x400')
    window_back.title('还书')

    img = Image.open('picture\\huanshu.jpg')
    photo3 = ImageTk.PhotoImage(img)
    tk.Label(window_back,image=photo3).place(x=300,y=100)

    tk.Label(window_back, text='请选择要还的书', font=('Arial', 14)).place(x=50, y=50)
    sql = "SELECT * FROM borrowed_books WHERE borrower = '%s'" % name
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        length += 1
    names = [0 for index in range(length)]

    # def waitorder():
    #     yuyin=threading.Thread(target=back)
    #     yuyin.start()

    def getinfo(i):
        global speak
        a = names[i]
        sql1 = 'DELETE FROM borrowed_books WHERE bookname = \'' + a + '\' and state1 = ' + '0' + ' and state2 = ' + '1'
        sql2 = "update books set state1=" + '1' + ',state2=' + '1' + " where bookname=\'" + a + "\'"
        # try:
        cursor.execute(sql1)
        conn.commit()
        cursor.execute(sql2)
        conn.commit()
        speak = "还书成功，欢迎下次再来"
        threading.Thread(target=say).start()
        if i == 0:
            btn1.destroy()
            tk.Label(window_back, text="已还", font=('Arial', 14)).place(x=250,y=100)
        elif i == 1:
            btn2.destroy()
            tk.Label(window_back, text="已还", font=('Arial', 14)).place(x=250,y=150)
        elif i == 2:
            btn3.destroy()
            tk.Label(window_back, text="已还", font=('Arial', 14)).place(x=250,y=200)
        # except:
        #     conn.rollback()
        #     conn.close()
        #window_back.destroy()
        #window.destroy()

    def exxit():
        window_back.destroy()

    for row in results:
        text = row[0]
        names[number] = text
        # tk.Label(window_back, text=text, font=('Arial', 14)).place(x=50, y=y_place*50)
        # btn_login = tk.Button(window_back, text='还书', command=lambda: getinfo(number))
        # btn_login.place(x=250, y=y_place*50)
        y_place += 1
        number += 1

    if y_place > 2:
        tk.Label(window_back, text=names[0], font=('Arial', 14)).place(x=50,y=100)
        btn1 = tk.Button(window_back, text='还书', command=lambda: getinfo(0))
        btn1.place(x=250, y=100)
    if y_place > 3:
        tk.Label(window_back, text=names[1], font=('Arial', 14)).place(x=50,y=150)
        btn2 = tk.Button(window_back, text='还书', command=lambda: getinfo(1))
        btn2.place(x=250, y=150)
    if y_place > 4:
        tk.Label(window_back, text=names[2], font=('Arial', 14)).place(x=50,y=200)
        btn3 = tk.Button(window_back, text='还书', command=lambda: getinfo(2))
        btn3.place(x=250, y=200)

    login = tk.Button(window_back, text='退出', command=exxit)
    login.place(x=300, y=300)


btn_login = tk.Button(window, text='注册', command=register)
btn_login.place(x=100, y=100)

btn_login = tk.Button(window, text='登录', command=sign_in)
btn_login.place(x=100, y=160)

btn_login = tk.Button(window, text='管理员登录', command=manage.manage_login)
btn_login.place(x=100, y=220)

getbook()
#scan("水浒传")
window.mainloop()
