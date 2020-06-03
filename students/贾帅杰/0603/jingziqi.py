import cv2
import numpy as np
import time as t
import recordsound as rs
import wave2pinyin as w2p
import baidusound as bd

global flag,turn,yflag,img,chess
def pointx(x):
    t=0
    if 120<=x<240:
        t=1
    elif 204<=x<360:
        t=2
    elif 360<=x<=480:
        t=3
    return t
def pointy(y):
    t=0
    if 120<=y<240:
        t=1
    elif 204<=y<360:
        t=2
    elif 360<=y<=480:
        t=3
    return t
def click(event,x,y,flags,param):
    global flag,turn
    if event==cv2.EVENT_RBUTTONDOWN and flag==2:
        print('mouse coords:',x,y)        
        t1=pointx(x)
        t2=pointy(y)
        if chess[t1-1][t2-1] != 1 and chess[t1-1][t2-1] != -1:
            cv2.circle(img,(120+120*t1-60,120+120*t2-60),50,(250,250,250),-1)
            cv2.imshow('qipan',img)
            chess[t1-1][t2-1]=1
            flag=1
            turn=turn+1
    if event==cv2.EVENT_LBUTTONDOWN and flag==1:
        print('mouse coords:',x,y)        
        t1=pointx(x)
        t2=pointy(y)
        if chess[t1-1][t2-1] != 1 and chess[t1-1][t2-1] != -1:
            cv2.circle(img,(120+120*t1-60,120+120*t2-60),50,(0,0,0),-1)
            cv2.imshow('qipan',img)
            chess[t1-1][t2-1]=-1
            flag=2
            turn=turn+1

def win(chess,winflag):
    win1=[0,0,0,0,0,0,0,0]
    win1[0]=chess[0][0]+chess[0][1]+chess[0][2]
    win1[1]=chess[1][0]+chess[1][1]+chess[1][2]
    win1[2]=chess[2][0]+chess[2][1]+chess[2][2]
    win1[3]=chess[0][0]+chess[1][0]+chess[2][0]
    win1[4]=chess[0][1]+chess[1][1]+chess[2][1]
    win1[5]=chess[0][2]+chess[1][2]+chess[2][2]
    win1[6]=chess[0][0]+chess[1][1]+chess[2][2]
    win1[7]=chess[0][2]+chess[1][1]+chess[2][0]
    for i in win1:
        if i==3 :
            winflag=1
            break
        if i==-3 :
            winflag=-1
    return winflag

def yuyin(img,chess):
    global yflag
    rs.shibie()
    command=w2p.zhuanhua()
    if command[2]=='a' and yflag==2:
        cv2.circle(img,(120+120*(int(command[0])+1)-60,120+120*(int(command[1])+1)-60),50,(250,250,250),-1)
        cv2.imshow('qipan',img)
        chess[int(command[0])][int(command[1])]=1
        yflag=1
    if command[2]=='b' and yflag==1:
        cv2.circle(img,(120+120*(int(command[0])+1)-60,120+120*(int(command[1])+1)-60),50,(0,0,0),-1)
        cv2.imshow('qipan',img)
        chess[int(command[0])][int(command[1])]=-1
        yflag=2

winflag=0
yflag=1
turn=1
flag=1

def new():
    global img,chess
    img=np.zeros((600,600,3),np.uint8)
    img[:]=[200,5,100]
    chess=[[0,0,0],
           [0,0,0],
           [0,0,0]]
    
    cv2.line(img,(120,120),(480,120),(250,230,200),3)
    cv2.line(img,(120,240),(480,240),(250,230,200),3)
    cv2.line(img,(120,360),(480,360),(250,230,200),3)
    cv2.line(img,(120,480),(480,480),(250,230,200),3)

    cv2.line(img,(120,120),(120,480),(250,230,200),3)
    cv2.line(img,(240,120),(240,480),(250,230,200),3)
    cv2.line(img,(360,120),(360,480),(250,230,200),3)
    cv2.line(img,(480,120),(480,480),(250,230,200),3)

    #cv2.circle(img,(180,180),50,(0,0,0),-1)
    #cv2.circle(img,(300,180),50,(250,250,250),-1)
    cv2.imshow('qipan',img)

new()
cv2.namedWindow('qipan')
cv2.setMouseCallback('qipan',click)
while True:
    t.sleep(1)
    yuyin(img,chess)
    winflag=win(chess,winflag)
    if winflag ==1:
        print('white win')
        winflag=0
        turn=0
        t.sleep(3)
        new()
        #break
    if winflag ==-1:
        print('black win')
        winflag=0
        turn=0
        t.sleep(3)
        new()
        #break
    if turn == 9:
        print('draw')
        t.sleep(3)
        break
    if cv2.waitKey(10)&0xFF==27:
            break

cv2.destroyAllWindows()
