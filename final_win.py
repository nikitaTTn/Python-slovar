from PyQt5.QtWidgets import *
from inst import *

class FinalWin(QWidget):
    def __init__(self, score):
        super().__init__()
        self.score = score
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle(txt_finalwin)
        self.initUI()
        self.show()

    def initUI(self):
        layout = QVBoxLayout()


        extroversion_text = txt_extroversion_high if self.score["extroversion"] > 2 else txt_extroversion_low
        neuroticism_text = txt_neuroticism_high if self.score["neuroticism"] > 1 else txt_neuroticism_low

        layout.addWidget(QLabel(extroversion_text))
        layout.addWidget(QLabel(neuroticism_text))

        self.setLayout(layout)