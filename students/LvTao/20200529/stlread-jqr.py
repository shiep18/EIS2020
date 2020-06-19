import vtk
import time
import serial

filename = "jqr.stl"
reader = vtk.vtkSTLReader()
reader.SetFileName(filename)
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(reader.GetOutputPort())
def __init__(self):
       self.ser=serial.Serial("COM11","9600",timeout=0.5)



if vtk.VTK_MAJOR_VERSION <= 5:
    mapper.SetInput(reader.GetOutput())
else:
    mapper.SetInputConnection(reader.GetOutputPort())
actor = vtk.vtkActor()
actor.SetMapper(mapper)
# Create a rendering window and renderer
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren) 
# Create a renderwindowinteractor
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
# Assign actor to the renderer
ren.AddActor(actor)

actor.SetOrigin(actor.GetCenter())
# Enable user interface interactor
iren.Initialize()
actor.RotateX(-90)
def front():
    renWin.Render()
    #iren.Start()
def back():
    actor.RotateZ(-180)
    renWin.Render()
    iren.Start()
while True:
    time.sleep(0.5)
    resp=self.ser.readline()
    print(str(resp))
    if resp !=b'':
        print(str(resp))
        if resp ==b'A':
            front()
            resp=ser.readline()
        if resp ==b'B':
            back()
            resp=ser.readline()
        



