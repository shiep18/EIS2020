import vtk
import time as t
import comjieshou as cs

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

interactor = vtk.vtkRenderWindowInteractor() #连接外部数据
interactor.SetRenderWindow(window)

renderer = vtk.vtkRenderer()
window.AddRenderer(renderer)

renderer.AddActor(actor)
renderer.AddActor(actor1)
renderer.SetBackground(0, 0, 1) #改颜色

actor.SetOrigin(0.5,0,0)
actor1.SetOrigin(0,9.038,10.055)
actor1.SetPosition(0,5,0)
actor1.RotateY(90)
for i in range(36):
    window.Render() #刷新界面
    t.sleep(0.5)
    actor.RotateY(10) #角色旋转度数
    actor1.RotateX(10)
'''
while True:
    ls,rs=cs.jieshou()
    window.Render() #刷新界面
    t.sleep(1)
    actor.RotateY(rs//10) #角色旋转度数
    actor1.RotateX(ls//10)
'''
interactor.Start()
