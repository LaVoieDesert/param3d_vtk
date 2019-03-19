#!/usr/bin/env python3
# coding: utf-8
#
# Christophe le Bourlot christophe.le-bourlot <> insa-lyon.fr
#

from vtk import *

# The source file
file_name = "ex/ex2_param3d.vtk"

# Read the source file.
reader = vtkUnstructuredGridReader()
reader.SetFileName(file_name)
reader.Update() # Needed because of GetScalarRange
output = reader.GetOutput()

scalar_range = output.GetScalarRange()
nb_of_cells = output.GetNumberOfCells()

print("scalar_range: {}".format(scalar_range))
print("nb_of_cells: {}".format(nb_of_cells))


celldata = output.GetCellData()
nb_of_CellData = celldata.GetNumberOfArrays()
for i in range(nb_of_CellData):
    print(" _ CELL_DATA({: 2d})-> \"{}\"".format(i, celldata.GetArrayName(i)))

    
array0 = celldata.GetArray(0)
array0.GetNumberOfValues()
array0_values = []
for i in range(array0.GetNumberOfValues()):
    array0_values.append(array0.GetValue(i))
#print(array0_values)

voids_ids = set(array0_values)
nb_of_voids = len(voids_ids)

print("Nb of voids: {}".format(nb_of_voids))
print("Voids ids: {}".format(voids_ids))
    
    
    
    
celldata.GetArrayName(1)

