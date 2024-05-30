from PyQt6.QtWidgets import QWidget, QLineEdit, QGridLayout, QPushButton
from PyQt6.QtCore import QSize
from martyconnect import MartyHandler

class ConnexionWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(250, 75))
        self.setWindowTitle("Connexion")
       
        layout = QGridLayout()

        input = QLineEdit(self)
        #input.setValidator(QDoubleValidator(0.99,99.99,2))
        input.setInputMask("000.000.000.000;_")
        input.setMaxLength(12)
        self.input = input

        btn = QPushButton(self)
        btn.setText("Press to connect")
        btn.setStyleSheet("background-color: red;")
        btn.clicked.connect(self.connect)
        self.btn = btn

        layout.addWidget(input, 0, 0)
        layout.addWidget(btn, 0, 1)

        self.setLayout(layout)

    def connect(self):
        ip = self.input.text()
        print(ip)

        if MartyHandler().isConnected():
            MartyHandler().marty.close()
            self.btn.setText("Press to connect")
            self.btn.setStyleSheet("background-color: red;")
        elif MartyHandler(ip).isConnected():
            self.btn.setText("Press to disconnect")
            self.btn.setStyleSheet("background-color: green;")
