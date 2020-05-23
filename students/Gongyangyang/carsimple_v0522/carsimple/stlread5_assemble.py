import vtk


#Read STL
reader1 = vtk.vtkSTLReader()
reader1.SetFileName("wheel1.stl")
reader2 = vtk.vtkSTLReader()
reader2.SetFileName("wheel2.stl")
reader3 = vtk.vtkSTLReader()
reader3.SetFileName("wheel3.stl")
reader4 = vtk.vtkSTLReader()
reader4.SetFileName("wheel4.stl")
reader5 = vtk.vtkSTLReader()
reader5.SetFileName("cframe.stl")
reader6 = vtk.vtkSTLReader()
reader6.SetFileName("pole.stl")
reader7 = vtk.vtkSTLReader()
reader7.SetFileName("indicator.stl")

 
#Create a mapper and actor
mapper1 = vtk.vtkPolyDataMapper()
mapper1.SetInputConnection(reader1.GetOutputPort())
mapper2 = vtk.vtkPolyDataMapper()
mapper2.SetInputConnection(reader2.GetOutputPort())
mapper3 = vtk.vtkPolyDataMapper()
mapper3.SetInputConnection(reader3.GetOutputPort())
mapper4 = vtk.vtkPolyDataMapper()
mapper4.SetInputConnection(reader4.GetOutputPort())
mapper5 = vtk.vtkPolyDataMapper()
mapper5.SetInputConnection(reader5.GetOutputPort())
mapper6 = vtk.vtkPolyDataMapper()
mapper6.SetInputConnection(reader5.GetOutputPort())
mapper7 = vtk.vtkPolyDataMapper()
mapper7.SetInputConnection(reader5.GetOutputPort())

actor1 = vtk.vtkActor()
actor1.SetMapper(mapper1)
actor2 = vtk.vtkActor()
actor2.SetMapper(mapper2)
actor3 = vtk.vtkActor()
actor3.SetMapper(mapper3)
actor4 = vtk.vtkActor()
actor4.SetMapper(mapper4)
actor5 = vtk.vtkActor()
actor5.SetMapper(mapper5)
actor5 = vtk.vtkActor()
actor5.SetMapper(mapper5)

# Setup a renderer, render window, and interactor
renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer);
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

#Add the actor to the scene
renderer.AddActor(actor1)
renderer.AddActor(actor2)
renderer.AddActor(actor3)
renderer.AddActor(actor4)
renderer.AddActor(actor5)

renderer.SetBackground(0,0,0.8) # RGB 0~1

print("actor1 center:",actor1.GetCenter())
print("actor2 center:",actor2.GetCenter())
print("actor3 center:",actor3.GetCenter())
print("actor4 center:",actor4.GetCenter())

actor1.SetOrigin(-4.5,9,10)
actor2.SetOrigin(-49.5,9,10)
actor3.SetOrigin(-49.5,63,10)
actor4.SetOrigin(-4.5,65,10)

#renderer.ResetCamera()
camera = renderer.GetActiveCamera()
#camera.SetPosition(0,0,0)
#camera.SetViewUp(0,0,1)
#camera.Azimuth(90)
camera.SetViewUp(-100,0,0)
camera.SetPosition(50,50,50)
camera.Zoom(0.4)


actor1.RotateX(-1)
actor2.RotateX(-1)
actor3.RotateX(-1)
actor4.RotateX(-1)
renderWindow.Render()

renderWindowInteractor.Start()



