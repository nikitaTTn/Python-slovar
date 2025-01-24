from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from second_win import TestWin

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle("Личностный тест Айзенка")
        self.initUI()
        self.connects()
        self.show()

    def initUI(self):
        self.btn_next = QPushButton("Начать тест", self)
        self.hello_text = QLabel("Добро пожаловать в личностный тест Айзенка!")
        self.instruction = QLabel("Этот тест поможет определить ваш уровень экстраверсии и нейротизма.")

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.instruction, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.setLayout(self.layout_line)

    def next_click(self):
        self.tw = TestWin()
        self.hide()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

app = QApplication([])
mw = MainWin()
app.exec_()