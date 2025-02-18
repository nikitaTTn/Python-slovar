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
            
            "<h2>2. Добавление и изменение элементов</h2>\n"
            "<ul>\n"
            "<li><b>Добавить элемент:</b></li>\n"
            "<pre><code style='color: #FF0000;'>dict[ключ] = значение</code></pre>\n"
            "<li><b>Изменить элемент:</b></li>\n"
            "<pre><code style='color: #FF0000;'>dict[ключ] = новое_значение</code></pre>\n"
            "</ul>\n\n"
            
            "<h2>3. Удаление элементов</h2>\n"
            "<ul>\n"
            "<li><b>Удалить по ключу:</b></li>\n"
            "<pre><code style='color: #FF0000;'>del dict[ключ]</code></pre>\n"
            "<pre><code style='color: #FF0000;'># или</code></pre>\n"
            "<pre><code style='color: #FF0000;'>dict.pop(ключ)</code></pre>\n"
            "</ul>\n\n"
            
            "<h2>4. Проверка наличия ключа</h2>\n"
            "<ul>\n"
            "<li>Проверка:</li>\n"
            "<pre><code style='color: #FF0000;'>key in dict  # Возвращает True, если ключ существует</code></pre>\n"
            "</ul>\n\n"
            
            "<h2>5. Получение элементов словаря</h2>\n"
            "<ul>\n"
            "<li><b>Ключи:</b></li>\n"
            "<pre><code style='color: #FF0000;'>dict.keys()</code></pre>\n"
            "<li><b>Значения:</b></li>\n"
            "<pre><code style='color: #FF0000;'>dict.values()</code></pre>\n"
            "<li><b>Пары ключ-значение:</b></li>\n"
            "<pre><code style='color: #FF0000;'>dict.items()</code></pre>\n"
            "</ul>\n\n"
            
            "<h2>6. Объединение словарей</h2>\n"
            "<ul>\n"
            "<li><b>Метод update:</b></li>\n"
            "<pre><code style='color: #FF0000;'>dict1.update(dict2)</code></pre>\n"
            "<li><b>Через распаковку:</b></li>\n"
            "<pre><code style='color: #FF0000;'>{**dict1, **dict2}</code></pre>\n"
            "</ul>\n\n"
            
            "<h2>7. Генераторы словарей</h2>\n"
            "<ul>\n"
            "<li>Пример:</li>\n"
            "<pre><code style='color: #FF0000;'>{key: value for key, value in iterable}</code></pre>\n"
            "</ul>\n\n"
            
            "<h2>8. Сортировка словаря</h2>\n"
            "<ul>\n"
            "<li><b>По ключам:</b></li>\n"
            "<pre><code style='color: #FF0000;'>sorted(dict.keys())</code></pre>\n"
            "<pre><code style='color: #FF0000;'># или</code></pre>\n"
            "<pre><code style='color: #FF0000;'>dict(sorted(dict.items()))</code></pre>\n"
            "</ul>\n\n"
            
            "<h2>9. Использование словаря как замены switch/case</h2>\n"
            "<p>В Python нет встроенной конструкции switch/case, но словари могут быть использованы для имитации такой логики.\n"
            "  Например, если нужно выбрать действие в зависимости от ввода пользователя:</p>\n"
            "<pre><code style='color: #FF0000;'>actions = {\n"
            "    'add': lambda x, y: x + y,\n"
            "    'subtract': lambda x, y: x - y,\n"
            "    'multiply': lambda x, y: x * y,\n"
            "}</code></pre>\n"
            "<pre><code style='color: #FF0000;'>action = 'add'</code></pre>\n"
            "<pre><code style='color: #FF0000;'>result = actions[action](5, 3)</code></pre>\n"
            "<pre><code style='color: #FF0000;'>print(result)  # 8</code></pre>\n\n"
            
            "<h2>10. Перебор словаря</h2>\n"
            "<p>Чтобы пройти по словарю, можно использовать методы <code>keys()</code>, <code>values()</code>, и <code>items()</code>:</p>\n"
            "<pre><code style='color: #FF0000;'>for key, value in dict.items():</code></pre>\n"
            "<pre><code style='color: #FF0000;'>    print(key, value)</code></pre>\n"
            "<p>Это полезно, если нужно выполнить операцию с каждым элементом словаря.</p>\n\n"
            
            "<h2>11. Словари и вложенные структуры данных</h2>\n"
            "<p>Словари могут содержать другие словари, списки, кортежи и любые другие структуры данных в качестве значений. "
            "Это позволяет создавать более сложные иерархические структуры.</p>\n"
            "<pre><code style='color: #FF0000;'>student = {\n"
            "    'name': 'Иван',\n"
            "    'courses': [\n"
            "        {'course_name': 'Python', 'grade': 'A'},\n"
            "        {'course_name': 'Math', 'grade': 'B'},\n"
            "    ]\n"
            "}</code></pre>\n"
            "<pre><code style='color: #FF0000;'>print(student['courses'][0]['course_name'])  # Python</code></pre>\n\n"
            
            "<h2>12. Использование defaultdict для упрощения работы со словарями</h2>\n"
            "<p><b>defaultdict</b> из модуля <code>collections</code> позволяет избежать ошибки <code>KeyError</code>, когда ключ не существует. "
            "При обращении к несуществующему ключу возвращается значение по умолчанию.</p>\n"
            "<pre><code style='color: #FF0000;'>from collections import defaultdict</code></pre>\n"
            "<pre><code style='color: #FF0000;'>dd = defaultdict(int)</code></pre>\n"
            "<pre><code style='color: #FF0000;'>dd['a'] += 1</code></pre>\n"
            "<pre><code style='color: #FF0000;'>print(dd['a'])  # 1</code></pre>\n"
            "<pre><code style='color: #FF0000;'>print(dd['b'])  # 0, ключ не существует, возвращается значение по умолчанию (int = 0)</code></pre>\n\n"
            
            "<hr>\n"
            "<p>Изучите материал и нажмите <b>'Перейти к тесту'</b>, чтобы начать.</p>"
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