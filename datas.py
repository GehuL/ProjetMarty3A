from PyQt6.QtWidgets import QWidget, QLabel
from PyQt6.QtCore import QSize, QTimer

from martyconnect import MartyHandler

class DataScreen(QWidget):
    def __init__(self):
        super().__init__()
        
        self.marty = MartyHandler()
        
        self.setFixedSize(QSize(300, 500))
        self.setWindowTitle("Données")
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateInfo)
        self.timer.setInterval(1000)
        self.timer.start()
        
        self.accelerometerText = QLabel(self)
        self.accelerometerText.setText("Accelerometer :")
        self.accelerometerText.move(0, 0)

        self.accelerometerXLabel = QLabel(self)
        self.accelerometerXLabel.setText("x = 00000")
        self.accelerometerXLabel.move(0, 10)

        self.accelerometerYLabel = QLabel(self)
        self.accelerometerYLabel.setText("y = 00000")
        self.accelerometerYLabel.move(0, 20)
        
        self.accelerometerZLabel = QLabel(self)
        self.accelerometerZLabel.setText("z = 00000")
        self.accelerometerZLabel.move(0, 30)
        
        self.obstacleLabel = QLabel(self)
        self.obstacleLabel.setText("Obstacle")
        self.obstacleLabel.move(0, 100)
        
        self.obstacleLeftLabel = QLabel(self)
        self.obstacleLeftLabel.setText("Left : 000000")
        self.obstacleLeftLabel.move(0, 110)
        
        self.obstacleRightLabel = QLabel(self)
        self.obstacleRightLabel.setText("Right : 000000")
        self.obstacleRightLabel.move(0, 120)
        
        self.obstacleColorLabel = QLabel(self)
        self.obstacleColorLabel.setText("Color : 000000")
        self.obstacleColorLabel.move(0, 130)
        
        self.obstacleIRLabel = QLabel(self)
        self.obstacleIRLabel.setText("IR : 000000")
        self.obstacleIRLabel.move(0, 140)

    def updateInfo(self):
        marty = self.marty.getMarty()
        if self.marty.isConnected():
            x, y, z = marty.get_accelerometer()

            self.accelerometerXLabel.setText(f"x = {x}")
            self.accelerometerYLabel.setText(f"y = {y}")
            self.accelerometerZLabel.setText(f"z = {z}")
            
            self.obstacleLeftLabel.setText("Left : " + str(marty.get_obstacle_sensor_reading("left")))
            self.obstacleRightLabel.setText("Right : " + str(marty.get_obstacle_sensor_reading("right")))
            self.obstacleColorLabel.setText("Color : " + str(marty.get_obstacle_sensor_reading("LeftColorSensor")))
            self.obstacleIRLabel.setText("IR : " + str(marty.get_obstacle_sensor_reading("RightIRFoot")))
