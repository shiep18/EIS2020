import vtk
import time
import serial
ser=serial.Serial("COM13",timeout=1)
cnt=0
leftspeed=10
rightspeed=0
#cone = vtk.vtkConeSource()

filename = "wheel1.stl"

reader = vtk.vtkSTLReader()

reader.SetFileName(filename)

mapper1 = vtk.vtkPolyDataMapper()

mapper1.SetInputConnection(reader.GetOutputPort())

actor1 = vtk.vtkActor()

actor1.SetMapper(mapper1)

#mapper = vtk.vtkPolyDataMapper()
#mapper.SetInputConnection(cone.GetOutputPort())
#actor = vtk.vtkActor()
#actor.SetMapper(mapper)

window = vtk.vtkRenderWindow() # Sets the pixel width, length of the window.
window.SetSize(800, 800)

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(window)

renderer = vtk.vtkRenderer()
window.AddRenderer(renderer)

#renderer.AddActor(actor)
renderer.AddActor(actor1)
renderer.SetBackground(0,0,1)
actor1.RotateY(90)
#actor.SetOrigin(0.5,0,0)
actor1.SetOrigin(0,9,10)
actor1.SetPosition(0,5,0)
window.Render()
while True:
    resp=ser.readline()
    cnt+=1
    print("moving remote car",cnt)
    print(resp)
    if resp!=b"":
        resp=resp.decode("ASCII")
        b=resp.strip()
        c=b.split(",")
        print(c)
        d=list(map(int,c))
        print(d)
        leftspeed=d[0]
        #rightspeed=d[1]
        #print("car wheel speed is ",leftspeed,rightspeed)
        print("car wheel speed is ",leftspeed)
    time.sleep(0.01)
    #actor.RotateY(10)
    actor1.RotateX(leftspeed)
    window.Render()
#interactor.Start()
