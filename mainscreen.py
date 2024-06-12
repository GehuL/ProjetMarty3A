from martyconnect import MartyHandler 
from PyQt6.QtWidgets import QWidget, QPushButton, QLabel
from PyQt6.QtCore import QSize, QTimer
from PyQt6 import QtCore

from martyCommunication import solveMaze


class MainScreen(QWidget):
    def __init__(self):
        super().__init__()
        #QtCore.pyqtSignal<(QtCore.QEvent).keyPressed.connect(self.on_key)

        self.marty = MartyHandler()
        self.setFixedSize(QSize(300, 500))

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateInfo)
        self.timer.start()
        
        self.nameLabel = QLabel(self)
        self.nameLabel.setText("AAAAAAAAAAA")
        self.nameLabel.move(0, 0)

        self.batteryPercentageLabel = QLabel(self)
        self.batteryPercentageLabel.setText("000 %")
        self.batteryPercentageLabel.move(250, 0)

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
        
        self.buttonRL = QPushButton("⟲", parent=self)
        self.buttonRL.clicked.connect(self.rotateleftClicked)
        self.buttonRL.setFixedSize(25,25)
        self.buttonRL.move(50, 300)
        self.buttonRL.show()
        
        self.buttonRR = QPushButton("⟳", parent=self)
        self.buttonRR.clicked.connect(self.rotaterightClicked)
        self.buttonRR.setFixedSize(25,25)
        self.buttonRR.move(150+self.buttonRight.width()-self.buttonRR.width(), 300)
        self.buttonRR.show()
    
    def keyPressEvent(self, event):
        print(event.key())
        if event.key() == QtCore.Qt.Key.Key_Q:
            self.leftClicked()
        if event.key() == QtCore.Qt.Key.Key_D:
            self.rightClicked()   
        if event.key() == QtCore.Qt.Key.Key_Z:
            self.upClicked()   
        if event.key() == QtCore.Qt.Key.Key_S:
            self.downClicked()   
        if event.key() == QtCore.Qt.Key.Key_E:
            self.rotaterightClicked()     
        if event.key() == QtCore.Qt.Key.Key_A:
            self.rotateleftClicked()  
        if event.key() == QtCore.Qt.Key.Key_Space:
           self.cancel()
            
    
    def cancel(self):
        if not MartyHandler().isConnected():
            return
        MartyHandler().getMarty().stop("clear queue")
    
    def leftClicked(self):
        if not MartyHandler().isConnected():
            return
        
        MartyHandler().getMarty().sidestep("left",1,35,1000,False)
        
    
    def rightClicked(self):
        if not MartyHandler().isConnected():
            return
        MartyHandler().getMarty().sidestep("right",1,35,1000,False)

    def rotateleftClicked(self):
        if not MartyHandler().isConnected():
            return 
        print("Left")
        for i in range(3):
            MartyHandler().getMarty().stand_straight(1000,False)
            MartyHandler().getMarty().walk(1,"auto",90/3,10,2500,False)
        MartyHandler().getMarty().stand_straight(1000,None)

    def rotaterightClicked(self):
        if not MartyHandler().isConnected():
            return 
        print("Right")
        for i in range(3):
            MartyHandler().getMarty().stand_straight(1000,False)
            MartyHandler().getMarty().walk(1,"auto",-30,10,2500,False)
        MartyHandler().getMarty().stand_straight(1000,None)
       

    def upClicked(self):
        if not MartyHandler().isConnected():
            return 
        print("Up")
        #marty.stand_straight(1000,False)
        MartyHandler().getMarty().walk(1,"auto",0,25,1000,False)

    def downClicked(self):
        if not MartyHandler().isConnected():
            return 
        print("Down")
        MartyHandler().getMarty().walk(1,"auto", 0,-50,2000,False)
        MartyHandler().getMarty().stand_straight(1000,False)


    def updateInfo(self):
        marty = self.marty.getMarty()
        if self.marty.isConnected():
            self.nameLabel.setText(marty.get_marty_name())
            self.batteryPercentageLabel.setText(str(marty.get_battery_remaining()) + " %")
