import vtk
import serial

class mytimercallback():
   def __init__(self):
       self.actors=[]
       self.timer_count=0
       self.ser=serial.Serial("COM13","9600",timeout=0.5)
       self.leftspeed=0
       self.rightspeed=0
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
         print("speed update",self.leftspeed,self.rightspeed)
      self.actors[0].RotateZ(self.leftspeed);
      self.actors[1].RotateZ(self.rightspeed);
      iren = obj
      iren.GetRenderWindow().Render()
      self.timer_count += 1

def main():
   #Create a sphere
   sphereSource = vtk.vtkSphereSource()
   sphereSource.SetCenter(0.0, 0.0, 0.0)
   sphereSource.SetRadius(1)

   sphereSource1 = vtk.vtkSphereSource()
   sphereSource1.SetCenter(0.0, 3.0, 0.0)
   sphereSource1.SetRadius(1.5)

   #Create a mapper and actor
   mapper = vtk.vtkPolyDataMapper()
   mapper.SetInputConnection(sphereSource.GetOutputPort())

   mapper1 = vtk.vtkPolyDataMapper()
   mapper1.SetInputConnection(sphereSource1.GetOutputPort())

   actor = vtk.vtkActor()
   actor.SetMapper(mapper)
   prop = actor.GetProperty()

   actor1=vtk.vtkActor()
   actor1.SetMapper(mapper1)
   actor1.SetOrigin(0,3,0)

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
   renderer.SetBackground(1,1,1) # Background color white

   #Render and interact
   renderWindow.Render()

   # Initialize must be called prior to creating timer events.
   renderWindowInteractor.Initialize()

   # Sign up to receive TimerEvent
   cb = mytimercallback()
   cb.actors.append(actor)
   cb.actors.append(actor1)
   renderWindowInteractor.AddObserver('TimerEvent', cb.execute)
   timerId = renderWindowInteractor.CreateRepeatingTimer(100);

   #start the interaction and timer
   renderWindowInteractor.Start()


if __name__ == '__main__':
   main()
