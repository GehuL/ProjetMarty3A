from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QSizePolicy
from PyQt6.QtCore import QSize, Qt, QPoint
from martyconnect import MartyHandler

class EmoteScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(300, 500))
        self.setWindowTitle("Émotes")

        layout = QGridLayout()

        btn1 = QPushButton("Eyes", self)
        btn1.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        btn1.setStyleSheet("background-color: yellow;")
        btn1.clicked.connect(lambda: self.on_clicked("eyes"))
        #btn1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        btn2 = QPushButton("Celebrate", self)
        btn2.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        btn2.clicked.connect(lambda: self.on_clicked("celebrate"))
        #btn2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        btn2.setStyleSheet("background-color: green;")
        
        btn3 = QPushButton("Wiggle", self)
        btn3.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        btn3.clicked.connect(lambda: self.on_clicked("wiggle"))
        #btn3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        btn3.setStyleSheet("background-color: red;")
        
        btn4 = QPushButton("Dance", self)
        btn4.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        btn4.clicked.connect(lambda: self.on_clicked("dance"))
        #btn4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        btn4.setStyleSheet("background-color: blue;")
        
        layout.addWidget(btn1, 0, 0)
        layout.addWidget(btn2, 0, 1)
        layout.addWidget(btn3, 1, 0)
        layout.addWidget(btn4, 1, 1)

        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(10)

        self.setLayout(layout)

    def on_clicked(self, type):
        marty = MartyHandler().getMarty()
        if marty == None:
            return

        if type == "wiggle":
            marty.wiggle()
        elif type == "dance":
            marty.dance()
        elif type == "celebrate":
            marty.celebrate()
        elif type == "eyes":
            marty.eyes("wiggle")