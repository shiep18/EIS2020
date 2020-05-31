import vtk
import serial

class mytimercallback():
   def __init__(self):
       self.actors=[]
       self.actors_qian=[]
       self.ass=[]
       self.timer_count=0
       self.ser=serial.Serial("COM13","9600",timeout=0.5)
       self.leftspeed=0
       
   def open(self):
      self.leftspeed=0
      f=open('C:\Apache24\htdocs\index0.html','w')
      f.write("开门")
      for i in range(360):
         self.actors[0].RotateY(-0.22)
         self.actors[1].RotateY(-0.22)
         self.actors[1].RotateZ(-0.083)
      self.actors[1].AddPosition(0,20,0)
   
   def close(self): 
      self.leftspeed=0
      f=open('C:\Apache24\htdocs\index0.html','w')
      f.write("关门")
      self.actors[1].AddPosition(0,-20,0)
      for i in range(360):
         self.actors[1].RotateZ(0.083)
         self.actors[1].RotateY(0.22)
         self.actors[0].RotateY(0.22)

         
   def execute(self,obj,event):
      print(self.timer_count,event)
      if event !="TimerEvent":
         return
      resp=self.ser.readline().decode().strip()
      if resp !="":
         spds=resp.split(",")
         print(resp)
         print(spds)
         speeds=list(map(str,spds))
         print(speeds,speeds[0])
         self.leftspeed=speeds[0]
         print("a:开门 b:关门 您的选项是：",self.leftspeed,self)
      if(self.leftspeed == 'a'):
         mytimercallback.open(self)
      if(self.leftspeed == 'b'):
         mytimercallback.close(self)
         
      iren = obj
      iren.GetRenderWindow().Render()
      self.timer_count += 1

##def face():
##    for i in range(360):
##        actor.RotateZ(-0.25)
##        renderWindow.Render()
##def noface():
##    for i in range(360):
##        actor.RotateZ(0.25) #背面
##        renderWindow.Render()
##    for i in range(360):
##        actor.RotateY(0.5)
##        renderWindow.Render()

def main():
   #Read STL
   reader1 = vtk.vtkSTLReader()
   reader1.SetFileName("frame.stl")
   reader2 = vtk.vtkSTLReader()
   reader2.SetFileName("door.stl")
   reader3 = vtk.vtkSTLReader()
   reader3.SetFileName("bashou.stl")

   #Create a mapper and actor
   mapper1 = vtk.vtkPolyDataMapper()
   mapper1.SetInputConnection(reader1.GetOutputPort())
   mapper2 = vtk.vtkPolyDataMapper()
   mapper2.SetInputConnection(reader2.GetOutputPort())
   mapper3 = vtk.vtkPolyDataMapper()
   mapper3.SetInputConnection(reader3.GetOutputPort())
   
   actor1 = vtk.vtkActor()
   actor1.SetMapper(mapper1)
   actor2 = vtk.vtkActor()
   actor2.SetMapper(mapper2)
   actor3 = vtk.vtkActor()
   actor3.SetMapper(mapper3)

   
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
   renderer.AddActor(actor3)
   renderer.SetBackground(0,0,0.8) # RGB 0~1

   actor1.SetOrigin(actor1.GetCenter())
   actor2.SetOrigin(-80, 66,6)
   actor3.SetOrigin(-80, 66,6)

   #Render and interact
   renderWindow.Render()

   # Initialize must be called prior to creating timer events.
   renderWindowInteractor.Initialize()

   # Sign up to receive TimerEvent
   cb = mytimercallback()
   cb.actors.append(actor2)
   cb.actors.append(actor3)
   renderWindowInteractor.AddObserver('TimerEvent', cb.execute)
   timerId = renderWindowInteractor.CreateRepeatingTimer(100);

   #start the interaction and timer
   renderWindowInteractor.Start()


if __name__ == '__main__':
   main()
