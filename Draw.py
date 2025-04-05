import vtk
def draw_3d(reader, segment, lower, upper, colors):
    select_tissue = vtk.vtkImageThreshold()
    select_tissue.SetInputConnection(reader.GetOutputPort())
    select_tissue.ThresholdBetween(lower, upper)
    select_tissue.SetInValue(1)
    select_tissue.SetOutValue(0)
    select_tissue.Update()

    tissueExtractor = vtk.vtkMarchingCubes()
    tissueExtractor.SetInputConnection(select_tissue.GetOutputPort())
    tissueExtractor.SetValue(0, 1)
    tissueExtractor.Update()

    #Wygładzenie
    smoother = vtk.vtkWindowedSincPolyDataFilter()
    smoother.SetInputConnection(tissueExtractor.GetOutputPort())
    smoother.SetNumberOfIterations(60)
    smoother.SetFeatureAngle(60.0)
    smoother.SetPassBand(0.001)
    smoother.NonManifoldSmoothingOn()
    smoother.Update()

    normals = vtk.vtkPolyDataNormals()
    normals.SetInputConnection(smoother.GetOutputPort())
    normals.SetFeatureAngle(60.0)

    #Optymalizacja
    tissueStripper = vtk.vtkStripper()
    tissueStripper.SetInputConnection(normals.GetOutputPort())
    tissueStripper.Update()

    tissueMapper = vtk.vtkPolyDataMapper()
    tissueMapper.SetInputConnection(tissueStripper.GetOutputPort())
    tissueMapper.ScalarVisibilityOff()

    tissue = vtk.vtkActor()
    tissue.SetMapper(tissueMapper)
    tissue.GetProperty().SetSpecular(.3)
    tissue.GetProperty().SetSpecularPower(20)

    rgba = [0.0, 0.0, 0.0, 0.0]
    colors.GetLookupTable().GetTableValue(segment, rgba)
    tissue.GetProperty().SetDiffuseColor(rgba[:3])

    return tissue