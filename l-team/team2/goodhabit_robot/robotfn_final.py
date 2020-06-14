import vtk
import time
import numpy as np
import cv2
import os
import win32com.client as win
from aip import AipSpeech
import speech_recognition as sr
import requests
import json
import re

#初始化语音识别系统
BAIDU_APP_ID = '19165943'
BAIDU_API_KEY = 'YZvt651qpTG8Sm0MmocMW9oz'
BAIDU_SECRET_KEY = 'GD5y6RcPciVdp05S6TWT9YHaQv3YGpbb'
aip_speech = AipSpeech(BAIDU_APP_ID, BAIDU_API_KEY, BAIDU_SECRET_KEY)
r = sr.Recognizer()
mic = sr.Microphone(sample_rate=16000)

#初始化yolo检测系统
yolo_dir = 'D:\BaiduNetdiskDownload\yolov3'  # YOLO文件路径一定不能有中文在路径里面
weightsPath = os.path.join(yolo_dir, 'yolov3.weights')  # 权重文件
configPath = os.path.join(yolo_dir, 'yolov3.cfg')  # 配置文件
labelsPath = os.path.join(yolo_dir, 'coco.names')  # label名称
imgPath = os.path.join(yolo_dir, 'desk.jpg')  # 测试图像
CONFIDENCE = 0.5  # 过滤弱检测的最小概率
THRESHOLD = 0.4  # 非最大值抑制阈值

with open(labelsPath, 'rt') as f:
    labels = f.read().rstrip('\n').split('\n')
# 加载网络、配置权重
net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)
# 加载图片、转为blob格式、送入网络输入层 获取网络输出层信息（所有输出层的名字），设定并前向传播
start = time.time()
img = cv2.imread(imgPath)
(H, W) = img.shape[:2]
blobImg = cv2.dnn.blobFromImage(img, 1.0/255.0, (416, 416), None, True, False)  ## net需要的输入是blob格式的，用blobFromImage这个函数来转格式
net.setInput(blobImg)  ## 调用setInput函数将图片送入输入层
outInfo = net.getUnconnectedOutLayersNames()  ## 前面的yolov3架构也讲了，yolo在每个scale都有输出，outInfo是每个scale的名字信息，供net.forward使用
layerOutputs = net.forward(outInfo)  # 得到各个输出层的、各个检测框等信息，是二维结构。
boxes = [] # 所有边界框（各层结果放一起）
coordinate = [] #物体坐标
ob = []  #物体名称
postion = [0,0] #机器人位置，初始在(0,0)
obbox = [0,100] #物品放置的位置
confidences = [] # 所有置信度
classIDs = [] # 所有分类ID
for out in layerOutputs:  # 各个输出层
    for detection in out:  # 各个框框
        # 拿到置信度
        scores = detection[5:]  # 各个类别的置信度
        classID = np.argmax(scores)  # 最高置信度的id即为分类id
        confidence = scores[classID]  # 拿到置信度
        # 根据置信度筛查
        if confidence > CONFIDENCE:
            box = detection[0:4] * np.array([W, H, W, H])  # 将边界框放会图片尺寸
            (centerX, centerY, width, height) = box.astype("int")
            
            x = int(centerX - (width / 2))
            
            y = int(centerY - (height / 2))
            coordinate.append([centerX,centerY])
            boxes.append([x, y, int(width), int(height)])
            confidences.append(float(confidence))
            classIDs.append(classID)
#应用非最大值抑制(non-maxima suppression，nms)进一步筛掉
idxs = cv2.dnn.NMSBoxes(boxes, confidences, CONFIDENCE, THRESHOLD) # boxes中，保留的box的索引index存入idxs
# 应用检测结果
np.random.seed(42)
COLORS = np.random.randint(0, 255, size=(len(labels), 3), dtype="uint8")  # 框框显示颜色，每一类有不同的颜色，每种颜色都是由RGB三个值组成的，所以size为(len(labels), 3)
if len(idxs) > 0:
    for i in idxs.flatten(): # indxs是二维的，第0维是输出层，所以这里把它展平成1维
        (x, y) = (boxes[i][0], boxes[i][1])
        (w, h) = (boxes[i][2], boxes[i][3])
        color = [int(c) for c in COLORS[classIDs[i]]]
        cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)  # 线条粗细为2px
        ob.append(labels[classIDs[i]])
        text = "{}: {:.4f}".format(labels[classIDs[i]], confidences[i])
        cv2.putText(img, text, (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)  # cv.FONT_HERSHEY_SIMPLEX字体风格、0.5字体大小、粗细2px
end = time.time()


def robotfont(a):
    for i in range(10):
        time.sleep(0.1)
        actor1.RotateY(-4.5)
        actor4.RotateY(-9)
        renderWindow.Render()

    for i in range(10):
        time.sleep(0.1)
        actor1.RotateY(+9)
        actor4.RotateY(+9)
        actor3.RotateY(-4.5)
        actor2.RotateY(-9)
        renderWindow.Render()

    for i in range(a):
        for i in range(10):
            time.sleep(0.1)
            actor1.RotateY(-9)
            actor4.RotateY(-9)
            actor3.RotateY(+9)
            actor2.RotateY(+9)
            renderWindow.Render()
        for i in range(10):
            time.sleep(0.1)
            actor1.RotateY(+9)
            actor4.RotateY(+9)
            actor3.RotateY(-9)
            actor2.RotateY(-9)
            renderWindow.Render()

    for  i in range (10):
        time.sleep(0.1)
        actor1.RotateY(-4.5)
        actor3.RotateY(+4.5)
        actor2.RotateY(+9)
        renderWindow.Render()


def robotfontwithob(a):
    for i in range(10):
        time.sleep(0.1)
        actor1.RotateY(-4.5)

        renderWindow.Render()

    for i in range(10):
        time.sleep(0.1)
        actor1.RotateY(+9)
  
        actor3.RotateY(-4.5)

        renderWindow.Render()

    for i in range(a):
        for i in range(10):
            time.sleep(0.1)
            actor1.RotateY(-9)

            actor3.RotateY(+9)

            renderWindow.Render()
        for i in range(10):
            time.sleep(0.1)
            actor1.RotateY(+9)

            actor3.RotateY(-9)

            renderWindow.Render()

    for  i in range (10):
        time.sleep(0.1)
        actor1.RotateY(-4.5)
        actor3.RotateY(+4.5)

        renderWindow.Render()


def robotleft():
    for i in range (10):
        time.sleep(0.1)
        actor1.RotateZ(-9)
        actor2.RotateZ(-9)
        actor3.RotateZ(-9)
        actor4.RotateZ(-9)
        actor5.RotateZ(-9)
        renderWindow.Render()


def robotright():
    for i in range (10):
        time.sleep(0.1)
        actor1.RotateZ(9)
        actor2.RotateZ(9)
        actor3.RotateZ(9)
        actor4.RotateZ(9)
        actor5.RotateZ(9)
        renderWindow.Render()


def robotback():
    for i in range (10):
        time.sleep(0.1)
        actor1.RotateZ(18)
        actor2.RotateZ(18)
        actor3.RotateZ(18)
        actor4.RotateZ(18)
        actor5.RotateZ(18)
        renderWindow.Render()

        
def robotraise():
    for i in range(10):
        time.sleep(0.1)
        actor4.RotateY(-3)
        actor2.RotateY(-3)
        renderWindow.Render()

        
def robotdown():
    for i in range(10):
        time.sleep(0.1)
        actor4.RotateY(+3)
        actor2.RotateY(+3)
        renderWindow.Render()

        
def robotembed():
    for i in range(10):
        time.sleep(0.1)
        actor4.RotateZ(-3)
        actor2.RotateZ(+3)
        renderWindow.Render()


def robotleave():
    for i in range(10):
        time.sleep(0.1)
        actor4.RotateZ(+3)
        actor2.RotateZ(-3)
        renderWindow.Render()


def robotposition():
    for i in range(10):
        time.sleep(0.1)
        actor4.RotateY(-3)
        actor2.RotateY(-3)
        renderWindow.Render()
    for i in range(33):
        time.sleep(0.1)
        actor5.SetPosition(0, 0, i*4)
        actor1.SetPosition(0, 0, i*4)
        actor2.SetPosition(0, 0, i*4)
        actor3.SetPosition(0, 0, i*4)
        actor4.SetPosition(0, 0, i*4)
        renderWindow.Render()


def fetch(x,y):
    if x >= 0 and y >= 0 :
        robotfont(int(y))
        robotleft()
        robotfont(int(x))
        robotembed()
        robotright()
    elif x >= 0 and y <= 0 :
        robotback()
        robotfont(int(-y))
        robotright()
        robotfont(int(x))
        robotembed()
        robotright()
    elif x <= 0 and y >= 0 :
        robotfont(int(y))
        robotright()
        robotfont(int(-x))
        robotembed()
        robotleft()
    elif x <= 0 and y <= 0 :
        robotback()
        robotfont(int(-y))
        robotleft()
        robotfont(int(-x))
        robotembed()
        robotleft()

        
def place(x,y):
    if x >= 0 and y >= 0 :
        robotfontwithob(int(y))
        robotleft()
        robotfontwithob(int(x))
        robotleave()
        robotright()
    elif x >= 0 and y <= 0 :
        robotback()
        robotfontwithob(int(-y))
        robotright()
        robotfontwithob(int(x))
        robotleave()
        robotright()
    elif x <= 0 and y >= 0 :
        robotfontwithob(int(y))
        robotright()
        robotfontwithob(int(-x))
        robotleave()
        robotleft()
    elif x <= 0 and y <= 0 :
        robotback()
        robotfontwithob(int(-y))
        robotleft()
        robotfontwithob(int(-x))
        robotleave()
        robotleft()

        
def showpic():
    print("YOLO1 took {:.6f} seconds".format(end - start))
    cv2.imshow('target detect result1', img)
    cv2.waitKey()
    cv2.destroyAllWindows()


#初始化VTK模型显示
#读取STL文件
reader1 = vtk.vtkSTLReader()
reader1.SetFileName("leftfoot.stl")
reader2 = vtk.vtkSTLReader()
reader2.SetFileName("lefthand.stl")
reader3 = vtk.vtkSTLReader()
reader3.SetFileName("rightfoot.stl")
reader4 = vtk.vtkSTLReader()
reader4.SetFileName("righthand.stl")
reader5 = vtk.vtkSTLReader()
reader5.SetFileName("body.stl")

mapper1 = vtk.vtkPolyDataMapper()
mapper1.SetInputConnection(reader1.GetOutputPort())
mapper2 = vtk.vtkPolyDataMapper()
mapper2.SetInputConnection(reader2.GetOutputPort())
mapper3 = vtk.vtkPolyDataMapper()
mapper3.SetInputConnection(reader3.GetOutputPort())
mapper4 = vtk.vtkPolyDataMapper()
mapper4.SetInputConnection(reader4.GetOutputPort())
mapper5 = vtk.vtkPolyDataMapper()
mapper5.SetInputConnection(reader5.GetOutputPort())

actor1 = vtk.vtkActor()
actor1.SetMapper(mapper1)
actor2 = vtk.vtkActor()
actor2.SetMapper(mapper2)
actor3 = vtk.vtkActor()
actor3.SetMapper(mapper3)
actor4 = vtk.vtkActor()
actor4.SetMapper(mapper4)
actor5 = vtk.vtkActor()
actor5.SetMapper(mapper5)

renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer);
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

renderer.AddActor(actor1)
renderer.AddActor(actor2)
renderer.AddActor(actor3)
renderer.AddActor(actor4)
renderer.AddActor(actor5)

#设定中心点
actor5.SetOrigin(actor5.GetCenter())
actor1.SetOrigin(actor5.GetCenter())
actor2.SetOrigin(actor5.GetCenter())
actor3.SetOrigin(actor5.GetCenter())
actor4.SetOrigin(actor5.GetCenter())
actor1.RotateZ(-90)
actor2.RotateZ(-90)
actor3.RotateZ(-90)
actor4.RotateZ(-90)
actor5.RotateZ(-90)
actor1.RotateY(-90)
actor2.RotateY(-90)
actor3.RotateY(-90)
actor4.RotateY(-90)
actor5.RotateY(-90)

renderer.SetBackground(0,0,0.8) # RGB 0~1


'''

'''

while True:
    renderWindow.Render()
    print('>>>>>>录音中...')
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    print('>>>>>>识别中...') 
    start_time = time.time()
    audio_data = audio.get_wav_data()
    ret = aip_speech.asr(audio_data, 'wav', 16000, {'dev_pid': 1537, })
    
    if ret and ret['err_no'] == 0:
        result = ret['result'][0]
        print(result)
        if "清理" in result:
            showpic()
            #coordinate = [[50,100],[100,100],[150,100]]#测试数据
            for i in ob:
                print('扫描得到物体:'+i)
            print("总物体个数:%s"%(str(len(ob))))
            for i in range(len(ob)):
                if obbox[0] > 600:
                    obbox[0] = 50
                    obbox[1] = obbox[1] + 50
                else:
                    obbox[0] = obbox[0] + 50
                
                x = (coordinate[i][0] - postion[0])/50
                y = (coordinate[i][1] - postion[1])/50
                if coordinate[i] == obbox:
                    print("物体"+ob[i]+"已在放置地点")
                    
                else:
                    print('正在前往'+ob[i])
                    fetch(x,y)
                    print('获取'+ob[i]+'成功'',正在前往放置地点')
                    position = coordinate[i]
                    x = (obbox[0] - position[0])/50
                    y = (obbox[1] - position[1])/50
                    place(x,y)
                    print('放置地点到达，放置成功')
                    position = obbox
                    coordinate[i] = obbox
            print('清理结束')
            speak = win.Dispatch("SAPI.SpVoice")
            speak.Speak("清理结束")
            
        if "天气" in result:
            a = input("请输入查询城市:")
            url = 'http://wthrcdn.etouch.cn/weather_mini?city='+a
            response = requests.get(url)
            wearher_json = json.loads(response.text)
            a = wearher_json['data']
            print(a['city']+"今天气温"+"："+a['wendu']+'℃'+"，"+"天气"+"："+a["forecast"][1]['type'])
            speak = win.Dispatch("SAPI.SpVoice")
            speak.Speak(a['city']+"今天气温"+a['wendu']+'℃'+"天气"+a["forecast"][1]['type'])
        end_time = time.time()
    else:
        print(" ")
    if cv2.waitKey(10)&0xFF==27:
        break












