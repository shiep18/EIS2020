import time

import serial
import vtk

robot_state_path = "C://Apache24//htdocs//door.html"

class mytimercallback():
   def __init__(self):
       self.actors = []
       self.timer_count = 0
       self.ser=serial.Serial("COM13","9600",timeout=0.5)
       self.leftspeed = 0
       self.rightspeed = 0

   def front(self,obj):
      for i in range(9):
         time.sleep(0.1)
         self.actors[0].RotateY(10)
         obj.GetRenderWindow().Render()

   def back(self,obj):
      for i in range(9):
         time.sleep(0.1)
         self.actors[0].RotateY(-10)
         obj.GetRenderWindow().Render()

   def execute(self,obj,event):
      print(self.timer_count,event)
      if event !="TimerEvent":
         return
      resp=self.ser.readline().decode().strip()
      if resp !="":
         if resp == "open":
            print(resp)
            self.front(obj)
            with open(robot_state_path, "w") as f:
               f.write("open")
         elif resp == "close":
            print(resp)
            self.back(obj)
            with open(robot_state_path, "w") as f:
               f.write("close")
      iren = obj
      iren.GetRenderWindow().Render()

def main():
   reader = vtk.vtkSTLReader()
   reader.SetFileName("door.stl")
   reader1 = vtk.vtkSTLReader()
   reader1.SetFileName("frame.stl")

   #Create a mapper and actor
   mapper = vtk.vtkPolyDataMapper()
   mapper.SetInputConnection(reader.GetOutputPort())
   mapper1 = vtk.vtkPolyDataMapper()
   mapper1.SetInputConnection(reader1.GetOutputPort())


   actor = vtk.vtkActor()
   actor.SetMapper(mapper)
   prop = actor.GetProperty()
   # actor.SetOrigin(actor.GetCenter())
   actor.SetOrigin(actor.GetBounds()[1],actor.GetCenter()[1],actor.GetCenter()[2])
   actor1 = vtk.vtkActor()
   actor1.SetMapper(mapper1)
   prop1 = actor1.GetProperty()
   actor1.SetOrigin(actor1.GetCenter())

   # Setup a renderer, render window, and interactor
   renderer = vtk.vtkRenderer()
   renderWindow = vtk.vtkRenderWindow()
   #renderWindow.SetWindowName("Test")

   renderWindow.AddRenderer(renderer);
   renderWindowInteractor = vtk.vtkRenderWindowInteractor()
   renderWindowInteractor.SetRenderWindow(renderWindow)

   #Add the actor to the scene
   renderer.AddActor(actor)
   renderer.AddActor(actor1)
   renderer.SetBackground(0,1,1) # Background color white

   #Render and interact
   renderWindow.Render()

   # Initialize must be called prior to creating timer events.
   renderWindowInteractor.Initialize()

   # Sign up to receive TimerEvent
   cb = mytimercallback()
   cb.actors.append(actor)
   cb.actors.append(actor1)

   print(actor.GetBounds())
   renderWindowInteractor.AddObserver('TimerEvent', cb.execute)
   timerId = renderWindowInteractor.CreateRepeatingTimer(100);

   #start the interaction and timer
   renderWindowInteractor.Start()

if __name__ == '__main__':
   main()
