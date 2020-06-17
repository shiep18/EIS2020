import random
import vtk
import time
import cv2
import serial
import tkinter as tk
import numpy as np
import os
from os import system
import win32com.client



# 读取视频
pic1 = cv2.imread('red_golf.jpg')
pic2 = cv2.imread('blue_golf.jpg')
pic3 = cv2.imread('white_golf.jpg')
pic4 = cv2.imread('background.jpg')
pic = pic4
width = 165  # 定义摄像头获取图像宽度
height = 160  # 定义摄像头获取图像长度
speaker = win32com.client.Dispatch("SAPI.SpVoice")




    
def get_return():
    global pic
    # 设定蓝色阈值
    lower_red = np.array([0, 40, 40])
    upper_red = np.array([15, 255, 255])
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    lower_white = np.array([0, 0, 120])
    upper_white = np.array([180, 60, 255])

    # 转换成HSV
    hsv = cv2.cvtColor(pic, cv2.COLOR_BGR2HSV)
    # 根据阈值构建掩模
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    mask2 = cv2.inRange(hsv, lower_blue, upper_blue)
    mask3 = cv2.inRange(hsv, lower_white, upper_white)

    def get_return_mask(mask):
        global pic, width, height
        contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                               cv2.CHAIN_APPROX_SIMPLE)  # 该函数计算一幅图像中目标的轮廓
        res = cv2.bitwise_and(pic, pic, mask=mask)
        xCenter = 0
        yCenter = 0
        for c in contours:
            if cv2.contourArea(c) < 200:  # 对于矩形区域，只显示大于给定阈值的轮廓，所以一些微小的变化不会显示。对于光照不变和噪声低的摄像头可不设定轮廓最小尺寸的阈值
                continue
            (x, y, w, h) = cv2.boundingRect(c)  # 该函数计算矩形的边界框
            xCenter = x + w / 2
            yCenter = y + h / 2
            cv2.rectangle(pic, (x, y), (x + w, y + h), (0, 255, 0), 1)
            cv2.rectangle(res, (x, y), (x + w - 1, y + h - 1), (0, 255, 0), 1)
        # 显示图层
        #cv2.imshow('res', res)
        cv2.imshow('frame', pic)
        if xCenter == 0 and yCenter == 0:
            return 1
        else:
            return 0

    if get_return_mask(mask1) == 0:
        print("red")
        speaker.Speak("红球")
        return 1
    elif get_return_mask(mask2) == 0:
        print("blue")
        speaker.Speak("蓝球,忽略")
        time.sleep(3)
        return 2
    elif get_return_mask(mask3) == 0:
        print("white")
        speaker.Speak("白球,忽略")
        time.sleep(3)
        return 3
    else:
        print("0")
        return 0


class vtkTimerCallback1:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.f = 1
        self.i = 0
        self.actors = []
        self.balls = []  # 坐标
        self.mballs = []
        self.commd = 9
        self.ser=serial.Serial("COM13","9600",timeout=0.5)


    def execute(self, obj, event):
        global pic, pic1, pic2, pic3, pic4
        num = ""
        numx = ""
        numy = ""
        speeds = ['9']
        resp=self.ser.readline().decode().strip()
        if resp !="":
            spds=resp.split(",")
            speeds=list(map(int,spds))
            self.commd = speeds[0]
            
        if self.commd == 1:
            if self.f == 1:
                if self.x < 205:
                    self.actors[0].SetPosition(self.x, self.y, 0)
                    self.x += 5
            elif self.f == -1:
                if self.x > 0:
                    self.actors[0].SetPosition(self.x, self.y, 0)
                    self.x -= 5

            if self.x == 205 or self.x == 0:
                self.actors[0].RotateZ(180)
                self.f = -self.f
                self.y += 5

            if self.y == 210:
                self.f = 2
            #print(self.x,self.y)
            for i in range(self.actors[1]):
                pic = pic4
                if self.x == self.balls[i][0] and self.y == self.balls[i][1]:
                    speaker.Speak("发现一个球")
                    print("球的坐标是x=", self.x, "y=", self.y)
                    if self.balls[i][3] == 1:
                        pic = pic1
                    elif self.balls[i][3] == 2:
                        pic = pic2
                    elif self.balls[i][3] == 3:
                        pic = pic3
                    # else:
                    #     pic = pic4
                    if get_return() == 1:
                        self.i += 1
                        self.mballs[i].SetPosition(10000, 10000, 10000)
                        self.balls[i][0] = 10000
                        self.balls[i][1] = 10000
                        print("红球数量是", self.i)
                        num=str(self.i)
                        speaker.Speak("红球数量为"+num)
                        time.sleep(1)

        elif self.commd == 2:                      #转向
            self.actors[0].RotateZ(90)
            self.commd = 9
            
            
        elif self.commd == 3:                      #前
            if self.x >=0 and self.x <=205 and self.y >=0 and self.y <205:
                self.y=self.y + 5
                self.actors[0].SetPosition(self.x, self.y, 0)
                self.commd = 10
            print(self.x,self.y)
                
        elif self.commd == 4:                       #后
            if self.x >= 0 and self.x <= 205 and self.y >= 5 and self.y <= 205:
                self.y=self.y - 5
                self.actors[0].SetPosition(self.x, self.y, 0)
                self.commd = 10
            print(self.x,self.y)
            
        elif self.commd == 5:                       #左
            if self.x >= 5 and self.x <= 205 and self.y >=0 and self.y <= 205:
                self.x=self.x-5
                self.actors[0].SetPosition(self.x, self.y, 0)
                self.commd = 10
            print(self.x,self.y)
            
        elif self.commd == 6:                       #右
            if self.x >= 0 and self.x <205 and self.y >=0 and self.y <= 205:
                self.x=self.x+5
                self.actors[0].SetPosition(self.x, self.y, 0)
                self.commd = 10
            print(self.x,self.y)
            
        elif self.commd == 7:                      #回到起点
            t = int(self.x / 5)
            u = int(self.y / 5)
            if self.x > 0:
                for i in range(t):
                    self.x=self.x - 5
                    self.actors[0].SetPosition(self.x, self.y, 0)
                time.sleep(3)
            if self.y > 0:
                for i in range(u):
                    self.y=self.y - 5
                    self.actors[0].SetPosition(self.x, self.y, 0)
            print(self.x,self.y)
            if self.x == 0 and self.y == 0:
                self.f = 1
                self.commd = 9
                
                                    
        elif self.commd == 8:                    #语音播报现在位置
            numx = str(self.x)
            numy = str(self.y)
            print(self.x,self.y)
            speaker.Speak("机器人现在的位置是x="+numx+"y="+numy)
            self.commd = 9
                      
        
        if self.commd == 10:                     #遇球判定
            for i in range(self.actors[1]):
                pic = pic4
                if self.x == self.balls[i][0] and self.y == self.balls[i][1]:
                    speaker.Speak("发现一个球")
                    print("球的坐标是x=", self.x, "y=", self.y)
                    if self.balls[i][3] == 1:
                        pic = pic1
                    elif self.balls[i][3] == 2:
                        pic = pic2
                    elif self.balls[i][3] == 3:
                        pic = pic3
                    # else:
                    #     pic = pic4
                    if get_return() == 1:
                        self.i += 1
                        self.mballs[i].SetPosition(10000, 10000, 10000)
                        self.balls[i][0] = 10000
                        self.balls[i][1] = 10000
                        print("红球数量是", self.i)
                        num=str(self.i)
                        speaker.Speak("红球数量为"+num)
                        time.sleep(1)
            self.commd = 9
            
        if self.commd == 0:
            if speeds[1] > 205 or speeds[1] <0 or speeds[2] >205 or speeds[2] <0:
                speaker.Speak("超出范围，请重新输入")
                self.commd = 10
            else:    
                self.x = speeds[1]
                self.y = speeds[2]
                self.actors[0].SetPosition(self.x, self.y, 0)
                self.commd = 10
            
            
            

        iren = obj
        iren.GetRenderWindow().Render()
        return self.x, self.y


def main():
    red_ball = 0
    blue_ball = 0
    white_ball = 0
    balls_coordinates = []
    balls_coordinates_and_color = []
    sphereSource = []
    actor = []
    mapper = []
    balls_numbers = random.randint(3, 20)   
    # Read STL
    reader1 = vtk.vtkSTLReader()
    reader1.SetFileName("golf_robot.stl")

    # Create a mapper and actor
    mapper111 = vtk.vtkPolyDataMapper()
    mapper111.SetInputConnection(reader1.GetOutputPort())
    actor111 = vtk.vtkActor()
    actor111.SetMapper(mapper111)
    prop = actor111.GetProperty()

    for a in range(balls_numbers):
        b = "sphereSource" + str(a)
        sphereSource.append(b)
        c = "actor" + str(a)
        actor.append(c)
        d = "mapper" + str(a)
        mapper.append(d)

        balls_coordinates_x = random.randint(1, 10) * 20
        balls_coordinates_y = random.randint(1, 10) * 20
        balls_color = random.randint(1, 3)
        if balls_color == 1:
            red_ball = red_ball + 1
        elif balls_color == 2:
            blue_ball = blue_ball + 1
        elif balls_color == 3:
            white_ball = white_ball + 1
        balls = [balls_coordinates_x, balls_coordinates_y, 0]
        balls_and_color = [balls_coordinates_x, balls_coordinates_y, 0, balls_color]
        balls_coordinates.append(balls)
        balls_coordinates_and_color.append(balls_and_color)

    print('balls =', balls_numbers, 'red balls =', red_ball, 'blue balls =', blue_ball, 'white balls =', white_ball)
    print(balls_coordinates_and_color)

    for i in range(balls_numbers):
        sphereSource[i] = vtk.vtkSphereSource()
        sphereSource[i].SetCenter(balls_coordinates[i][0:3])
        sphereSource[i].SetRadius(10)
        sphereSource[i].SetThetaResolution(64)
        sphereSource[i].SetPhiResolution(64)

        # Create a mapper and actor
        mapper[i] = vtk.vtkPolyDataMapper()
        mapper[i].SetInputConnection(sphereSource[i].GetOutputPort())
        actor[i] = vtk.vtkActor()
        actor[i].SetMapper(mapper[i])
        if balls_coordinates_and_color[i][3] == 1:
            prop = actor[i].GetProperty().SetColor(1, 0, 0) #红
        elif balls_coordinates_and_color[i][3] == 2:
            prop = actor[i].GetProperty().SetColor(0, 0, 1) #蓝
        elif balls_coordinates_and_color[i][3] == 3:
            prop = actor[i].GetProperty()  #白

    # Setup a renderer, render window, and interactor
    renderer = vtk.vtkRenderer()
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # Add the actor to the scene
    for a in range(balls_numbers):
        # Add the actor to the scene
        renderer.AddActor(actor[a])
    renderer.AddActor(actor111)
    renderer.SetBackground(0, 1, 0)  # Background color white

    actor111.SetOrigin(0,0,0)

    # Render and interact
    renderWindow.Render()

    # Initialize must be called prior to creating timer events.
    renderWindowInteractor.Initialize()

    # Sign up to receive TimerEvent
    cb = vtkTimerCallback1()
    cb.actors.append(actor111)
    cb.actors.append(balls_numbers)
    for i in range(balls_numbers):
        cb.balls.append(balls_coordinates_and_color[i])
        cb.mballs.append(actor[i])
    renderWindowInteractor.AddObserver('TimerEvent', cb.execute)
    timerId = renderWindowInteractor.CreateRepeatingTimer(100)

    # start the interaction and timer
    renderWindowInteractor.Start()


if __name__ == '__main__':
    main()
    
    
