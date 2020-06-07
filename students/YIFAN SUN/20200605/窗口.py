import tkinter as tk
import tkinter.messagebox
import pickle
import pymysql
import cv2
import os

window = tk.Tk()
window.title('')
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
window.geometry("%dx%d" %(w, h))

conn = pymysql.connect('localhost', 'root', '', 'mysql')
cursor = conn.cursor()
sql = "UPDATE basketball SET borrow_left='30' "
print("欢迎使用本系统，篮球储备：30")
try:
    cursor.execute(sql)
    conn.commit()
except:
    conn.rollback()
    conn.close()
        
def usr_sign_up():
    window_sign_up = tk.Toplevel(window)
    h = window_sign_up.winfo_screenwidth()
    w = window_sign_up.winfo_screenheight()
    window_sign_up.geometry('%dx%d' %(h, w))
    window_sign_up.title('借球')

    cap = cv2.VideoCapture(0)
    conn = pymysql.connect('localhost', 'root', '', 'mysql')
    cursor = conn.cursor()
    
    tk.Label(window_sign_up, text='年级', font=('Arial', 14)).place(x=10, y=90)
    tk.Label(window_sign_up, text='班级', font=('Arial', 14)).place(x=10, y=130)
    tk.Label(window_sign_up, text='学号', font=('Arial', 14)).place(x=10, y=170)
    tk.Label(window_sign_up, text='姓名', font=('Arial', 14)).place(x=10, y=210)
    tk.Label(window_sign_up, text='数量(球)', font=('Arial', 14)).place(x=10, y=250)

    var_usr_name = tk.StringVar()
    entry_usr_name = tk.Entry(window_sign_up, textvariable=var_usr_name, font=('Arial', 14))
    entry_usr_name.place(x=120,y=90)

    var_usr_name = tk.StringVar()
    entry_usr_name1 = tk.Entry(window_sign_up, textvariable=var_usr_name, font=('Arial', 14))
    entry_usr_name1.place(x=120,y=130)

    var_usr_name = tk.StringVar()
    entry_usr_name2 = tk.Entry(window_sign_up, textvariable=var_usr_name, font=('Arial', 14))
    entry_usr_name2.place(x=120,y=170)

    var_usr_name = tk.StringVar()
    entry_usr_name3 = tk.Entry(window_sign_up, textvariable=var_usr_name, font=('Arial', 14))
    entry_usr_name3.place(x=120,y=210)

    var_usr_name = tk.StringVar()
    entry_usr_name4 = tk.Entry(window_sign_up, textvariable=var_usr_name, font=('Arial', 14))
    entry_usr_name4.place(x=120,y=250)

    def usr_login():
        a=entry_usr_name.get()
        b=entry_usr_name1.get()
        c=entry_usr_name2.get()
        d=entry_usr_name3.get()
        e=entry_usr_name4.get()
        f=a + "-" + b + "-" + c + "-" + d + "-" + e + ".jpg"
        g=a + "," + b + "," + c + ",'" + d + "'," + e
        #while True:
           # ret, frame = cap.read()
           # cv2.imshow("frame",frame)
           # if cv2.waitKey(1) & 0xFF == 27:
             #   cv2.imencode('.jpg',frame)[1].tofile(f)
             #   break
              #  os.exit()
        sql = "INSERT INTO borrow VALUES (" + g + ")"
        sqlcmd ="SELECT * FROM basketball"
        cursor.execute(sqlcmd)
        D = cursor.fetchone()
        count = int(D[0])-int(e)
        if count >= 0:
            sqlfinal = "UPDATE basketball SET borrow_left='%s' "%(str(count))
            
            try:
                cursor.execute(sql)
                cursor.execute(sqlfinal)
                print("借球成功，剩余数量:%s"%(str(count)))
                conn.commit()
            except:
                conn.rollback()
                conn.close()
        else:
            print("借球数太多，请重新借")
        cap.release()
        cv2.destroyAllWindows()
        
        window_sign_up.destroy()
        
    login = tk.Button(window_sign_up, text='确定', command=usr_login)
    login.place(x=200, y=300)

def sign_up():
    sign_up = tk.Toplevel(window)
    h = sign_up.winfo_screenwidth()
    w = sign_up.winfo_screenheight()
    sign_up.geometry('%dx%d' %(h, w))
    sign_up.title('还球')

    conn = pymysql.connect('localhost', 'root', '', 'mysql')
    cursor = conn.cursor()

    tk.Label(sign_up, text='年级', font=('Arial', 14)).place(x=10, y=90)
    tk.Label(sign_up, text='班级', font=('Arial', 14)).place(x=10, y=130)
    tk.Label(sign_up, text='学号', font=('Arial', 14)).place(x=10, y=170)
    tk.Label(sign_up, text='姓名', font=('Arial', 14)).place(x=10, y=210)
    tk.Label(sign_up, text='数量(球)', font=('Arial', 14)).place(x=10, y=250)

    var_usr_name = tk.StringVar()
    entry_usr_name = tk.Entry(sign_up, textvariable=var_usr_name, font=('Arial', 14))
    entry_usr_name.place(x=120,y=90)

    var_usr_name = tk.StringVar()
    entry_usr_name1 = tk.Entry(sign_up, textvariable=var_usr_name, font=('Arial', 14))
    entry_usr_name1.place(x=120,y=130)

    var_usr_name = tk.StringVar()
    entry_usr_name2 = tk.Entry(sign_up, textvariable=var_usr_name, font=('Arial', 14))
    entry_usr_name2.place(x=120,y=170)

    var_usr_name = tk.StringVar()
    entry_usr_name3 = tk.Entry(sign_up, textvariable=var_usr_name, font=('Arial', 14))
    entry_usr_name3.place(x=120,y=210)

    var_usr_name = tk.StringVar()
    entry_usr_name4 = tk.Entry(sign_up, textvariable=var_usr_name, font=('Arial', 14))
    entry_usr_name4.place(x=120,y=250)

    def usr_login():
        a=entry_usr_name.get()
        b=entry_usr_name1.get()
        c=entry_usr_name2.get()
        d=entry_usr_name3.get()
        e=entry_usr_name4.get()
        sqlcmd ="SELECT * FROM basketball"
        cursor.execute(sqlcmd)
        D = cursor.fetchone()
        sqlball ="SELECT borrow_count FROM borrow"
        cursor.execute(sqlball)
        C = cursor.fetchone()
        f = int(C[0])- int(e)
        count1 = int(D[0])+int(e)
        if f == 0:
            sql = "DELETE FROM `mysql`.`borrow` WHERE `borrow`.`grade` = \'%s\' AND `borrow`.`class` = \'%s\' AND `borrow`.`number` = \'%s\' AND `borrow`.`name` = \'%s\' AND `borrow`.`borrow_count` = \'%s\' LIMIT 1 "%(a,b,c,d,e)
            print("还球成功，您的所有篮球都已还完")
        elif f > 0:
            sql = "UPDATE borrow SET borrow_count='%s' WHERE grade = '%s' AND class = '%s' AND number = '%s' AND name = '%s'"%(str(f),a,b,c,d)
            print("还球成功，剩余%s个未还"%(str(f)))
        else:
            print("错误，重新还球")
        sqlfinal = "UPDATE basketball SET borrow_left='%s' "%(str(count1))
        
        try:
            cursor.execute(sql)
            cursor.execute(sqlfinal)
            print("剩余数量:%s"%(str(count1)))
            conn.commit()
        except:
            conn.rollback()
            conn.close()

        sign_up.destroy()

    login = tk.Button(sign_up, text='确定', command=usr_login)
    login.place(x=200, y=300)

btn_login = tk.Button(window, text='借球', command=usr_sign_up)
btn_login.place(x=100, y=100)

btn_login = tk.Button(window, text='还球', command=sign_up)
btn_login.place(x=200, y=100)

window.mainloop()
       
