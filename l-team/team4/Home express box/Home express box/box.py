import vtk
import serial
import os
from os import system
import win32com.client


class mytimercallback():
   def __init__(self):
       self.actors=[]
       self.timer_count=0
       self.ser=serial.Serial("COM3","9600",timeout=0.5)
       self.change=0
       self.flag=0
       self.check=0
   def execute(self,obj,event):
      #print(self.timer_count,event)
      if event !="TimerEvent":
         return
      resp=self.ser.readline().decode().strip()
      f = open(r"C:\Users\38098\AppData\Roaming\.homeassistant\custom_components\package_send.txt",'r+')
      g = open(r"C:\Users\38098\AppData\Roaming\.homeassistant\custom_components\package_accept.txt",'r+')
      a=f.read()
      b=g.read()
      #print(a)
      #print(b)
      h = open(r"C:\Users\38098\AppData\Roaming\.homeassistant\custom_components\check.txt",'r+')
      c=h.read()

      j = open(r"C:\Users\38098\AppData\Roaming\.homeassistant\custom_components\open.txt",'r+')
      if j.read()=="1":
         j = open(r"C:\Users\38098\AppData\Roaming\.homeassistant\custom_components\open.txt",'r+')
         j.truncate()
         self.change=0
         self.flag=1
         self.check=0
         self.actors[1].SetOrigin(-50,50,50)
         self.actors[1].RotateZ(70)
         self.actors[1].SetOrigin(self.actors[0].GetCenter())
      if c=="1" and a!="" and self.change==0:
         if a in b:
            f = open(r"C:\Users\38098\AppData\Roaming\.homeassistant\custom_components\package_send.txt",'r+')
            f.truncate()
            print("对不起！快递小哥！快递箱内还有未取出的快递，请择日配送！")
            speaker=win32com.client.Dispatch("SAPI.SpVoice")
            speaker.Speak("对不起！快递小哥！快递箱内还有未取出的快递，请择日配送！")
         else:
            print("二维码匹配失败！")
            speaker=win32com.client.Dispatch("SAPI.SpVoice")
            speaker.Speak("二维码匹配失败！")
            f = open(r"C:\Users\38098\AppData\Roaming\.homeassistant\custom_components\package_send.txt",'r+')
            f.truncate()
      if a!="" and c=="":
         if a in b:
            self.change=1
         else:
            print("二维码匹配失败！")
            speaker=win32com.client.Dispatch("SAPI.SpVoice")
            speaker.Speak("二维码匹配失败！")
            f = open(r"C:\Users\38098\AppData\Roaming\.homeassistant\custom_components\package_send.txt",'r+')
            f.truncate()
         if self.change==1 and self.flag==0 and self.check==0:
            self.actors[1].SetOrigin(-50,50,50)
            self.actors[1].RotateZ(70)
            self.actors[1].SetOrigin(self.actors[0].GetCenter())
            self.flag=1
            self.check=1
            
            print("你好！快递小哥！箱门即将打开，请放入快递！")
            speaker=win32com.client.Dispatch("SAPI.SpVoice")
            speaker.Speak("你好！快递小哥！箱门即将打开，请放入快递！")
            h = open(r"C:\Users\38098\AppData\Roaming\.homeassistant\custom_components\check.txt",'r+')
            h.write("1")
      if resp !="":
         if resp =="open":
            self.change=1
         else:
            self.change=0
            f = open(r"C:\Users\38098\AppData\Roaming\.homeassistant\custom_components\package_send.txt",'r+')
            f.truncate()
         if self.change==1 and self.flag==0:
            self.actors[1].SetOrigin(-50,50,50)
            self.actors[1].RotateZ(70)
            self.actors[1].SetOrigin(self.actors[0].GetCenter())
            self.flag=1
         if self.change==0 and self.flag==1:
            self.actors[1].SetOrigin(-50,50,50)
            self.actors[1].RotateZ(-70)
            self.actors[1].SetOrigin(self.actors[0].GetCenter())
            self.flag=0
      
      iren = obj
      iren.GetRenderWindow().Render()
      self.timer_count += 1

def main():
   #Read STL
   reader1 = vtk.vtkSTLReader()
   reader1.SetFileName("box.stl")
   reader2 = vtk.vtkSTLReader()
   reader2.SetFileName("door.stl")
   #Create a mapper and actor
   mapper1 = vtk.vtkPolyDataMapper()
   mapper1.SetInputConnection(reader1.GetOutputPort())
   mapper2 = vtk.vtkPolyDataMapper()
   mapper2.SetInputConnection(reader2.GetOutputPort())
   actor1 = vtk.vtkActor()
   actor1.SetMapper(mapper1)
   actor2=vtk.vtkActor()
   actor2.SetMapper(mapper2)
   renderer = vtk.vtkRenderer()
   renderWindow = vtk.vtkRenderWindow()
   renderWindow.AddRenderer(renderer);
   renderWindowInteractor = vtk.vtkRenderWindowInteractor()
   renderWindowInteractor.SetRenderWindow(renderWindow)
   #Add the actor to the scene
   renderer.AddActor(actor1)
   renderer.AddActor(actor2)
   renderer.SetBackground(1,1,1) # Background color white
   actor1.SetOrigin(actor1.GetCenter())
   actor2.SetOrigin(actor1.GetCenter())
   actor1.RotateZ(-90)
   actor1.RotateY(-90)
   actor2.RotateZ(-90)
   actor2.RotateY(-90)
   #Render and interact
   renderWindow.Render()
   # Initialize must be called prior to creating timer events.
   renderWindowInteractor.Initialize()
   # Sign up to receive TimerEvent
   cb = mytimercallback()
   cb.actors.append(actor1)
   cb.actors.append(actor2)
   renderWindowInteractor.AddObserver('TimerEvent', cb.execute)
   timerId = renderWindowInteractor.CreateRepeatingTimer(100);
   #start the interaction and timer
   renderWindowInteractor.Start()


if __name__ == '__main__':
   main()
