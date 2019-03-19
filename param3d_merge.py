#!/usr/bin/env python3
# coding: utf-8
#
# Christophe le Bourlot christophe.le-bourlot <> insa-lyon.fr
#

from vtk import *


def param3d_show(
        files_name,
        output_file_name=None):
    
    if output_file_name is None:
        output_file_name = "output/param3d_merge_ex1and2.vtk"
    
    # Combine the two data sets
    appendFilter = vtk.vtkAppendFilter()
    
    for file_name in files_name:

        # Read the source file.
        reader = vtkUnstructuredGridReader()
        reader.SetFileName(file_name)
        reader.Update() # Needed because of GetScalarRange
        
        appendFilter.AddInputData(reader.GetOutput())
        
    appendFilter.Update()
    
    # save the data
    writer = vtkUnstructuredGridWriter()
    writer.SetFileName(output_file_name)
    writer.SetInputData(appendFilter.GetOutput())
    writer.Update()

if __name__ == "__main__":
    
    # The source file
    file_name1 = "ex/ex1_param3d.vtk"
    file_name2 = "ex/ex2_param3d.vtk"
    param3d_show([file_name1, file_name2])