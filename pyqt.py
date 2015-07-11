from PyQt4 import QtGui, QtCore, QtWebKit
from PyQt4.QtCore import *
from mainWindow import Ui_MainWindow # or what it says in module

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        """
        Some comment here
        """
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
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
