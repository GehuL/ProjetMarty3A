from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel
from PyQt6.QtCore import QSize, Qt, QPoint


class EmoteScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(300, 500))
        self.setWindowTitle("Émotes")

        layout = QGridLayout()

        label = QLabel("test", self)
        label.setStyleSheet("background-color: yellow;")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)


        label2 = QLabel("test", self)
        label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label2.setStyleSheet("background-color: green;")
        
        label3 = QLabel("test", self)
        label3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label3.setStyleSheet("background-color: red;")
        
        label4 = QLabel("test", self)
        label4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label4.setStyleSheet("background-color: blue;")
        
        layout.addWidget(label, 0, 0)
        layout.addWidget(label2, 0, 1)
        layout.addWidget(label3, 1, 0)
        layout.addWidget(label4, 1, 1)

        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(10)

        self.setLayout(layout)


