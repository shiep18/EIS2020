import vtk
import time

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

window = vtk.vtkRenderWindow() # Sets the pixel width, length of the window.
window.SetSize(500, 500)

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(window)

renderer = vtk.vtkRenderer()
window.AddRenderer(renderer)

renderer.AddActor(actor)
renderer.AddActor(actor1)
renderer.SetBackground(0, 0, 1)

actor.SetOrigin(0,0,0)
actor1.SetOrigin(0,0,10)
actor1.SetPosition(10,0,0)

for i in range(9):
    time.sleep(1)
    actor.RotateY(0)
    actor1.RotateY(-10)
    window.Render()

#iren.Start()
