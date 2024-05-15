from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QSize

class EmoteScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(300, 500))
        self.setWindowTitle("Émotes")
