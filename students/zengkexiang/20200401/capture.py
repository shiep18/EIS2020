import cv2
import numpy as np
import pygame

file = r'D:\0\Music\Scott Bradley - Touche,  Cat! (1954, Tom and Jerry).mp3'
pygame.mixer.init()
track = pygame.mixer.music.load(file)


cap = cv2.VideoCapture(0)

background = None
a = 0
while True:
    # 读取视频流
    ret, frame = cap.read()
    gray_lwpCV = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 将第一帧设置为整个输入的背景
    if background is None:
        background = gray_lwpCV
        continue
    # 对于每个从背景之后读取的帧都会计算其与背景之间的差异，并得到一个差分图（different map）。
    diff = cv2.absdiff(background, gray_lwpCV)
    diff = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]  # 二值化阈值处理

    index = 0
    # 显示矩形框
    i = 0
    binary,contours, hierarchy = cv2.findContours(diff.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # 该函数计算一幅图像中目标的轮廓
    for c in contours:
        if cv2.contourArea(c) > 1200:  # 对于矩形区域，只显示大于给定阈值的轮廓，所以一些微小的变化不会显示。对于光照不变和噪声低的摄像头可不设定轮廓最小尺寸的阈值
            (x, y, w, h) = cv2.boundingRect(c)  # 该函数计算矩形的边界框
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            index = 1
            i -= 1
        else:
            i += 1
    if i >= len(contours) - 1:
        index = 0

    if index ==1 and a == 0:
        pygame.mixer.music.play()
        a = 1
    if index == 0 and a == 1:
        pygame.mixer.music.pause()
        a = 0

    j =str(len(contours))

    print("len = :"+j,"i = :"+str(i))



 #   if index == 0:
       # pygame.mixer.music.pause()


    cv2.imshow('contours', frame)
    cv2.imshow('dis', diff)

    key = cv2.waitKey(1) & 0xFF
    # 按'q'健退出循环
    if key == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

