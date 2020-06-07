import tkinter as tk
import tkinter.messagebox
import pickle
import pymysql
import cv2
import os
global basketball_counter
def getnumber():
    global basketball_counter
    conn = pymysql.connect('localhost', 'root', '', 'sport_test')
    cursor = conn.cursor()
    basketball_counter=20
    sql = "SELECT * FROM test WHERE borrow_count > '%d'" % (0)
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        basketball_counter = basketball_counter-int(row[4])
    return basketball_counter

def make():
    global basketball_counter,window
    window = tk.Tk()
    window.title('')
    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    window.geometry("%dx%d" %(w, h))
    def usr_sign_up():
        window_sign_up = tk.Toplevel(window)
        
        h = window_sign_up.winfo_screenwidth()
        w = window_sign_up.winfo_screenheight()
        window_sign_up.geometry('%dx%d' %(h, w))
        window_sign_up.title('借球')


        cap = cv2.VideoCapture(0)
        conn = pymysql.connect('localhost', 'root', '', 'sport_test')
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
            global basketball_counter,window
            a=entry_usr_name.get()
            b=entry_usr_name1.get()
            c=entry_usr_name2.get()
            d=entry_usr_name3.get()
            e=entry_usr_name4.get()


            #修改部分
            if basketball_counter-int(e)<0:
                basketball_counter=10000+basketball_counter
                window_sign_up.destroy()
                window.destroy()
            #截止
            else :
                f=a + "-" + b + "-" + c + "-" + d + "-" + e + ".jpg"
                g=a + "," + b + "," + c + ",'" + d + "'," + e
                while True:
                    ret, frame = cap.read()
                    cv2.imshow("frame",frame)
                    if cv2.waitKey(1) & 0xFF == 27:
                        cv2.imencode('.jpg',frame)[1].tofile(f)
                        break
                        os.exit()
                sql = "INSERT INTO test(grade,class,number,name,borrow_count) VALUES (" + g + ")"
                try:
                    cursor.execute(sql)
                    conn.commit()
                    basketball_counter=getnumber()
                    tk.Label(window, text='剩余数量'+str(basketball_counter), font=('Arial', 14)).place(x=100, y=150)
                except:
                    conn.rollback()
                    conn.close()
                cap.release()
                cv2.destroyAllWindows()
                
                window_sign_up.destroy()
                window.destroy()
        login = tk.Button(window_sign_up, text='确定', command=usr_login)
        login.place(x=200, y=300)

    def sign_up():
        sign_up = tk.Toplevel(window)
        h = sign_up.winfo_screenwidth()
        w = sign_up.winfo_screenheight()
        sign_up.geometry('%dx%d' %(h, w))
        sign_up.title('还球')

        conn = pymysql.connect('localhost', 'root', '', 'sport_test')
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

            #sql='DELETE FROM user WHERE 1'

            sql = 'DELETE FROM test WHERE grade = '+ a +' and class = '+ b +' and number = '+ c +' and name = '+ d +' and borrow_count = '+ e
            try:
                cursor.execute(sql)
                conn.commit()
                basketball_counter=getnumber()
            except:
                conn.rollback()
                conn.close()
            sign_up.destroy()
            window.destroy()

            

        login = tk.Button(sign_up, text='确定', command=usr_login)
        login.place(x=200, y=300)

    btn_login = tk.Button(window, text='借球', command=usr_sign_up)
    btn_login.place(x=100, y=100)

    btn_login = tk.Button(window, text='还球', command=sign_up)
    btn_login.place(x=200, y=100)

    conn = pymysql.connect('localhost', 'root', '', 'sport_test')
    cursor = conn.cursor()
    basketball_counter=getnumber()
    tk.Label(window, text='剩余数量'+str(basketball_counter), font=('Arial', 14)).place(x=100, y=150)  

    window.mainloop()

    return basketball_counter    

# a=make()
# print(a)
