import vtk
import serial
import os
from os import system
import win32com.client
from mcpi.minecraft import Minecraft
import time
import expressboxinfo


class mytimercallback():
   def __init__(self):
       self.actors=[]
       self.timer_count=0
       self.ser=serial.Serial("COM2","9600",timeout=0.5)
       self.change=0
       self.flag=0
       self.check=0
       self.number=""
   def execute(self,obj,event):
      #print(self.timer_count,event)
      if event !="TimerEvent":
         return
      resp=self.ser.readline().decode().strip()
      
      num=open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\roomnumber.txt",'r+')
      roomnum=num.read()
      #print(roomnum)
      s=expressboxinfo.express_info(roomnum)
      #print(s)
      if s[2]=='1':
         self.actors[2].SetPosition(0, 15, 0)
      f = open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\Password_verification.txt",'r+')
      a=f.read()
      #print(a)
      if a!="":
         self.change=1
         f = open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\Password_verification.txt",'r+')
         f.truncate()
         self.number=a
         print("房间号："+self.number)
         a=""
         print("你好！快递小哥！箱门即将打开，请放入快递！")
         speaker=win32com.client.Dispatch("SAPI.SpVoice")
         speaker.Speak("你好！快递小哥！箱门即将打开，请放入快递！")
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
      g= open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\openexpress1.txt",'r+')
      b=g.read()
      if b!="":
         g= open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\openexpress1.txt",'r+')
         g.truncate()
         b=""
         self.actors[1].SetOrigin(-50,50,50)
         self.actors[1].RotateZ(70)
         self.actors[1].SetOrigin(self.actors[0].GetCenter())
         self.change=1
         self.flag=1
         h=open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\closecap.txt",'r+')
         h.write("closecapflag")
      g= open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\openexpress2.txt",'r+')
      b=g.read()
      if b!="":
         g= open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\openexpress2.txt",'r+')
         g.truncate()
         b=""
         self.actors[1].SetOrigin(-50,50,50)
         self.actors[1].RotateZ(70)
         self.actors[1].SetOrigin(self.actors[0].GetCenter())
         self.change=1
         self.flag=1
         h=open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\closecap.txt",'r+')
         h.write("closecapflag")
      g= open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\openexpress3.txt",'r+')
      b=g.read()
      if b!="":
         g= open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\openexpress3.txt",'r+')
         g.truncate()
         b=""
         self.actors[1].SetOrigin(-50,50,50)
         self.actors[1].RotateZ(70)
         self.actors[1].SetOrigin(self.actors[0].GetCenter())
         self.change=1
         self.flag=1
         h=open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\closecap.txt",'r+')
         h.write("closecapflag")
      g= open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\openexpress4.txt",'r+')
      b=g.read()
      if b!="":
         g= open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\openexpress4.txt",'r+')
         g.truncate()
         b=""
         self.actors[1].SetOrigin(-50,50,50)
         self.actors[1].RotateZ(70)
         self.actors[1].SetOrigin(self.actors[0].GetCenter())
         self.change=1
         self.flag=1
         h=open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\closecap.txt",'r+')
         h.write("closecapflag")
      g= open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\openexpress5.txt",'r+')
      b=g.read()
      if b!="":
         g= open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\openexpress5.txt",'r+')
         g.truncate()
         b=""
         self.actors[1].SetOrigin(-50,50,50)
         self.actors[1].RotateZ(70)
         self.actors[1].SetOrigin(self.actors[0].GetCenter())
         self.change=1
         self.flag=1
         h=open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\closecap.txt",'r+')
         h.write("closecapflag")
      g= open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\openexpress6.txt",'r+')
      b=g.read()
      if b!="":
         g= open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\openexpress6.txt",'r+')
         g.truncate()
         b=""
         self.actors[1].SetOrigin(-50,50,50)
         self.actors[1].RotateZ(70)
         self.actors[1].SetOrigin(self.actors[0].GetCenter())
         self.change=1
         self.flag=1
         h=open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\closecap.txt",'r+')
         h.write("closecapflag")
         
      g= open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\openexpress7.txt",'r+')
      b=g.read()
      if b!="":
         g= open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\openexpress7.txt",'r+')
         g.truncate()
         b=""
         self.actors[1].SetOrigin(-50,50,50)
         self.actors[1].RotateZ(70)
         self.actors[1].SetOrigin(self.actors[0].GetCenter())
         self.change=1
         self.flag=1
         h=open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\closecap.txt",'r+')
         h.write("closecapflag")
      g= open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\openexpress8.txt",'r+')
      b=g.read()
      if b!="":
         g= open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\openexpress8.txt",'r+')
         g.truncate()
         b=""
         self.actors[1].SetOrigin(-50,50,50)
         self.actors[1].RotateZ(70)
         self.actors[1].SetOrigin(self.actors[0].GetCenter())
         self.change=1
         self.flag=1
         h=open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\closecap.txt",'r+')
         h.write("closecapflag")
      g= open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\openexpress9.txt",'r+')
      b=g.read()
      if b!="":
         g= open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\openexpress9.txt",'r+')
         g.truncate()
         b=""
         self.actors[1].SetOrigin(-50,50,50)
         self.actors[1].RotateZ(70)
         self.actors[1].SetOrigin(self.actors[0].GetCenter())
         self.change=1
         self.flag=1
         h=open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\closecap.txt",'r+')
         h.write("closecapflag")
      g= open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\openexpress10.txt",'r+')
      b=g.read()
      if b!="":
         g= open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\openexpress10.txt",'r+')
         g.truncate()
         b=""
         self.actors[1].SetOrigin(-50,50,50)
         self.actors[1].RotateZ(70)
         self.actors[1].SetOrigin(self.actors[0].GetCenter())
         self.change=1
         self.flag=1
         h=open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\closecap.txt",'r+')
         h.write("closecapflag")
      g= open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\openexpress11.txt",'r+')
      b=g.read()
      if b!="":
         g= open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\openexpress11.txt",'r+')
         g.truncate()
         b=""
         self.actors[1].SetOrigin(-50,50,50)
         self.actors[1].RotateZ(70)
         self.actors[1].SetOrigin(self.actors[0].GetCenter())
         self.change=1
         self.flag=1
         h=open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\closecap.txt",'r+')
         h.write("closecapflag")
      g= open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\openexpress12.txt",'r+')
      b=g.read()
      if b!="":
         g= open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\openexpress12.txt",'r+')
         g.truncate()
         b=""
         self.actors[1].SetOrigin(-50,50,50)
         self.actors[1].RotateZ(70)
         self.actors[1].SetOrigin(self.actors[0].GetCenter())
         self.change=1
         self.flag=1
         h=open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\closecap.txt",'r+')
         h.write("closecapflag")
      if resp !="":
         if resp =="open":
            self.change=1
         elif resp =="close":
            self.change=0
            h=open(r"C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\closecap.txt",'r+')
            h.truncate()
         if resp =="put in":
            self.actors[2].SetPosition(0, 15, 0)
            expressboxinfo.deposit(str(self.number))
         elif resp == "take out":
            self.actors[2].SetPosition(0, 15, -68.31)
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

def detectpos():
    mc=Minecraft.create("47.100.46.95",4784)
    entityId= mc.getPlayerEntityId("W")
    pos=mc.entity.getTilePos(entityId)
    if 1287<=pos.x<=1288 and pos.y==5 and 1185<=pos.z<=1187:
        for i in range(3):
            time.sleep(1)
        pos=mc.entity.getTilePos(entityId)
        if 1287<=pos.x<=1288 and pos.y==5 and 1185<=pos.z<=1187:
            return 1
        else:
            return 0
        
    pos=mc.entity.getTilePos(entityId)
    if 1282<=pos.x<=1283 and pos.y==5 and 1185<=pos.z<=1187:
        for i in range(3):
            time.sleep(1)
        pos=mc.entity.getTilePos(entityId)
        if 1282<=pos.x<=1283 and pos.y==5 and 1185<=pos.z<=1187:
            return 2
        else:
            return 0

    pos=mc.entity.getTilePos(entityId)
    if 1287<=pos.x<=1288 and pos.y==11 and 1185<=pos.z<=1187:
        for i in range(3):
            time.sleep(1)
        pos=mc.entity.getTilePos(entityId)
        if 1287<=pos.x<=1288 and pos.y==11 and 1185<=pos.z<=1187:
            return 3
        else:
            return 0

    pos=mc.entity.getTilePos(entityId)
    if 1282<=pos.x<=1283 and pos.y==11 and 1185<=pos.z<=1187:
        for i in range(3):
            time.sleep(1)
        pos=mc.entity.getTilePos(entityId)
        if 1282<=pos.x<=1283 and pos.y==11 and 1185<=pos.z<=1187:
            return 4
        else:
            return 0

    pos=mc.entity.getTilePos(entityId)
    if 1287<=pos.x<=1288 and pos.y==17 and 1185<=pos.z<=1187:
        for i in range(3):
            time.sleep(1)
        pos=mc.entity.getTilePos(entityId)
        if 1287<=pos.x<=1288 and pos.y==17 and 1185<=pos.z<=1187:
            return 5
        else:
            return 0

    pos=mc.entity.getTilePos(entityId)
    if 1282<=pos.x<=1283 and pos.y==17 and 1185<=pos.z<=1187:
        for i in range(3):
            time.sleep(1)
        pos=mc.entity.getTilePos(entityId)
        if 1282<=pos.x<=1283 and pos.y==17 and 1185<=pos.z<=1187:
            return 6
        else:
            return 0

    pos=mc.entity.getTilePos(entityId)
    if 1211<=pos.x<=1212 and pos.y==5 and 1185<=pos.z<=1187:
        for i in range(3):
            time.sleep(1)
        pos=mc.entity.getTilePos(entityId)
        if 1211<=pos.x<=1212 and pos.y==5 and 1185<=pos.z<=1187:
            return 7
        else:
            return 0
        
    pos=mc.entity.getTilePos(entityId)
    if 1206<=pos.x<=1207 and pos.y==5 and 1185<=pos.z<=1187:
        for i in range(3):
            time.sleep(1)
        pos=mc.entity.getTilePos(entityId)
        if 1206<=pos.x<=1207 and pos.y==5 and 1185<=pos.z<=1187:
            return 8
        else:
            return 0

    pos=mc.entity.getTilePos(entityId)
    if 1211<=pos.x<=1212 and pos.y==11 and 1185<=pos.z<=1187:
        for i in range(3):
            time.sleep(1)
        pos=mc.entity.getTilePos(entityId)
        if 1211<=pos.x<=1212 and pos.y==11 and 1185<=pos.z<=1187:
            return 9
        else:
            return 0
        
    pos=mc.entity.getTilePos(entityId)
    if 1206<=pos.x<=1207 and pos.y==11 and 1185<=pos.z<=1187:
        for i in range(3):
            time.sleep(1)
        pos=mc.entity.getTilePos(entityId)
        if 1206<=pos.x<=1207 and pos.y==11 and 1185<=pos.z<=1187:
            return 10
        else:
            return 0

    pos=mc.entity.getTilePos(entityId)
    if 1211<=pos.x<=1212 and pos.y==17 and 1185<=pos.z<=1187:
        for i in range(3):
            time.sleep(1)
        pos=mc.entity.getTilePos(entityId)
        if 1211<=pos.x<=1212 and pos.y==17 and 1185<=pos.z<=1187:
            return 11
        else:
            return 0
        
    pos=mc.entity.getTilePos(entityId)
    if 1206<=pos.x<=1207 and pos.y==17 and 1185<=pos.z<=1187:
        for i in range(3):
            time.sleep(1)
        pos=mc.entity.getTilePos(entityId)
        if 1206<=pos.x<=1207 and pos.y==17 and 1185<=pos.z<=1187:
            return 12
        else:
            return 0
def main():
   #Read STL
   reader1 = vtk.vtkSTLReader()
   reader1.SetFileName("box.stl")
   reader2 = vtk.vtkSTLReader()
   reader2.SetFileName("door.stl")
   reader3 = vtk.vtkSTLReader()
   reader3.SetFileName("express.stl")
   #Create a mapper and actor
   mapper1 = vtk.vtkPolyDataMapper()
   mapper1.SetInputConnection(reader1.GetOutputPort())
   mapper2 = vtk.vtkPolyDataMapper()
   mapper2.SetInputConnection(reader2.GetOutputPort())
   mapper3 = vtk.vtkPolyDataMapper()
   mapper3.SetInputConnection(reader3.GetOutputPort())
   actor1 = vtk.vtkActor()
   actor1.SetMapper(mapper1)
   actor2=vtk.vtkActor()
   actor2.SetMapper(mapper2)
   actor3=vtk.vtkActor()
   actor3.SetMapper(mapper3)
   renderer = vtk.vtkRenderer()
   renderWindow = vtk.vtkRenderWindow()
   renderWindow.AddRenderer(renderer);
   renderWindowInteractor = vtk.vtkRenderWindowInteractor()
   renderWindowInteractor.SetRenderWindow(renderWindow)
   #Add the actor to the scene
   renderer.AddActor(actor1)
   renderer.AddActor(actor2)
   renderer.AddActor(actor3)
   renderer.SetBackground(1,1,1) # Background color white
   actor1.SetOrigin(actor1.GetCenter())
   actor2.SetOrigin(actor1.GetCenter())
   actor3.SetOrigin(actor1.GetCenter())
   actor1.RotateZ(-90)
   actor1.RotateY(-90)
   actor2.RotateZ(-90)
   actor2.RotateY(-90)
   actor3.RotateZ(-90)
   actor3.RotateY(-90)
   actor3.SetPosition(0, 15, -68.31)
   #Render and interact
   renderWindow.Render()
   # Initialize must be called prior to creating timer events.
   renderWindowInteractor.Initialize()
   # Sign up to receive TimerEvent
   cb = mytimercallback()
   cb.actors.append(actor1)
   cb.actors.append(actor2)
   cb.actors.append(actor3)
   renderWindowInteractor.AddObserver('TimerEvent', cb.execute)
   timerId = renderWindowInteractor.CreateRepeatingTimer(100);
   #start the interaction and timer
   renderWindowInteractor.Start()
