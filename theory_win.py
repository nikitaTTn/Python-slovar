from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit
from PyQt5.QtCore import Qt
from second_win import TestWin

class TheoryWin(QWidget):
    def __init__(self, user_info):
        super().__init__()
        self.user_info = user_info
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Теоретический материал")
        self.initUI()
        self.connects()
        self.show()

    def initUI(self):
        self.theory_text = QTextEdit(self)
        self.theory_text.setReadOnly(True)

        # Убедимся, что передаем строку с Markdown-текстом
        markdown_content = (
            "<h1>Теоретический материал по словарям в Python</h1>\n\n"
            "<p><b>Словарь</b> в Python — это неупорядоченный набор объектов, где каждый объект состоит "
            "из пары «уникальный ключ — значение».</p>\n\n"
            "<h2>1. Создание словаря</h2>\n"
            "<ul>\n"
            "<li><b>Пустой словарь:</b></li>\n"
            "<pre><code style='color: #FF0000;'>имя_словаря = dict()</code></pre>\n"
            "<pre><code style='color: #FF0000;'># или</code></pre>\n"
            "<pre><code style='color: #FF0000;'>имя_словаря = {}</code></pre>\n"
            "<li><b>Словарь с элементами:</b></li>\n"
            "<pre><code style='color: #FF0000;'>имя_словаря = {'ключ1': 'значение1', 'ключ2': 'значение2'}</code></pre>\n"
            "</ul>\n\n"
            # Добавьте остальной Markdown-текст здесь
        )
        self.theory_text.setMarkdown(markdown_content)

        self.btn_next = QPushButton("Перейти к тесту", self)

        layout = QVBoxLayout()
        layout.addWidget(self.theory_text)
        layout.addWidget(self.btn_next, alignment=Qt.AlignCenter)
        self.setLayout(layout)

    def next_click(self):
        self.tw = TestWin(self.user_info)
        self.hide()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)