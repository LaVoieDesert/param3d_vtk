#!/usr/bin/env python3
# coding: utf-8
#
# Christophe le Bourlot christophe.le-bourlot <> insa-lyon.fr
#

from vtk import *
import numpy as np


def param3d_split(
        file_name,
        voids_to_extract=None):

    # Read the source file.
    reader = vtkUnstructuredGridReader()
    reader.SetFileName(file_name)
    reader.Update() # Needed because of GetScalarRange
    
    output = reader.GetOutput()
    cell_data = output.GetCellData() #This contains just the cells data

    # get the first array: 'value'
    array0 = cell_data.GetArray(0)
    cells_per_array = set()                        # a set of values
    for i in range(output.GetNumberOfCells()):
        cells_per_array.add(array0.GetValue(i))
        
    if voids_to_extract is None:
        voids_to_extract = cells_per_array
    else:
        voids_to_extract = set(voids_to_extract)
    
    assert len(voids_to_extract) == len(voids_to_extract.intersection(cells_per_array))


    calculator = vtkArrayCalculator()
    calculator.SetFunction("1")
    calculator.SetResultArrayName('azerty')
    calculator.SetAttributeModeToUsePointData()
    calculator.SetInputData(output)
    calculator.Update()
    
    output2 = calculator.GetOutput()
    

    # prepare the threshold
    threshold = vtkThreshold()
    threshold.AddInputData(output2)
    threshold.SetInputArrayToProcess(0, 0, 0, vtkDataObject.FIELD_ASSOCIATION_CELLS, 0)
    
    # Prepare the writer
    writer = vtkUnstructuredGridWriter()
    writer.SetInputData(threshold.GetOutput())
    
    #acquisition_step = np.ones(output.GetNumberOfCells())
    #scalar3_array = util.numpy_support.numpy_to_vtk(acquisition_step)
    #scalar3_array.SetName('scalar3')
    #cell_data.AddArray(scalar3_array)



    print("Extracted voids ids: {}".format(voids_to_extract))
    # for each void, select the cells and create a new vtk file
    for value in voids_to_extract:

        # threshold the void
        threshold.ThresholdBetween(value, value)
        threshold.Update()

        # save the data
        writer.SetFileName("output/param3d_extract_void_{}.vtk".format(value))
        writer.Update()

if __name__ == "__main__":

    # The source file
    file_name = "ex/ex2_param3d.vtk"
    param3d_split(file_name)
    
    param3d_split(file_name, [114])
    

