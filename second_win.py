from PyQt5.QtWidgets import *

from PyQt5.QtCore import Qt
from inst import *
from final_win import FinalWin

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle(txt_title)
        self.initUI()
        self.connects()
        self.show()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.question_index = 0
        self.score = {"extroversion": 0, "neuroticism": 0}
        self.question_label = QLabel(questions[self.question_index]["text"])
        self.layout.addWidget(self.question_label, alignment = Qt.AlignCenter)

        self.answer_group = QButtonGroup(self)
        self.answer_yes = QRadioButton(txt_yes)
        self.answer_no = QRadioButton(txt_no)
        self.answer_group.addButton(self.answer_yes)
        self.answer_group.addButton(self.answer_no)
        self.layout.addWidget(self.answer_yes, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.answer_no, alignment = Qt.AlignCenter)

        self.btn_next = QPushButton(txt_next_question)
        self.layout.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)

    def connects(self):
        self.btn_next.clicked.connect(self.next_question)

    def next_question(self):
        if self.answer_yes.isChecked():
            if questions[self.question_index]["type"] == "extroversion":
                self.score["extroversion"] += 1
            else:
                self.score["neuroticism"] += 1

        self.question_index += 1
        if self.question_index < len(questions):
            self.question_label.setText(questions[self.question_index]["text"])
            self.answer_group.setExclusive(False)
            self.answer_yes.setChecked(False)
            self.answer_no.setChecked(False)
            self.answer_group.setExclusive(True)
        else:
            self.show_results()

    def show_results(self):
        self.result_window = FinalWin(self.score)
        self.result_window.show()
        self.close()