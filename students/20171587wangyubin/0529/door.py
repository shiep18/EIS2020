import vtk
import serial

class mytimercallback():
   def __init__(self):
       self.actors=[]
       self.timer_count=0
       self.ser=serial.Serial("COM2","9600",timeout=0.5)
       self.res=0
       self.state=0
   def execute(self,obj,event):
      print(self.timer_count,event)
      if event !="TimerEvent":
         return
      resp=self.ser.readline().decode().strip()
      if resp !="":
         spds=resp.split(",")
         print(resp)
         print(spds)
         states=list(map(int,spds))
         self.res=states[0]
         self.actors[0].SetOrigin(-44,22.5,0)
         self.actors[1].SetOrigin(-6,22.5,0)
         if self.res==0 and self.state==0:
               self.actors[0].RotateY(90)
               self.actors[1].RotateY(-90)
               self.state=1
               filename = 'state.txt'
               with open(filename, 'w') as file_object:
                   file_object.write("open")
         elif self.res==1 and self.state==1:
               self.actors[0].RotateY(-90)
               self.actors[1].RotateY(90)
               self.state=0
               filename = 'state.txt'
               with open(filename, 'w') as file_object:
                   file_object.write("close") 
      iren = obj
      iren.GetRenderWindow().Render()
      self.timer_count += 1

def main():
   #Read STL
   reader1 = vtk.vtkSTLReader()
   reader1.SetFileName("leftdoor.stl")
   reader2 = vtk.vtkSTLReader()
   reader2.SetFileName("rightdoor.stl")
   reader3 = vtk.vtkSTLReader()
   reader3.SetFileName("doorframe.stl")


   #(-6,22.5,0)  (-44,22,5,0)
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

   #Add the actor to the scene
   renderer.AddActor(actor1)
   renderer.AddActor(actor2)
   renderer.AddActor(actor3)


   renderer.SetBackground(0,0,0.8) # RGB 0~1

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


if __name__ == '__main__':
   main()
