import vtk
import time
import serial

class mytimercallback():
   def __init__(self):
       self.actors=[]
       self.timer_count=0
       self.ser=serial.Serial("COM13","9600",timeout=0.1)
       self.leftspeed=0
       self.rightspeed=0
       self.indic_angle = 0
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
         self.indic_angle = speeds[2] - self.indic_angle
         print("speed update",self.leftspeed,self.rightspeed,self.indic_angle)
         self.actors[3].RotateX(self.indic_angle);
         self.indic_angle = speeds[2]  
      self.actors[0].RotateZ(self.leftspeed);
      self.actors[1].RotateZ(self.rightspeed);
      iren = obj
      iren.GetRenderWindow().Render()
      self.timer_count += 1

#Read STL
reader1 = vtk.vtkSTLReader()
reader1.SetFileName("wheel1.stl")
reader2 = vtk.vtkSTLReader()
reader2.SetFileName("wheel2.stl")
reader5 = vtk.vtkSTLReader()
reader5.SetFileName("cframe.stl")
reader6 = vtk.vtkSTLReader()
reader6.SetFileName("pole.stl")
reader7 = vtk.vtkSTLReader()
reader7.SetFileName("indicator.stl")

 
#Create a mapper and actor
mapper1 = vtk.vtkPolyDataMapper()
mapper1.SetInputConnection(reader1.GetOutputPort())
mapper2 = vtk.vtkPolyDataMapper()
mapper2.SetInputConnection(reader2.GetOutputPort())
mapper5 = vtk.vtkPolyDataMapper()
mapper5.SetInputConnection(reader5.GetOutputPort())
mapper6 = vtk.vtkPolyDataMapper()
mapper6.SetInputConnection(reader6.GetOutputPort())
mapper7 = vtk.vtkPolyDataMapper()
mapper7.SetInputConnection(reader7.GetOutputPort())

actor1 = vtk.vtkActor()
actor1.SetMapper(mapper1)
actor2 = vtk.vtkActor()
actor2.SetMapper(mapper2)
actor5 = vtk.vtkActor()
actor5.SetMapper(mapper5)
actor6 = vtk.vtkActor()
actor6.SetMapper(mapper6)
actor7 = vtk.vtkActor()
actor7.SetMapper(mapper7)

# assembly actor6 and actor7
assembly = vtk.vtkAssembly()
assembly.AddPart(actor6)
assembly.AddPart(actor7)
assembly.SetOrigin(actor6.GetCenter())

# Setup a renderer, render window, and interactor
renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer);
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

#Add the actor to the scene
renderer.AddActor(actor1)
renderer.AddActor(actor2)
renderer.AddActor(actor5)
renderer.AddActor(assembly)

renderer.SetBackground(0,0,0.8) # RGB 0~1

print("actor1 center:",actor1.GetCenter())
print("actor2 center:",actor2.GetCenter())

actor1.SetOrigin(actor1.GetCenter())
actor2.SetOrigin(actor2.GetCenter())

    
#Render and interact
renderWindow.Render()

# Initialize must be called prior to creating timer events.
renderWindowInteractor.Initialize()

# Sign up to receive TimerEvent
cb = mytimercallback()
cb.actors.append(actor1)
cb.actors.append(actor2)
cb.actors.append(actor5)
cb.actors.append(assembly)

renderWindowInteractor.AddObserver('TimerEvent', cb.execute)
timerId = renderWindowInteractor.CreateRepeatingTimer(100);


renderWindowInteractor.Start()
