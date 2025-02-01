from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt
from theory_win import TheoryWin

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle("Тест по словарям в Python")
        self.initUI()
        self.connects()
        self.show()

    def initUI(self):
        self.btn_next = QPushButton("Начать обучение", self)
        self.hello_text = QLabel("Добро пожаловать на тест по словарям в Python!")
        self.instruction = QLabel("Этот тест поможет вам проверить свои знания по работе со словарями в Python.")

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.instruction, alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.btn_next, alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)

    def next_click(self):
        self.tw = TheoryWin()
        self.hide()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

app = QApplication([])
mw = MainWin()
app.exec_()