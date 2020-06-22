from tkinter import *
from PIL import Image
from PIL import ImageTk
import cv2
import weather as t1
import tkinter.filedialog
import face
import pymysql
import os

window = Tk()
window.title('智能服装搭配')
window.geometry('500x600')

img = None
image_file = None

flag = 0
flag1 = 0

conn = pymysql.connect('localhost', 'root', '', 'basketball')
cursor = conn.cursor()
def readpic(shoulder,leg):
    a = "`"+str(shoulder)+"`"
    b = leg

    cursor.execute("SELECT * FROM " + a + " WHERE person_id = " + str(b))
    for image in cursor.fetchall():
        with open("{}.jpg".format(image[0]), "wb")as f:
            f.write(image[1])

    #cursor.close()
    #conn.close()
    img = Image.open(str(b) + '.jpg')
    return img

def readcloth(cloth):
    a = cloth
    cursor.execute("SELECT * FROM `cloth` WHERE person_id = '" + a + "'")
    for image in cursor.fetchall():
        with open("{}.png".format(image[0]), "wb")as f:
            f.write(image[1])

    img = cv2.imread(a + '.png')
    return img

def findpic(flag1):
    a = ['m_Tb_Kb','m_Tb_Ky','m_Tw_Kb','m_Tw_Ky','m_Ty_Kb','m_Ty_Ky']
    b = a[flag1-1]
    return b

def begin():
    global img
    global image_file
    # 第1步，实例化object，建立窗口window
    root = Toplevel(window)
    # 第2步，给窗口的可视化起名字
    root.title('体型选择')

    # 第3步，设定窗口的大小(长 * 宽)
    root.geometry('500x600')  # 这里的乘是小x

    # 放置图片
    canvas =Canvas(root, width=188, height=464, bg='white')
    img = Image.open('./body/36/40.jpg')
    image_file = ImageTk.PhotoImage(img)
    image = canvas.create_image(96, 2, anchor='n', image=image_file)
    canvas.pack(side='top')
    root.update()

    def dress():

        m2 = readcloth('X1')
        m_T = readcloth('m_T')
        m_K = readcloth('m_K')
        m_T_black = readcloth('m_T_black3')
        m_T_white = readcloth('m_T_white3')
        m_T_yellow = readcloth('m_T_yellow3')
        m_K_black = readcloth('m_K_black3')
        m_K_yellow = readcloth('m_K_yellow3')
        m_Tb_Kb = readcloth('m_Tb_Kb')
        m_Tb_Ky = readcloth('m_Tb_Ky')
        m_Tw_Kb = readcloth('m_Tw_Kb')
        m_Tw_Ky = readcloth('m_Tw_Ky')
        m_Ty_Kb = readcloth('m_Ty_Kb')
        m_Ty_Ky = readcloth('m_Ty_Ky')



        cv2.namedWindow('Manually choose', 0)
        cv2.resizeWindow('Manually choose', 300, 600)
        cv2.imshow('Manually choose', m2)



        def click(event, x, y, flags, param):
            global flag
            global flag1
            if event == cv2.EVENT_RBUTTONDOWN:
                cv2.imshow('Manually choose', m2)
                flag = 0
            if event == cv2.EVENT_LBUTTONDOWN:
                if 850 < x < 1080 and 0 < y < 210:
                    flag =55
               # print('mouse coords:', x, y)
                if flag == 0:
                    if 0 < x < 200 and 950 < y < 1050:
                        cv2.imshow('Manually choose', m_T)  # 衬衫
                        flag = 1
                    if 0 < x < 200 and 1150 < y < 1250:
                        cv2.imshow('Manually choose', m_K)  # 裤子
                        flag = 2
                elif flag == 1:
                    if 0 < x < 360 and 1780 < y < 2100:
                        cv2.imshow('Manually choose', m_T_black)
                        flag = 11
                    if 360 < x < 720 and 1780 < y < 2100:
                        cv2.imshow('Manually choose', m_T_white)
                        flag = 12
                    if 720 < x < 1080 and 1780 < y < 2100:
                        cv2.imshow('Manually choose', m_T_yellow)
                        flag = 13
                elif flag == 2:
                    if 0 < x < 540 and 1800 < y < 2100:
                        cv2.imshow('Manually choose', m_K_black)
                        flag = 21
                    if 540 < x < 1080 and 1800 < y < 2100:
                        cv2.imshow('Manually choose', m_K_yellow)
                        flag = 22
                elif flag == 11:
                    if 0 < x < 540 and 1800 < y < 2100:
                        cv2.imshow('Manually choose', m_Tb_Kb)
                        flag1 = 1
                    if 540 < x < 1080 and 1800 < y < 2100:
                        cv2.imshow('Manually choose', m_Tb_Ky)
                        flag1 = 2
                elif flag == 12:
                    if 0 < x < 540 and 1800 < y < 2100:
                        cv2.imshow('Manually choose', m_Tw_Kb)
                        flag1 = 3
                    if 540 < x < 1080 and 1800 < y < 2100:
                        cv2.imshow('Manually choose', m_Tw_Ky)
                        flag1 = 4
                elif flag == 13:
                    if 0 < x < 540 and 1800 < y < 2100:
                        cv2.imshow('Manually choose', m_Ty_Kb)
                        flag1 = 5
                    if 540 < x < 1080 and 1800 < y < 2100:
                        cv2.imshow('Manually choose', m_Ty_Ky)
                        flag1 = 6

                elif flag == 21:
                    if 0 < x < 360 and 1780 < y < 2100:
                        cv2.imshow('Manually choose', m_Tb_Kb)
                        flag1 = 1
                    if 360 < x < 720 and 1780 < y < 2100:
                        cv2.imshow('Manually choose', m_Tw_Kb)
                        flag1 = 3
                    if 720 < x < 1080 and 1780 < y < 2100:
                        cv2.imshow('Manually choose', m_Ty_Kb)
                        flag1 = 5
                elif flag == 22:
                    if 0 < x < 360 and 1780 < y < 2100:
                        cv2.imshow('Manually choose', m_Tb_Ky)
                        flag1 = 2
                    if 360 < x < 720 and 1780 < y < 2100:
                        cv2.imshow('Manually choose', m_Tw_Ky)
                        flag1 = 4
                    if 720 < x < 1080 and 1780 < y < 2100:
                        cv2.imshow('Manually choose', m_Ty_Ky)
                        flag1 = 6

        cv2.namedWindow('Manually choose', 0)
        cv2.resizeWindow('Manually choose', 300, 600)
        cv2.setMouseCallback('Manually choose', click)

        while True:
            global flag1
            if cv2.waitKey(10) & 0xFF == 27 or flag ==55:
                print(flag1)
                break
        cv2.destroyAllWindows()

    def usr_sign_weather():
        print("我们将通过今日天气为您挑选衣服")
        t1.all_weather()


    def shoulder(ev=None):
        global img
        global image_file
        shoulder = s1.get()
        leg = s2.get()
        img = readpic(shoulder, leg)
        image_file = ImageTk.PhotoImage(img)
        image = canvas.create_image(96, 2, anchor='n', image=image_file)
        canvas.pack(side='top')
        root.update()
        path = str(leg) + '.jpg'
        # os.remove(path)
        print('ok')
        '''
        try:
            img = readpic(shoulder,leg)
            image_file = ImageTk.PhotoImage(img)
            image = canvas.create_image(96, 2, anchor='n', image=image_file)
            canvas.pack(side='top')
            root.update()
            path = str(leg)+'.jpg'
            #os.remove(path)
            print('ok')
        except:
            pass
            '''

        print('shoulder: ',shoulder)
        print('leg: ',leg )

    def changeface():
        global flag1
        a = tkinter.filedialog.askopenfilename()
        l = a.split('/')[-1]
        b = findpic(flag1)
        face.test(b,l)



    s1 = Scale(root,from_=36,to=46,tickinterval=4,resolution=6,length=200,orient=HORIZONTAL,command = shoulder)
    s1.pack()
    s2 = Scale(root,from_=40,to=50,tickinterval=4,resolution=5,orient=HORIZONTAL,length=200,command = shoulder)
    s2.pack()
    Label(root,text='肩宽:',font=('楷体',12)).place(x = 100,y = 488)
    Label(root,text='腿长:',font=('楷体',12)).place(x = 100,y = 552)
    Button(root,text = '手动换衣',width=10,height = 2,bg = 'white',fg = 'black',relief="ridge",bd=7,command = dress).place(x = 400,y = 400)
    Button(root, text='推荐搭配', width=10, height=2, bg='white', fg='black', relief="ridge", bd=7,command=usr_sign_weather).place( x=10, y=400)
    Button(root, text='换脸', width=10, height=2, bg='white', fg='black', relief="ridge", bd=7,command=changeface).place(x=400, y=300)



photo = Image.open('timg.jpg')
photo = ImageTk.PhotoImage(photo)  # file：t图片路径
imgLabel = Label(window, image=photo)  # 把图片整合到标签类中
imgLabel.pack(side=RIGHT)  # 自动对齐

Button(window,text = '开始',width=8,height = 2,bg = 'white',fg = 'black',relief="ridge",bd=7,command = begin).place(x = 200,y = 330)

mainloop()
