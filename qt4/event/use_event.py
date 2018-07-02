#!/usr/bin/env python3
#-*- coding : utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore


class PixmapLabel(QtGui.QLabel):
    def __init__(self):
        super(PixmapLabel, self).__init__()
        self.point = None    

    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, event):
        self.point = event.pos()

    def mouseReleaseEvent(self, event):
        if self.point == event.pos():
            self.emit(QtCore.SIGNAL('clicked()'))


class MainWidget(QtGui.QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.setWindowTitle('use_event')
        self.resize(300, 300)

        self.vLayout = QtGui.QVBoxLayout(self)
        self.pixmapLabel = PixmapLabel()
        #self.pixmap = QtGui.QPixmap('/opt/VShare/FreshSalt.jpg')
        #self.pixmapLabel.setPixmap(self.pixmap)
        self.pixmapLabel.setText('Custom_Event')

        self.button = QtGui.QPushButton('Button')
        self.vLayout.addWidget(self.button)
        self.vLayout.addWidget(self.pixmapLabel)
        
        self.pixmapLabel.clicked.connect(self.custom_slot)

    @QtCore.pyqtSlot()
    def custom_slot(self):
        print('pixmap clicked !!!')

app = QtGui.QApplication( sys.argv )
mainWidget = MainWidget()
mainWidget.resize(300, 300)
mainWidget.show()
app.exec_()

