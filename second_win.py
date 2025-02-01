from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QRadioButton, QButtonGroup, QLabel, QStackedWidget
from final_win import FinalWin  

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 300, 150) 
        self.setWindowTitle("Тест по словарям в Python")
        self.questions = [
            {"question": "Как создать пустой словарь?", "options": ["dict()", "{}", "[]"], "answer": ["dict()", "{}"]},
            {"question": "Как добавить элемент в словарь?", "options": ["dict[key] = value", "dict.add(key, value)", "dict.insert(key, value)"], "answer": ["dict[key] = value"]},

        ]
        self.current_question_index = 0
        self.total_score = 0  
        self.button_groups = []  
        self.initUI()
        self.connects() 
        self.show()

    def initUI(self):
        self.layout = QVBoxLayout(self)

        self.stacked_widget = QStackedWidget(self)
        self.layout.addWidget(self.stacked_widget)

        self.load_questions()

        self.next_btn = QPushButton("Следующий вопрос", self)
        self.layout.addWidget(self.next_btn)

        self.submit_btn = QPushButton("Завершить тест", self)
        self.layout.addWidget(self.submit_btn)
        self.submit_btn.hide()  

        self.setLayout(self.layout)

    def load_questions(self):
        for question in self.questions:
            question_widget = QWidget()
            question_layout = QVBoxLayout(question_widget)

            question_label = QLabel(question["question"], question_widget)
            question_layout.addWidget(question_label)

            button_group = QButtonGroup(question_widget)
            for option in question["options"]:
                radio_button = QRadioButton(option, question_widget)
                button_group.addButton(radio_button)
                question_layout.addWidget(radio_button)

            self.button_groups.append(button_group)

            self.stacked_widget.addWidget(question_widget)

    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.stacked_widget.setCurrentIndex(self.current_question_index)
        else:
            self.next_btn.hide()
            self.submit_btn.show()

    def check_answers(self):
        for i, button_group in enumerate(self.button_groups):
            selected_button = button_group.checkedButton()  
            if selected_button:
                selected_answer = selected_button.text()
                if selected_answer in self.questions[i]["answer"]:
                    self.total_score += 1 

        self.fw = FinalWin(self.total_score, len(self.questions))  
        self.fw.show()
        self.hide()

    def connects(self):
        self.next_btn.clicked.connect(self.next_question)
        self.submit_btn.clicked.connect(self.check_answers)