import numpy as np
import cv2
from PIL import Image

m = cv2.imread('m.jpg')
m1 = cv2.imread('T1.png')
m2 = cv2.imread('X1.png')

m_T = cv2.imread('m_T.png')
m_T_black = cv2.imread('m_T_black3.png')
m_T_white = cv2.imread('m_T_white3.png')

m_T_yellow = cv2.imread('m_T_yellow3.png')

m_K = cv2.imread('m_K.png')
m_K_black = cv2.imread('m_K_black3.png')
m_K_yellow = cv2.imread('m_K_yellow3.png')


m_Tb_Kb = cv2.imread('m_Tb_Kb.jpg')
m_Tb_Ky = cv2.imread('m_Tb_Ky.jpg')
m_Tw_Kb = cv2.imread('m_Tw_Kb.jpg')

m_Tw_Ky = cv2.imread('m_Tw_Ky.jpg')
m_Ty_Kb = cv2.imread('m_Ty_Kb.jpg')
m_Ty_Ky = cv2.imread('m_Ty_Ky.jpg')


flag = 0
cv2.namedWindow('result',0)
cv2.resizeWindow('result',300,600)
cv2.imshow('result',m2)


def click(event,x,y,flags,param):
    global flag
    if event==cv2.EVENT_RBUTTONDOWN:
        cv2.imshow('result',m2)
        flag = 0
    if event==cv2.EVENT_LBUTTONDOWN:
        print('mouse coords:',x,y)
        if flag == 0:
            if 0<x<200 and 950<y<1050:
                cv2.imshow('result',m_T)#衬衫
                flag = 1
            if 0<x<200 and 1150<y<1250:
                cv2.imshow('result',m_K)#裤子
                flag = 2
        elif flag == 1:
            if 0<x<360 and 1780<y<2100:
                cv2.imshow('result',m_T_black)
                flag = 11
            if 360<x<720 and 1780<y<2100:
                cv2.imshow('result',m_T_white)
                flag = 12
            if 720<x<1080 and 1780<y<2100:
                cv2.imshow('result',m_T_yellow)
                flag = 13
        elif flag == 2:
            if 0<x<540 and 1800<y<2100:
                cv2.imshow('result',m_K_black)
                flag = 21
            if 540<x<1080 and 1800<y<2100:
                cv2.imshow('result',m_K_yellow)
                flag = 22
        elif flag == 11:
            if 0<x<540 and 1800<y<2100:
                cv2.imshow('result',m_Tb_Kb)
            if 540<x<1080 and 1800<y<2100:
                cv2.imshow('result',m_Tb_Ky)
        elif flag == 12:
            if 0<x<540 and 1800<y<2100:
                cv2.imshow('result',m_Tw_Kb)
            if 540<x<1080 and 1800<y<2100:
                cv2.imshow('result',m_Tw_Ky)
        elif flag == 13:
            if 0<x<540 and 1800<y<2100:
                cv2.imshow('result',m_Ty_Kb)
            if 540<x<1080 and 1800<y<2100:
                cv2.imshow('result',m_Tw_Ky)
    
        elif flag == 21:
            if 0<x<360 and 1780<y<2100:
                cv2.imshow('result',m_Tb_Kb)
            if 360<x<720 and 1780<y<2100:
                cv2.imshow('result',m_Tw_Kb)
            if 720<x<1080 and 1780<y<2100:
                cv2.imshow('result',m_Ty_Kb)
        elif flag == 22:
            if 0<x<360 and 1780<y<2100:
                cv2.imshow('result',m_Tb_Ky)
            if 360<x<720 and 1780<y<2100:
                cv2.imshow('result',m_Tw_Ky)
            if 720<x<1080 and 1780<y<2100:
                cv2.imshow('result',m_Ty_Ky)


cv2.namedWindow('result',0)
cv2.resizeWindow('result',300,600)
cv2.setMouseCallback('result',click)

while True:
    if cv2.waitKey(10)&0xFF==27:
            break
cv2.destroyAllWindows()
