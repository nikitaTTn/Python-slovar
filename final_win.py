from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class FinalWin(QWidget):
    def __init__(self, total_score, total_questions):
        super().__init__()
        self.setGeometry(100, 100, 300, 150)  
        self.setWindowTitle("Результаты теста")
        self.initUI(total_score, total_questions)

    def initUI(self, total_score, total_questions):
        layout = QVBoxLayout(self)
        result_label = QLabel(
            f"Ваш результат: {total_score} из {total_questions} баллов", self
        )
        layout.addWidget(result_label, alignment=Qt.AlignCenter)
        self.setLayout(layout)