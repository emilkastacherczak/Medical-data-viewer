import vtk
#Funkcja do utworzenia 3 ortogonalnych plaszczyzn ze zdjec CT
def draw_planes(reader, Colors):
    #Pobranie wymiarów
    [xmin, xmax, ymin, ymax, zmin, zmax] = reader.GetOutput().GetExtent()
    x_center = (xmin + xmax) // 2
    y_center = (ymin + ymax) // 2
    z_center = (zmin + zmax) // 2

    #1 plaszczyzna
    sagittal = vtk.vtkImageActor()
    sagittal.GetMapper().SetInputConnection(Colors.GetOutputPort())
    sagittal.SetDisplayExtent(x_center, x_center, ymin, ymax, zmin, zmax)


    #2 plaszczyzna
    axial = vtk.vtkImageActor()
    axial.GetMapper().SetInputConnection(Colors.GetOutputPort())
    axial.SetDisplayExtent(xmin, xmax, y_center, y_center, zmin, zmax)

    #3plaszczyzna
    coronal = vtk.vtkImageActor()
    coronal.GetMapper().SetInputConnection(Colors.GetOutputPort())
    coronal.SetDisplayExtent(xmin, xmax, ymin, ymax, z_center, z_center)

    return sagittal, axial, coronal