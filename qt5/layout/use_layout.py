#!/usr/bin/env python3
#-*- coding : utf-8 -*-


import sys
from PyQt5 import QtWidgets,QtCore


class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.resize(400, 400)
        
        self.vLayout = QtWidgets.QVBoxLayout(self)
        self.label = QtWidgets.QLabel('Hello, Qt5')
        self.vLayout.addWidget(self.label)


app = QtWidgets.QApplication( sys.argv )
mainWidget = MainWidget()
mainWidget.show()
app.exec_()

