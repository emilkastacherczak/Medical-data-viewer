import vtk
def set_camera(aRenderer, renWin):
    aCamera = vtk.vtkCamera()
    aCamera.SetViewUp(0, 0, -1)
    aCamera.SetPosition(0, -1, 0)
    aCamera.SetFocalPoint(0, 0, 0)
    aCamera.Azimuth(30.0)
    aCamera.Elevation(30.0)
    aRenderer.SetActiveCamera(aCamera)
    renWin.Render()
    aRenderer.ResetCamera()
    aCamera.Dolly(1.5) #zbliżenie kamery
    aRenderer.ResetCameraClippingRange()