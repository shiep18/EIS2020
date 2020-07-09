#!/usr/bin/python3
#coding:utf8
####深度学习，自主寻线####
import time
time_start = time.time()
import os
import cv2
import sys
import CarConf
#import CarMotor
import threading
import numpy as np
import tensorflow as tf
from PIL import Image
import pyautogui as pg

while True:
    f = open('e:/2020class/QianRuShi/大作业(组)/自动驾驶及app控制/relate.txt')
    w = f.read()
    if w == '1':
        f.close()
        f = open('relate.txt','r+')
        f.write('0')
        f.close()
        break
    else:
        pass
    f.close()


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

time_end = time.time()
t = time_end - time_start
print("加载库耗时:{:.0f}m{:.0f}s ".format(t//60, t % 60))

########################################################
time_start = time.time()
# Restore model

model_path2 = CarConf.path_model + CarConf.model_names2
model_path = CarConf.path_model + CarConf.model_names

print(model_path2)
if not (os.path.exists(model_path2 + '.yaml') and  os.path.exists(model_path2 + '.h5')):
    print('Model does not exists!')
    sys.exit(0)   
with open(model_path2 + '.yaml') as yamlfile:
     loaded_model_yaml2 = yamlfile.read()

print(model_path)
if not (os.path.exists(model_path + '.yaml') and  os.path.exists(model_path + '.h5')):
    print('Model does not exists!')
    sys.exit(0)   
with open(model_path + '.yaml') as yamlfile:
     loaded_model_yaml = yamlfile.read()
     
model_track = tf.keras.models.model_from_yaml(loaded_model_yaml)
model_track2 = tf.keras.models.model_from_yaml(loaded_model_yaml2)


model_track.load_weights(model_path + '.h5')
model_track2.load_weights(model_path2 + '.h5')

sgd = tf.keras.optimizers.Adam(lr=CarConf.learn_rate)
model_track.compile(loss='mse',optimizer=sgd, metrics=['accuracy'])
model_track2.compile(loss='mse',optimizer=sgd, metrics=['accuracy'])

time_end = time.time()
t = time_end - time_start
print("加载模型耗时:{:.0f}m{:.0f}s ".format(t//60, t % 60))



########################################################
orgFrame = None
frame    = None
Running  = True

ret = False
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
               #time.sleep(0.001)
        else:
            time.sleep(0.01)

#作为子线程启动
th1 = threading.Thread(target=get_image)
th1.setDaemon(True)
th1.start()


flag = 1 #红绿灯
key = 0
#预测函数
def pred_data(orgFrame):
    global model_track
    global model_track2
    global flag
    global key 
    
    orgFrame_rgb = cv2.cvtColor(orgFrame, cv2.COLOR_BGR2RGB)#转为RGB图，opencv读取时默认是BGR
    roi_track = orgFrame_rgb[CarConf.roi_range[0]:CarConf.roi_range[1], CarConf.roi_range[2]:CarConf.roi_range[3]]#提取跑道区域，防止过多无关因素的干扰
    roi_led = orgFrame_rgb[CarConf.roi_rangeled[0]:CarConf.roi_rangeled[1], CarConf.roi_rangeled[2]:CarConf.roi_rangeled[3]]
    mask_track = cv2.resize(roi_track, CarConf.image_size, interpolation = cv2.INTER_LINEAR)#将图像缩小到和训练一样到尺寸
    mask_led = cv2.resize(roi_led, CarConf.image_size, interpolation = cv2.INTER_LINEAR)

    img_array = tf.keras.preprocessing.image.img_to_array(mask_track)#将图像转成数组
    img_led = tf.keras.preprocessing.image.img_to_array(mask_led)#将图像转成数组

    img_expand_dims = np.expand_dims(img_array, axis=0)#将数组转成矩阵   
    img_led_expand_dims = np.expand_dims(img_led, axis=0)#将数组转成矩阵

    x_track = tf.keras.applications.resnet50.preprocess_input(img_expand_dims)#去值中心化
    x_track_led = tf.keras.applications.resnet50.preprocess_input(img_led_expand_dims)#去值中心化
    #time1 = time.time()

    roi = orgFrame[CarConf.roi_range[0]:CarConf.roi_range[1], CarConf.roi_range[2]:CarConf.roi_range[3]]#截取跑道区域，防止其他干扰 高度截取（ROI[0]-ROI[1])
    blur = cv2.GaussianBlur(roi, (5, 5), 0)
    # mask
    mask = cv2.inRange(blur,np.array([[14,16,136]]), np.array([[175,133,194]]))
    # wei cao zuo
    res = cv2.bitwise_and(blur, blur, mask=mask)        
    imgray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    retNew, threshNew = cv2.threshold(imgray, 58, 255, 0)
    x, y, w, h = cv2.boundingRect(threshNew)
    print(w,h)
    #cv2.imshow('HSV', threshNew)

    if flag == 0 :
        result_track_led = model_track2.predict_classes(x_track_led,verbose=0)#预测输出
        if result_track_led[0] == 0:#预测标签值为1时
            #ledflag = True`
            pg.keyUp('w')  #一直按住前进`
            print("stop2")
            time.sleep(2)
            flag = 0
            #pg.keyUp('w')  #一直按住前进
        elif result_track_led[0] == 1:#预测标签值为1时
             print("go")
             time.sleep(5)
             #for a in range(key):
             pg.moveRel(70, 70, duration=0.15)
             pg.keyDown('w')
             time.sleep(5)
             flag = 1 
        else:
            pass
    else:
        result_track = model_track.predict_classes(x_track,verbose=0)#预测输出
        if (result_track[0] == 0) :#预测标签值为0时
            pg.keyDown('w')  #一直按住前进
            print("go1")
        elif (result_track[0] == 1) & (flag == 2) :#预测标签值为3时
            pg.moveRel(80, 0, duration=0.15)
            print("turn")
        elif (result_track[0] == 2) & (flag == 2) :#预测标签值为3时
            pg.moveRel(-80, 0, duration=0.15)
            print("left")
   
    if (w >295) & (h > 90) :  #对红色标志的识别
        flag = 0
        if key < 1:
            pg.keyUp('w')
            time.sleep(8)
            #pg.keyUp('w')  #一直按住前进`
            #pg.moveRel(-70, -70, duration=0.15)
        key = key + 1
        #time.sleep(5)
        print("stop")

                  
while True:
    if orgFrame is not None:
        t1 = cv2.getTickCount()#记录程序运行时间
        frame = orgFrame       
        pred_data(frame)
        frame = frame[CarConf.roi_rangeled[0]:CarConf.roi_rangeled[1], CarConf.roi_rangeled[2]:CarConf.roi_rangeled[3]]
        frame2 = orgFrame[CarConf.roi_range[0]:CarConf.roi_range[1],CarConf.roi_range[2]:CarConf.roi_range[3]]
        
        t2 = cv2.getTickCount()
        time_r = (t2 - t1) / cv2.getTickFrequency()
        fps = 1.0/time_r#计算帧率
        
        cv2.putText(frame, "FPS " + str("%.1f" % fps),
                    (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)#显示帧率
        cv2.imshow("frame", frame) #显示图像
        cv2.imshow("frame2", frame2)
        cv2.waitKey(1)       
    else:
        time.sleep(0.001)
#car.SetSpeed(0, 0)
