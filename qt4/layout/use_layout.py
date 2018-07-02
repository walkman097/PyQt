#!/usr/bin/env python3
#-*- coding : utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore


class MainWidget(QtGui.QWidget):
    """
    def __init__(self):
        super(MainWidget, self).__init__() #初始化父类
        self.setWindowTitle('VBoxLayout')
        self.resize(150, 150)
        
        vLayout = QtGui.QVBoxLayout(self)
        titleLabel = QtGui.QLabel('Title')
        contentLabel = QtGui.QLabel('Content')

        vLayout.addWidget(titleLabel)
        vLayout.addWidget(contentLabel)

        self.setLayout(vLayout)
    """
    """
    def __init__(self):
        super(MainWidget, self).__init__()
        self.setWindowTitle('HBoxLayout')
        self.resize(150, 150)
        
        hLayout = QtGui.QHBoxLayout(self)
        titleLabel = QtGui.QLabel('Title')
        contentLabel = QtGui.QLabel('Content')

        hLayout.addWidget(titleLabel)
        hLayout.addWidget(contentLabel)
    """
    def __init__(self):
        super(MainWidget, self).__init__()
        self.setWindowTitle('GridLayout')
        self.resize(400, 400)
        
        glayout = QtGui.QGridLayout(self)
        count = 0
        while count < 10:
            label = QtGui.QLabel('Title' + str(count))
            row = count / 3
            col = count % 3
            glayout.addWidget(label, row, col)
            count += 1


app = QtGui.QApplication(sys.argv)
mainWidget = MainWidget()
mainWidget.show()
app.exec_()


