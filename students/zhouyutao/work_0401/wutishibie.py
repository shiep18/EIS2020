import cv2
import numpy as np
import os
import time

cap = cv2.VideoCapture(0) 
 
background = None

x=0
while True:
  # 读取视频流
  ret, frame= cap.read()
  gray_lwpCV = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
  # 将第一帧设置为整个输入的背景
  if background is None:
      background = gray_lwpCV
      continue

  
  # 对于每个从背景之后读取的帧都会计算其与背景之间的差异，并得到一个差分图（different map）。
  diff = cv2.absdiff(background, gray_lwpCV)
  diff = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1] # 二值化阈值处理
 
  # 显示矩形框
  contours, hierarchy = cv2.findContours(diff.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # 该函数计算一幅图像中目标的轮廓
  for c in contours:
    if cv2.contourArea(c) < 1500: # 对于矩形区域，只显示大于给定阈值的轮廓，所以一些微小的变化不会显示。对于光照不变和噪声低的摄像头可不设定轮廓最小尺寸的阈值
      continue
    (x, y, w, h) = cv2.boundingRect(c) # 该函数计算矩形的边界框
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
  print(x)
  if x>=100:
    x=0
    os.startfile('颁奖音乐.mp3')
    time.sleep(12)
    continue
    
  cv2.imshow('contours', frame)
  cv2.imshow('dis', diff)
 
  key = cv2.waitKey(1) & 0xFF
  # 按'q'健退出循环
  if key == ord('q'):
    break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
