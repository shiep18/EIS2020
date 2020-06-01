import vtk
import serial

class mytimercallback():
   def __init__(self):
       self.actors=[]
       self.timer_count=0
       self.ser=serial.Serial("COM2","9600",timeout=0.5)
       self.com=' '
       self.tangle=0
       self.flag=0
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
         self.com=speeds[0]
         if self.com=='a' and self.flag==1:
             self.flag=0
             self.actors[0].RotateX(35);
             f=open('C:\Apache24\htdocs\index1.html','w')
             f.write("close       ")
        
         elif self.com=='b' and self.flag==0:
             self.flag=1
             print(self.flag)
             self.actors[0].RotateX(-35);
             f=open('C:\Apache24\htdocs\index1.html','w')
             f.write("open       ")
      iren = obj
      iren.GetRenderWindow().Render()
      self.timer_count += 1

def main():
   #Read STL
   reader1 = vtk.vtkSTLReader()
   reader1.SetFileName("door.stl")



   #Create a mapper and actor
   mapper1 = vtk.vtkPolyDataMapper()
   mapper1.SetInputConnection(reader1.GetOutputPort())


   actor1 = vtk.vtkActor()
   actor1.SetMapper(mapper1)


   # assembly actor6 and actor7
   assembly = vtk.vtkAssembly()



   # Setup a renderer, render window, and interactor
   renderer = vtk.vtkRenderer()
   renderWindow = vtk.vtkRenderWindow()
   renderWindow.AddRenderer(renderer);
   renderWindowInteractor = vtk.vtkRenderWindowInteractor()
   renderWindowInteractor.SetRenderWindow(renderWindow)

   #Add the actor to the scene
   renderer.AddActor(actor1)

   renderer.AddActor(assembly)

   renderer.SetBackground(0,0,0.8) # RGB 0~1

   actor1.SetOrigin(actor1.GetCenter())


   #Render and interact
   renderWindow.Render()

   # Initialize must be called prior to creating timer events.
   renderWindowInteractor.Initialize()
   actor1.RotateZ(-90)

   # Sign up to receive TimerEvent
   cb = mytimercallback()
   cb.actors.append(actor1)

   cb.actors.append(assembly)
   renderWindowInteractor.AddObserver('TimerEvent', cb.execute)
   timerId = renderWindowInteractor.CreateRepeatingTimer(100);

   #start the interaction and timer
   renderWindowInteractor.Start()


if __name__ == '__main__':
   main()
