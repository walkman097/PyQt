#!/usr/bin/env python3
#-*- coding : utf-8 -*-

import sys
from PyQt5 import QtCore, QtWidgets

class Command(QtCore.QObject):

    timeout = QtCore.pyqtSignal()

    def __init__(self):
        super(Command, self).__init__()
        print('Command init ...')
        self.timeout.connect(self.timeoutSlot)

    def timeoutSlot(self):
        print('Command execute timeout ...')
        app.quit()

    def execute(self):
        QtCore.QTimer.singleShot(3000, self.timeout.emit)
    

app = QtWidgets.QApplication( sys.argv )
command = Command()
command.execute()
app.exit(app.exec_())

