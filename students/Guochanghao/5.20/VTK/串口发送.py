import vtk
import time
import serial

ser=serial.Serial("COM1",timeout=1)

cone = vtk.vtkConeSource()
cnt=0
speed = 20

filename = "wheel1.stl"

reader = vtk.vtkSTLReader()
reader.SetFileName(filename)

mapper1 = vtk.vtkPolyDataMapper()
mapper1.SetInputConnection(reader.GetOutputPort())

actor1 = vtk.vtkActor()
actor1.SetMapper(mapper1)

window = vtk.vtkRenderWindow() # Sets the pixel width, length of the window.
window.SetSize(500, 500)

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(window)

renderer = vtk.vtkRenderer()
window.AddRenderer(renderer)

renderer.AddActor(actor1)
renderer.SetBackground(0.1,0.1,0.4)

actor1.SetOrigin(0,9.038,10.055)
actor1.SetPosition(0,5,0)
actor1.RotateY(90)

while True:
    time.sleep(1)
    actor1.RotateX(speed)
    window.Render()

    resp=ser.readline()
    cnt+=1
    print("moving remote car",cnt)
    print(resp)
    if resp!=b"":
        resp=resp.decode("ASCII")
        b=resp.strip()
        speed=int(b)
    print("car wheel speed is",speed)
