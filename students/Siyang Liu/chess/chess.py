import cv2
import numpy as np
from mat import *
from voice import *
from xpinyin import Pinyin
import time

def init():
    global img, a, b, zone
    print('===========  对局开始  ===========')
    img = np.zeros((600,600,3), np.uint8)
    img[:] = [200,5,100]
    chess = np.zeros((3,3),np.int8)
    cv2.line(img,(120,120),(480,120),(250,230,200),3)
    cv2.line(img,(120,120*2),(480,120*2),(250,230,200),3)
    cv2.line(img,(120,120*3),(480,120*3),(250,230,200),3)
    cv2.line(img,(120,120*4),(480,120*4),(250,230,200),3)

    cv2.line(img,(120,120),(120,120*4),(250,230,200),3)
    cv2.line(img,(120*2,120),(120*2,120*4),(250,230,200),3)
    cv2.line(img,(120*3,120),(120*3,120*4),(250,230,200),3)
    cv2.line(img,(120*4,120),(120*4,120*4),(250,230,200),3)

    cv2.imshow('chess',img)

    zone = [(j*120,i*120) for i in range(1,4) for j in range(1,4)]

    a,b = np.zeros((3,3)),np.zeros((3,3))

init()
num = ['yi','er','san','si','wu','liu','qi','ba','jiu']
flag = 0

def getPinYin(result):
    pin = Pinyin()
    return pin.get_pinyin(result)

def click(event,x,y,flags,param):
    global img, a, b, zone, flag

    if event == cv2.EVENT_LBUTTONDOWN:
        if flag == 1:
            flag = 0
            init()
            cv2.imshow('chess',img)
        else:
            record()
            co = recognize()
            if co is not None:
                co = getPinYin(co).split('-')
                print(co)
                for i in co:
                    if i in num:
                        point = zone[num.index(i)]
                        if 'hei' in co:
                            cv2.circle(img,(point[0]+60,point[1]+60),(50),(0,0,0),-1)
                            a[zone.index(point)//3][zone.index(point)%3] = 1
                            s = mat(a)
                            if s is 'WIN':
                                print('Black',s,'（Tap screen to start over.)')
                                flag = 1
                            cv2.imshow('chess',img)
                        elif 'bai' in co:
                            cv2.circle(img,(point[0]+60,point[1]+60),(50),(255,255,255),-1)
                            b[zone.index(point)//3][zone.index(point)%3] = 1
                            s = mat(b)
                            if s is 'WIN':
                                print('White',s,'（Tap screen to start over.）')
                                flag = 1
                            cv2.imshow('chess',img)

cv2.namedWindow('chess')
cv2.setMouseCallback('chess',click)

while True:
    if cv2.waitKey(10)&0xFF == 27:
            break
cv2.destroyAllWindows()
