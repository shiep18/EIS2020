import vtk
import serial

class mytimercallback():
   def __init__(self):
       self.actors=[]
       self.timer_count=0
       self.ser=serial.Serial("COM1","9600",timeout=0.5)
       self.leftspeed=0
       self.rightspeed=0
       self.state=""
       self.state1='a'
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
         self.state = speeds[0]
         if self.state=='b' and self.state1=='a':
            actor2.RotateY(90)
            self.state1='b'
            f=open("C:\\Apache24\\Apache24\\htdocs\\index1.html","w")
            f.write("<meta http-equiv=\"refresh\" content=\"1\">\n")
            f.write("open")
            f.close()
         if self.state=='a' and self.state1=='b':
            actor2.RotateY(-90)
            self.state1='a'
            f=open("C:\\Apache24\\Apache24\\htdocs\\index1.html","w")
            f.write("<meta http-equiv=\"refresh\" content=\"1\">\n")
            f.write("close")
            f.close()
         print("state is : ",self.state,self.state1)
         renderWindow.Render()
      self.timer_count += 1

      

    

    
    #Read STL
reader1 = vtk.vtkSTLReader()
reader1.SetFileName("door1.stl")
reader2 = vtk.vtkSTLReader()
reader2.SetFileName("door2.stl")
reader3 = vtk.vtkSTLReader()
reader3.SetFileName("door3.stl")


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









#Render and interact
renderWindow.Render()

# Initialize must be called prior to creating timer events.
renderWindowInteractor.Initialize()

# Sign up to receive TimerEvent
cb = mytimercallback()
#cb.actors.append(actor)
cb.actors.append(actor1)
cb.actors.append(actor2)
cb.actors.append(actor3)
renderWindowInteractor.AddObserver('TimerEvent', cb.execute)
timerId = renderWindowInteractor.CreateRepeatingTimer(100);

#start the interaction and timer
renderWindowInteractor.Start()
    



