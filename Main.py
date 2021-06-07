import sys
import os
import vtk
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import pydicom
import glob
from vtk.util.misc import vtkGetDataRoot
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from partBb import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ##############################################################
        self.Slider = [self.ui.horizontalSlider , self.ui.horizontalSlider_2 , self.ui.horizontalSlider_3 , self.ui.horizontalSlider_4]
        self.ui.horizontalSlider.valueChanged.connect(lambda: self.slider_SLOT(0))
        self.ui.horizontalSlider_2.valueChanged.connect(lambda: self.slider_SLOT(1))
        self.ui.horizontalSlider_3.valueChanged.connect(lambda: self.slider_SLOT(2))
        self.ui.horizontalSlider_4.valueChanged.connect(lambda: self.slider_SLOT(3))
        self.ui.LoadDICOM.clicked.connect(lambda: self.Load_DICOM_Series())
        self.ui.comboBox.activated.connect(lambda: self.Rendering_Mode())
        # ##############################################################
        
        self.surfaceExtractor = vtk.vtkContourFilter()
        self.RenMD = 0
        self.Flag = False
        self.SliderChanged = False
        self.Edit_UI(0)

    def DICOM_SERIES_PATH(self):
        path = QFileDialog.getExistingDirectory(self, 'Choose DICOM Directory') + '/'
        self.Name = path.split('/')[-2]
        return path 
                
    def Load_DICOM_Series(self):
        print("H")
        self.Flag = True   

        # Read Dataset using vtkDICOMImageReader
        pathDicomDir = None  
        pathDicomDir = self.DICOM_SERIES_PATH()
        self.reader = vtk.vtkDICOMImageReader()
        self.reader.SetDirectoryName(pathDicomDir)
        self.reader.Update()

        if type(pathDicomDir) != 'NoneType':
            self.ui.label_9.setText(self.Name)
            self.Rendering_Mode()

    def Rendering_Mode(self):
        self.RenMD = self.ui.comboBox.currentIndex() 

        if self.RenMD == 1:
            self.Edit_UI(self.RenMD)
            self.Surface_Rendering()

        elif self.RenMD == 2:
            self.Edit_UI(self.RenMD)
            self.Ray_Casting_Rendering()
    
    def slider_SLOT(self , ID):
        val = self.Slider[ID].value()

        if ID == 0:
            self.iren = QVTKRenderWindowInteractor()
            self.surfaceExtractor.SetValue(0, val)
            self.iren.update()

        elif ID == 1:
            val = val/100.0
            self.SliderChanged = True
            print("Heba")
            print(val)
            self.iren = QVTKRenderWindowInteractor()
            volumecolor = vtk.vtkColorTransferFunction()
            # volumecolor.GetRedValue(val)
            # RemoveAllPoints()
            volumecolor.AddRGBPoint(0,    0.0, 0.0, 0.0)
            volumecolor.AddRGBPoint(500,  val, 0.5, 0.3)
            volumecolor.AddRGBPoint(1000, val, 0.5, 0.3)
            volumecolor.AddRGBPoint(1150, val, 1.0, 0.9) 

            volumeProperty = vtk.vtkVolumeProperty()
            volumeProperty.SetColor(volumecolor)
            volume = vtk.vtkVolume()
            volume.SetProperty(volumeProperty)
            self.iren.update() 
            self.Ray_Casting_Rendering()
            print("T")
            
        elif ID == 2:
            val = val/100.0
            print("Hebaaa")
            self.SliderChanged = True
            print(val)
            self.iren = QVTKRenderWindowInteractor()
            volumecolor = vtk.vtkColorTransferFunction()
            # volumecolor.GetGreenValue(val)
            # # RemoveAllPoints()
            volumecolor.AddRGBPoint(0,    0.0, 0.0, 0.0)
            volumecolor.AddRGBPoint(500,  1.0, val, 0.3)
            volumecolor.AddRGBPoint(1000, 1.0, val, 0.3)
            volumecolor.AddRGBPoint(1150, 1.0, 1.0, 0.9) 

            volumeProperty = vtk.vtkVolumeProperty()
            volumeProperty.SetColor(volumecolor)
            volume = vtk.vtkVolume()
            volume.SetProperty(volumeProperty)
            self.iren.update()
            # self.Ray_Casting_Rendering()
            print("k")
            
        elif ID == 3:
            val = val/100.0
            print("Bebo")
            self.SliderChanged = True
            print(val)
            self.iren = QVTKRenderWindowInteractor()
            volumecolor = vtk.vtkColorTransferFunction()
            # volumecolor.GetBlueValue (val)
            volumecolor.AddRGBPoint(0,    0.0, 0.0, 0.0)
            volumecolor.AddRGBPoint(500,  1.0, 0.5, val)
            volumecolor.AddRGBPoint(1000, 1.0, 0.5, val)
            volumecolor.AddRGBPoint(1150, 1.0, 1.0, 0.9)
            volumeProperty = vtk.vtkVolumeProperty()
            volumeProperty.SetColor(volumecolor)
            volume = vtk.vtkVolume()
            volume.SetProperty(volumeProperty)
            self.iren.update()
            # self.Ray_Casting_Rendering()
            print("A")
            

    #  Surface_Rendering Mode
    def Surface_Rendering(self):
        print("B")
        if self.Flag == True : 
            self.iren = QVTKRenderWindowInteractor()
            self.viewer = self.iren.GetRenderWindow()
            self.aRenderer = vtk.vtkRenderer()
            self.viewer.AddRenderer(self.aRenderer) 

            self.surfaceExtractor.SetInputConnection(self.reader.GetOutputPort())
            self.surfaceExtractor.SetValue(0, 500)
            self.surfaceNormals = vtk.vtkPolyDataNormals()
            self.surfaceNormals.SetInputConnection(self.surfaceExtractor.GetOutputPort())
            self.surfaceNormals.SetFeatureAngle(60.0)
            self.surfaceMapper = vtk.vtkPolyDataMapper()
            self.surfaceMapper.SetInputConnection(self.surfaceNormals.GetOutputPort())
            self.surfaceMapper.ScalarVisibilityOff()

            surface = vtk.vtkActor()
            surface.SetMapper(self.surfaceMapper)
        
            aCamera = vtk.vtkCamera()
            aCamera.SetViewUp(0, 0, -1)
            aCamera.SetPosition(0, 1, 0)
            aCamera.SetFocalPoint(0, 0, 0)
            aCamera.ComputeViewPlaneNormal()

            self.aRenderer.AddActor(surface)
            self.aRenderer.SetActiveCamera(aCamera)
            self.aRenderer.ResetCamera()
            aCamera.Dolly(1)

            self.aRenderer.SetBackground(0, 0, 0)
            self.viewer.SetSize(640, 480)
            self.aRenderer.ResetCameraClippingRange()

            self.iren.Initialize()
            self.viewer.Render()
            self.iren.Start()
            self.iren.show()
            print("E")
        
    # Ray Casting Rendering Mode
    def Ray_Casting_Rendering(self):
        if self.Flag == True and  self.SliderChanged == False:

            iren = QVTKRenderWindowInteractor()
            renWin = iren.GetRenderWindow()
            ren = vtk.vtkRenderer()
            renWin.AddRenderer(ren) 

            # # ren = vtk.vtkRenderer()
            # renWin = vtk.vtkRenderWindow()
            # renWin.AddRenderer(ren)
            # iren = vtk.vtkRenderWindowInteractor()
            # iren.SetRenderWindow(renWin)

            volumeMapper = vtk.vtkGPUVolumeRayCastMapper()
            volumeMapper.SetInputConnection(self.reader.GetOutputPort())
            volumeMapper.SetBlendModeToComposite()

            volumeColor = vtk.vtkColorTransferFunction()
            volumeColor.AddRGBPoint(0,    0.0, 0.0, 0.0)
            volumeColor.AddRGBPoint(500,  1.0, 0.5, 0.3)
            volumeColor.AddRGBPoint(1000, 1.0, 0.5, 0.3)
            volumeColor.AddRGBPoint(1150, 1.0, 1.0, 0.9)

            volumeScalarOpacity = vtk.vtkPiecewiseFunction()
            volumeScalarOpacity.AddPoint(0,    0.00)
            volumeScalarOpacity.AddPoint(500,  0.15)
            volumeScalarOpacity.AddPoint(1000, 0.15)
            volumeScalarOpacity.AddPoint(1150, 0.85)

            volumeGradientOpacity = vtk.vtkPiecewiseFunction()
            volumeGradientOpacity.AddPoint(0,   0.0)
            volumeGradientOpacity.AddPoint(90,  0.5)
            volumeGradientOpacity.AddPoint(100, 1.0)

            volumeProperty = vtk.vtkVolumeProperty()
            if self.SliderChanged == False:
                volumeProperty.SetColor(volumeColor)
            volumeProperty.SetScalarOpacity(volumeScalarOpacity)
            volumeProperty.SetGradientOpacity(volumeGradientOpacity)
            volumeProperty.SetInterpolationTypeToLinear()
            volumeProperty.ShadeOn()
            volumeProperty.SetAmbient(0.4)
            volumeProperty.SetDiffuse(0.6)
            volumeProperty.SetSpecular(0.2)
    
            volume = vtk.vtkVolume()
            volume.SetMapper(volumeMapper)
            volume.SetProperty(volumeProperty)

            ren.AddViewProp(volume)
            
            camera =  ren.GetActiveCamera()
            c = volume.GetCenter()
            camera.SetFocalPoint(c[0], c[1], c[2])
            camera.SetPosition(c[0] + 500, c[1], c[2])
            camera.SetViewUp(0, 0, -1)

            renWin.SetSize(640, 480)

            iren.Initialize()
            renWin.Render()
            iren.Start()
            iren.show()

    
    def Edit_UI (self , RenMD):
        if RenMD == 0:
            self.ui.horizontalSlider.hide()
            self.ui.horizontalSlider_2.hide()
            self.ui.horizontalSlider_3.hide()
            self.ui.horizontalSlider_4.hide()
            self.ui.label.hide()
            self.ui.label_2.hide()
            self.ui.label_3.hide()
            self.ui.label_4.hide()
            self.ui.label_5.hide()
            self.ui.label_6.hide()
            self.ui.label_7.hide()
            self.ui.label_8.hide()
            MainWindow.resize(self, 529, 100)

        if RenMD == 1:
            self.ui.horizontalSlider.show()
            self.ui.horizontalSlider_2.hide()
            self.ui.horizontalSlider_3.hide()
            self.ui.horizontalSlider_4.hide()
            self.ui.label.show()
            self.ui.label_2.show()
            self.ui.label_3.hide()
            self.ui.label_4.hide()
            self.ui.label_5.hide()
            self.ui.label_6.hide()
            self.ui.label_7.hide()
            self.ui.label_8.hide()
            MainWindow.resize(self, 529, 250)

        elif RenMD== 2:
            self.ui.horizontalSlider.hide()
            self.ui.horizontalSlider_2.show()
            self.ui.horizontalSlider_3.show()
            self.ui.horizontalSlider_4.show()
            self.ui.label.hide()
            self.ui.label_2.hide()
            self.ui.label_3.show()
            self.ui.label_4.show()
            self.ui.label_5.show()
            self.ui.label_6.show()
            self.ui.label_7.show()
            self.ui.label_8.show()
            MainWindow.resize(self, 529, 500)

def main():
    path = os.getcwd()
    os.chdir(path + '/data')
    directory = os.getcwd()
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
   

    
 # if(Heba != 0):
        #     self.viewer.Finalize()
        #     self.iren.TerminateApp()
        #     del self.viewer, self.iren