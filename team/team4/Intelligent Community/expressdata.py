import pymysql
import cv2
from pyzbar import pyzbar
from MyQR import myqr
import tkinter as tk
from xpinyin import Pinyin
import tkinter.messagebox as tkm

def adduser():
    conn = pymysql.connect('localhost', 'root', '', 'expressbox')
    cursor = conn.cursor()   

    for i in range(1,13):
        if i<3:
            a='1-10'+str(i)
        elif i<5:
            a='1-20'+str(i-2)
        elif i<7:
            a='1-30'+str(i-4)
        elif i<9:
            a='2-10'+str(i-6)
        elif i<11:
            a='2-20'+str(i-8)
        else:
            a='2-30'+str(i-10)
        print(a)
        res=str(i)+','+ "'"+a+"'"
        sql = "INSERT INTO user(bianhao,password) VALUES (" + res + ")"
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()
            conn.close()
def makedemo():
    conn = pymysql.connect('localhost', 'root', '', 'expressbox')
    cursor = conn.cursor()

    sql="SELECT * FROM user"
    cursor.execute(sql)
    results = cursor.fetchall()

    for row in results:
        myqr.run(words=row[0]+','+row[1],save_name='user'+'\\'+row[0]+'_'+row[1]+'.jpg')

def getinfo(name):
    conn = pymysql.connect('localhost', 'root', '', 'expressbox')
    cursor = conn.cursor()
    sql = "SELECT * FROM userinfo WHERE name = '%s'" % name
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        return row[1]
    return 0

#数据库信息对比
def compared(result,apartment): 
    conn = pymysql.connect('localhost', 'root', '', 'expressbox')
    cursor = conn.cursor()   
    sql = "SELECT * FROM apartment"+str(apartment)+" WHERE id = '%s'" % result[1]
    cursor.execute(sql)
    name= cursor.fetchall()
    def getPinYin(result):
        pin = Pinyin()
        return pin.get_pinyin(result)
    def delate(reset,apartment):
        conn = pymysql.connect('localhost', 'root', '', 'expressbox')
        cursor = conn.cursor()
        sql ="DELETE FROM apartment"+str(apartment)+" WHERE id = \'" + reset + "\'"
        cursor.execute(sql)
        conn.commit()
        
    for n in name:
        if getPinYin(n[0]) == result[0]:
            delate(result[1],apartment)
            return 1 #可以开门
        else:
            return 0 #不可以

def info():
    window = tk.Tk()
    window.title('信息录入')
    window.geometry("500x300")

    tk.Label(window, text='姓名', font=('Arial', 14)).place(x=20, y=50)
    tk.Label(window, text='身份证号', font=('Arial', 14)).place(x=20,y=90)
    tk.Label(window, text='单元号', font=('Arial', 14)).place(x=20,y=140)
    tk.Label(window, text='单元号请输入你要进入的单元用‘,’隔开', font=('Arial', 14)).place(x=20,y=190)

    var_usr_name = tk.StringVar()
    entry_usr_name = tk.Entry(window,textvariable=var_usr_name,font=('Arial', 14))
    entry_usr_name.place(x=120, y=50)

    var_usr_name = tk.StringVar()
    entry_usr_name1 = tk.Entry(window,textvariable=var_usr_name,font=('Arial', 14))
    entry_usr_name1.place(x=120, y=90)

    var_usr_name = tk.StringVar()
    entry_usr_name2 = tk.Entry(window,textvariable=var_usr_name,font=('Arial', 14))
    entry_usr_name2.place(x=120, y=140)

    def courier_info():
        a = entry_usr_name.get()
        b = entry_usr_name1.get()
        c = entry_usr_name2.get()

        def getPinYin(result):
            pin = Pinyin()
            return pin.get_pinyin(result)

        name=getPinYin(a)
        myqr.run(words=name+','+b,save_name='courier'+'\\'+a+'.jpg')

        res="'"+a+"'"+','+"'"+b+"'"
        apartment=c.split(',')
        conn = pymysql.connect('localhost', 'root', '', 'expressbox')
        cursor = conn.cursor()
        for i in apartment:
            sql = "INSERT INTO apartment"+str(i)+"(name,id) VALUES (" + res + ")"
            try:
                cursor.execute(sql)
                conn.commit()
            except:
                conn.rollback()
                conn.close()
        tkm.showinfo('提示', '信息录入成功！')       
        window.destroy()
        img=cv2.imread('courier'+'\\'+a+'.jpg')
        cv2.imshow('save_QRcode_please',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
            
    login = tk.Button(window, text='确定', command=courier_info)
    login.place(x=80, y=250)
    window.mainloop()
def user_info(num):
    conn = pymysql.connect('localhost', 'root', '', 'expressbox')
    cursor = conn.cursor()

    sql = "SELECT * FROM usercar WHERE licenseplate = '%s'" % num

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            return row  # 返回值格式(车牌, 用户名, 车位序号)
    except:
        conn.rollback()
        conn.close()
        return 0  # 外来车辆

# num:车牌号。字符类型
def delate(num):
    conn = pymysql.connect('localhost', 'root', '', 'expressbox')
    cursor = conn.cursor()
    sql = "DELETE FROM licenseplate WHERE number = \'" + num + "\'"
    cursor.execute(sql)
    conn.commit()

# num:车牌号。字符类型
def car_add(num):
    conn = pymysql.connect('localhost', 'root', '', 'expressbox')
    cursor = conn.cursor()
    res="'"+num+"','0'"
    sql = "INSERT INTO licenseplate(number,state) VALUES (" + res + ")"
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
        conn.close()