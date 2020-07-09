#!/usr/bin/python3
#coding:utf8
import os
import sys
import cv2
import time
import shutil
import pygame
import CarConf
#import CarMotor
import threading
import getUsedSpace
import numpy as np
####手柄控制， 收集图像####
import pyautogui as pg

#检测窗口
pic=pg.screenshot()
img = cv2.cvtColor(np.array(pic),cv2.COLOR_RGB2BGR)
template = cv2.imread('xb.PNG')
backworld = cv2.imread('back.PNG')
(h, w )= template.shape[:2]

threshold = 0.6
res2 = cv2.matchTemplate(img,backworld,cv2.TM_CCOEFF_NORMED)
loc_back = np.where( res2 >= threshold)

pg.moveTo(loc_back[1],loc_back[0])
pg.click()
# pg.moveRel(0, 50, duration=0.25)
# time.sleep(2)

res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
loc = np.where( res >= threshold)
print("窗体的面积：",1027-int(loc[0]),"*",int(loc[1])+w+6) #高*宽


if sys.version_info.major == 2:
    print('Please run this program with python3!')
    sys.exit(0)
    
print('''
   操作指南：
#1 先将USB手柄接收器插在电脑上
#2 打开手柄开关，自动连接
#3 按下ANALOG后可使用方向键
#4 此时按下start开始收集(此时图片没有存储)
# 建议行驶轨迹图片的收集和指示灯的分开进行
#5 按下手柄"前进"键MC人物前进并收集窗口内轨迹图(以第一人称),左键——鼠标左移动，人物左转，收集左转轨迹
#  右键——鼠标左移动，人物右转，收集右转轨迹，
#6 收集指示灯图片，后退键——人物停止，收集指示灯灭图，PSB_R1——灯亮图
#7 再次按下select可退出。

''')

Running = True
ret = False
orgFrame = None
#图像获取函数
#图像获取函数
def get_image():
    global orgFrame
    global ret
    global Running
    global cap
    while True:
        if Running:
               pic=pg.screenshot(region=(0,int(loc[0]),int(loc[1])+w+6,539)) #region的含义？
               #pic = cv2.imread("test.PNG")
               orgFrame = cv2.cvtColor(np.array(pic),cv2.COLOR_RGB2BGR) #屏幕拷贝转Opencv格式
               #time.sleep(0.01)
               
        else:
            time.sleep(0.01)


#作为子线程启动
th1 = threading.Thread(target=get_image)
th1.setDaemon(True)
th1.start()

#判断图像保存位置是否已经有图像来，有的话删除掉，重新建立新的文件夹
if os.path.exists(CarConf.path_image):
    shutil.rmtree(CarConf.path_image)
os.makedirs(CarConf.path_image)
print('Create Path \'' + CarConf.path_image + '\' success!')

direction = 'noo'
start = False
def save_image():
    global orgFrame
    global ret
    global Running
    global direction, start
    
    o = g = s = r = l =0
    t0 = 0
    while True:
        if Running:
            if orgFrame is not None:
                roi = orgFrame[CarConf.roi_range[0]:CarConf.roi_range[1], CarConf.roi_range[2]:CarConf.roi_range[3]]#提取跑道区域
                roi1 = orgFrame[CarConf.roi_rangeled[0]:CarConf.roi_rangeled[1], CarConf.roi_rangeled[2]:CarConf.roi_rangeled[3]]#提取跑道区域
                frame = roi.copy()
                frame_num = len(os.listdir(CarConf.path_image))
                if start is False:
                    t1 = time.time()
                    if frame_num == 0:
                        save_speed = 0
                    else:
                        t0 = t
                else:
                    t2 = time.time()
                    t = t2 - t1 + t0
                    save_speed = int(frame_num/(t))

                cv2.putText(frame, "Speed: " + str(save_speed) + '/s',
                            (40, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)#显示帧率                        
                cv2.putText(frame, "Num: " + str(frame_num),
                            (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)#显示帧率                   
                cv2.imshow('frame', frame)           
                cv2.imshow('led', roi1)           
                cv2.waitKey(1)
                 
                if start:
                    if (direction == 'off') | (direction == 'on'): #此处是采集灯的亮灭
                         roi = orgFrame[CarConf.roi_rangeled[0]:CarConf.roi_rangeled[1], CarConf.roi_rangeled[2]:CarConf.roi_rangeled[3]]#提取跑道区域
                    roi = cv2.resize(roi, CarConf.image_size, interpolation = cv2.INTER_LINEAR)#将图像缩小为指定尺寸                            
                    #根据按键的不同，将图像分类保存
                    if direction == 'go_straight':#go 
                        cv2.imwrite(CarConf.path_image + 'g_' + str(g) + '.png', roi)
                        g += 1
                        time.sleep(0.02)
                    elif direction == 'off':#speed_up
                        cv2.imwrite(CarConf.path_image + 's_' + str(s) + '.png', roi)
                        s += 1
                        time.sleep(0.02)
                    elif direction == 'turn_right':#right
                        cv2.imwrite(CarConf.path_image + 'r_' + str(r) + '.png', roi)
                        r += 1
                        time.sleep(0.02)
                    elif direction == 'turn_left':#left
                        cv2.imwrite(CarConf.path_image + 'l_' + str(l) + '.png', roi)
                        l += 1
                        time.sleep(0.02)
                    elif direction == 'on':#亮灯
                        cv2.imwrite(CarConf.path_image + 'o_' + str(o) + '.png', roi)
                        o += 1
                        time.sleep(0.02)
                    else:
                        pass
                else:
                    time.sleep(0.001)
            else:
                time.sleep(0.001)
        else:
            time.sleep(0.01)

#作为子线程启动
th2 = threading.Thread(target=save_image)
th2.setDaemon(True)
th2.start()

#####################################################################
key_map = {"PSB_CROSS":2, "PSB_CIRCLE":1, "PSB_SQUARE":3, "PSB_TRIANGLE":0,
        "PSB_L1": 4, "PSB_R1":5, "PSB_L2":6, "PSB_R2":7,
        "PSB_SELECT":8, "PSB_START":9, "PSB_L3":10, "PSB_R3":11};
action_map = ["CROSS", "CIRCLE", "", "SQUARE", "TRIANGLE", "L1", "R1", "L2", "R2", "SELECT", "START", "", "L3", "R3"]

# pygame.mixer.init()
# os.environ["SDL_VIDEODRIVER"] = "dummy"
# pygame.display.init()
# pygame.joystick.init()
# if pygame.joystick.get_count() > 0:
#     js=pygame.joystick.Joystick(0)
#     js.init()
#     jsName = js.get_name()
#     print("Name of the joystick:", jsName)
#     jsAxes=js.get_numaxes()
#     print("Number of axis:",jsAxes)
#     jsButtons=js.get_numbuttons()
#     print("Number of buttons:", jsButtons);
#     jsBall=js.get_numballs()
#     print("Numbe of balls:", jsBall)
#     jsHat= js.get_numhats()
#     print("Number of hats:", jsHat)

pygame.init()
go_ = False
while True:
    if True :
        pygame.joystick.init()
        jscount =  pygame.joystick.get_count()
        if jscount > 0:
            try:
                js=pygame.joystick.Joystick(0)
                js.init()
            except Exception as e:
                print(e)
        else:
            pygame.joystick.quit()
    else:
        js.quit();
        pygame.joystick.quit()

    pygame.event.pump()
    try:
        hat = js.get_hat(0)

        '''
        if js.get_button(key_map["PSB_R1"]) :
            print("R1")
        if js.get_button(key_map["PSB_R2"])  :
            print("R2")
        if js.get_button(key_map["PSB_SQUARE"]) :
            print("PSB_SQUARE")
        if js.get_button(key_map["PSB_CIRCLE"]) :
            print("PSB_CIRCLE")
        if js.get_button(key_map["PSB_TRIANGLE"]) :
            print("TRIANGLE")
        if js.get_button(key_map["PSB_CROSS"]) :
            print("CROSS")
        if js.get_button(key_map["PSB_R3"]) :
            print("R3")
        if js.get_button(key_map["PSB_L3"]) :
            print("L3")
        if js.get_button(key_map["PSB_L1"]) :
            print("PSB_L1")
        if js.get_button(key_map["PSB_L2"]) :
            print("PSB_L2")
        '''
        if js.get_button(key_map["PSB_START"]):
            #print("START")
            if start :
                time.sleep(0.15)
                start = False
            else:
                #direction = 'go_straight'
                time.sleep(0.15)
                start = True
        if js.get_button(key_map["PSB_SELECT"]):
            #print("SELECT")
            if go_ :
                go_ = False
                break
            else:
                #pg.keyDown('w')  #一直按住前进
                time.sleep(0.15)
                go_ = True
        
        if start:
            #print(hat)
            if hat[0] > 0:
                print("right")
                pg.moveRel(60, 0, duration=0.15)  #386为90度
                #speed = CarConf.turn_right
                direction = 'turn_right'
                #car.SetSpeed(speed[0], speed[1])
            elif hat[0] < 0:
                print("left")
                pg.moveRel(-60, 0, duration=0.15)
                #speed = CarConf.turn_left
                direction = 'turn_left'
                #car.SetSpeed(speed[0], speed[1])
            elif hat[1] > 0:
                print('go_straight')
                pg.keyDown('w')  #一直按住前进
                #speed = CarConf.go_straight
                direction = 'go_straight'
                #car.SeatSpeed(speed[0], speed[1])
            elif hat[1] < 0:
                print('off')
                direction = 'off'
                pg.keyUp('w')  #一直按住前进
            elif js.get_button(key_map["PSB_R1"]) :
                direction = 'on'
                print("on")
            else:
                direction = 'noo'
                #if direction != 'stop':
                #    direction = 'go_straight'
                #direction = 'go_straight'
                print(direction)
                
        else:
            pass
    except Exception as e:
        print(e)
#car.SetSpeed(0, 0)
