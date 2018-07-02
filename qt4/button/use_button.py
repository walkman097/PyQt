#!/usr/bin/env pyton3
#-*- coding : utf-8 -*-


import sys
from PyQt4 import QtGui, QtCore


class MainWidget(QtGui.QWidget):
        
    count = -1 # 意味着是静态变量

    def __init__(self):
        super(MainWidget, self).__init__()
        self.setWindowTitle('doTestButton')
        self.resize(300, 300)

        self.vLayout = QtGui.QVBoxLayout(self)  # 类的内部变量
        self.button = QtGui.QPushButton('Close')
        self.label = QtGui.QLabel('Show')
        self.vLayout.addWidget(self.button)
        self.vLayout.addWidget(self.label)

        MainWidget.count = 0
        #self.connect(self.button, QtCore.SIGNAL('clicked()'), app, QtCore.SLOT('quit()'))
        self.connect(self.button, QtCore.SIGNAL('clicked()'), self.showMsg)
    
    def showMsg(self):
        self.label.setText('Close')
        print('count is {}'.format(MainWidget.count))
        app.quit()


app = QtGui.QApplication( sys.argv )
mainWidget = MainWidget()
mainWidget.show()
app.exec_()


