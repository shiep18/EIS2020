import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.messagebox
import pickle
from PIL import Image
from PIL import ImageTk
import MXMqtt as MXMqtt
import numpy as np
import cv2
import os
import time

# 定义密码
usr_file = ['1234']

#mqtt初始化
MQTTHOST = "mqtt.16302.com"
MQTTPORT = 1883
mqtt = MXMqtt.MXMqtt(MQTTHOST,MQTTPORT)

mqtt.SUB("HA")
mqtt.SUB("MC")

mqtt.PUB("HA","DoorClose")
mqtt.PUB("MC","CloseDoor")
# 第1步，实例化object，建立窗口window
window = tk.Tk()
 
# 第2步，给窗口的可视化起名字
window.title('人脸识别系统')
 
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('400x300')  # 这里的乘是小x

# 第4步，加载 wellcome image
canvas = tk.Canvas(window, bg='white', height=300, width=400)
image_file = tk.PhotoImage(file='D:\\Users\\ouyes\\Desktop\\QRS\\work\\face\\face1\\face1.PNG')
image = canvas.create_image(120, 60, anchor='n', image=image_file)
canvas.pack(side='top')

# 第5步，定义密码输入功能
def useInputPwd():
    def comfirmInputPwd():
        while True:
            # 以下就是获取我们注册时所输入的信息
            pp = input_pwd.get()

            if pp in usr_file:
                tkinter.messagebox.showinfo(title='Success', message='密码正确，欢迎您！')
                window_input_pwd.destroy()
                mqtt.PUB("HA","DoorOpen")
                mqtt.PUB("MC","OpenDoor")
                time.sleep(10)
                mqtt.PUB("HA","DoorClose")
                mqtt.PUB("MC","CloseDoor")
                print("密码解锁成功，欢迎您！")
                break

            else:
                tkinter.messagebox.showerror(title='Error', message='密码错误，请重新输入！')         # 提出错误对话窗
                #tkinter.messagebox.showerror('密码错误，请重新输入！')
    
    # 定义长在窗口上的窗口
    window_input_pwd = tk.Toplevel(window)
    window_input_pwd.geometry('300x200')
    window_input_pwd.title('密码解锁')

    input_pwd = tk.StringVar()  # 将输入的注册名赋值给变量
    tk.Label(window_input_pwd, text='密码: ').place(x=30, y=20)  # 将`User name:`放置在坐标（10,10）。
    entry_input_pwd = tk.Entry(window_input_pwd, textvariable=input_pwd,  show='*') # 创建一个注册名的`entry`，变量为`new_name`
    entry_input_pwd.place(x=80, y=20)  # `entry`放置在坐标（130,10）.

    btn_comfirm_input_pwd = tk.Button(window_input_pwd, text='确定',font=('Arial', 12), width=10, height=1,command=comfirmInputPwd)
    btn_comfirm_input_pwd.place(x=100, y=50)

# 第6步，定义人脸录入功能
def useFaceCollect():
    def comfirmInputPwd():
        # 以下就是获取我们注册时所输入的信息
        pp = input_pwd.get()

        if pp in usr_file :
            tkinter.messagebox.showinfo(title='Success', message='密码正确，即将进行人脸识别！')
            window_input_pwd.destroy()

            def faceCollect():
                # 调用笔记本内置摄像头，所以参数为0，如果有其他的摄像头可以调整参数为1，2
                cap = cv2.VideoCapture(0)
                # 人脸识别分类器 //填入的路径为你建立的新的文件夹的路径
                face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
                # 识别眼睛的分类器
                eyeCascade = cv2.CascadeClassifier('haarcascade_eye.xml')

                face_id = face_collect.get()

                print('正在初始化面部捕捉...')
                time.sleep(2)
                print('正在录入您的面容，请等待...')

                count = 0
                while True:
                    #time.sleep(5)
                    mqtt.PUB("WZY123","DoorClose")
                    # 从摄像头读取图片
                    sucess, img = cap.read()
                    # 转为灰度图片
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    # 检测人脸
                    faces = face_detector.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        fac_gray = gray[y: (y+h), x: (x+w)]
                        cv2.rectangle(img, (x, y), (x+w, y+w), (255, 0, 0))
                        result = []
                        eyes = eyeCascade.detectMultiScale(fac_gray, 1.3, 2)
                        for (ex, ey, ew, eh) in result:
                            cv2.rectangle(img, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
                            
                        count += 1
                        time.sleep(0.3)

                        # 保存图像
                        cv2.imwrite("Facedata/User." + str(face_id) + '.' + str(count) + '.jpg', gray[y: y + h, x: x + w])
                        #print("User." + str(face_id) + '--' + str(count) + '.jpg')
                        print("面部录入已完成" + str(count) + '%') 
                        #time.sleep(0.5)
                        cv2.imshow('image', img)
                    # 保持画面的持续。
                    k = cv2.waitKey(1)
                    if k == 27: # 通过esc键退出摄像
                        break
                    elif count >= 100: # 得到1000个样本后退出摄像
                        time.sleep(3)
                        # 人脸数据路径
                        path = 'Facedata'

                        recognizer = cv2.face.LBPHFaceRecognizer_create()
                        detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                        def getImagesAndLabels(path):
                            imagePaths = [os.path.join(path, f) for f in os.listdir(path)] # join函数的作用？
                            faceSamples = []
                            ids = []
                            for imagePath in imagePaths:
                                PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
                                img_numpy = np.array(PIL_img, 'uint8')
                                id = int(os.path.split(imagePath)[-1].split(".")[1])
                                faces = detector.detectMultiScale(img_numpy)
                                for (x, y, w, h) in faces:
                                    faceSamples.append(img_numpy[y:y + h, x: x + w])
                                    ids.append(id)
                            return faceSamples, ids
                        print('正在储存人脸数据，请稍后...')
                        faces, ids = getImagesAndLabels(path)
                        recognizer.train(faces, np.array(ids))

                        recognizer.write(r'D:\Users\ouyes\Desktop\QRS\work\face\face1\face_trainer\trainer.yml')
                        print("{0} 个面容已储存".format(len(np.unique(ids))))
                        #print("面容已储存")
                        print("人脸录入已完成")
                        tkinter.messagebox.showinfo(title='Success', message='人脸录入完成')
                        time.sleep(3)
                        window_face_collect.destroy()
                        # 关闭摄像头
                        cap.release()
                        cv2.destroyAllWindows()
                        break

            window_face_collect = tk.Toplevel(window)
            window_face_collect.geometry('300x200')
            window_face_collect.title('人脸录入')

            face_collect = tk.StringVar()  # 将输入的注册名赋值给变量
            tk.Label(window_face_collect, text='输入序号: ').place(x=10, y=20)  # 将`User name:`放置在坐标（10,10）。
            entry_face_collect = tk.Entry(window_face_collect, textvariable=face_collect) # 创建一个注册名的`entry`，变量为`new_name`
            entry_face_collect.place(x=80, y=20)  # `entry`放置在坐标（130,10）.

            btn_comfirm_face_collect = tk.Button(window_face_collect, text='确定',font=('Arial', 12), width=10, height=1,command=faceCollect)
            btn_comfirm_face_collect.place(x=100, y=50)

                

        else:
            tkinter.messagebox.showerror(title='Error', message='密码错误，请重新输入！')         # 提出错误对话窗
            #tkinter.messagebox.showerror('密码错误，请重新输入！')
    

    # 定义长在窗口上的窗口
    # 人脸识别前输入密码确认身份
  
    window_input_pwd = tk.Toplevel(window)
    window_input_pwd.geometry('300x200')
    window_input_pwd.title('密码输入')

    input_pwd = tk.StringVar()  # 将输入的注册名赋值给变量
    tk.Label(window_input_pwd, text='请输入密码确认身份').place(x=100, y=20)  # 将`User name:`放置在坐标（10,10）。
    entry_input_pwd = tk.Entry(window_input_pwd, textvariable=input_pwd,  show='*') # 创建一个注册名的`entry`，变量为`new_name`
    entry_input_pwd.place(x=80, y=50)  # `entry`放置在坐标（130,10）.

    btn_comfirm_input_pwd = tk.Button(window_input_pwd, text='确定',font=('Arial', 12), width=10, height=1,command=comfirmInputPwd)
    btn_comfirm_input_pwd.place(x=40, y=80)
    btn_comfirm_input_pwd = tk.Button(window_input_pwd, text='取消',font=('Arial', 12), width=10, height=1,command=comfirmInputPwd)
    btn_comfirm_input_pwd.place(x=160, y=80)
        

# 第7步，定义人脸解锁功能
def useFaceRecognize():
    def faceRecognize():
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read('face_trainer/trainer.yml')
        cascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascadePath)
        font = cv2.FONT_HERSHEY_SIMPLEX

        idnum = 0

        names = ['0', '1','2','3']

        cap = cv2.VideoCapture(0)
        minW = 0.1*cap.get(3)
        minH = 0.1*cap.get(4)

        while True:
            ret, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(int(minW), int(minH))
                )
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
                idnum, confidence = recognizer.predict(gray[y:y+h, x:x+w])
                
                if confidence < 100:
                    idnum = names[idnum]
                    confidence = "{0}%".format(round(100 - confidence))
                    cv2.putText(img, str(idnum), (x+50, y-5), font, 1, (0, 0, 255), 1)
                    cv2.putText(img, str(confidence), (x+50, y+h-5), font, 1, (0, 0, 0), 1)
                    print("人脸识别成功，您是" +idnum)
                    window_face_recognize.destroy()
                    mqtt.PUB("HA","DoorOpen")
                    mqtt.PUB("MC","OpenDoor")
                    break
                else:
                    idnum = "unknown"
                    confidence = "{0}%".format(round(100 - confidence))
                    cv2.putText(img, str(idnum), (x+50, y-5), font, 1, (0, 0, 255), 1)
                    cv2.putText(img, str(confidence), (x+50, y+h-5), font, 1, (0, 0, 0), 1)
            cv2.imshow('camera', img)
            k = cv2.waitKey(10)
            if k == 27:
                mqtt.PUB("HA","DoorClose")
                mqtt.PUB("MC","CloseDoor")
                break


    # 定义长在窗口上的窗口
    window_face_recognize = tk.Toplevel(window)
    window_face_recognize.geometry('300x200')
    window_face_recognize.title('人脸解锁')

    face_recognize = tk.StringVar()  # 将输入的注册名赋值给变量
    tk.Label(window_face_recognize, text='是否进行人脸解锁').place(x=100, y=20)  # 将`User name:`放置在坐标（10,10）。
    # entry_face_recognize = tk.Entry(window_face_recognize, textvariable=face_recognize) # 创建一个注册名的`entry`，变量为`new_name`
    # entry_face_recognize.place(x=80, y=20)  # `entry`放置在坐标（130,10）.

    btn_comfirm_face_recognize = tk.Button(window_face_recognize, text='确定',font=('Arial', 12), width=10, height=1,command=faceRecognize)
    btn_comfirm_face_recognize.place(x=40, y=50)
    btn_comfirm_face_recognize = tk.Button(window_face_recognize, text='取消',font=('Arial', 12), width=10, height=1,command=faceRecognize)
    btn_comfirm_face_recognize.place(x=160, y=50)




# 第8步，login and sign up 按钮
btn_face_collect = tk.Button(window, text='录入面容', font=('Arial', 12), width=10, height=3, command=useFaceCollect)
btn_face_collect.place(x=250, y=37)
btn_face_recognize = tk.Button(window, text='面容解锁',font=('Arial', 12), width=10, height=3, command=useFaceRecognize)
btn_face_recognize.place(x=250, y=124)
btn_input_pwd = tk.Button(window, text='密码解锁',font=('Arial', 12), width=10, height=3, command=useInputPwd)
btn_input_pwd.place(x=250, y=211)

# 第10步，主窗口循环显示
window.mainloop()
