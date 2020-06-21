import vtk
import time

#cone = vtk.vtkConeSource()

#mapper = vtk.vtkPolyDataMapper()
#mapper.SetInputConnection(cone.GetOutputPort())

cone=vtk.vtkConeSource()
cone.SetHeight(30)
cone.SetRadius(10)
cone.SetResolution(10)

coneMapper = vtk.vtkPolyDataMapper()  
coneMapper.SetInputConnection(cone.GetOutputPort()) 

actor = vtk.vtkActor()
actor.SetMapper(coneMapper)

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
renderer.SetBackground(0.1,0.1,0.4)

actor.SetOrigin(0,0,0)
actor.SetPosition(0,-5,0)
actor1.SetOrigin(0,9.038,10.055)
actor1.SetPosition(0,5,0)
#actor.RotateY(90)
actor1.RotateY(90)


for i in range(36):
    time.sleep(1)
    actor.RotateX(10)
    actor1.RotateX(20)
    window.Render()

iren.Start()
