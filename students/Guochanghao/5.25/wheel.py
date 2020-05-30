import vtk
import serial

class mytimercallback():
   def __init__(self):
       self.actors=[]
       self.timer_count=0
       self.ser=serial.Serial("COM1","9600",timeout=0.5)
       self.leftspeed=0
       self.rightspeed=0
       self.camera=0
       self.check=0
       
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
         print(speeds,speeds[0],speeds[1],speeds[2])
         self.leftspeed=speeds[0]
         self.rightspeed=speeds[1]
         self.camera=speeds[2]
         print("speed update",self.leftspeed,self.rightspeed)
      self.actors[0].RotateZ(self.leftspeed);
      self.actors[1].RotateZ(self.rightspeed);
      if self.camera!=self.check:

         self.actors[3].RotateZ(self.camera);
         self.camera=0
         self.check=0
      iren = obj
      iren.GetRenderWindow().Render()
      self.timer_count += 1
      
def main():
   #Read STL
   reader1 = vtk.vtkSTLReader()
   reader1.SetFileName("wheel1.stl")
   reader2 = vtk.vtkSTLReader()
   reader2.SetFileName("wheel2.stl")
   reader3 = vtk.vtkSTLReader()
   reader3.SetFileName("cframe.stl")
   reader4 = vtk.vtkSTLReader()
   reader1.SetFileName("camera.stl")

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
   actor2=vtk.vtkActor()
   actor2.SetMapper(mapper2)
   actor3 = vtk.vtkActor()
   actor3.SetMapper(mapper3)
   actor4 = vtk.vtkActor()
   actor4.SetMapper(mapper4)
   
   # Setup a renderer, render window, and interactor
   renderer = vtk.vtkRenderer()
   renderWindow = vtk.vtkRenderWindow()
   
   #renderWindow.SetWindowName("Test")
   renderWindow.AddRenderer(renderer);
   renderWindowInteractor = vtk.vtkRenderWindowInteractor()
   renderWindowInteractor.SetRenderWindow(renderWindow)

   #Add the actor to the scene
   renderer.AddActor(actor1)
   renderer.AddActor(actor2)
   renderer.AddActor(actor3)
   renderer.AddActor(actor4) 
   renderer.SetBackground(1,1,1)# Background color white
   actor1.SetOrigin(actor1.GetCenter())
   actor2.SetOrigin(actor2.GetCenter())
   actor4.SetOrigin(actor4.GetCenter())

   #Render and interact
   renderWindow.Render()

   # Initialize must be called prior to creating timer events.
   renderWindowInteractor.Initialize()

   # Sign up to receive TimerEvent
   cb = mytimercallback()
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
