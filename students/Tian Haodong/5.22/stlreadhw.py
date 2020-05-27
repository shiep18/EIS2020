import vtk
import time


#Read STL
reader1 = vtk.vtkSTLReader()
reader1.SetFileName("wheel1hw.stl")
reader2 = vtk.vtkSTLReader()
reader2.SetFileName("wheel2hw.stl")
#reader3 = vtk.vtkSTLReader()
#reader3.SetFileName("wheel3.stl")
#reader4 = vtk.vtkSTLReader()
#reader4.SetFileName("wheel4.stl")
reader5 = vtk.vtkSTLReader()
reader5.SetFileName("cframehw.stl")
 
#Create a mapper and actor
mapper1 = vtk.vtkPolyDataMapper()
mapper1.SetInputConnection(reader1.GetOutputPort())
mapper2 = vtk.vtkPolyDataMapper()
mapper2.SetInputConnection(reader2.GetOutputPort())
#mapper3 = vtk.vtkPolyDataMapper()
#mapper3.SetInputConnection(reader3.GetOutputPort())
#mapper4 = vtk.vtkPolyDataMapper()
#mapper4.SetInputConnection(reader4.GetOutputPort())
mapper5 = vtk.vtkPolyDataMapper()
mapper5.SetInputConnection(reader5.GetOutputPort())

actor1 = vtk.vtkActor()
actor1.SetMapper(mapper1)
actor2 = vtk.vtkActor()
actor2.SetMapper(mapper2)
#actor3 = vtk.vtkActor()
#actor3.SetMapper(mapper3)
#actor4 = vtk.vtkActor()
#actor4.SetMapper(mapper4)
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
#renderer.AddActor(actor3)
#renderer.AddActor(actor4)
renderer.AddActor(actor5)

renderer.SetBackground(0.1,0.1,0.8) # RGB 0~1


actor1.SetOrigin(actor1.GetCenter())
actor2.SetOrigin(actor2.GetCenter())
#actor3.SetOrigin(actor3.GetCenter())
#actor4.SetOrigin(actor4.GetCenter())
actor5.SetOrigin(actor2.GetCenter())
renderer.ResetCamera()
camera = renderer.GetActiveCamera()



for i in range(360):
    time.sleep(0.2)
    actor1.RotateZ(1)
    actor2.RotateZ(1)
    #actor3.RotateX(1)
    #actor4.RotateX(1)
    renderWindow.Render()
    #camera.Azimuth(i)
    #camera.Yaw(i*0.1)



