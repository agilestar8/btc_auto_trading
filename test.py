import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import pykorbit

ui = uic.loadUiType("design2.ui")[0]

class mywindow(QMainWindow,ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QApplication(sys.argv)
window = mywindow()
window.show()
app.exec_()
