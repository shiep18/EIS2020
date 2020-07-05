import vtk
import serial
import time
import vtk
import serial
#from lianxi0529 import case1,case2
class mytimercallback():
   def __init__(self):
       self.actors=[]
       self.timer_count=0
       self.ser=serial.Serial("COM12","9600",timeout=0.5)
       self.leftspeed=0
       self.rightspeed=0
       self.flag1=1
   def execute(self,obj,event):
      print(self.timer_count,event)
      if event !="TimerEvent":
         return
      resp=self.ser.readline().decode().strip()
      if resp !="":
         spds=resp.split(",")
         print(resp)
         print(spds)
         speeds=list(map(int,spds))
         self.flag=speeds[0]
         #1  LOCKED  2  CLOSED  3  OPEN
         if self.flag==1 and self.flag1!=1:
            if self.flag1==2:
               print("CLOSED->LOCKED")
               self.actors[3].RotateZ(-90)
            elif self.flag1==3:
               print("OPEN->LOCKED")
               self.actors[1].RotateY(90)
               self.actors[2].RotateY(-90)
               self.actors[3].RotateZ(-90)
            self.flag1=self.flag
         elif self.flag==2 and self.flag1!=2:
            if self.flag1==1:
               print("LOCKED->CLOSED")
               self.actors[3].RotateZ(90)
            elif self.flag1==3:
               print("OPEN->CLOSED")
               self.actors[1].RotateY(90)
               self.actors[2].RotateY(-90)
            self.flag1=self.flag
         elif self.flag==3 and self.flag1!=3:
            if self.flag1==1:
               print("LOCKED->OPEN")
               self.actors[1].RotateY(-90)
               self.actors[2].RotateY(90)
               self.actors[3].RotateZ(90)
            elif self.flag1==2:
               print("CLOSED->OPEN")
               self.actors[1].RotateY(-90)
               self.actors[2].RotateY(90)
            self.flag1=self.flag
      iren = obj
      iren.GetRenderWindow().Render()
      self.timer_count += 1

def main():

   reader1 = vtk.vtkSTLReader()
   reader1.SetFileName("door1.stl")
   reader2 = vtk.vtkSTLReader()
   reader2.SetFileName("doorleft.stl")
   reader3 = vtk.vtkSTLReader()
   reader3.SetFileName("doorright.stl")
   reader4 = vtk.vtkSTLReader()
   reader4.SetFileName("lock.stl")
   #Create a mapper and actor
   mapper1 = vtk.vtkPolyDataMapper()
   mapper1.SetInputConnection(reader1.GetOutputPort())
   mapper2 = vtk.vtkPolyDataMapper()
   mapper2.SetInputConnection(reader2.GetOutputPort())
   mapper3 = vtk.vtkPolyDataMapper()
   mapper3.SetInputConnection(reader3.GetOutputPort())
   mapper4 = vtk.vtkPolyDataMapper()
   mapper4.SetInputConnection(reader4.GetOutputPort())
   actor1 = vtk.vtkActor()
   actor1.SetMapper(mapper1)
   actor2 = vtk.vtkActor()
   actor2.SetMapper(mapper2)
   actor3 = vtk.vtkActor()
   actor3.SetMapper(mapper3)
   actor4 = vtk.vtkActor()
   actor4.SetMapper(mapper4)
   #prop = actor.GetProperty()
   # Setup a renderer, render window, and interactor
   renderer = vtk.vtkRenderer()
   renderWindow = vtk.vtkRenderWindow()
   renderWindow.AddRenderer(renderer);
   renderWindowInteractor = vtk.vtkRenderWindowInteractor()
   renderWindowInteractor.SetRenderWindow(renderWindow)
   renderer.AddActor(actor1)
   renderer.AddActor(actor2)
   renderer.AddActor(actor3)
   renderer.AddActor(actor4)
   renderer.SetBackground(0,0,1) # RGB 0~1
   actor1.SetOrigin(actor1.GetCenter())
   actor2.SetOrigin(-142.5,35,55)
   actor3.SetOrigin(-57.5,35,55)
   actor4.SetOrigin(-142.5,35,55)
   cb = mytimercallback()
   #Render and interact
   renderWindow.Render()
   # Initialize must be called prior to creating timer events.
   renderWindowInteractor.Initialize()
   # Sign up to receive TimerEvent
   cb.actors.append(actor1)
   cb.actors.append(actor2)
   cb.actors.append(actor3)
   cb.actors.append(actor4)
   renderWindowInteractor.AddObserver('TimerEvent', cb.execute)
   timerId = renderWindowInteractor.CreateRepeatingTimer(100);
   #start the interaction and timer
   renderWindowInteractor.Start()
if __name__ == '__main__':
   main()
