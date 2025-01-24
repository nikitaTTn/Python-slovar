from PyQt5.QtWidgets import *
from final_win import FinalWin

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 600, 400)  # Увеличиваем размер окна для удобства
        self.setWindowTitle("Тест по словарям")
        self.initUI()
        self.connects()
        self.show()

    def initUI(self):
        self.questions = [
            {
                "question": "1. Как создать пустой словарь в Python?",
                "options": ["dict()", "{}", "[]", "set()"],
                "answer": ["dict()", "{}"]
            },
            {
                "question": "2. Как добавить элемент в словарь?",
                "options": ["dict[key] = value", "dict.add(key, value)", "dict.insert(key, value)", "dict.append(key, value)"],
                "answer": ["dict[key] = value"]
            },
            {
                "question": "3. Как удалить элемент из словаря по ключу?",
                "options": ["del dict[key]", "dict.pop(key)", "dict.remove(key)", "dict.delete(key)"],
                "answer": ["del dict[key]", "dict.pop(key)"]
            },
            {
                "question": "4. Как проверить, существует ли ключ в словаре?",
                "options": ["key in dict", "dict.has_key(key)", "dict.contains(key)", "dict.exists(key)"],
                "answer": ["key in dict"]
            },
            {
                "question": "5. Как получить список всех ключей словаря?",
                "options": ["dict.keys()", "dict.get_keys()", "dict.all_keys()", "dict.keys"],
                "answer": ["dict.keys()"]
            },
            {
                "question": "6. Как получить список всех значений словаря?",
                "options": ["dict.values()", "dict.get_values()", "dict.all_values()", "dict.values"],
                "answer": ["dict.values()"]
            },
            {
                "question": "7. Как получить список пар ключ-значение из словаря?",
                "options": ["dict.items()", "dict.get_items()", "dict.all_items()", "dict.items"],
                "answer": ["dict.items()"]
            },
            {
                "question": "8. Как объединить два словаря в один?",
                "options": ["dict1.update(dict2)", "{**dict1, **dict2}", "dict1 + dict2", "dict1.merge(dict2)"],
                "answer": ["dict1.update(dict2)", "{**dict1, **dict2}"]
            },
            {
                "question": "9. Как создать словарь с помощью генератора словаря?",
                "options": ["{key: value for key, value in iterable}", "dict((key, value) for key, value in iterable)", "dict.fromkeys(iterable)", "dict.generate(key, value)"],
                "answer": ["{key: value for key, value in iterable}"]
            },
            {
                "question": "10. Как отсортировать словарь по ключам?",
                "options": ["sorted(dict.keys())", "dict(sorted(dict.items()))", "dict.sort()", "dict.order_by_key()"],
                "answer": ["sorted(dict.keys())", "dict(sorted(dict.items()))"]
            },
        ]

        self.answers = []  # Список для хранения выбранных ответов
        self.layout = QVBoxLayout()

        # Добавляем вопросы и варианты ответов
        for i, q in enumerate(self.questions):
            question_label = QLabel(q["question"])
            self.layout.addWidget(question_label)

            # Сетка для радиокнопок
            grid_layout = QGridLayout()
            for j, option in enumerate(q["options"]):
                radio_button = QRadioButton(option)
                grid_layout.addWidget(radio_button, j // 2, j % 2)  # 2 колонки
                if j == 0:  # Первая кнопка в группе
                    button_group = QButtonGroup(self)
                button_group.addButton(radio_button, j)  # ID кнопки

            # Сохраняем группу кнопок для проверки ответов
            self.answers.append(button_group)
            self.layout.addLayout(grid_layout)

        self.submit_btn = QPushButton("Завершить тест", self)
        self.layout.addWidget(self.submit_btn)
        self.setLayout(self.layout)

    def check_answers(self):
        score = {"dict_knowledge": 0, "dict_practice": 0}

        # Проверка ответов
        for i, q in enumerate(self.questions):
            selected_button = self.answers[i].checkedButton()
            if selected_button:
                selected_answer = selected_button.text()
                if selected_answer in q["answer"]:
                    if i < 5:  # Первые 5 вопросов — теоретические
                        score["dict_knowledge"] += 1
                    else:  # Остальные — практические
                        score["dict_practice"] += 1

        self.fw = FinalWin(score)
        self.hide()

    def connects(self):
        self.submit_btn.clicked.connect(self.check_answers)