#!/usr/bin/env python3
#-*- coding : utf-8 -*-

import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

widget = QtGui.QLabel()
widget.setText('Hello world')
widget.resize(250, 150)
widget.setWindowTitle('simple')
widget.show()

sys.exit(app.exec_())
