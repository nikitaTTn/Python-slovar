from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class FinalWin(QWidget):
    def __init__(self, total_score, total_questions, elapsed_time, user_info):
        super().__init__()
        self.user_info = user_info
        self.total_score = total_score
        self.total_questions = total_questions
        self.elapsed_time = elapsed_time
        self.setGeometry(100, 100, 300, 150)
        self.setWindowTitle("Результаты теста")
        self.initUI()
        self.save_results()

    def initUI(self):
        layout = QVBoxLayout(self)

        result_label = QLabel(f"Ваш результат: {self.total_score} из {self.total_questions} баллов", self)
        time_label = QLabel(f"Затраченное время: {self.elapsed_time} секунд", self)

        layout.addWidget(result_label, alignment=Qt.AlignCenter)
        layout.addWidget(time_label, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def save_results(self):
        with open("results.txt", "a") as file:
            file.write(f"{self.user_info['name']}, {self.user_info['group']}, {self.total_score}/{self.total_questions}, {self.elapsed_time} сек\n")