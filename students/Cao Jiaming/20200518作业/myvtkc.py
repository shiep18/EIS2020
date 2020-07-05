import vtk
import time
cone = vtk.vtkConeSource()

filename = "wheel1.stl"

reader = vtk.vtkSTLReader()

reader.SetFileName(filename)

mapper1 = vtk.vtkPolyDataMapper()

mapper1.SetInputConnection(reader.GetOutputPort())

actor1 = vtk.vtkActor()

actor1.SetMapper(mapper1)

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(cone.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)

window = vtk.vtkRenderWindow() # Sets the pixel width, length of the window.
window.SetSize(1400, 800)

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(window)

renderer = vtk.vtkRenderer()
window.AddRenderer(renderer)

renderer.AddActor(actor)
renderer.AddActor(actor1)
renderer.SetBackground(0,0,1)
actor1.RotateY(90)
actor.SetOrigin(0.5,0,0)
actor1.SetOrigin(0,9,10)
actor1.SetPosition(0,5,0)
window.Render()
for i in range(36):
    time.sleep(0.1)
    actor.RotateY(10)
    actor1.RotateX(10)
    window.Render()
interactor.Start()
