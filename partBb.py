# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'partBb.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(529, 474)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 489, 421))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.LoadDICOM = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.LoadDICOM.setObjectName("LoadDICOM")
        self.gridLayout.addWidget(self.LoadDICOM, 2, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 3, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 10, 2, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(self.gridLayoutWidget)
        self.horizontalSlider.setMaximum(2000)
        self.horizontalSlider.setSingleStep(100)
        self.horizontalSlider.setPageStep(100)
        self.horizontalSlider.setSliderPosition(500)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_2.addWidget(self.horizontalSlider, 3, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 12, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 9, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 8, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 13, 2, 1, 1)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.gridLayoutWidget)
        self.horizontalSlider_2.setMaximum(100)
        self.horizontalSlider_2.setProperty("value", 100)
        self.horizontalSlider_2.setSliderPosition(100)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.gridLayout_2.addWidget(self.horizontalSlider_2, 6, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 5, 2, 1, 1)
        self.horizontalSlider_4 = QtWidgets.QSlider(self.gridLayoutWidget)
        self.horizontalSlider_4.setMaximum(100)
        self.horizontalSlider_4.setSliderPosition(30)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.gridLayout_2.addWidget(self.horizontalSlider_4, 12, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 3, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 11, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 7, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 4, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 6, 3, 1, 1)
        self.horizontalSlider_3 = QtWidgets.QSlider(self.gridLayoutWidget)
        self.horizontalSlider_3.setMaximum(100)
        self.horizontalSlider_3.setSliderPosition(50)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.gridLayout_2.addWidget(self.horizontalSlider_3, 9, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 5, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 529, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.horizontalSlider_3.valueChanged['int'].connect(self.label_7.setNum)
        self.horizontalSlider_2.valueChanged['int'].connect(self.label_6.setNum)
        self.horizontalSlider.valueChanged['int'].connect(self.label.setNum)
        self.horizontalSlider_4.valueChanged['int'].connect(self.label_8.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DICOM Viewer"))
        self.LoadDICOM.setText(_translate("MainWindow", "Load DICOM            "))
        self.comboBox.setItemText(0, _translate("MainWindow", "                                         Choose Rendering Mode"))
        self.comboBox.setItemText(1, _translate("MainWindow", "                                              Surface Rendering"))
        self.comboBox.setItemText(2, _translate("MainWindow", "                                                    Ray Casting"))
        self.label_8.setText(_translate("MainWindow", "30"))
        self.label_7.setText(_translate("MainWindow", "50"))
        self.label_4.setText(_translate("MainWindow", "Green Compnent"))
        self.label_3.setText(_translate("MainWindow", "Red Compnent"))
        self.label.setText(_translate("MainWindow", "500"))
        self.label_5.setText(_translate("MainWindow", "Blue Compnent"))
        self.label_2.setText(_translate("MainWindow", "Iso Value"))
        self.label_6.setText(_translate("MainWindow", "100"))
        self.label_9.setText(_translate("MainWindow", "                                                  "))
