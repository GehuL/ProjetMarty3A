from martyconnect import MartyHandler 
from PyQt6.QtWidgets import QWidget, QPushButton, QLabel
from PyQt6.QtCore import QSize, QTimer
from PyQt6.QtWidgets import QWidget, QPushButton
from PyQt6.QtCore import QSize
from martyconnect import MartyHandler

class MainScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.marty = MartyHandler()
        self.setFixedSize(QSize(300, 500))

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateInfo)
        self.timer.start()

        self.accelerometerText = QLabel(self)
        self.accelerometerText.setText("Accelerometer :")
        self.accelerometerText.move(0, 0)

        self.accelerometerXLabel = QLabel(self)
        self.accelerometerXLabel.setText("x = 000")
        self.accelerometerXLabel.move(0, 10)

        self.accelerometerYLabel = QLabel(self)
        self.accelerometerYLabel.setText("y = 000")
        self.accelerometerYLabel.move(0, 20)
        
        self.accelerometerZLabel = QLabel(self)
        self.accelerometerZLabel.setText("z = 000")
        self.accelerometerZLabel.move(0, 30)

        self.batteryPercentageLabel = QLabel(self)
        self.batteryPercentageLabel.setText("battery: 000")
        self.batteryPercentageLabel.move(100, 0)

        self.buttonLeft = QPushButton("⬅️", parent=self)
        self.buttonLeft.clicked.connect(self.leftClicked)
        self.buttonLeft.move(50, 350)
        self.buttonLeft.show()

        self.buttonRight = QPushButton("➡️", parent=self)
        self.buttonRight.clicked.connect(self.rightClicked)
        self.buttonRight.move(150, 350)
        self.buttonRight.show()

        self.buttonUp = QPushButton("⬆️", parent=self)
        self.buttonUp.clicked.connect(self.upClicked)
        self.buttonUp.move(100, 300)
        self.buttonUp.show()

        self.buttonDown = QPushButton("⬇️", parent=self)
        self.buttonDown.clicked.connect(self.downClicked)
        self.buttonDown.move(100, 400)
        self.buttonDown.show()

    def leftClicked(self):
        marty = self.marty.getMarty()
        if marty == None:
            return 
        print("Left")
        marty.get_ready(None)
        marty.walk(4,"auto",-90,25,2500,None)
        marty.get_ready(None)


    def rightClicked(self):
        marty = self.marty.getMarty()
        if marty == None:
            return 
        print("Right")
        marty.get_ready(None)
        marty.walk(2,"auto",90,25,1500,None)
        marty.get_ready(None)

    def upClicked(self):
        marty = self.marty.getMarty()
        if marty==None:
            return 
 
        print("Up")
        marty.get_ready(None)
        marty.walk(2,"auto",0,25,1500,None)
        marty.get_ready(None)

    def downClicked(self):
        marty = self.marty.getMarty()
        if marty == None:
            return 
        print("Down")
        marty.get_ready(None)
        marty.walk(5,"auto",45,10,2500,None)
        marty.walk(5,"auto",45,10,2500,None)#est sensé faire un demi tour droite
        marty.get_ready(None)


    def updateInfo(self):
        marty = self.marty.getMarty()
        if marty != None:
            x, y, z = marty.get_accelerometer()

            self.accelerometerXLabel.setText(f"x = {x}")
            self.accelerometerYLabel.setText(f"y = {y}")
            self.accelerometerZLabel.setText(f"z = {z}")

            self.batteryPercentageLabel.setText(f"battery: " + str(marty.get_battery_remaining()))
