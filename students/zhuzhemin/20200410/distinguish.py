#-----检测、校验并输出结果-----
import cv2
from mcpi.minecraft import Minecraft
import serial
import serial.tools.list_ports
import time
ports = list(serial.tools.list_ports.comports())
print (ports)
ser=serial.Serial(port='COM12')
time.sleep(2)
#准备好识别方法
recognizer = cv2.face.LBPHFaceRecognizer_create()
mc=Minecraft.create()
#使用之前训练好的模型
recognizer.read('trainner/trainner.yml')

#再次调用人脸分类器
cascade_path = "E:\zhu/face/haarcascade_frontalface_default.xml"#脸部识别
face_cascade = cv2.CascadeClassifier(cascade_path)

#加载一个字体，用于识别后，在图片上标注出对象的名字
font = cv2.FONT_HERSHEY_SIMPLEX

idnum = 0
#设置好与ID号码对应的用户名，如下，如0对应的就是初始

names = ['Yuhao','Zhuzhemin','Stranger']

#调用摄像头
cam = cv2.VideoCapture(0)
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:
    ret,img = cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #识别人脸
    faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW),int(minH))
            )
    #进行校验
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        idnum,confidence = recognizer.predict(gray[y:y+h,x:x+w])

        #计算出一个检验结果
        if confidence < 100:
            print(idnum)
            print(confidence)
            if 1<=idnum<=800:
                idnum=0
                ser.write("0".encode())
                print("0 send")
                mc.setBlock(-22,20,-33,0)
                mc.setBlock(-22,19,-33,0)
            elif 801<=idnum<=1600:
                idnum=1
                ser.write("1".encode())
                print("1 send")
                mc.setBlock(-22,20,-33,0)
                mc.setBlock(-22,19,-33,0)
            elif 1601<=idnum<=2400:
                idnum=2
                ser.write("2".encode())
                print("2 send")
                mc.setBlock(-22,20,-33,20)
                mc.setBlock(-22,19,-33,20)
            idum = names[idnum]
            confidence = "{0}%",format(round(100-confidence))
        else:
            idum = "unknown"
            confidence = "{0}%",format(round(100-confidence))

        #输出检验结果以及用户名
        cv2.putText(img,str(idum),(x+5,y-5),font,1,(0,0,255),1)
        cv2.putText(img,str(confidence),(x+5,y+h-5),font,1,(0,0,0),1)

        #展示结果
        cv2.imshow('camera',img)
        key = cv2.waitKey(20) & 0xFF
        if key == ord('q'):
            break

#释放资源
cam.release()
cv2.destroyAllWindows()