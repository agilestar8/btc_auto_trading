import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("design1.ui")[0]

class mywindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_event)

    def btn_event(self):
        print("버튼 클릭됨!")

app = QApplication(sys.argv)
window = mywindow()
window.show()
app.exec_()

