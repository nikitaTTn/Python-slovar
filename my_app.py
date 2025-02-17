from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QInputDialog, QMessageBox
from PyQt5.QtCore import Qt
from theory_win import TheoryWin

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle("Тест по словарям в Python")
        self.user_info = {}  # Для хранения данных пользователя
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
        # Запрашиваем ФИО и группу
        name, ok1 = QInputDialog.getText(self, 'Ввод данных', 'Введите ваше ФИО:')
        group, ok2 = QInputDialog.getText(self, 'Ввод данных', 'Введите вашу группу:')
        
        if ok1 and ok2 and name and group:
            self.user_info['name'] = name
            self.user_info['group'] = group
            self.tw = TheoryWin(self.user_info)
            self.hide()
        else:
            QMessageBox.warning(self, 'Ошибка', 'Пожалуйста, введите ФИО и группу.')

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

app = QApplication([])
mw = MainWin()
app.exec_()