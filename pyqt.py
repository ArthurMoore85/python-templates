"""
.. module: pyqt
.. description: Main controller file for managing a PyQt app.
.. author: Arthur Moore <arthur.moore85@gmail.com>
.. License: GPLv2
"""

from PyQt4 import QtGui, QtCore, QtWebKit
from PyQt4.QtCore import *
from mainWindow import Ui_MainWindow # Class of mainWindow UI python module.

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        """
        MainWindow class.
        This controls the UI for PyQt
        """
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        
        # The following can be used for multiple windows.
        self.window1 = None
        self.window2 = None
        self.window3 = None
        self.window4 = None


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
