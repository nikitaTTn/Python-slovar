from PyQt5.QtWidgets import *

class FinalWin(QWidget):
    def __init__(self, score):
        super().__init__()
        self.score = score
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle("Результаты теста по словарям")
        self.initUI()
        self.show()

    def initUI(self):
        layout = QVBoxLayout()

        dict_knowledge_text = "Отлично! Вы хорошо знаете словари в Python." if self.score["dict_knowledge"] > 3 else "Вам нужно подтянуть знания по словарям."

        dict_practice_text = "Вы отлично справляетесь с практическими задачами по словарям!" if self.score["dict_practice"] > 2 else "Практические навыки работы со словарями требуют улучшения."

        layout.addWidget(QLabel(dict_knowledge_text))
        layout.addWidget(QLabel(dict_practice_text))

        self.setLayout(layout)