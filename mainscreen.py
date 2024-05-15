from PyQt6.QtWidgets import QWidget, QPushButton
from PyQt6.QtCore import QSize

class MainScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(300, 500))

        self.button_left = QPushButton("Left", parent=self)
        self.button_left.clicked.connect(self.left_clicked)

        self.button_left.show()

    def left_clicked(self):
        print("Left")
        
