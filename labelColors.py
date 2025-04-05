import vtk
def label_colors(reader):
    labelLut = vtk.vtkLookupTable()
    labelLut.SetNumberOfColors(99)
    labelLut.SetTableRange(0, 98)
    labelLut.Build()

    colors = vtk.vtkNamedColors()
    colors.SetColor("tlo", [0, 0, 0, 0])
    colors.SetColor("miesnie", [230, 125, 125, 150])
    colors.SetColor("wiezadla", [255, 255, 255, 150])
    colors.SetColor("sciegna", [240, 220, 220, 150])
    colors.SetColor("nerwy", [245, 225, 16, 150])
    colors.SetColor("zyly", [41, 166, 255, 255])
    colors.SetColor("tetnice", [253, 99, 71, 150])
    colors.SetColor("lekotka", [235, 160, 205, 150])
    colors.SetColor("chrzastka", [180, 180, 255, 150])
    colors.SetColor("kosci", [197, 189, 177, 150])

    labelLut.SetTableValue(0, colors.GetColor4d('tlo')) #tło
    for label in range(1, 12): #tłuszcz
        labelLut.SetTableValue(label, colors.GetColor4d('tlo'))
    for label in range(12, 27): #mięśnie
        labelLut.SetTableValue(label, colors.GetColor4d('miesnie'))
    for label in range(31, 36): #więzadła
        labelLut.SetTableValue(label, colors.GetColor4d('wiezadla'))
    for label in range(41, 49):  #ścięgna
        labelLut.SetTableValue(label, colors.GetColor4d('sciegna'))
    for label in range(61, 65):  #nerwy
        labelLut.SetTableValue(label, colors.GetColor4d('nerwy'))
    for label in [72, 77, 78]:  #zyly
        labelLut.SetTableValue(label, colors.GetColor4d('zyly'))
    for label in [71, 73, 74, 75]:  #tetnice
        labelLut.SetTableValue(label, colors.GetColor4d('tetnice'))
    for label in range(81, 83):  #łękotka
        labelLut.SetTableValue(label, colors.GetColor4d('lekotka'))
    for label in range(83, 87):  #chrząstka
        labelLut.SetTableValue(label, colors.GetColor4d('chrzastka'))
    for label in range(95, 99):  #kości
        labelLut.SetTableValue(label, colors.GetColor4d('kosci'))

    segColors = vtk.vtkImageMapToColors()
    segColors.SetInputConnection(reader.GetOutputPort())
    segColors.SetLookupTable(labelLut)
    segColors.Update()
    return segColors