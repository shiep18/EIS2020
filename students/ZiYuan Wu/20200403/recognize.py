import cv2
import numpy as np
import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
from PyUserInput import pykeyboard

picposition_x = 0
picposition_y = 0

def key_con(xmax,ymax,k): # 控制移动

    if xmax > 340:
        k.press_key("d")
    elif xmax < 270:
        k.press_key("a")
    else:
        k.release_key("a")
        k.release_key("d")

    if ymax > 300:
        k.press_key("s")
    elif ymax < 240:
        k.press_key("w")
    else:
        k.release_key("w")
        k.release_key("s")       



    #回调函数，此处并无它用，只是函数要求要有
def callback(object):
    pass



print('Running......')


def move(posx,posy,times,kk):
    if times == 0:
        mc.player.setPos(posx,5,posy)
        times += 1
    else:
        pos = mc.player.getTilePos()            #重新获取坐标位置
        key_con(posx,posy,kk)

def find_obj(framenew, num_p, upper_all, lower_all):
    blur_new = cv2.GaussianBlur(framenew, (5, 5), 0)
    for i in range(1, num_p+1):
        maskNEW = cv2.inRange(blur_new, lower_all[i], upper_all[i])
        # wei cao zuo
        res1 = cv2.bitwise_and(blur_new, blur_new, mask=maskNEW)
        imgray = cv2.cvtColor(res1, cv2.COLOR_BGR2GRAY)
        thresh = cv2.getTrackbarPos("thresh", "new1")  # 获取滑杆值V
        retNew, threshNew = cv2.threshold(imgray, thresh, 255, 0)
        #threshNew = cv2.adaptiveThreshold(imgray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
        #cv2.imshow('new2', threshNew)
        x, y, w, h = cv2.boundingRect(threshNew)
        img = cv2.circle(framenew, (int(x+w/2), int(y+h/2)),20, [255,0,0])
        cv2.rectangle(img,(270,240),(340,300),(0,255,0), 1)
        cv2.imshow('new1', img)
        #print("x: ",x,"y: ",y)
        return x ,y


def dynamic():
  global picposition_x
  global picposition_y
  upper_save = np.zeros((1, 3)) #阈值存储
  lower_save = np.zeros((1, 3))
  tm = 0
  key = 1
  num = 0
  k1 = pykeyboard.PyKeyboard()
  cap = cv2.VideoCapture(0) 
  background = None
  cv2.namedWindow("HSV_SET",cv2.WINDOW_NORMAL)
    #创建滑动条，参数1：滑动条名称;参数2：滑动条要显示在的图像名称;参数3,4：滑动条的范围;参数5：回调函数，每次滑动时会调用该函数，若无需要可设为空
  cv2.createTrackbar("upper_H","HSV_SET",0,255, callback)
  cv2.createTrackbar("upper_S","HSV_SET",0,255, callback)
  cv2.createTrackbar("upper_V","HSV_SET",0,255, callback)
  cv2.createTrackbar("lower_H","HSV_SET",0,255, callback)
  cv2.createTrackbar("lower_S","HSV_SET",0,255, callback)
  cv2.createTrackbar("lower_V","HSV_SET",0,255, callback)
  cv2.setTrackbarPos("upper_H", "HSV_SET",255)
  cv2.setTrackbarPos("upper_S", "HSV_SET",255)
  cv2.setTrackbarPos("upper_V", "HSV_SET",255)
  while True:
    # 读取视频流
  
    ret, Frame= cap.read()
    if key == 1:
        frame = Frame.copy()
        blur = cv2.GaussianBlur(frame, (5, 5), 0)
        upper_H = cv2.getTrackbarPos("upper_H", "HSV_SET")  # 获取滑杆值H
        upper_S = cv2.getTrackbarPos("upper_S", "HSV_SET")  # 获取滑杆值S
        upper_V = cv2.getTrackbarPos("upper_V", "HSV_SET")  # 获取滑杆值V
        lower_H = cv2.getTrackbarPos("lower_H", "HSV_SET")  # 获取滑杆值H
        lower_S = cv2.getTrackbarPos("lower_S", "HSV_SET")  # 获取滑杆值S
        lower_V = cv2.getTrackbarPos("lower_V", "HSV_SET")  # 获取滑杆值V
        lower_pic = np.array([[lower_H, lower_S, lower_V]])
        upper_pic = np.array([[upper_H, upper_S, upper_V]])
                # mask
        mask = cv2.inRange(blur, lower_pic, upper_pic)
                # wei cao zuo
        res = cv2.bitwise_and(blur, blur, mask=mask)
                #两个窗体分开，不然无法调节滑杆值
        cv2.imshow('HSV', res)
    elif key == 2:
        if Frame is not None and ret:
            frame = Frame.copy()
            picposition_x, picposition_y = find_obj(frame, num, upper_save, lower_save)
            move(picposition_x,picposition_y,tm,k1)
            print(picposition_x,picposition_y)
            tm = tm + 1 
            if tm > 50:
                tm = 5
                        #print(picposition_x,picposition_y)
        else:
            time.sleep(0.01)

    k = cv2.waitKey(5) & 0xFF
    # 按'q'健退出循环
    if k == ord('q'):
      cap.release()
      cv2.destroyAllWindows()
      break
    elif k == ord('z'):
        key = 1
    elif k == ord('o'):
        key = 2
        cv2.destroyWindow("HSV")
        cv2.destroyWindow("HSV_SET")
        cv2.namedWindow("new1", cv2.WINDOW_NORMAL)
        cv2.createTrackbar("thresh","new1",0,255, callback)
    elif k == ord('x'): #阈值存储
        upper_save = np.append(upper_save, upper_pic, axis=0)
        lower_save = np.append(lower_save, lower_pic, axis=0)
        num = num + 1
        print("the all sample:", num)
    else:
        pass
   
  # When everything done, release the capture
dynamic()