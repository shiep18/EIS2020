import tkinter as tk
import tkinter.messagebox
import pickle
import pymysql
import cv2
import os
import My_Speech_end
import time
import face_rec
import win32com.client
import MXMqtt as MXMqtt
import time

MQTTHOST = "mqtt.16302.com"
MQTTPORT = 1883
mqtt = MXMqtt.MXMqtt(MQTTHOST,MQTTPORT)

speaker = win32com.client.Dispatch("SAPI.SpVoice")

window = tk.Tk()
window.title('智能篮球借还系统—一号机')
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
window.geometry("%dx%d" %(512, 512))
name = ''
def usr_sign_up():

    window_sign_up = tk.Toplevel(window)
    h = 350
    w = 400
    window_sign_up.geometry('%dx%d' %(h, w))
    window_sign_up.title('借球')

    cap = cv2.VideoCapture(0)
    conn = pymysql.connect('localhost', 'root', '', 'basketball')
    cursor = conn.cursor()

    tk.Label(window_sign_up, text='年级', font=('Arial', 14)).place(x=10, y=90)
    tk.Label(window_sign_up, text='班级', font=('Arial', 14)).place(x=10, y=130)
    tk.Label(window_sign_up, text='学号', font=('Arial', 14)).place(x=10, y=170)
    tk.Label(window_sign_up, text='姓名', font=('Arial', 14)).place(x=10, y=210)
    tk.Label(window_sign_up, text='数量(借球)', font=('Arial', 14)).place(x=10, y=250)

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
    entry_usr_name4 = tk.Label(window_sign_up, text='0', font=('Arial', 14))
    entry_usr_name4.place(x=120,y=250)

    My_Speech_end.intelluct()
    borrow = My_Speech_end.sqlname_backnumber('wzy',1,None,'borrow')
    rest = My_Speech_end.sqlname_backnumber('wzy',1,None,'rest')
    mqtt.PUB("WZY123","1,B"+str(borrow)+","+str(rest))  #发送借球数和球总数 1表示号机B表示借球
    #rest = My_Speech_end.sqlname_backnumber('wzy', 1, None, 'rest')
    entry_usr_name4.config(text = '%s'%borrow)
    def usr_login():
        global name
        name = entry_usr_name3.get()
        num = 0
        a=entry_usr_name.get()
        b=entry_usr_name1.get()
        c=entry_usr_name2.get()
        d=entry_usr_name3.get()
        e=entry_usr_name4.cget('text')
        f=a + "-" + b + "-" + c + "-" + d + "-" + e + ".jpg"
        g=a + "," + b + "," + c + ",'" + d + "'," + e
        #print(type(g))
        print("即将录入您的人脸，请对准摄像头")
        speaker.Speak("即将录入您的人脸，请对准摄像头")
        while True:
            ret, frame = cap.read()
            cv2.imshow("frame",frame)
            cv2.imencode('.jpg',frame)[1].tofile(d+str(num)+".jpg") #存图片
            face_rec.face_register('./'+d+str(num)+".jpg",d,d+str(num)) #人脸注册
            num += 1 
            cv2.waitKey(2000)
            if num>3: #读取三张图片
                break
                #os.exit()
        fp = open(d+"0.jpg", 'rb')
        img = fp.read()
        fp.close()
        sql = "INSERT INTO basketball (`grade`, `class`, `number`, `name`, `borrow_count`,`pic`) VALUES  ( %s,%s,%s,%s,%s,%s );"
        args = (a,b,c,d,e,img)
        try:
            cursor.execute(sql,args)
            conn.commit()
            print("new1")
        except pymysql.Error as e:
            print(e.args[0], e.args[1])
            conn.rollback()
            conn.close()
        cap.release()
        cv2.destroyAllWindows()
        print("人脸录入完成，借球成功")
        speaker.Speak("人脸录入完成，借球成功")
        
        window_sign_up.destroy()
        
    login = tk.Button(window_sign_up, text='确定', command=usr_login)
    login.place(x=200, y=300)

def sign_up():
    global name #这样必须先注册再还球
    sign_up = tk.Toplevel(window)
    h = 350
    w = 400
    sign_up.geometry('%dx%d' %(h, w))
    sign_up.title('还球')
    cap = cv2.VideoCapture(0)

    conn = pymysql.connect('localhost', 'root', '', 'basketball')
    cursor = conn.cursor()

    
    tk.Label(sign_up, text='年级', font=('Arial', 14)).place(x=10, y=90)
    tk.Label(sign_up, text='班级', font=('Arial', 14)).place(x=10, y=130)
    tk.Label(sign_up, text='学号', font=('Arial', 14)).place(x=10, y=170)
    tk.Label(sign_up, text='姓名', font=('Arial', 14)).place(x=10, y=210)
    tk.Label(sign_up, text='还球数', font=('Arial', 14)).place(x=10, y=250)

    var_usr_name = tk.StringVar()
    entry_usr_name = tk.Label(sign_up, text='0', font=('Arial', 14))
    entry_usr_name.place(x=120,y=90)

    var_usr_name = tk.StringVar()
    entry_usr_name1 = tk.Label(sign_up,text='0', font=('Arial', 14))
    entry_usr_name1.place(x=120,y=130)

    var_usr_name = tk.StringVar()
    entry_usr_name2 = tk.Label(sign_up, text='0', font=('Arial', 14))
    entry_usr_name2.place(x=120,y=170)

    var_usr_name = tk.StringVar()
    entry_usr_name3 = tk.Label(sign_up, text='0', font=('Arial', 14))
    entry_usr_name3.place(x=120,y=210)

    var_usr_name = tk.StringVar()
  
    entry_usr_name4 = tk.Label(sign_up, text='0', font=('Arial', 14))#要直接显示text='0'，tk.Label
    entry_usr_name4.place(x=120,y=250)

    while True:
        ret, frame = cap.read()
        cv2.imshow("frame",frame)
        print("人脸登录中，请稍等")
        speaker.Speak("人脸登录中，请稍等")
        cv2.waitKey(1000)
        cv2.imencode('.jpg',frame)[1].tofile("new"+".jpg") #存图片
        facedata = face_rec.face_test('./new.jpg',name) #人脸识别
        #cv2.waitKey(1000)
        break
    cap.release()
    cv2.destroyAllWindows()
    if(int(facedata['result']['user_list'][0]['score'])>80): #识别成功后，直接将数据读下来，显示在界面上
        #name表示借球姓名，1查阅/2更新总数/3更新借球数，第三个参数在更新数据时使用，grade表示年级
        grade = My_Speech_end.sqlname_backnumber(name,1,None,'grade')
        Class = My_Speech_end.sqlname_backnumber(name,1,None,'Class')
        number = My_Speech_end.sqlname_backnumber(name,1,None,'number')
        name = My_Speech_end.sqlname_backnumber(name,1,None,'name')
        borrow = My_Speech_end.sqlname_backnumber(name,1,None,'borrow')

        entry_usr_name.config(text = '%s'%grade)
        entry_usr_name1.config(text = '%s'%Class)
        entry_usr_name2.config(text = '%s'%number)
        entry_usr_name3.config(text = '%s'%name)
        entry_usr_name4.config(text = '%s'%borrow)
        print("人脸识别通过，请核对信息")
        speaker.Speak("人脸识别通过，请核对信息")
    else:
        print("对不起，不存在您的信息")
        speaker.Speak("对不起，不存在您的信息")
        sign_up.destroy()


    def usr_login():
    
        a=entry_usr_name.cget('text')
        b=entry_usr_name1.cget('text')
        c=entry_usr_name2.cget('text')
        d=entry_usr_name3.cget('text')
        e=entry_usr_name4.cget('text')
        rest = My_Speech_end.sqlname_backnumber('wzy', 1, None, 'rest')
        balls = int(rest)+ int(e)
        print('balls',balls)
        My_Speech_end.sqlname_backnumber('wzy', 2, balls, None)
        mqtt.PUB("WZY123","1,R"+str(e)+","+str(balls)) #发送还球数和剩余球数 1表示1号机R表示还球
        sql = "DELETE FROM `basketball` WHERE `name` = '" + d + "'"
        try:
            cursor.execute(sql)
            conn.commit()
            print("还球成功，谢谢")
            speaker.Speak("还球成功，谢谢")

        except:
            print("还球失败，请重试")
            speaker.Speak("还球失败，请重试")
            conn.rollback()
            conn.close()
        sign_up.destroy()

    login = tk.Button(sign_up, text='确定', command=usr_login)
    login.place(x=200, y=300)

photo = tk.PhotoImage(file="3.gif")  # file：t图片路径
imgLabel = tk.Label(window, image=photo)  # 把图片整合到标签类中
imgLabel.pack(side=tk.RIGHT)  # 自动对齐

btn_login = tk.Button(window, text='借球',width=10,height=2,bg="white", fg="blue",relief="ridge",bd=7,command=usr_sign_up)
btn_login.place(x=130, y=50)

btn_login = tk.Button(window, text='还球', width=10,height=2,bg="white", fg="blue",relief="ridge",bd=7,command=sign_up)
btn_login.place(x=300, y=50)



shuoming1 = tk.Label(window, text='操作说明：', fg='black',bg='white')
shuoming1.place(x=200,y=360)
shuoming1 = tk.Label(window, text='第一步：回答‘需要几个球’', fg='black',bg='white')
shuoming1.place(x=200,y=390)
shuoming1 = tk.Label(window, text='第二步：回答‘谢谢’', fg='black',bg='white')
shuoming1.place(x=200,y=420)
shuoming1 = tk.Label(window, text='第三步：填写相关信息', fg='black',bg='white')
shuoming1.place(x=200,y=450)

window.mainloop()
       
