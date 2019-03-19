#!/usr/bin/env python3
# coding: utf-8
#
# Christophe le Bourlot christophe.le-bourlot <> insa-lyon.fr
#

from vtk import *


def param3d_split(
        file_name,
        voids_to_extract=None,
        generique_name=None):
    
    if generique_name is None:
        generique_name = "output/param3d_split_void_"

    # Read the source file.
    reader = vtkUnstructuredGridReader()
    reader.SetFileName(file_name)
    reader.Update() # Needed because of GetScalarRange
    output = reader.GetOutput()

    # prepare the threshold
    threshold = vtkThreshold()
    threshold.AddInputData(output)
    threshold.SetInputArrayToProcess(0, 0, 0, vtkDataObject.FIELD_ASSOCIATION_CELLS, 0)
    
    # Prepare the writer
    writer = vtkUnstructuredGridWriter()
    writer.SetInputData(threshold.GetOutput())

    # get the first array: 'value'
    array0 = output.GetCellData().GetArray(0)
    cells_per_array = set()                        # a set of values
    for i in range(output.GetNumberOfCells()):
        cells_per_array.add(array0.GetValue(i))
        
    if voids_to_extract is None:
        voids_to_extract = cells_per_array
    else:
        voids_to_extract = set(voids_to_extract)
    
    assert len(voids_to_extract) == len(voids_to_extract.intersection(cells_per_array))

    print("Extracted voids ids: {}".format(voids_to_extract))
    # for each void, select the cells and create a new vtk file
    for value in voids_to_extract:

        # threshold the void
        threshold.ThresholdBetween(value, value)
        threshold.Update()

        # save the data
        writer.SetFileName("{}{}.vtk".format(generique_name, value))
        writer.Update()

if __name__ == "__main__":

    # The source file
    file_name = "ex/ex2_param3d.vtk"
    param3d_split(file_name)
    
    param3d_split(file_name, [114])
    
    import glob
    fichiers = glob.glob("insitu/*.vtk")
    for i, fichier in enumerate(fichiers):
        param3d_split(fichier, generique_name="insitu/all_voids/step{}/void_".format(i))

