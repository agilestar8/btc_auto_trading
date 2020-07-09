import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import pykorbit

form_class = uic.loadUiType("design2.ui")[0]

class mywindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("코빗 시세 조회기")
        # self.pushButton.clicked.connect(self.inquiry_event)

        self.timer = QTimer(self)
        self.timer.start(1000)      # 1초 마다, interval = 1
        self.timer.timeout.connect(self.inquiry_event)
        
                # timeout이벤트는 interval마다 발생

    def inquiry_event(self):
        price = pykorbit.get_current_price("BTC")
        self.lineEdit.setText(str(price))

        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        self.statusBar().showMessage(str_time)
    

app = QApplication(sys.argv)
window = mywindow()
window.show()
app.exec_()


