from martyconnect import MartyHandler 
from PyQt6.QtWidgets import QWidget, QPushButton, QLabel
from PyQt6.QtCore import QSize, QTimer

class MainScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.marty = MartyHandler().getMarty()
        self.setFixedSize(QSize(300, 500))

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_info)
        self.timer.start()

        self.accelerometer_x_label = QLabel(self)
        self.accelerometer_x_label.setText("x = 0")
        self.move(100, 400)

        # self.accelerometer_y_label = QLabel(self)
        # self.accelerometer_y_label.setText("y = 0")

        # self.accelerometer_z_label = QLabel(self)
        # self.accelerometer_z_label.setText("z = 0")

        # self.distance_label = QLabel(self)
        # self.distance_label.setText("distance: ")

        # self.obstacle_label = QLabel(self)
        # self.obstacle_label.setText("obstacle: ")

        # self.battery_percentage_label = QLabel(self)
        # self.battery_percentage_label.setText("battery: ")

        # self.button_left = QPushButton("⬅️", parent=self)
        # self.button_left.clicked.connect(self.left_clicked)
        # self.button_left.move(10, 50)
        # self.button_left.show()

        # self.button_right = QPushButton("➡️", parent=self)
        # self.button_right.clicked.connect(self.right_clicked)
        # self.button_left.move(20, 50)
        # self.button_right.show()

        # self.button_up = QPushButton("⬆️", parent=self)
        # self.button_up.clicked.connect(self.up_clicked)
        # self.button_left.move(30, 50)
        # self.button_up.show()

        # self.button_down = QPushButton("⬇️", parent=self)
        # self.button_down.clicked.connect(self.down_clicked)
        # self.button_left.move(40, 150)
        # self.button_down.show()

    def left_clicked(self):
        print("Left")

    def right_clicked(self):
        print("Right")

    def up_clicked(self):
        print("Up")

    def down_clicked(self):
        print("Down")

    def update_info(self):
        marty = MartyHandler().getMarty()
        if marty == None:
            x, y, z = 0, 0, 0
        else:
            x, y, z = self.marty.get_accelerometer()

        self.accelerometer_x_label.setText(f"x = {x}")
        # self.accelerometer_y_label.setText(f"x = {y}")
        # self.accelerometer_z_label.setText(f"x = {z}")

        # self.distance_label.setText(f"distance: {self.marty.get_distance_sensor()} mm")
        # self.obstacle_label.setText(f"obstacle: {self.marty.foot_obstacle_sensed("left")}")
        # self.battery_percentage_label.setText(f"battery_percentage: {self.marty.foot_obstacle_sensed("left")}")


        
