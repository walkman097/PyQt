#!/usr/bin/env python3
#-*- coding : utf-8 -*-


import sys
from PyQt4 import QtGui, QtCore


class MainWidget(QtGui.QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.setWindowTitle('SIGNAL')
        self.resize(200, 200)
        
        self.vLayout = QtGui.QVBoxLayout(self)
        self.button = QtGui.QPushButton('Signals')
        self.label = QtGui.QLabel('close') 
        self.vLayout.addWidget(self.button)
        self.vLayout.addWidget(self.label)
    
        self.connect(self.button, QtCore.SIGNAL('clicked()'), self, QtCore.SLOT('custom_slot()'))
        self.connect(self.button, QtCore.SIGNAL('clicked()'), self, QtCore.SLOT('custom_signals()'))
        self.connect(self, QtCore.SIGNAL('on_clicked()'), self, QtCore.SLOT('on_clicked_response()'))

        # custom signals
        self.connect(self.button, QtCore.SIGNAL('clicked()'), self, QtCore.SIGNAL('custom_clicked()'))
        self.connect(self, QtCore.SIGNAL('custom_clicked()'), self, QtCore.SLOT('on_clicked_response()'))
        
        # callback
        self.button.clicked.connect(self.custom_slot)
        self.button.clicked.connect(self.on_clicked_response)

    custom_clicked = QtCore.pyqtSignal()

    @QtCore.pyqtSlot()
    def custom_slot(self):
        self.label.setText('oh, my custom slot fuck')
        
    @QtCore.pyqtSlot()
    def custom_signals(self):
        self.emit(QtCore.SIGNAL('on_clicked()'))
        # test emit signals        

    @QtCore.pyqtSlot()
    def on_clicked_response(self):
        print('button clicked and emit signals')


app = QtGui.QApplication( sys.argv )
mainWidget = MainWidget()
mainWidget.show()
app.exec_()


