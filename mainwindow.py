# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(903, 811)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 1, 0, 1, 5)
        self.fileSelectBtn = QtWidgets.QPushButton(self.centralwidget)
        self.fileSelectBtn.setObjectName("fileSelectBtn")
        self.gridLayout.addWidget(self.fileSelectBtn, 0, 4, 1, 1)
        self.saveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.saveBtn.setObjectName("saveBtn")
        self.gridLayout.addWidget(self.saveBtn, 2, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.gammaSlider = QtWidgets.QSlider(self.centralwidget)
        self.gammaSlider.setMinimum(1)
        self.gammaSlider.setMaximum(10)
        self.gammaSlider.setOrientation(QtCore.Qt.Horizontal)
        self.gammaSlider.setObjectName("gammaSlider")
        self.gridLayout.addWidget(self.gammaSlider, 2, 1, 1, 2)
        self.gammaLcdNum = QtWidgets.QLCDNumber(self.centralwidget)
        self.gammaLcdNum.setMaximumSize(QtCore.QSize(100, 16777215))
        self.gammaLcdNum.setObjectName("gammaLcdNum")
        self.gridLayout.addWidget(self.gammaLcdNum, 2, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 4)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 903, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.fileSelectBtn.setText(_translate("MainWindow", "File"))
        self.saveBtn.setText(_translate("MainWindow", "Save"))
        self.label.setText(_translate("MainWindow", "Gamma"))

