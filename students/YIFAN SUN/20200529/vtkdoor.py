import vtk
import serial

class mytimercallback():
   def __init__(self):
       self.actors=[]
       self.timer_count=0
       self.ser=serial.Serial("COM3","9600",timeout=0.5)
       self.side=''
       self.flag='O'
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
         self.side=speeds[0]
         if self.side=='C' and self.flag=='O':
           f=open("C:\\Apache24\\htdocs\\index.html", "w")
           f.write("关")
           f.close()
           self.actors[0].RotateY(-20)
           self.flag='C'
         if self.side=='O' and self.flag=='C':
           f=open("C:\\Apache24\\htdocs\\index.html", "w")
           f.write("开")
           f.close()
           self.actors[0].RotateY(20)
           self.flag='O'
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

   # Setup a renderer, render window, and interactor
   renderer = vtk.vtkRenderer()
   renderWindow = vtk.vtkRenderWindow()
   renderWindow.AddRenderer(renderer);
   renderWindowInteractor = vtk.vtkRenderWindowInteractor()
   renderWindowInteractor.SetRenderWindow(renderWindow)

   #Add the actor to the scene
   renderer.AddActor(actor1)

   renderer.SetBackground(0,0,0.8) # RGB 0~1

   actor1.SetOrigin(-48,45,5)
   #Render and interact
   renderWindow.Render()

   # Initialize must be called prior to creating timer events.
   renderWindowInteractor.Initialize()

   # Sign up to receive TimerEvent
   cb = mytimercallback()
   cb.actors.append(actor1)
   renderWindowInteractor.AddObserver('TimerEvent', cb.execute)
   timerId = renderWindowInteractor.CreateRepeatingTimer(100);
   #start the interaction and timer
   renderWindowInteractor.Start()


if __name__ == '__main__':
   main()
