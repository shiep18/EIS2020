import cv2
import numpy as np
import pygame,sys
pygame.init()
pygame.mixer.init()
panduan=False
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW) 
 
background = None
  
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
    if cv2.contourArea(c) < 2000: # 对于矩形区域，只显示大于给定阈值的轮廓，所以一些微小的变化不会显示。对于光照不变和噪声低的摄像头可不设定轮廓最小尺寸的阈值
      continue
    (x, y, w, h) = cv2.boundingRect(c) # 该函数计算矩形的边界框
    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)
    panduan=True

  #screen = pygame.display.set_mode([640, 480])
  # pygame.time.delay(1000)
  if panduan:
    cv2.imshow("comtours",frame)#原图
    cv2.imshow("dis",diff)
    if not pygame.mixer.music.get_busy(): 
      print("music\n") 
      pygame.mixer.music.load("ok.mp3")
      pygame.mixer.music.play()
    else:
      key = cv2.waitKey(1) & 0xFF
      if key == ord('q'):
        break 
  else:
    print("1\n")
    cv2.imshow("comtours",frame)#原图
    cv2.imshow("dis",diff) 

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
