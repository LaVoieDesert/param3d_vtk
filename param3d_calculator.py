#!/usr/bin/env python3
# coding: utf-8
#
# Christophe le Bourlot christophe.le-bourlot <> insa-lyon.fr
#

from vtk import *


def param3d_show(file_name):

    # Read the source file.
    reader1 = vtkUnstructuredGridReader()
    reader1.SetFileName(file_name)
    reader1.Update()  # Needed because of GetScalarRange

    # add an array for color
    calculator_array1 = vtkArrayCalculator()
    calculator_array1.SetInputData(reader1.GetOutput())
    calculator_array1.SetAttributeModeToUsePointData()
    calculator_array1.SetFunction("1")
    calculator_array1.SetResultArrayName("label2")
    calculator_array1.Update()

    # Read the source file.
    reader2 = vtkUnstructuredGridReader()
    reader2.SetFileName(file_name)
    reader2.Update()  # Needed because of GetScalarRange

    # add an array for color
    calculator_array2 = vtkArrayCalculator()
    calculator_array2.SetInputData(reader2.GetOutput())
    calculator_array2.SetAttributeModeToUsePointData()
    calculator_array2.SetFunction("2")
    calculator_array2.SetResultArrayName("label2")
    calculator_array2.Update()

    # translate the structure
    calculator_coord = vtkArrayCalculator()
    calculator_coord.SetInputData(calculator_array2.GetOutput())
    calculator_coord.AddCoordinateVectorVariable("coords")
    calculator_coord.AddCoordinateScalarVariable("cX", 0)
    calculator_coord.AddCoordinateScalarVariable("cY", 1)
    calculator_coord.AddCoordinateScalarVariable("cZ", 2)
    calculator_coord.CoordinateResultsOn()

    calculator_coord.SetFunction("(cX+3)*iHat + (cY+3)*jHat + (cZ+3.5)*kHat")
    calculator_coord.Update()

    # Combine the two data sets
    appendFilter = vtk.vtkAppendFilter()
    appendFilter.AddInputData(calculator_array1.GetOutput())
    appendFilter.AddInputData(calculator_coord.GetOutput())
    appendFilter.Update()

    # save the data
    writer = vtkUnstructuredGridWriter()
    writer.SetFileName("output/param3d_merged_and_calculate.vtk")
    writer.SetInputData(appendFilter.GetOutput())
    writer.Update()

    # Create the mapper that corresponds the objects of the vtk file
    # into graphics elements
    mapper = vtkDataSetMapper()
    mapper.SetInputData(appendFilter.GetOutput())
    mapper.SetScalarRange(appendFilter.GetOutput().GetScalarRange())

    # Create the Actor
    actor = vtkActor()
    actor.SetMapper(mapper)

    # Create the Renderer
    renderer = vtkRenderer()
    renderer.AddActor(actor)
    renderer.SetBackground(1, 1, 1)  # Set background to white

    # Create the RendererWindow
    renderer_window = vtkRenderWindow()
    renderer_window.AddRenderer(renderer)

    # Create the RendererWindowInteractor and display the vtk_file
    interactor = vtkRenderWindowInteractor()
    interactor.SetRenderWindow(renderer_window)
    interactor.Initialize()
    interactor.Start()


if __name__ == "__main__":

    # The source file
    file_name = "ex/simple1.vtk"
    param3d_show(file_name)
