# Medical-data-viewer
This project is a simple medical data viewer where you can see the anatomy of the human knee. It is based on MRI scan data prepared using segmentation and 3D reconstruction algorithms. The purpose of the viewer is to visualize medical data for educational purposes.
The browser program was developed using Python version 3.10 and the VisualizationToolKit library version 9.4.1 Download the appropriate joint atlas from openanatomy.org knee (https://www.openanatomy.org/atlas-pages/atlas-spl-knee.html) and unpack the data into the created folder. After starting, the program will ask for paths to the 2 necessary files containing:
1) Radiological data from MRI scan - belongs from the created folder to which the atlas has been downloaded, go to the Data folder and copy the path to the file I.nrrd
2) Segmented data - also located in the Data folder under the name seg.nrrd
The authors of the atlas are Jen Richolt, Marianna Jakab and Ron Kikinis, it was developed in Boston at Harvard Medical School's Department of Radiology in 2015.

# Program construction
1. vtk_main

Objects from the VTK library are created, starting with a reader object to enable file loading, as well as basic components such as the renderer, render window, interactor, and color palettes used later in the program. Then, the user-visible objects are created: a bounding box in the form of a black wireframe cuboid, a grayscale cross-sectional plane, and colorful 3D solids. These solids are also stored in a dictionary to facilitate efficient program operation. Sliders are created to adjust the transparency of individual tissues. Each object is added to the renderer, the camera is configured, and the program begins execution.

2. draw_planes

The function returns 3 orthogonal planes. First, it takes the dimensions data and calculates coordinates, then creates 3 actor objects, maps data per actor, sets the color palette and coordinates.

3. bw_colors

The function builds its own color array using the class vtkLookupTable(). This is a grayscale color filter that then using vtkImageMapToColors() maps to the pixels of the loaded one image.

4. label_colors

It works in the same way as bw_colors, but uses the SetColor function from the VTK color classes to define custom colors by specifying their names and RGBA values. These colors are then assigned to labels (numerical identifiers) in the color table that correspond to the structure IDs in the data. As a result, the color palette is accurately matched to the dataset.

5. set_camera

Creates a camera object from the vtk library and sets the basics properties.

6. draw_3d

The function returns a 3D model of the specified tissue, based on the provided arguments: the previously created color palette, the segment number used to select the appropriate tissue color, and the lower and upper threshold values that define the segment range for the tissue. These thresholds are applied using a thresholding object. The tissue model is generated using the Marching Cubes algorithm, which creates a triangle mesh representing the isosurface. This mesh is then smoothed using a low-pass filter with a sinc function.

8. opacity_sliders

Slider objects are created, and their properties and positions are configured. Each slider is then associated with a widget and linked to the interactor. It is defined an additional callback function, which is used whenever the user changes a slider's value. This function is responsible for updating the transparency of the corresponding tissue.

# Results
![image](https://github.com/user-attachments/assets/1352be39-ee1c-4e4f-a467-2b5964da581a)
![image](https://github.com/user-attachments/assets/8bc18989-5277-4dad-801a-a299d97b93ce)
The view after launching the program. In the center, the generated 3D model of the knee joint is displayed. You can rotate the model using the mouse. On the right side of the screen are sliders - by moving them with the mouse, their values change, which in turn adjusts the transparency of individual tissues.

![image](https://github.com/user-attachments/assets/9fb66b99-c417-4abd-944e-000a8d73ffb4)
After setting the transparency of each tissue to 0, it is possible to view the planes with the MRI output images, which intersect the model through the center from each side. The individual tissues remain colored to make it easier to distinguish between different structures.




