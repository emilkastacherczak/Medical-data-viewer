import vtk
def bw_colors(reader):
    bwLut = vtk.vtkLookupTable()
    bwLut.SetTableRange(0, 2000)
    bwLut.SetSaturationRange(0, 0)
    bwLut.SetHueRange(0, 0)
    bwLut.SetValueRange(0, 1)
    bwLut.Build()
    Colors = vtk.vtkImageMapToColors()
    Colors.SetInputConnection(reader.GetOutputPort())
    Colors.SetLookupTable(bwLut)
    Colors.Update()
    return Colors