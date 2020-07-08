import vtk
import time
import pyaudio
import wave
from aip import AipSpeech
from xpinyin import Pinyin
import requests
#from weather import *
#from nature import *
#from music import *
import os
from os import system
import win32com.client
import threading

speaker = win32com.client.Dispatch("SAPI.SpVoice")
 

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 8000
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "audio1.wav"


APP_ID = '18980660'
API_KEY = 'hwoVnCcUV1VoizMZzHU7ayu6'
SECRET_KEY = 'Z1ynGkPNF1GBoYnnMPBdxt4lY8mm48QS'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

s=100
be=100
STATE = 0
TIME_START = 0
TIME_END = 0
ptt=1
m=20
num_basketball = 10

class vtkTimerCallback1():
   
   def __init__(self):
       self.timer_count = 0
       self.actors=[]
       self.f = 1
   def execute(self,obj,event):
       if self.f == 1:
           self.actors[0].RotateX(-50)
           self.actors[1].RotateX(-50)
           self.f = -self.f
           time.sleep(1)
       elif self.f == -1:
           self.actors[0].RotateX(50)
           self.actors[1].RotateX(50)
           self.f = -self.f
           time.sleep(1)

       iren = obj
       iren.GetRenderWindow().Render()
       #iren.GetRenderWindow().Finalize()
       self.timer_count += 1
       print('a')
def fun_timer():
    global s,be,ptt,m
    print('hello timer')   #打印输出
    global timer  #定义变量
    timer = threading.Timer(40,fun_timer)   #60秒调用一次函数
    if ptt == 1:

       putong()
    else :

       kuangpen()
##    s=s-3
##    be=be-1
    m=m-0.5
    if s == 5 :
       speaker.Speak("系统自动检测到消毒液余量为百分之五，系统即将自动关闭")
       os._exit(0)
    if m == 0 :
       speaker.Speak("消毒完成，系统即将自动关闭")
       os._exit(0)    
    #定时器构造函数主要有2个参数，第一个参数为时间，第二个参数为函数名
    timer.start()    #启用定时器
    result = getBaiduText()
    pinyin = getPinYin(result)
    print(result)
    wakeUp(result,pinyin)

def  putong():
    global s,be
    s=s-3
    be=be-1

def  kuangpen():
    global s,be
    s=s-5
    be=be-2
    
    
def playVoice(fileName):
    os.system("madplay -v " + fileName)
 

def readFile(fileName):
    with open(fileName, 'rb') as fp:
        return fp.read()
    
def writeFile(fileName,result):
    with open(fileName, 'wb') as fp:
        fp.write(result)
        
def getBaiduText():
    global r
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    stream.start_stream()
    r=1
    r=r+1
    if r==1:
       speaker.Speak("正在消毒，目前消毒液充足 ，请随时说出暂停将暂停消毒,您也可以随时说出指令普通模式或狂喷模式改变消毒强度")
    else:
       speaker.Speak("正在消毒，目前消毒液充足 ，请随时说出暂停将暂停消毒")
    print("请随时说出暂停将暂停消毒")
    print("说出消毒液余量，将为您检查消毒液余量")
    print("说出电量余量，将为您检查电量液余量")
    print("说出机器人状态，将为您检查机器人状态参数")
    print("您也可以随时说出指令普通模式或狂喷模式改变消毒强度")
    
    
    
    print("* 开始录音......")
    
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
 
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    
    print("正在识别......")
    result = client.asr(readFile('audio1.wav'), 'wav', 16000, {
    'dev_pid': 1537,
})
    if result["err_no"] == 0:
        for t in result["result"]:
            return t
    else:
        print("没有识别到语音\n")
        return ""
      
def getBaiduVoice(text):
    result  = client.synthesis(text, 'zh', 6, {'vol': 5, 'per':4,'spd':5})
    if not isinstance(result, dict):
        writeFile("back.mp3",result)
    os.system("back.mp3")
    #playVoice("back.mp3")


def getVoiceResult():
    return baiduVoice()

def getPinYin(result):
    pin = Pinyin()
    return pin.get_pinyin(result)

def wakeUp(result,pinyin):
    global ptt,m
    if getPinYin("暂停") in pinyin or getPinYin("再见") in pinyin or getPinYin("不需要") in pinyin :
        
        print("谢谢你的使用，感谢下次光临！")
        speaker.Speak("谢谢你的使用，感谢下次光临！")
        os._exit(0)
    elif  getPinYin("消毒液") in pinyin :
      
        speaker.Speak("消毒液余量为百分之"+str(s))
    elif  getPinYin("普通") in pinyin :
        ptt=1
        speaker.Speak("正在切换普通模式，请稍后，切换成功，目前模式维普通模式")
    elif  getPinYin("狂喷") in pinyin :
        ptt=2
        speaker.Speak("正在切换狂喷模式，请稍后，切换成功，目前模式维狂喷模式，请注意此模式下消毒液使用量及耗电量将增加")
    elif  getPinYin("电量") in pinyin : 
        speaker.Speak("电量余量为百分之"+str(be))
    elif  getPinYin("状态") in pinyin :
       

        if ptt == 1:
           speaker.Speak("机器人自检中请稍后，机器状态良好，目前模式维普通模式")
        else :
           speaker.Speak("机器人自检中请稍后，机器状态良好，目前模式维狂喷模式")
        speaker.Speak("消毒液余量为百分之"+str(s))
        speaker.Speak("电量余量为百分之"+str(be))
        speaker.Speak("预计消毒结束还有"+str(m)+"分钟")
        speaker.Speak("感谢查询，我将继续为您消毒哦主人")
    else:
        print("无法识别，请重新操作")
        speaker.Speak("无法识别，请重新说出指令")
        



def main():

      #Read STL
      reader1 = vtk.vtkSTLReader()
      reader1.SetFileName("arml.stl")
      reader2 = vtk.vtkSTLReader()
      reader2.SetFileName("armr.stl")
      reader5 = vtk.vtkSTLReader()
      reader5.SetFileName("body.stl")


     #Create a mapper and actor
      mapper1 = vtk.vtkPolyDataMapper()
      mapper1.SetInputConnection(reader1.GetOutputPort())
      mapper2 = vtk.vtkPolyDataMapper()
      mapper2.SetInputConnection(reader2.GetOutputPort())
      mapper5 = vtk.vtkPolyDataMapper()
      mapper5.SetInputConnection(reader5.GetOutputPort())

      actor1 = vtk.vtkActor()
      actor1.SetMapper(mapper1)
      actor2 = vtk.vtkActor()
      actor2.SetMapper(mapper2)
      actor5 = vtk.vtkActor()
      actor5.SetMapper(mapper5)


      # Setup a renderer, render window, and interactor
      renderer = vtk.vtkRenderer()
      renderWindow = vtk.vtkRenderWindow()
      renderWindow.AddRenderer(renderer);
      renderWindowInteractor = vtk.vtkRenderWindowInteractor()
      renderWindowInteractor.SetRenderWindow(renderWindow)

      #renderWindow.SetWindowName("Test")
      renderWindow.AddRenderer(renderer);
      renderWindowInteractor = vtk.vtkRenderWindowInteractor()
      renderWindowInteractor.SetRenderWindow(renderWindow)

      #Add the actor to the scene
      renderer.AddActor(actor1)
      renderer.AddActor(actor2)
      renderer.AddActor(actor5)
      renderer.SetBackground(0,0,0.8) # RGB 0~1
      actor1.SetOrigin(-75.98744583129883, 55.179789543151855+10, 28.96554946899414)
      actor2.SetOrigin(-16.002686738967896, 54.13501167297363+10, 28.966289520263672)
      actor5.SetOrigin(actor5.GetCenter())

      #Render and interact
      renderWindow.Render()

      # Initialize must be called prior to creating timer events.
      renderWindowInteractor.Initialize()

      # Sign up to receive TimerEvent
      cb = vtkTimerCallback1()
      cb.actors.append(actor1)
      cb.actors.append(actor2)
      cb.actors.append(actor5)
      renderWindowInteractor.AddObserver('TimerEvent', cb.execute)
      timerId = renderWindowInteractor.CreateRepeatingTimer(100);

      timer = threading.Timer(1,fun_timer)  #首次启动
      timer.start()      
      
      #start the interaction and timer
      #renderWindowInteractor.Start()
      renderWindowInteractor.GetRenderWindow().Finalize()
      



        

if __name__ == '__main__':
   main()
   p=input('a:')
