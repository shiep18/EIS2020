import recordsound as rs
import wave2pinyin as w2p
import baidusound as bd
import time
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
img = cv2.imread('1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    pass
head=img[y:(y+h),x:(x+w)]
head=cv2.resize(head,(130,130),interpolation=cv2.INTER_CUBIC)

black = cv2.imread('cloth1.jpg')
white = cv2.imread('cloth2.jpg')
yellow = cv2.imread('cloth3.jpg')
cv2.namedWindow('result')

black[187:317,312:442]=head[0:130,0:130]
white[187:317,312:442]=head[0:130,0:130]
yellow[187:317,312:442]=head[0:130,0:130]

print('若换衣服，请说换某种颜色衣服')
str1='你好，欢迎使用语音系统'
times=bd.speak(str1)
time.sleep(times)
while True:
    rs.shibie()
    command=w2p.zhuanhua()
    if command == '白色衣服':
        print('好的，白色衣服')
        str1='好的，白色衣服'
        times=bd.speak(str1)
        time.sleep(times)
        cv2.imshow('result',white)
    elif command == '黑色衣服':
        print('好的，黑色衣服')
        str1='好的，黑色衣服'
        times=bd.speak(str1)
        time.sleep(times)
        cv2.imshow('result',black)
    elif command == '黄色衣服':
        print('好的，黄色衣服')
        str1='好的，黄色衣服'
        times=bd.speak(str1)
        time.sleep(times)
        cv2.imshow('result',yellow)
    else :
        print('不好意思，我不知道')
        str1='不好意思，我不知道'
        times=bd.speak(str1)
        time.sleep(times)
    if cv2.waitKey(10)&0xFF=='q':
        break

cv2.destroyAllWindows()
