import vtk
import time
import serial

ser = serial.Serial("COM3",timeout=1)
cnt = 0
speed = 0


mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(cone.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)

filename = "wheel.stl"
cone = vtk.vtkConeSource ()
cone.SetHeight( 30 )
cone.SetRadius( 10 )
cone.SetResolution( 10 )
cone.SetCenter(0,-10,0)

reader = vtk.vtkSTLReader()
reader.SetFileName(filename)

mapper1 = vtk.vtkPolyDataMapper()
mapper1.SetInputConnection(reader.GetOutputPort())

actor1 = vtk.vtkActor()
actor1.SetMapper(mapper1)

window = vtk.vtkRenderWindow()  # Sets the pixel width, length of the window.
window.SetSize(500, 500)

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(window)

renderer = vtk.vtkRenderer()
window.AddRenderer(renderer)

renderer.AddActor(actor)
renderer.AddActor(actor1)
renderer.SetBackground(0, 0, 1)

actor.SetOrigin(0.5,0,0)
actor1.SetOrigin(0,9,10)
actor1.SetPosition(0,5,0)

actor1.RotateY(90)

while True:
    resp = ser.readline()
    cnt += 1
    if resp !=  b'':
        print("moving remote car",cnt)
        resp = resp.decode("ASCII")
        b = resp.strip()
        c = b.split(',')
        d = list(map(int,c))
        print(d)
        speed = d[0]
        print("car wheel speed is ",speed)
        for i in range(3):
            time.sleep(1)
            actor.RotateY(speed)
            actor1.RotateX(speed)
            window.Render()
        print("end")
