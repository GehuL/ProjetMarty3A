from PyQt6.QtWidgets import QWidget, QPushButton
from PyQt6.QtCore import QSize
from martyconnect import MartyHandler

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
        marty=MartyHandler().getMarty()
        if marty==None:
            return 
        print("Left")
        marty.walk(2,"auto",-90,25,1500,None)

    def right_clicked(self):
        marty=MartyHandler().getMarty()
        if marty==None:
            return 
        print("Right")
        marty.walk(2,"auto",90,25,1500,None)

    def up_clicked(self):
        marty=MartyHandler().getMarty()
        if marty==None:
            return 
        print("Up")
        marty.walk(2,"auto",0,25,1500,None)

    def down_clicked(self):
        marty=MartyHandler().getMarty()
        if marty==None:
            return 
        print("Down")
        marty.walk(5,"auto",90,25,1500,None)
        marty.walk(5,"auto",90,25,1500,None)#est sensé faire un demi tour droite
