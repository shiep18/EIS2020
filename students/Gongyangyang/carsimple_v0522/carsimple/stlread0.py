import vtk


#Read STL
reader = vtk.vtkSTLReader()
reader.SetFileName("wheel1.stl")

#Create a mapper and actor
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(reader.GetOutputPort())
actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.SetOrigin(0,0,0)

# Setup a renderer, render window, and interactor
renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer);
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

#Add the actor to the scene
renderer.AddActor(actor)
renderer.SetBackground(1,0,0) # RGB 0~1

renderWindow.Render()
renderWindowInteractor.Start()

