import vtk

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
renderer.SetBackground(1, 0.1, 0.4)

window.Render()
interactor.Start()
