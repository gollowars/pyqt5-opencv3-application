# opencv3 + PyQt5 サンプル

# require
```
pyqt5
pyinstaller
opencv3
numpy
```

qtのインストールとか => [Python QTアプリ Standalone App化メモ](http://qiita.com/gollowars/items/387d5fecd29c26cace99)
opencv3をいれる。=> [https://github.com/gollowars/install-opencv3-python-osx/blob/master/install-opencv3-python3-osx.sh](https://github.com/gollowars/install-opencv3-python-osx/blob/master/install-opencv3-python3-osx.sh)

```
brew install qt5
```
するとQtDesignerが手に入る。
QtDeisgnerでuiつくって


```
pyuic5 mywidgets.ui -o mywidgest.py
```
で利用出来る。


### reference
  - [OpenCVで取得した画像をPySideで表示する](http://code.tiblab.net/python/opencv/pyside_window)
  - [7.5 QPixmapからQImageへの変換とファイルへの保存](http://spica00.style.coocan.jp/qt/qtPrg3_splite/splitt_saveact/prgtoolbox_qt2Prg3spl_sam5.html)
  - [PyQt(PySide)で画像処理その3（OpenCVとの連携）](http://tatabox.hatenablog.com/entry/2014/09/02/185727)