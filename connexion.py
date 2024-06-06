from PyQt6.QtWidgets import QWidget, QLineEdit, QGridLayout, QPushButton
from PyQt6.QtCore import QSize
from martyconnect import MartyHandler

class ConnexionWidget(QWidget):
    def __init__(self, martyHandler):
        super().__init__()

        self.martyHandler = martyHandler

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

        if self.martyHandler.ip != None:
         input.setText(self.martyHandler.ip)

        self.setButton(self.martyHandler.isConnected())

    def setButton(self, connected):
        if connected:
            self.btn.setText("Press to disconnect")
            self.btn.setStyleSheet("background-color: green;")
        else:
            self.btn.setText("Press to connect")
            self.btn.setStyleSheet("background-color: red;")

    def connect(self):
        ip = self.input.text()
        print(ip)

        if self.martyHandler.isConnected():
            self.martyHandler.marty.close()
        else:
            self.martyHandler.connect(ip)

        self.setButton(self.martyHandler.isConnected())
