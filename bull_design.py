import sys
from PyQt5.QtWidgets import * 
from PyQt5 import uic
from PyQt5.QtCore import *
import pybithumb

form = uic.loadUiType("bull.ui")[0]

tickers = ["BTC", "ETH", "BCH", "ETC"]

class mywindow(QMainWindow,form):
    def __init__(self):
        # 초기화 및 UI세팅
        super().__init__()
        self.setupUi(self)

        # table widget에 행 순서넣기
        self.tableWidget.setRowCount(len(tickers))

        # 3초 마다 event실행
        timer = QTimer(self)
        timer.start(3000)
        timer.timeout.connect(self.time_event)

    def time_event(self):
        # table에 화폐이름 갱신
        for i, ticker in enumerate(tickers):
            ticker_item = QTableWidgetItem(ticker)
            self.tableWidget.setItem(i, 0, ticker_item)

        # table에 가격,ma,상승/하락 갱신
            price, last_ma5, state = self.get_market_infos(ticker)
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(price)))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(last_ma5)))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(state))

    def get_market_infos(self, ticker):
        # df = pybithumb.get_ohlcv(ticker)
        df = pybithumb.get_candlestick(ticker)
        
        ma5 = df["close"].rolling(5).mean()
        last_ma5 = ma5[-2]
        price = pybithumb.get_current_price(ticker)

        state = None

        if price > last_ma5:
            state = "상승장"
        else:
            state = "하락장"

        return price,last_ma5,state


app = QApplication(sys.argv)
window = mywindow()
window.show()
app.exec_()





