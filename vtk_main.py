import vtk
from planes import draw_planes
from bwColors import bw_colors
from labelColors import label_colors
from Camera import set_camera
from Draw import draw_3d
from Sliders import opacity_sliders

def main():
    raw_nrrd_path = input("Podaj ścieżkę do pliku z danymi radiologicznymi(I.nrrd):")
    seg_nrrd_path = input("Podaj ścieżkę do pliku z danymi segmentacji(seg.nrrd):")

#creating an object that reads photos
    my_raw_nrrd_reader = vtk.vtkNrrdReader()
    seg_nrrd_reader = vtk.vtkNrrdReader()

#reading photos
    my_raw_nrrd_reader.SetFileName(raw_nrrd_path)
    raw_nrrd_reader = vtk.vtkImageFlip()
    raw_nrrd_reader.SetInputConnection(my_raw_nrrd_reader.GetOutputPort())
    raw_nrrd_reader.SetFilteredAxes(1)
    raw_nrrd_reader.Update()

    seg_nrrd_reader.SetFileName(seg_nrrd_path)
    seg_nrrd_reader.Update()

#setting colours
    colors = vtk.vtkNamedColors()
    colors.SetColor("BkgColor", [240, 200, 220, 255]) #RGB i przezroczystosc
    bwColors = bw_colors(raw_nrrd_reader)
    segColors = label_colors(seg_nrrd_reader)

#Creating a renderer, window and interactor
    aRenderer = vtk.vtkRenderer()
    renWin = vtk.vtkRenderWindow()
    renWin.AddRenderer(aRenderer)
    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    interactorStyle = vtk.vtkInteractorStyleTrackballCamera()
    iren.SetInteractorStyle(interactorStyle)

    aRenderer.SetBackground(colors.GetColor3d("BkgColor"))
    renWin.SetSize(640, 480)

#Data size outline - black cuboid
    outlineData = vtk.vtkOutlineFilter()
    outlineData.SetInputConnection(seg_nrrd_reader.GetOutputPort())
    outlineData.Update()
    mapOutline = vtk.vtkPolyDataMapper()
    mapOutline.SetInputConnection(outlineData.GetOutputPort())
    outline = vtk.vtkActor()
    outline.SetMapper(mapOutline)
    outline.GetProperty().SetColor(colors.GetColor3d("Black"))

#Planes
    raw_sagittal, raw_axial, raw_coronal = draw_planes(raw_nrrd_reader, bwColors)
    seg_sagittal, seg_axial, seg_coronal = draw_planes(seg_nrrd_reader, segColors)
    seg_sagittal2, seg_axial2, seg_coronal2 = draw_planes(seg_nrrd_reader, segColors)

    raw_sagittal.SetPosition(0, 140.5, 0)
    raw_axial.SetPosition(0, 140.5, 0)
    raw_coronal.SetPosition(0, 140.5, 0)
    seg_sagittal2.SetPosition(1, 0, 0)
    seg_axial2.SetPosition(0, -2, 0)
    seg_coronal2.SetPosition(0, 0, -1)

#3D tissues
    miesnie = draw_3d(seg_nrrd_reader,12,  12, 26, segColors)
    wiezadla = draw_3d(seg_nrrd_reader, 31, 31, 36, segColors)
    sciegna = draw_3d(seg_nrrd_reader, 41, 41, 49, segColors)
    nerwy = draw_3d(seg_nrrd_reader, 61, 61, 65, segColors)
    zyla_podkolanowa = draw_3d(seg_nrrd_reader, 72, 72, 72, segColors)
    zyly = draw_3d(seg_nrrd_reader, 77, 77, 78, segColors)
    tetnica_podkolanowa = draw_3d(seg_nrrd_reader, 71, 71, 71, segColors)
    tetnice = draw_3d(seg_nrrd_reader, 73, 73, 74, segColors)
    lekotka = draw_3d(seg_nrrd_reader, 81, 81, 83, segColors)
    chrzastka = draw_3d(seg_nrrd_reader, 83, 83, 87, segColors)
    kosci = draw_3d(seg_nrrd_reader,95,  95, 99, segColors)

#Saving tissues in a dictionary
    tkanki = {
        "mięśnie": miesnie,
        "więzadła": wiezadla,
        "ścięgna": sciegna,
        "nerwy": nerwy,
        "żyła podkolanowa": zyla_podkolanowa,
        "żyły": zyly,
        "tętnica podkolanowa": tetnica_podkolanowa,
        "tetnice": tetnice,
        "łękotka": lekotka,
        "chrząstka": chrzastka,
        "kości": kosci
    }

#Creating tissue transparency sliders
    sliders = opacity_sliders(aRenderer, iren, tkanki)

#Adding actors to renderer
    aRenderer.AddActor(outline)
    aRenderer.AddActor(raw_sagittal)
    aRenderer.AddActor(raw_axial)
    aRenderer.AddActor(raw_coronal)
    aRenderer.AddActor(seg_sagittal)
    aRenderer.AddActor(seg_axial)
    aRenderer.AddActor(seg_coronal)
    aRenderer.AddActor(seg_sagittal2)
    aRenderer.AddActor(seg_axial2)
    aRenderer.AddActor(seg_coronal2)
    for tkanka in tkanki.values():
        aRenderer.AddActor(tkanka)

#Setting camera
    set_camera(aRenderer, renWin)
    aCamera = vtk.vtkCamera()
    aCamera.SetViewUp(0, 0, -1)
    aCamera.SetPosition(0, -1, 0)
    aCamera.SetFocalPoint(0, 0, 0)
    aCamera.ComputeViewPlaneNormal()
    aCamera.Azimuth(30.0)
    aCamera.Elevation(30.0)
    aRenderer.SetActiveCamera(aCamera)
    renWin.Render()
    aRenderer.ResetCamera()
    aCamera.Dolly(1.5)
    aRenderer.ResetCameraClippingRange()
    aRenderer.ResetCamera()
    aRenderer.ResetCameraClippingRange()

#Interaction
    renWin.Render()
    iren.Initialize()
    iren.Start()

main()
