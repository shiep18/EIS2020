import vtk
import serial

class mytimercallback():
   def __init__(self):
       self.actors=[]
       self.timer_count=0
       self.ser=serial.Serial("COM3","9600",timeout=0.5)
       self.state=''
       self.state1='O'
   def execute(self,obj,event):
      print(self.timer_count,event)
      if event !="TimerEvent":
         return
      resp=self.ser.readline().decode().strip()
      if resp !="":
         spds=resp.split(",")
         print(resp)
         print(spds)
         NN=list(map(str,spds))
         self.state=NN[0]
         if self.state=='O' and self.state1=='O':
           self.actors[0].RotateZ(180)
           self.state1='C'
           f = open(r"C:\Users\38098\AppData\Roaming\.homeassistant\custom_components\state.txt",'w')
           f.write("ON")
         if self.state=='C' and self.state1=='C':
           self.actors[0].RotateZ(180)
           self.state1='O'
           f = open(r"C:\Users\38098\AppData\Roaming\.homeassistant\custom_components\state.txt",'w')
           f.write("OFF")
         print("state is : ",self.state)
      iren = obj
      iren.GetRenderWindow().Render()
      self.timer_count += 1

def main():
    reader1 = vtk.vtkSTLReader()
    reader1.SetFileName("door.stl")
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

