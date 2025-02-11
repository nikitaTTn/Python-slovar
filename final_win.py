from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class FinalWin(QWidget):
    def __init__(self, total_score, total_questions, elapsed_time):
        super().__init__()
        self.setGeometry(100, 100, 300, 150)
        self.setWindowTitle("Результаты теста")
        self.initUI(total_score, total_questions, elapsed_time)

    def initUI(self, total_score, total_questions, elapsed_time):
        layout = QVBoxLayout(self)

        result_label = QLabel(f"Ваш результат: {total_score} из {total_questions} баллов", self)
        time_label = QLabel(f"Затраченное время: {elapsed_time} секунд", self)

        layout.addWidget(result_label, alignment=Qt.AlignCenter)
        layout.addWidget(time_label, alignment=Qt.AlignCenter)

        self.setLayout(layout)