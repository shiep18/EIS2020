import time
import serial
import vtk

class mytimercallback():
   def __init__(self):
       self.actors=[]
       self.timer_count=0
       self.ser=serial.Serial("COM13","9600",timeout=0.5)
       self.leftspeed=0
       self.rightspeed=0
       self.flag1=0

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
         if self.flag==1 and self.flag1!=1:
            self.flag1=self.flag
            print("1")
            self.actors[0].RotateY(90)
            f = open("C:\\Apache24\\htdocs\\index2.html",'w')
            f.write("open")
            f.close()
         elif self.flag==2 and self.flag1!=2:
            self.flag1=self.flag
            print("2")
            self.actors[0].RotateY(-90)
            f = open("C:\\Apache24\\htdocs\\index2.html",'w')
            f.write("close")
            f.close()
      iren = obj
      iren.GetRenderWindow().Render()

def main():
   reader = vtk.vtkSTLReader()
   reader.SetFileName("door.stl")
   reader1 = vtk.vtkSTLReader()
   reader1.SetFileName("doorcase.stl")

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
   renderer.SetBackground(0,0,1) # Background color white

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
