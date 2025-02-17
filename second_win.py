from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QRadioButton, 
    QButtonGroup, QLabel, QStackedWidget, QLineEdit
)
from PyQt5.QtCore import QTimer
from final_win import FinalWin

class TestWin(QWidget):
    def __init__(self, user_info):
        super().__init__()
        self.user_info = user_info
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Тест по словарям в Python")

        # Вопросы с разными типами
        self.questions = [
            {
                "type": "choice",  # Тип вопроса: выбор из вариантов
                "question": "Как создать пустой словарь?",
                "options": ["dict()", "{}", "[]"],
                "answer": ["dict()", "{}"]
            },
            {
                "type": "input",  # Тип вопроса: ручной ввод
                "question": "Какой метод используется для удаления элемента из словаря?",
                "answer": ["del", "pop"]
            },
            {
                "type": "choice",
                "question": "Как проверить наличие ключа в словаре?",
                "options": ["key in dict", "dict.contains(key)", "dict.has_key(key)"],
                "answer": ["key in dict"]
            },
            {
                "type": "input",
                "question": "Какой метод возвращает все ключи словаря?",
                "answer": ["keys"]
            }
        ]

        self.current_question_index = 0
        self.total_score = 0
        self.button_groups = []  # Только для вопросов с выбором
        self.input_fields = []  # Для вопросов с ручным вводом
        self.start_time = 0

        self.initUI()
        self.connects()
        self.show()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.elapsed_time = 0
        self.timer.start(1000)

    def initUI(self):
        self.layout = QVBoxLayout(self)

        self.stacked_widget = QStackedWidget(self)
        self.layout.addWidget(self.stacked_widget)

        self.load_questions()

        self.prev_btn = QPushButton("Назад", self)
        self.prev_btn.setEnabled(False)
        self.layout.addWidget(self.prev_btn)

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

            if question["type"] == "choice":
                # Вопрос с выбором ответа
                button_group = QButtonGroup(question_widget)
                for option in question["options"]:
                    radio_button = QRadioButton(option, question_widget)
                    button_group.addButton(radio_button)
                    question_layout.addWidget(radio_button)
                self.button_groups.append(button_group)
            elif question["type"] == "input":
                # Вопрос с ручным вводом
                input_field = QLineEdit(question_widget)
                question_layout.addWidget(input_field)
                self.input_fields.append(input_field)

            self.stacked_widget.addWidget(question_widget)

    def next_question(self):
        self.current_question_index += 1
        self.stacked_widget.setCurrentIndex(self.current_question_index)

        self.prev_btn.setEnabled(True)
        if self.current_question_index == len(self.questions) - 1:
            self.next_btn.hide()
            self.submit_btn.show()

    def prev_question(self):
        if self.current_question_index > 0:
            self.current_question_index -= 1
            self.stacked_widget.setCurrentIndex(self.current_question_index)

            if self.current_question_index == 0:
                self.prev_btn.setEnabled(False)

            self.next_btn.show()
            self.submit_btn.hide()

    def check_answers(self):
        self.total_score = 0  # Сбрасываем счетчик перед проверкой
        button_group_index = 0  # Индекс для button_groups
        input_field_index = 0   # Индекс для input_fields

        for i, question in enumerate(self.questions):
            if question["type"] == "choice":
                # Проверка вопросов с выбором
                selected_button = self.button_groups[button_group_index].checkedButton()
                if selected_button:
                    selected_answer = selected_button.text()
                    if selected_answer in question["answer"]:
                        self.total_score += 1
                button_group_index += 1  # Переходим к следующей группе кнопок
            elif question["type"] == "input":
                # Проверка вопросов с ручным вводом
                user_answer = self.input_fields[input_field_index].text().strip()
                if user_answer in question["answer"]:
                    self.total_score += 1
                input_field_index += 1  # Переходим к следующему полю ввода

        self.timer.stop()
        self.fw = FinalWin(self.total_score, len(self.questions), self.elapsed_time, self.user_info)
        self.fw.show()
        self.hide()

    def update_timer(self):
        self.elapsed_time += 1

    def connects(self):
        self.next_btn.clicked.connect(self.next_question)
        self.prev_btn.clicked.connect(self.prev_question)
        self.submit_btn.clicked.connect(self.check_answers)