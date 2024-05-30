from martyconnect import MartyHandler 
from PyQt6.QtWidgets import QWidget, QPushButton, QLabel
from PyQt6.QtCore import QSize, QTimer

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
        self.accelerometerXLabel.setText("x = 0")
        self.accelerometerXLabel.move(0, 10)

        self.accelerometerYLabel = QLabel(self)
        self.accelerometerYLabel.setText("y = 0")
        self.accelerometerYLabel.move(0, 20)
        
        self.accelerometerZLabel = QLabel(self)
        self.accelerometerZLabel.setText("z = 0")
        self.accelerometerZLabel.move(0, 30)

        self.distanceLabel = QLabel(self)
        self.distanceLabel.setText("distance: ")
        self.distanceLabel.move(100, 0)

        self.obstacleLabel = QLabel(self)
        self.obstacleLabel.setText("obstacle: ")
        self.obstacleLabel.move(100, 10)

        self.batteryPercentageLabel = QLabel(self)
        self.batteryPercentageLabel.setText("battery: ")
        self.batteryPercentageLabel.move(100, 20)

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
        print("Left")

    def rightClicked(self):
        print("Right")

    def upClicked(self):
        print("Up")

    def downClicked(self):
        print("Down")

    def updateInfo(self):
        marty = self.marty.getMarty()
        if marty != None:
            x, y, z = self.marty.get_accelerometer()

            self.accelerometerXLabel.setText(f"x = {x}")
            self.accelerometerYLabel.setText(f"y = {y}")
            self.accelerometerZLabel.setText(f"z = {z}")

            self.distanceLabel.setText(f"distance: {marty.get_distance_sensor()} mm")
            self.obstacle_label.setText(f"obstacle: " + marty.foot_obstacle_sensed("left"))
            self.batteryPercentageLabel.setText(f"battery_percentage: " + self.marty.footObstacleSensed("left"))


        
