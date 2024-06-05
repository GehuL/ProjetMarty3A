from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QComboBox
from connexion import ConnexionWidget
from martyconnect import MartyHandler, MartyHandler2
import martyCommunication

class AutomodeUI(QWidget):
    def __init__(self):
        super().__init__()

        grid = QGridLayout(self)

        connect1 = ConnexionWidget(MartyHandler())
        connect1.setParent(self) # 1e marty
        connect2 = ConnexionWidget(MartyHandler2())
        connect2.setParent(self) # 2e marty
 
        colorList1 = QComboBox()
        calibrateBtn1 = QPushButton(text="Calibrate Marty 1")
        calibrateBtn1.clicked.connect(self.calibrateMarty1)
        colorList1.addItems(['white','red', 'blue', 'yellow', 'green', 'black', 'pink', 'lightblue'])
        self.colorList1 = colorList1

        grid.addWidget(connect1)
        grid.addWidget(colorList1)
        grid.addWidget(calibrateBtn1)
        
        #grid.addWidget(calibrateGrid1)
        colorList2 = QComboBox()
        colorList2.addItems(['white','red', 'blue', 'yellow', 'green', 'black', 'pink', 'lightblue'])
        self.colorList2 = colorList2

        calibrateBtn2 = QPushButton(text="Calibrate Marty 2")
        calibrateBtn2.clicked.connect(self.calibrateMarty2)
        grid.addWidget(connect2)
        grid.addWidget(colorList2)
        grid.addWidget(calibrateBtn2)

        start_btn = QPushButton(parent=self, text="START")
        start_btn.clicked.connect(self.onStart)

        grid.addWidget(start_btn)

    def onStart(self, event):
        print("Start")
        print(MartyHandler().getColor())

    def calibrateMarty1(self, event):
        color = self.colorList1.currentText()
        MartyHandler().calibrate(color)

    def calibrateMarty2(self, event):
        color = self.colorList2.currentText()
        MartyHandler2().calibrate(color)

