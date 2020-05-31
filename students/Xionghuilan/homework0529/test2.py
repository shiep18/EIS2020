import vtk
import serial

class mytimercallback():
   def __init__(self):
       self.actors=[]
       self.timer_count=0
       self.ser=serial.Serial("COM3","9600",timeout=0.5)
       self.leftspeed=0
   def execute(self,obj,event):
      # print(self.timer_count,event)
      if event !="TimerEvent":
         return
      resp=self.ser.readline().decode().strip()
      if resp !="":
          if resp == "o":
              self.actors[0].RotateX(60)
              f = open('C:\\Apache24\\htdocs\\index1.html', 'w')
              f.write("<meta http-equiv=\"refresh\" content=\"1\">\n")
              f.write("open")
              f.close()
          elif resp == "c":
              # self.actors[0].RotateZ(-90)
              self.actors[0].RotateX(-60)
              f = open('C:\\Apache24\\htdocs\\index1.html', 'w')
              f.write("<meta http-equiv=\"refresh\" content=\"1\">\n")
              f.write("close")
              f.close()
         # spds=resp.split(",")
         # print(resp)
         # print(spds)
         # speeds=list(map(int,spds))
         # print(speeds,speeds[0],speeds[1],speeds[2])
         # self.leftspeed=speeds[0]
         # print("speed update",self.leftspeed)
      # self.actors[0].RotateZ(self.leftspeed)
      iren = obj
      iren.GetRenderWindow().Render()
      self.timer_count += 1

def main():
    reader = vtk.vtkSTLReader()
    reader.SetFileName("door.stl")

    # Create a mapper and actor
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.SetOrigin(actor.GetCenter())

    # Setup a renderer, render window, and interactor
    renderer = vtk.vtkRenderer()
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.AddRenderer(renderer);
    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # Add the actor to the scene
    renderer.AddActor(actor)
    renderer.SetBackground(0, 0, 0.8)  # RGB 0~1
    actor.RotateZ(-90)
    # actor.RotateX(60)

   #Render and interact
    renderWindow.Render()

   # Initialize must be called prior to creating timer events.
    renderWindowInteractor.Initialize()

   # Sign up to receive TimerEvent
    cb = mytimercallback()
    cb.actors.append(actor)
    renderWindowInteractor.AddObserver('TimerEvent', cb.execute)
    timerId = renderWindowInteractor.CreateRepeatingTimer(100);

   #start the interaction and timer

    renderWindowInteractor.Start()


if __name__ == '__main__':
   main()