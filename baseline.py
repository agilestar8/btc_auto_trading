import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWinodw(QMainWindow):
    # 초기화 부분
    def __init__(self):
        super().__init__()      # PyQt클래스 상속 시 명시적으로 호출
        self.setGeometry(600,300,300,400)       # 윈도우 크기 변경
        self.setWindowTitle("Practice")         # 텍스트바 변경
        self.setWindowIcon(QIcon("d29fb659a2bab2170d4c159081f6b88f-star"))      # 아이콘 변경
        
        btn1 = QPushButton("button1", self) # 버튼 객체 생성
        btn1.move(5,10)                     # 버튼 위치 변경
        btn1.clicked.connect(self.btn_event)# 버튼 이벤트 발생 시 함수call

    # 이벤트 처리
    def btn_event(self):
        print("버튼이 클릭됐습니다")

app = QApplication(sys.argv)    # QApplication 객체 생성
window = MyWinodw()
window.show()
app.exec_()     # 이벤트 루프
