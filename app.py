import sys
# qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from mainwindow import Ui_MainWindow as MainWindow
# opencv 
import cv2

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

  def addEvent(self):
    print('addEvent')
    self.fileSelectBtn.clicked.connect(self.fileSelectBtnClickHandler)
    self.lineEdit.textChanged.connect(self.changeFileHandler)


  def fileSelectBtnClickHandler(self):
    print('clicked!')
    file = self.fileDialog.getOpenFileName(self, "Open file", "/home")
    if file[0]:
      self.lineEdit.setText(file[0])

  def changeFileHandler(self):
    self.opencPic(self.lineEdit.text())

  def opencPic(self, imgsrc):
    items = self.graphicsscene.items()
    for item in items:
      self.graphicsscene.removeItem(item)

    viewWidth = self.graphicsView.frameGeometry().width()
    viewHeight = self.graphicsView.frameGeometry().height()
    
    pixmap = QPixmap(imgsrc)
    pixRatioMap = pixmap.scaled(viewWidth, viewHeight, Qt.KeepAspectRatio)
    pixItem = QGraphicsPixmapItem(pixRatioMap)
    self.graphicsscene.addItem(pixItem)
    self.graphicsscene.update()



if __name__ == "__main__":
  app = QApplication(sys.argv)
  w = MainWindow()
  w.show()
  sys.exit(app.exec_())
