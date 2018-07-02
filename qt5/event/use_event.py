#!/usr/bin/env python3
#-*- coding : utf-8 -*-


import sys
from PyQt5 import QtWidgets,QtCore


class Label(QtWidgets.QLabel):

    clicked = QtCore.pyqtSignal(int)

    def __init__(self):
        super(Label, self).__init__()
        self.resize(300, 300)
        self.setText('Hello, Qt')
        self.clicked.connect(self.custom_clicked)

        
    def mousePressEvent(self, event):
        self.point = event.pos()

    def mouseReleaseEvent(self, event):
        if event.pos() == self.point:
            print('label clicked !!!')
            self.clicked.emit(self.point.x())

    def custom_clicked(self, val):
        print('pos x is {}'.format(val))


app = QtWidgets.QApplication( sys.argv )
label = Label()
label.show()
app.exec_()


