import vtk
def opacity_sliders(aRenderer, interactor, tissues):
    sliders =[]
    y = 0.08

    for label, tissue in tissues.items():
        slider = vtk.vtkSliderRepresentation2D()
        slider.SetMinimumValue(0.0)
        slider.SetMaximumValue(1.0)
        slider.SetValue(1.0)
        slider.SetTitleText(label)
        #pozycja
        slider.GetTitleProperty().SetFontSize(10)
        slider.GetSliderProperty().SetColor(0.0, 0.0, 0.0)  # Kolor suwaka
        slider.GetLabelProperty().SetFontSize(12)
        slider.GetLabelProperty().SetColor(0.0, 0.0, 0.0)

        slider.GetPoint1Coordinate().SetCoordinateSystemToNormalizedDisplay()
        slider.GetPoint2Coordinate().SetCoordinateSystemToNormalizedDisplay()

        slider_widget = vtk.vtkSliderWidget()
        slider_widget.SetInteractor(interactor)
        slider_widget.SetRepresentation(slider)

        def callback(slider_wid, event, tissue=tissue):
            opacity = slider_wid.GetRepresentation().GetValue()
            tissue.GetProperty().SetOpacity(opacity)

        slider_widget.AddObserver("InteractionEvent", callback)
        slider_widget.GetRepresentation().GetPoint1Coordinate().SetValue(0.8, y)
        slider_widget.GetRepresentation().GetPoint2Coordinate().SetValue(1.0, y)
        slider_widget.EnabledOn()
        sliders.append(slider_widget)
        y += 0.09  # Przesunięcie kolejnego suwaka w dół

    return sliders