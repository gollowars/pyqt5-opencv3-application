import sys
import os
# qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from mainwindow import Ui_MainWindow as MainWindow
# opencv 
import cv2

import numpy as np

class MainWindow(QMainWindow, MainWindow):
  def __init__(self, parent=None, name=None, fl=0):
    QMainWindow.__init__(self, parent)
    self.setupUi(self)
    self.setup()
    self.addEvent()

  def setup(self):
    print('setup')
    self.fileDialog = QFileDialog()

    self.graphicsscene = QGraphicsScene()
    self.graphicsView.setScene(self.graphicsscene)


    self.image = None

    # gamma
    self.gammaValue = self.gammaSlider.value()
    self.gammaLcdNum.display(self.gammaValue)
    self.currentCvImage = None

  def addEvent(self):
    print('addEvent')
    self.fileSelectBtn.clicked.connect(self.fileSelectBtnClickHandler)
    self.lineEdit.textChanged.connect(self.lineEditChangeHandler)
    self.gammaSlider.valueChanged.connect(self.gammaValueChangedHandler)
    self.saveBtn.clicked.connect(self.saveBtnClickHandler)

  # file changed
  def fileSelectBtnClickHandler(self):
    print('clicked!')
    file = self.fileDialog.getOpenFileName(self, "Open file", os.path.expanduser('~') + '/home')
    if file[0]:
      self.lineEdit.setText(file[0])

  # lineEditChangeHandler
  def lineEditChangeHandler(self):
    self.opencPic(self.lineEdit.text())


  def opencPic(self, imgsrc):
    self.image = cv2.imread(imgsrc)
    # reset
    self.currentCvImage = None
    self.gammaSlider.setValue(1)

    self.currentCvImage = self.image.copy()
    pixmap = QPixmap(imgsrc)
    self.updateImage(pixmap)

  def updateImage(self, qpixmap):
    self.deleteSceneItems()
    viewWidth = self.graphicsView.frameGeometry().width()
    viewHeight = self.graphicsView.frameGeometry().height()
    
    pixRatioMap = qpixmap.scaled(viewWidth, viewHeight, Qt.KeepAspectRatio)
    pixItem = QGraphicsPixmapItem(pixRatioMap)
    self.graphicsscene.addItem(pixItem)
    self.graphicsscene.update()

  def deleteSceneItems(self):
    items = self.graphicsscene.items()
    for item in items:
      self.graphicsscene.removeItem(item)


  def gammaValueChangedHandler(self,value):
    self.gammaValue = value
    self.gammaLcdNum.display(value)

    if self.image != None:
      gammaImage = self.getGammaImage(self.image, self.gammaValue)
      self.currentCvImage = gammaImage
      pixmap = self.changeCvToQPixmap(gammaImage)
      self.updateImage(pixmap)

  def getGammaImage(self, cvImage, value):
    self.lookUpTable = np.ones((256,1), dtype='uint8')*0

    if value != 0:
      for i in range(256):
        self.lookUpTable[i][0] = 255 * pow(float(i) / 255, 1.0 / value)

    return cv2.LUT(cvImage, self.lookUpTable)

  def changeCvToQPixmap(self, cvImage):
    # 画像の高さ、幅を読み込み
    height, width, dim = cvImage.shape
    # 全ピクセル数
    bytesPerLine = dim * width
    # Opencv（numpy）画像をQtのQImageに変換
    qimg = QImage(cvImage.data, width, height, bytesPerLine, QImage.Format_RGB888)

    # QimageをQPixmapに変換
    return QPixmap.fromImage(qimg)


  def saveBtnClickHandler(self):
    if self.currentCvImage != None:
      file = self.fileDialog.getSaveFileName(self, "Save file", os.path.expanduser('~') + '/home')
      if file[0]:
        cv2.imwrite(file[0],self.currentCvImage)


if __name__ == "__main__":
  app = QApplication(sys.argv)
  w = MainWindow()
  w.show()
  sys.exit(app.exec_())
