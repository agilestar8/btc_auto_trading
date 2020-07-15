import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import pykorbit

ui = uic.loadUiType("design1.ui")[0]

class mywindow(QMainWindow,ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 버튼 이벤트
        self.pushButton.clicked.connect(self.btn_click)
        
        # timer객체
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.time_table)

    def time_table(self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        self.statusBar().showMessage(str_time)

    def btn_click(self):
        btc_price = pykorbit.get_current_price("BTC")
        self.lineEdit.setText(str(btc_price))

app = QApplication(sys.argv)
window = mywindow()
window.show()
app.exec_()
