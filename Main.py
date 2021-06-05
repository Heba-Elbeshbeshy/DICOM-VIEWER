import sys
import os
import vtk
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import pydicom
import glob
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from partB import Ui_MainWindow



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
       # ##############################################################
        self.Slider =[self.ui.verticalSlider , self.ui.verticalSlider_2]
        ##############################################################

       # LoadButton , verticalSlider , verticalSlider_2 , comboBox , label , label_2 , openGLWidget ,  openGLWidget_2 
        ##############################################################
        self.ui.verticalSlider.valueChanged.connect(lambda: self.slider_SLOT(0))
        self.ui.verticalSlider_2.valueChanged.connect(lambda: self.slider_SLOT(1))
        self.ui.LoadDICOM.clicked.connect(lambda: self.Load_DICOM_Series())
        # self.ui.comboBox.activated.connect()
        # ##############################################################
        self.iren = QVTKRenderWindowInteractor()
        self.surfaceExtractor = vtk.vtkContourFilter()

    def DICOM_SERIES_PATH(self):
        # shyla path el folder nafso 
        path = QFileDialog.getExistingDirectory(self, 'Choose DICOM Directory') + '/'
        # f de array shayl kol el paths bta3t el swar ely gwa el folder
        f = glob.glob(rf'{path}/*.dcm')
        # slices = [pydicom.read_file(s, force=True) for s in f] // baianaat om el patient w elsora bd5loni f tafsel malesh da3wa beha leh bgdd :"
        print(path)
        return path 
    

    def slider_SLOT(self , ID):
        val = self.Slider[ID].value()
        # print(val, ID)
        self.surfaceExtractor.SetValue(0, val)
        self.iren.update()
            
    def Load_DICOM_Series(self):
        print("H")
        # self.ui.openGLWidget_2
        viewer = self.iren.GetRenderWindow()
        aRenderer = vtk.vtkRenderer()
        viewer.AddRenderer(aRenderer)

        # Read Dataset using vtkDICOMImageReader
        pathDicomDir = self.DICOM_SERIES_PATH()
        print(pathDicomDir)
        self.reader = vtk.vtkDICOMImageReader()
        self.reader.SetDirectoryName(pathDicomDir)
        self.reader.Update()

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

        aRenderer.AddActor(surface)
        aRenderer.SetActiveCamera(aCamera)
        aRenderer.ResetCamera()
        aCamera.Dolly(1)

        aRenderer.SetBackground(0, 0, 0)
        viewer.SetSize(640, 480)
        aRenderer.ResetCameraClippingRange()

        self.iren.Initialize()
        viewer.Render()
        self.iren.Start()
        self.iren.show()
        print("E")


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
   

    
