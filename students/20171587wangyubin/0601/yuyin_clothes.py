import wave2pinyin as w2p
import recordsound as rs
import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
img = cv2.imread('face.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    pass


head=img[y:(y+h),x:(x+w)]
head=cv2.resize(head,(130,130),interpolation=cv2.INTER_CUBIC)



pd = cv2.imread('shirt1.jpg')
pd1 = cv2.imread('shirt2.jpg')
pd2 = cv2.imread('shirt3.jpg')
cv2.namedWindow('result')

pd[187:317,312:442]=head[0:130,0:130]
pd1[187:317,312:442]=head[0:130,0:130]
pd2[187:317,312:442]=head[0:130,0:130]

while True:
    rs.record()
    order=w2p.w2p()
    if order == "结束":
        print("感谢使用")
        break               
    elif order == '白色':
        print("显示白色衣服")
        cv2.imshow('result',pd)
    elif order == '黑色':
        print("显示黑色衣服")
        cv2.imshow('result',pd1)
    elif order == '黄色':
        print("显示黄色衣服")
        cv2.imshow('result',pd2)
    if cv2.waitKey(10)&0xFF=='q':
        break
cv2.destroyAllWindows()