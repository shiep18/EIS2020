import vtk
import serial
import time

class mytimercallback():
   def __init__(self):
       self.actors=[]
       self.timer_count=0
       self.ser=serial.Serial("COM3","9600",timeout=0.5)
       self.state=''
       self.state1='on'
   def execute(self,obj,event):
      print(self.timer_count,event)
      if event !="TimerEvent":
         return
      resp=self.ser.readline().decode().strip()
      if resp !="":
         spds=resp.split(",")
         print(resp)
         print(spds)
         #self.actors[0].SetOrigin(0,207.5,50)
         speeds=list(map(str,spds))
         self.state=speeds[0]
         if self.state=='on' and self.state1=='on':
           f=open("C:\\Apache24\\htdocs\\index.html", "w")
           #f.write("<meta http-equiv=\"refresh\" content=\"1\">\n  ")
           f.write('open')
           self.actors[0].RotateZ(-90)
           self.state1='off'
         if self.state=='off' and self.state1=='off':
           f=open("C:\\Apache24\\htdocs\\index.html", "w")
           #f.write("<meta http-equiv=\"refresh\" content=\"1\">\n  ")
           f.write('close')
           self.actors[0].RotateZ(90)
           self.state1='on'
         print("state is : ",self.state,self.state1)
      iren = obj
      iren.GetRenderWindow().Render()
      self.timer_count += 1
def zhengmian(actor1,actor2):
    actor1.SetOrigin(-75.00000000000001, 415, 50)
    actor2.SetOrigin(-75.00000000000001, 415, 50)
    # -75.00000000000001, 207.5, 50.0
    actor1.RotateX(-90)
    actor2.RotateX(-90)
    actor1.RotateZ(270)
    actor2.RotateZ(270)
def main():
    reader1 = vtk.vtkSTLReader()
    reader1.SetFileName("door.stl")
    reader2 = vtk.vtkSTLReader()
    reader2.SetFileName("menkuang.stl")

    mapper1 = vtk.vtkPolyDataMapper()
    mapper1.SetInputConnection(reader1.GetOutputPort())
    mapper2 = vtk.vtkPolyDataMapper()
    mapper2.SetInputConnection(reader2.GetOutputPort())

    actor1 = vtk.vtkActor()
    actor1.SetMapper(mapper1)
    actor2 = vtk.vtkActor()
    actor2.SetMapper(mapper2)

    renderer = vtk.vtkRenderer()
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.AddRenderer(renderer);
    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    renderer.AddActor(actor1)
    renderer.AddActor(actor2)
    #renderer.AddActor(assembly)

    renderer.SetBackground(0,0,0.8) # RGB 0~1
    zhengmian(actor1,actor2)
    time.sleep(1)
    
    #actor1.SetOrigin(0,207.5,50)
    #actor2.SetOrigin(actor2.GetCenter())
    #assembly.SetOrigin(actor3.GetCenter())

    #actor1.RotateY(-90)
    #actor1.RotateX(-90)
   
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

