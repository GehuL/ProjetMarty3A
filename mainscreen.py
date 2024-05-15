from PyQt6.QtWidgets import QWidget, QPushButton
from PyQt6.QtCore import QSize

class MainScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(300, 500))

        self.button_left = QPushButton("⬅️", parent=self)
        self.button_left.clicked.connect(self.left_clicked)
        self.button_left.show()

        self.button_right = QPushButton("➡️", parent=self)
        self.button_right.clicked.connect(self.left_clicked)
        self.button_right.show()

        self.button_up = QPushButton("⬆️", parent=self)
        self.button_up.clicked.connect(self.left_clicked)
        self.button_up.show()

        self.button_down = QPushButton("⬇️", parent=self)
        self.button_down.clicked.connect(self.left_clicked)
        self.button_down.show()

    def left_clicked(self):
        print("Left")

    def right_clicked(self):
        print("Right")

    def up_clicked(self):
        print("Up")

    def down_clicked(self):
        print("Down")
        
