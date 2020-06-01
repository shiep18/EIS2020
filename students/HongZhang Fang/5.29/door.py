import time

import serial
import vtk
data=['open','close']

class mytimercallback():
   def __init__(self):
       self.actors=[]
       self.timer_count=0
       self.ser=serial.Serial("COM11","9600",timeout=0.5)
       #self.leftspeed=0
       #self.rightspeed=0

   def front(self,obj):
      f=open(r"D:\BaiduNetdiskDownload\5.29\vtk\state.txt","r")
      a=f.read()
      if a!="open":
         for i in range(18):
            time.sleep(0.1)
            #self.actors[0].RotateX(270)
            self.actors[0].RotateZ(10)
            obj.GetRenderWindow().Render()

   def back(self,obj):
      
      #for i in range(27):
        # time.sleep(0.1)
         #self.actors[0].RotateX(270)
        # self.actors[0].RotateX(10)
        # obj.GetRenderWindow().Render()
      f=open(r"D:\BaiduNetdiskDownload\5.29\vtk\state.txt","r")
      a=f.read()
      if a!="close":
         for j in range(18):
            time.sleep(0.1)
            #self.actors[0].RotateX(270)
            #self.actors[0].RotateZ(180)
            self.actors[0].RotateZ(10)
            obj.GetRenderWindow().Render()

   def execute(self,obj,event):
      print(self.timer_count,event)
      if event !="TimerEvent":
         return
      resp=self.ser.readline().decode().strip()
      if resp !="":
         if resp == "opendoor":
            print(resp)
            self.front(obj)
            f=open(r"D:\BaiduNetdiskDownload\5.29\vtk\state.txt","w")
            f.write(data[0])
            f.close()
         elif resp == "closedoor":
            print(resp)
            self.back(obj)
            f=open(r"D:\BaiduNetdiskDownload\5.29\vtk\state.txt","w")
            f.write(data[1])
            f.close()
      iren = obj
      iren.GetRenderWindow().Render()

def main():
   reader = vtk.vtkSTLReader()
   reader.SetFileName("door.stl")
   #Create a mapper and actor
   mapper = vtk.vtkPolyDataMapper()
   mapper.SetInputConnection(reader.GetOutputPort())


   actor = vtk.vtkActor()
   actor.SetMapper(mapper)

   
   prop = actor.GetProperty()
   actor.SetOrigin(actor.GetCenter())


   # Setup a renderer, render window, and interactor
   renderer = vtk.vtkRenderer()
   renderWindow = vtk.vtkRenderWindow()
   #renderWindow.SetWindowName("Test")

   renderWindow.AddRenderer(renderer);
   renderWindowInteractor = vtk.vtkRenderWindowInteractor()
   renderWindowInteractor.SetRenderWindow(renderWindow)

   #Add the actor to the scene
   renderer.AddActor(actor)
   renderer.SetBackground(0,0,1) # Background color white

   #Render and interact
   renderWindow.Render()
   

   # Initialize must be called prior to creating timer events.
   renderWindowInteractor.Initialize()
    
   # Sign up to receive TimerEvent
   actor.RotateY(270)
   actor.RotateX(90)
   cb = mytimercallback()
   
   cb.actors.append(actor)



   print(actor.GetBounds())
   renderWindowInteractor.AddObserver('TimerEvent', cb.execute)
   timerId = renderWindowInteractor.CreateRepeatingTimer(100);

   #start the interaction and timer
   renderWindowInteractor.Start()

if __name__ == '__main__':
   main()
