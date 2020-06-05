import cv2
import numpy as np
import time
import wave2pinyin as w2p
import recordsound as rs
from xpinyin import Pinyin
p=Pinyin()
order=""

def click(event,x,y,flags,param):
    global turn
    x=int(x/120)
    y=int(y/120)
    if 1<=x<=3 and 1<=y<=3:
        if event==cv2.EVENT_LBUTTONDOWN:
            if turn%2==0 and chess[x-1][y-1]==0:
                print('mouse coords:',x,y)        
                cv2.circle(img,(x*120+60,y*120+60),(50),(255,255,255),-1)
                cv2.imshow('result',img)
                chess[x-1][y-1]=1
                turn+=1
            elif turn%2==1 and chess[x-1][y-1]==0:
                print('mouse coords:',x,y)        
                cv2.circle(img,(x*120+60,y*120+60),(50),(0,0,0),-1)
                cv2.imshow('result',img)
                chess[x-1][y-1]=-1
                turn+=1        


def ctrl(order):
    global turn,i
    if len(order)<3:
        order='none'
    x=p.get_pinyin(order[0])
    y=p.get_pinyin(order[1])
    c=p.get_pinyin(order[2])

    if x=='yao' or x=='yi':
        x=1
    elif x=='er':
        x=2
    elif x=='san' or y=='ban':
        x=3
    else: 
        x=0
    if y=='yao' or y=='yi':
        y=1
    elif y=='er':
        y=2
    elif y=='san' or y=='ban':
        y=3
    else: 
        y=0
    if 1<=x<=3 and 1<=y<=3 and chess[x-1][y-1]==0:
        if (c=='bai' or c=='ban') and turn%2==0:
            cv2.circle(img,(x*120+60,y*120+60),(50),(255,255,255),-1)
            cv2.imshow('result',img)
            chess[x-1][y-1]=1
            turn+=1 
        elif c=='hei' and turn%2==1:
            cv2.circle(img,(x*120+60,y*120+60),(50),(0,0,0),-1)
            cv2.imshow('result',img)
            chess[x-1][y-1]=-1
            turn+=1  

def win():
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
            return 1
        elif i==-3 :
            return -1
    return 0
        




#cv2.setMouseCallback('result',click)
while True:
    img=np.zeros((600,600,3),np.uint8)
    img[:]=[200,5,100]
    chess=np.zeros((3,3),np.int8)
    flag=0
    global turn,i
    turn=0
    i=1
    cv2.line(img,(120,120),(480,120),(250,230,200),3)
    cv2.line(img,(120,240),(480,240),(250,230,200),3)
    cv2.line(img,(120,360),(480,360),(250,230,200),3)
    cv2.line(img,(120,480),(480,480),(250,230,200),3)

    cv2.line(img,(120,120),(120,480),(250,230,200),3)
    cv2.line(img,(240,120),(240,480),(250,230,200),3)
    cv2.line(img,(360,120),(360,480),(250,230,200),3)
    cv2.line(img,(480,120),(480,480),(250,230,200),3)

    cv2.namedWindow('result')
    while True:
        cv2.imshow('result',img)
        if flag==1:
            time.sleep(3)
            break
        if i!=1:
            rs.record()
            order=w2p.w2p()
            print(p.get_pinyin(order))
            ctrl(order)
        i+=1
        res=win()
        if res==1:
            print('white win')
            flag=1
        if res==-1:
            print('black win')
            flag=1
        if turn==9:
            print('dogfall')
            flag=1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()