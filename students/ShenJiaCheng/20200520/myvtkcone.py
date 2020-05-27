import vtk
import time
import serial

ser = serial.Serial("COM13",timeout=0.01)
wheel_speed = 100
cone = vtk.vtkConeSource()
cone.SetHeight(10.0)
cone.SetRadius(5.0)
cone.SetResolution(10)

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(cone.GetOutputPort())
actor = vtk.vtkActor()
actor.SetMapper(mapper)

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
renderer.AddActor(actor)
renderer.AddActor(actor1)
renderer.SetBackground(0,0,1)

actor.SetOrigin(1,0,0)
actor1.SetPosition(0,5,0)
actor1.SetOrigin(-4.5,9,10)
window.Render()
time.sleep(1)

for i in range(9):

    actor.RotateY(10)

    actor1.RotateY(10)

    window.Render()

    time.sleep(0.1)

while True:
    response = ser.readline()
    if response is not b"":
        response = response.decode("ASCII")
        wheel_speed = int(response.strip())
    actor.RotateY(10)
    actor1.RotateX(wheel_speed//10)
    window.Render()
    time.sleep(0.1)


interactor.Start()
