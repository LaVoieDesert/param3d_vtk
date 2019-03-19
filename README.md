# param3d_vtk
python vtk example files for vtk data manipulation

[![pythvers](https://img.shields.io/badge/python-2.7%7C3.6-brightgreen.svg)]

The repository contains examples files in the 'ex' and the 'insitu' directory, and a bunch of simple python files to expose some usage of vtk function, 'open', 'manipulate', 'visualize' and 'save' vtk files.

## VTK object used

 * vtkUnstructuredGridReader => read VTK data
 * vtkUnstructuredGridWriter => write VTK data
 * vtkArrayCalculator
 * vtkAppendFilter
 * vtkThreshold

## examples files

### param3d_info.py
Read data and look at the different array cell information

 * vtkUnstructuredGridReader

### param3d_visualize.py
Read and visualize data

Read VTK data
 
 * vtkUnstructuredGridReader
 
Visualization
 
 * vtkDataSetMapper
 * vtkActor
 * vtkRenderer
 * vtkRenderWindow
 * vtkRenderWindowInteractor
 
### param3d_merge.py
Read a list of files, and merge then in a single one

 * vtkUnstructuredGridReader
 * vtkAppendFilter
 * vtkUnstructuredGridWriter
 
### param3d_calculator.py
Read a simple file, copy and translate the cells while adding a new array (with 2 different values for color visualization).
The calcultator is used twice: i) to add an array, ii) to translate the cell (change the coordinates)

 * vtkUnstructuredGridReader
 * vtkArrayCalculator
 * vtkAppendFilter
 * vtkUnstructuredGridWriter
 * => visualization

### param3d_split.py
The example file contains 2 cells with a 'label' array containing a single value per array. The Threshold is used to extract and save each cell.

 * vtkUnstructuredGridReader
 * vtkThreshold
 * vtkUnstructuredGridWriter

### param3d_threshold.py
The example file contains 2 cells with a 'label' array containing a single value per array. The Threshold is used to extract visualize a one of them.

 * vtkUnstructuredGridReader
 * vtkThreshold
 * => visualization

### param3d_extract2.py
Extract cells from an example file and add data as a new array before saving it.

 * vtkUnstructuredGridReader
 * vtkArrayCalculator
 * vtkThreshold
 * vtkUnstructuredGridWriter

