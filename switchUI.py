from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QSizePolicy
from PyQt6.QtCore import QSize, Qt, QPoint
from martyconnect import MartyHandler

class SwitchUI(QWidget):
    def __init__(self, onSwitchcallback, name):
        super().__init__()
        self.setFixedSize(QSize(250, 50))
        self.setWindowTitle("Switch")

        self.switch = QPushButton(name, self)
        self.switch.setMinimumSize(75, 25)
        self.switch.move(self.geometry().center() - self.switch.geometry().center())
        self.switch.show()

        self.switch.clicked.connect(onSwitchcallback)
