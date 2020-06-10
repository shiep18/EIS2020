import vtk
import serial

class mytimercallback():
   def __init__(self):
       self.actors=[]
       self.timer_count=0
       self.ser=serial.Serial("COM1","9600",timeout=0.5)
       self.state=''
       self.state1='h'
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
         self.state=speeds[0]
         if self.state=='p' and self.state1=='p':
           self.actors[0].RotateZ(-180)
           self.state1='h'
           filename='C:\Apache24\htdocs\index.html'
           with open(filename,'w') as file_object:
              file_object.write("on")
         if self.state=='h' and self.state1=='h':
           self.actors[0].RotateZ(-180)
           self.state1='p'
           filename='C:\Apache24\htdocs\index.html'
           with open(filename,'w') as file_object:
              file_object.write("off")
         print("state is : ",self.state,self.state1)
      iren = obj
      iren.GetRenderWindow().Render()
      self.timer_count += 1

def main():
    reader1 = vtk.vtkSTLReader()
    reader1.SetFileName("robot.stl")
    #reader2 = vtk.vtkSTLReader()
    #reader2.SetFileName("xin.stl")

    mapper1 = vtk.vtkPolyDataMapper()
    mapper1.SetInputConnection(reader1.GetOutputPort())
    #mapper2 = vtk.vtkPolyDataMapper()
    #mapper2.SetInputConnection(reader2.GetOutputPort())

    actor1 = vtk.vtkActor()
    actor1.SetMapper(mapper1)
    #actor2 = vtk.vtkActor()
    #actor2.SetMapper(mapper2)

    renderer = vtk.vtkRenderer()
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.AddRenderer(renderer);
    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    renderer.AddActor(actor1)
    #renderer.AddActor(actor2)

    renderer.SetBackground(0,0,0.8) # RGB 0~1

    actor1.SetOrigin(actor1.GetCenter())
    #actor2.SetOrigin(actor2.GetCenter())

    actor1.RotateY(-90)
    actor1.RotateX(-90)
   
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

