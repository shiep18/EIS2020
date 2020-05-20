import vtk
import time
filename = "E:/2020class/QianRuShi/2020.5.18/vtk/wheel1.stl"


reader = vtk.vtkSTLReader()
reader.SetFileName(filename)
 
mapper1 = vtk.vtkPolyDataMapper()
mapper1.SetInputConnection(reader.GetOutputPort())

actor1 = vtk.vtkActor()
actor1.SetMapper(mapper1)

cone = vtk.vtkConeSource()
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(cone.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)

window = vtk.vtkRenderWindow() # Sets the pixel width, length of the window.
window.SetSize(500, 500)

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(window)

renderer = vtk.vtkRenderer()
window.AddRenderer(renderer)

renderer.AddActor(actor)
renderer.AddActor(actor1)
renderer.SetBackground(1, 0.1, 0.4)



cone = vtk.vtkConeSource ()
cone.SetHeight( 3.0 )
cone.SetRadius( 1.0 )
cone.SetResolution( 10 )

actor.SetPosition(-5,8,0)
actor1.SetOrigin(0,0,1)
actor1.SetPosition(0,1,0)

for i in range(36):
    time.sleep(1)
    #actor.RotateZ(10)
    actor1.RotateX(10)
    window.Render()

window.Render()
interactor.Start()
