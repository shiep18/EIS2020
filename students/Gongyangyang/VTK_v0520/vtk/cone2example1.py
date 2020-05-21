#!/usr/bin/env python
#
# This example demonstrates the creation of multiple actors and the
# manipulation of their properties and transformations. It is a
# derivative of Cone.py, see that example for more information.
#

import vtk
import time

cone = vtk.vtkConeSource ()
cone.SetHeight( 3.0 )
cone.SetRadius( 1.0 )
cone.SetResolution( 10 )

coneMapper = vtk.vtkPolyDataMapper()
coneMapper.SetInputConnection(cone.GetOutputPort())

coneActor = vtk.vtkActor()
coneActor.SetMapper(coneMapper)
coneActor.GetProperty().SetColor(0.2, 0.63, 0.79)
coneActor.GetProperty().SetDiffuse(0.7)
coneActor.GetProperty().SetSpecular(0.4)
coneActor.GetProperty().SetSpecularPower(20)

property = vtk.vtkProperty()
property.SetColor(0, 1, 0)
property.SetDiffuse(0.7)
property.SetSpecular(0.4)
property.SetSpecularPower(20)

coneActor2 = vtk.vtkActor()
coneActor2.SetMapper(coneMapper)
coneActor2.SetProperty(property)
coneActor2.SetPosition(0, 2, 0)
coneActor2.SetOrigin(1.5,0,0)

ren1 = vtk.vtkRenderer()
ren1.AddActor(coneActor)
ren1.AddActor(coneActor2)
ren1.SetBackground(0.1, 0.2, 0.4)

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren1)
renWin.SetSize(300, 300)

for i in range(0,360):
    time.sleep(0.1)
    coneActor2.RotateY(2)
    renWin.Render()
    #ren1.GetActiveCamera().Azimuth( 1 )
