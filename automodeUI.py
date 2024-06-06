from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QComboBox
from connexion import ConnexionWidget
from martyconnect import MartyHandler, MartyHandler2
from martyCommunication import solveMaze

from PyQt6.QtCore import QTimer

class AutomodeUI(QWidget):
    def __init__(self):
        super().__init__()

        self.timer = QTimer()

        grid = QGridLayout(self)

        connect1 = ConnexionWidget(MartyHandler())
        connect1.setParent(self) # 1e marty
        connect2 = ConnexionWidget(MartyHandler2())
        connect2.setParent(self) # 2e marty
 
        colorList1 = QComboBox()
        calibrateBtn1 = QPushButton(text="Calibrate Marty 1")
        calibrateBtn1.clicked.connect(self.calibrateMarty1)
        colorList1.addItems(['red', 'blue', 'yellow', 'green', 'black', 'pink', 'lightblue'])
        self.colorList1 = colorList1

        grid.addWidget(connect1)
        grid.addWidget(colorList1)
        grid.addWidget(calibrateBtn1)
        
        self.buttonStart = QPushButton("Start", parent=self)
        self.buttonStart.clicked.connect(self.onStart)
        self.buttonStart.move(300, 500)
        self.buttonStart.show()

        self.buttonEnd = QPushButton("End", parent=self)
        self.buttonEnd.clicked.connect(self.onEnd)
        self.buttonEnd.move(300, 500)
        self.buttonEnd.show()

        #grid.addWidget(calibrateGrid1)
        colorList2 = QComboBox()
        colorList2.addItems(['red', 'blue', 'yellow', 'green', 'black', 'pink', 'lightblue'])
        self.colorList2 = colorList2

        calibrateBtn2 = QPushButton(text="Calibrate Marty 2")
        calibrateBtn2.clicked.connect(self.calibrateMarty2)
        grid.addWidget(connect2)
        grid.addWidget(colorList2)
        grid.addWidget(calibrateBtn2)

        start_btn = QPushButton(parent=self, text="START")
        start_btn.clicked.connect(self.onStart)

        stop_btn = QPushButton(parent=self, text="STOP")
        stop_btn.clicked.connect(self.onEnd)

        grid.addWidget(start_btn)
        grid.addWidget(stop_btn)

    def onStart(self, event):
        self.timer.setInterval(1000)
        self.timer.timeout.connect(solveMaze)
        self.timer.start()
    
    def onEnd(self):
        self.timer.stop()

    def calibrateMarty1(self, event):
        print(self.colorList1.currentText())

    def calibrateMarty2(self, event):
        print(self.colorList2.currentText())

