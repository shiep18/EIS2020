import vtk
import time
import serial

ser = serial.Serial("COM2",timeout=1)
cnt = 0
leftspeed = 0
rightspeed = 0

cone = vtk.vtkConeSource()

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

window = vtk.vtkRenderWindow()  # Sets the pixel width, length of the window.
window.SetSize(500, 500)

renderer = vtk.vtkRenderer()
window.AddRenderer(renderer)

renderer.AddActor(actor)
renderer.AddActor(actor1)
renderer.SetBackground(0, 0, 1)

actor1.RotateY(90)
actor.SetOrigin(0.5, 0, 0)
actor1.SetOrigin(0, 9, 10)
actor1.SetPosition(0, 5, 0)

while True:
    resp = ser.readline()
    cnt += 1
    print("moving remote car", cnt)
    print(resp)
    if resp != b"":
        resp = resp.decode()
        b = resp.strip()
        c = b.split(",")
        d = list(map(int, c))
        leftspeed = d[0]/10
        rightspeed = d[1]/10

    for i in range(5):
        time.sleep(0.1)
        actor.RotateY(leftspeed)
        actor1.RotateX(leftspeed)
        window.Render()

