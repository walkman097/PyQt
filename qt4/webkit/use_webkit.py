#!/usr/bin/env python3

import sys
from PyQt4 import QtGui, QtCore, QtWebKit


app = QtGui.QApplication( sys.argv )
webkit = QtWebKit.QWebView()
url = QtCore.QUrl('https://www.baidu.com/')
webkit.load(url)
webkit.show()
app.exec_()


