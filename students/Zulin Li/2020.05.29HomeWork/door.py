import vtk
import time
import serial

addr=r'C:\Apache24\htdocs\Blank.html'

class mytimercallback():
   def __init__(self):
       self.timer_count=0
       self.ser=serial.Serial("COM13","9600",timeout=0.5)
   def execute(self,obj,event):
      print(self.timer_count,event)
      global Face
      if event !="TimerEvent":
         return
      resp=self.ser.readline().decode().strip()
      if resp !="":
         if resp=='A':
             Open()
         elif resp=='B':
             Close()
      iren = obj
      iren.GetRenderWindow().Render()
      self.timer_count += 1

flag=2

def Open():
    global flag
    if flag==2:
        actor1.RotateZ(60)
        renderWindow.Render()
        actor4.RotateZ(-60)
        renderWindow.Render()
        f = open(addr, 'w')
        f.write("Opened")
        f.close()
        flag = 1

def Close():
    global flag
    if flag == 1:
        actor1.RotateZ(-60)
        renderWindow.Render()
        actor4.RotateZ(60)
        renderWindow.Render()
        f = open(addr, 'w')
        f.write("Closed")
        f.close()
        flag = 2

reader1 = vtk.vtkSTLReader()
reader1.SetFileName("Left.stl")
reader2 = vtk.vtkSTLReader()
reader2.SetFileName("onleft.stl")
reader3 = vtk.vtkSTLReader()
reader3.SetFileName("onright.stl")
reader4 = vtk.vtkSTLReader()
reader4.SetFileName("Right.stl")

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
actor2 = vtk.vtkActor()
actor2.SetMapper(mapper2)
actor3 = vtk.vtkActor()
actor3.SetMapper(mapper3)
actor4 = vtk.vtkActor()
actor4.SetMapper(mapper4)


assembly = vtk.vtkAssembly()
assembly.AddPart(actor1)
assembly.AddPart(actor2)
assembly.AddPart(actor3)
assembly.AddPart(actor4)

renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

renderer.AddActor(assembly)

renderer.SetBackground(0,0,0.8) # RGB 0~1

actor1.SetOrigin(actor2.GetCenter())
actor4.SetOrigin(actor3.GetCenter())

assembly.RotateZ(-90)
assembly.RotateY(-90)
renderWindow.Render()

cb = mytimercallback()
renderWindowInteractor.AddObserver('TimerEvent', cb.execute)
timerId = renderWindowInteractor.CreateRepeatingTimer(100)

renderWindowInteractor.Start()
