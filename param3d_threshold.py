#!/usr/bin/env python3
# coding: utf-8
#
# Christophe le Bourlot christophe.le-bourlot <> insa-lyon.fr
#

from vtk import *


def param3D_threshold(
        file_name,
        threshold):
    
    reader = vtkUnstructuredGridReader()
    reader.SetFileName(file_name)
    reader.Update()
    output = reader.GetOutput()



    toto = vtkThreshold()
    toto.AddInputData(output)
    toto.ThresholdBetween(threshold, threshold)

    toto.SetInputArrayToProcess(0, 0, 0, vtkDataObject.FIELD_ASSOCIATION_CELLS, 0)
    toto.Update()



    output = toto.GetOutput()
    scalar_range = output.GetScalarRange()


    # Create the mapper that corresponds the objects of the vtk file
    # into graphics elements
    mapper = vtkDataSetMapper()
    mapper.SetInputData(output)
    mapper.SetScalarRange(scalar_range)

    # Create the Actor
    actor = vtkActor()
    actor.SetMapper(mapper)

    # Create the Renderer
    renderer = vtkRenderer()
    renderer.AddActor(actor)
    renderer.SetBackground(1, 1, 1) # Set background to white

    # Create the RendererWindow
    renderer_window = vtkRenderWindow()
    renderer_window.AddRenderer(renderer)

    # Create the RendererWindowInteractor and display the vtk_file
    interactor = vtkRenderWindowInteractor()
    interactor.SetRenderWindow(renderer_window)
    interactor.Initialize()
    interactor.Start()


if __name__ == "__main__":
    file_name = "ex/ex2_param3d.vtk"
    param3D_threshold(file_name, 114)