import os
import cv2
import numpy as np
import win32api,win32con
from os import system
import win32com.client
import time
import copy

speaker = win32com.client.Dispatch("SAPI.SpVoice")
best_weizhi= (4, 0, 2, 6, 8, 1, 3, 5, 7)

def exit():
    cv2.destroyAllWindows()

def board(history=list()):
    global flag,piz,pix,img,pizs
    flag = 0
    piz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    pix = []
    pizs=history
    img = np.zeros((600, 600, 3), np.uint8)
    img[:] = [255,127,0]
    cv2.line(img,(120,120),(480,120),(250,230,200),3)
    cv2.line(img,(120,240),(480,240),(250,230,200),3)
    cv2.line(img,(120,360),(480,360),(250,230,200),3)
    cv2.line(img,(120,480),(480,480),(250,230,200),3)
    cv2.line(img,(120,120),(120,480),(250,230,200),3)
    cv2.line(img,(240,120),(240,480),(250,230,200),3)
    cv2.line(img,(360,120),(360,480),(250,230,200),3)
    cv2.line(img,(480,120),(480,480),(250,230,200),3)
    cv2.rectangle(img, (120, 40), (240, 80), (255, 255, 255))
    cv2.rectangle(img, (240, 40), (360, 80), (255, 255, 255))
    cv2.rectangle(img, (360, 40), (480, 80), (255, 255, 255))
    font = cv2.FONT_HERSHEY_TRIPLEX
    cv2.putText(img, 'clear', (135, 70), font, 1, (255, 255, 0), 1, False)
    cv2.putText(img, 'back', (260, 70), font, 1, (255, 255, 0), 1, False)
    cv2.putText(img, 'quit', (380, 70), font, 1, (255, 255, 0), 1, False)
    cv2.imshow('chess',img)

def empty(pix):
    moves = []
    for i in range(9):
        if pix[i] == 0:
            moves.append(i)
    return moves

def win(pix):
    player=1
    computer=-1
    no=0
    lines = [pix[0:3], pix[3:6], pix[6:9], pix[0::3], pix[1::3], pix[2::3], pix[0::4], pix[2:7:2]]
    if [1] * 3 in lines:
        return player
    elif [-1] * 3 in lines:
        return computer
    elif [1] * 3 not in lines and [1] * 3 not in lines and flag >= 9:
        return no
    else:
        return None

def Judge():
    player=1
    computer=-1
    no=0
    winner = win(pix)
    if winner == computer:
        print('black lost,white wins!')
        print('the game finish!')
        speaker.Speak("白棋赢了")
        win32api.MessageBox(0, "白棋赢了", "提示",win32con.MB_OK)
    elif winner == player:         
        print('black wins,white lost!')
        print('the game finish!')
        speaker.Speak("黑棋赢了")
        win32api.MessageBox(0, "黑棋赢了", "提示",win32con.MB_OK)
    elif winner == no:
        print('draw!')
        print('the game finish!')
        speaker.Speak("平局")
        win32api.MessageBox(0, "平局", "提示",win32con.MB_OK)

def pix_to_piz(x):
    a=[0,1,2,3,4,5,6,7,8]
    b=[[0,0],[1,0],[2,0],[0,1],[1,1],[2,1],[0,2],[1,2],[2,2]]
    m=b[a[x]][1]
    n=b[a[x]][0]
    return m,n

def computer_move(pix):
    player=1
    computer=-1
    pix = pix[:]
    for move in empty(pix):
        pix[move] = computer
        if win(pix) == computer:
            m,n = pix_to_piz(move)
            return m,n
        pix[move] = 0
    for move in empty(pix):
        pix[move] = player
        if win(pix) == player:
            m,n = pix_to_piz(move)
            return m,n
        pix[move] = 0
    for move in best_weizhi:
        if move in empty(pix):
            m,n = pix_to_piz(move)
            return m,n

def click_pvp(event, x, y, flags, param=0):
    global flag,pix,pizs,piz
    if event == cv2.EVENT_LBUTTONDOWN:
        # print('mouse coords:', x, y)
        if 360 < x < 480 and 40 < y < 80:
            exit()
        if 240 < x < 360 and 40 < y < 80:
            pizs.pop()  # pop堆出拷贝的棋盘
            pizs.pop()
            board(pizs)
            if len(pizs)!=0:
                flag -= 1
                piz=copy.deepcopy(pizs[-1]) # 拷贝出来的棋盘的上一步复制到原棋盘
                for i in range(3):
                    for j in range(3):
                        if piz[i][j]==1:
                            cv2.circle(img, ((i + 1) * 120 + 60, (j + 1) * 120 + 60), 50, (0, 0, 0), -1)
                            cv2.imshow('chess',img)
                        elif piz[i][j]==-1:
                            cv2.circle(img, ((i + 1) * 120 + 60, (j + 1) * 120 + 60), 50, (255, 255, 255), -1)
                            cv2.imshow('chess',img)
        if 120 < x < 240 and 40 < y < 80:
            print("重新开始")
            board()
        for i in range(3):
            for j in range(3):
                if (i + 1) * 120 < x < (i + 2) * 120 and (j + 1) * 120 < y < (j + 2) * 120 and piz[i][j] == 0:
                    if flag % 2 == 0:
                        cv2.circle(img, ((i + 1) * 120 + 60, (j + 1) * 120 + 60), 50, (0, 0, 0), -1)
                        cv2.imshow('chess',img)
                        piz[i][j] = 1
                        pizs.append(copy.deepcopy(piz))
                    else:
                        cv2.circle(img, ((i + 1) * 120 + 60, (j + 1) * 120 + 60), 50, (255, 255, 255), -1)
                        cv2.imshow('chess',img)
                        piz[i][j] = -1
                        pizs.append(copy.deepcopy(piz))
                    flag = flag + 1
                    pix = sum(piz, [])
        Judge()

def click_pve(event, x, y, flags, param=0):
    global flag,pix,pizs,piz
    if event == cv2.EVENT_LBUTTONDOWN:
        # print('mouse coords:', x, y)
        if 360 < x < 480 and 40 < y < 80:
            exit()
        if 240 < x < 360 and 40 < y < 80:
            pizs.pop()
            pizs.pop()
            board(pizs)
            if len(pizs)!=0:
                piz=copy.deepcopy(pizs[-1])
                for i in range(3):
                    for j in range(3):
                        if piz[i][j]==1:
                            cv2.circle(img, ((i + 1) * 120 + 60, (j + 1) * 120 + 60), 50, (0, 0, 0), -1)
                            cv2.imshow('chess',img)
                        elif piz[i][j]==-1:
                            cv2.circle(img, ((i + 1) * 120 + 60, (j + 1) * 120 + 60), 50, (255, 255, 255), -1)
                            cv2.imshow('chess',img)
        if 120 < x < 240 and 40 < y < 80:
            print("重新开始")
            board()
        for i in range(3):
            for j in range(3):
                if (i + 1) * 120 < x < (i + 2) * 120 and (j + 1) * 120 < y < (j + 2) * 120 and piz[i][j] == 0:
                    cv2.circle(img, ((i + 1) * 120 + 60, (j + 1) * 120 + 60), 50, (0, 0, 0), -1)
                    cv2.imshow('chess',img)
                    piz[i][j] = 1
                    pizs.append(copy.deepcopy(piz))
                    pix = sum(piz, [])
                    if 0 in pix:
                        i,j = computer_move(pix)
                        cv2.circle(img, ((i + 1) * 120 + 60, (j + 1) * 120 + 60), 50, (255, 255, 255), -1)
                        cv2.imshow('chess',img)
                        piz[i][j] = -1
                        pizs.append(copy.deepcopy(piz))
                        pix = sum(piz, [])
                    else:
                        print('draw!')
                        print('the game finish!')
                        speaker.Speak("平局")
                        win32api.MessageBox(0, "平局", "提示",win32con.MB_OK)
        Judge()

def jzq_pve():
    board()
    cv2.namedWindow('chess')
    cv2.setMouseCallback('chess', click_pve)

def jzq_pvp():
    board()
    cv2.namedWindow('chess')
    cv2.setMouseCallback('chess', click_pvp)
