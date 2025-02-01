from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit
from PyQt5.QtCore import Qt
from second_win import TestWin  

class TheoryWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle("Теоретический материал")
        self.initUI()
        self.connects()
        self.show()

    def initUI(self):
        self.theory_text = QTextEdit(self)
        self.theory_text.setReadOnly(True)  
        self.theory_text.setPlainText(
            "Теоретический материал по словарям в Python:\n\n"
            "Словарь в python - это неупорядоченный набор объектов,\n"
            "где каждый объект состоит из пары «уникальный ключ — значение\n\n"
            "1. Создание словаря:\n"
            "   - Пустой словарь: dict() или `{}`\n"
            "   - Словарь с элементами: `{'key1': 'value1', 'key2': 'value2'}`\n\n"
            "2. Добавление и изменение элементов:\n"
            "   - Добавить элемент: `dict[key] = value`\n"
            "   - Изменить элемент: `dict[key] = new_value`\n\n"
            "3. Удаление элементов:\n"
            "   - Удалить по ключу: del dict[key] или `dict.pop(key)`\n\n"
            "4. Проверка наличия ключа:\n"
            "   - key in dict возвращает True, если ключ существует\n\n"
            "5. Получение элементов словаря:\n"
            "   - Ключи: `dict.keys()`\n"
            "   - Значения: `dict.values()`\n"
            "   - Пары ключ-значение: `dict.items()`\n\n"
            "6. Объединение словарей:\n"
            "   - dict1.update(dict2) или `{**dict1, **dict2}`\n\n"
            "7. Генераторы словарей:\n"
            "   - `{key: value for key, value in iterable}`\n\n"
            "8. Сортировка словаря:\n"
            "   - По ключам: sorted(dict.keys()) или `dict(sorted(dict.items()))`\n\n"
            "Изучите материал и нажмите 'Перейти к тесту', чтобы начать."
        )

        self.btn_next = QPushButton("Перейти к тесту", self)

        layout = QVBoxLayout()
        layout.addWidget(self.theory_text)
        layout.addWidget(self.btn_next, alignment=Qt.AlignCenter)
        self.setLayout(layout)

    def next_click(self):
        self.tw = TestWin()
        self.hide()  

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)