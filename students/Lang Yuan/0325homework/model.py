import vtk
import time

class vtkTimerCallback1():
   def __init__(self):
       self.timer_count = 0
       self.actors=[]
   def execute(self,obj,event):
       print(self.timer_count)
       cnt=0
       for act in self.actors:
          if cnt%2==0:
             act.SetPosition(self.timer_count, 0,0);
          else:
             act.SetPosition(0, self.timer_count,0);
          cnt+=1
       iren = obj
       iren.GetRenderWindow().Render()
       self.timer_count += 1


def main():
   
   #Create a sphere
##   sphereSource = vtk.vtkSphereSource()
##   sphereSource.SetCenter(0.0, 0.0, 0.0)
##   sphereSource.SetRadius(5)

##   sphereSource1 = vtk.vtkSphereSource()
##   sphereSource1.SetCenter(0.0, 0.0, 0.0)
##   sphereSource1.SetRadius(1)
   
   #Read STL
   reader = vtk.vtkSTLReader()
   reader.SetFileName("robot.stl")

   


   #Create a mapper and actor
   mapper = vtk.vtkPolyDataMapper()
   mapper.SetInputConnection(reader.GetOutputPort())
   actor = vtk.vtkActor()
   actor.SetMapper(mapper)
   prop = actor.GetProperty()

##   mapper1 = vtk.vtkPolyDataMapper()
##   mapper1.SetInputConnection(sphereSource1.GetOutputPort())
##   actor1 = vtk.vtkActor()
##   actor1.SetMapper(mapper1)


   # Setup a renderer, render window, and interactor
   renderer = vtk.vtkRenderer()
   renderWindow = vtk.vtkRenderWindow()
   #renderWindow.SetWindowName("Test")

   renderWindow.AddRenderer(renderer);
   renderWindowInteractor = vtk.vtkRenderWindowInteractor()
   renderWindowInteractor.SetRenderWindow(renderWindow)

   #Add the actor to the scene
   renderer.AddActor(actor)
##   renderer.AddActor(actor1)
   renderer.SetBackground(1,1,1) # Background color white

   #Render and interact
   renderWindow.Render()

   # Initialize must be called prior to creating timer events.
   renderWindowInteractor.Initialize()

   # Sign up to receive TimerEvent
   cb = vtkTimerCallback1()
   cb.actors.append(actor)
   cb.actors.append(actor1)
   renderWindowInteractor.AddObserver('TimerEvent', cb.execute)
   timerId = renderWindowInteractor.CreateRepeatingTimer(100);

   #start the interaction and timer
   renderWindowInteractor.Start()


if __name__ == '__main__':
   main()
