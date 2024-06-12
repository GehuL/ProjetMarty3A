import platform
from PyQt6.QtCore import QSize, Qt, QPoint, QTimer
from PyQt6.QtWidgets import QApplication, QWidget, QStyle, QPushButton, QGridLayout, QMainWindow
from PyQt6.QtGui import *

class Side:
    LEFT = 0
    TOP = 1
    BOT = 2
    RIGHT = 3
    CENTER = 4

class SideDockWidget(QMainWindow):
        
    def __init__(self):
        super().__init__()
       
        self.volets = [None] * 5
        self.buttons = [None] * 4

        self.setFixedSize(400, 600)

        btn = self.buttons[Side.LEFT] = QPushButton('<')
        btn.setParent(self)
        btn.move(self.rect().center() - btn.rect().center())
        btn.show()

        self.buttons[Side.TOP] = QPushButton('^')
        self.buttons[Side.RIGHT] = QPushButton('>')
        self.buttons[Side.BOT] = QPushButton('\\/')

        for button in self.buttons:
            button.hide()
            button.clicked.connect(self.button_event)
            button.setFixedSize(25, 25)
            button.setParent(self)

        self.buttons[Side.TOP].move(int(self.width() / 2 - self.buttons[Side.TOP].width() / 2), 0)
        self.buttons[Side.RIGHT].move(self.width() - self.buttons[Side.RIGHT].width(), int(self.height() / 2 - self.buttons[Side.TOP].height() / 2))
        self.buttons[Side.LEFT].move(0, int(self.height() / 2 - self.buttons[Side.TOP].height() / 2))
        self.buttons[Side.BOT].move(int(self.width() / 2 - self.buttons[Side.TOP].width() / 2), self.height() - self.buttons[Side.BOT].height())

        if platform.system() == "Linux":
            timer = QTimer(self)
            timer.setInterval(100)
            timer.timeout.connect(self.moveEventCb)
            timer.start()

    def button_event(self):
        sender = self.sender()
        id = self.buttons.index(sender)
        volet = self.volets[id]

        if volet:
            isHidden = volet.isHidden()
            volet.setHidden(not isHidden)

    def setDock(self, widget, side : Side):
        
        self.volets[side] = widget
    
        if side is Side.CENTER:
            widget.setParent(self)
            widget.move(self.rect().center() - widget.rect().center())
        else:
            self.buttons[side].show()
            widget.setParent(self)
            widget.setWindowFlag(Qt.WindowType.Window | Qt.WindowType.FramelessWindowHint)

        widget.show()

    def closeEvent(self, event):
        for window in self.volets:
            if window:
                window.close()
    
    def getDock(self, side: Side):
        return self.volets[side]
    
    def moveEventCb(self):
        self.moveWindow(self.pos())

    def moveEvent(self, a0):
        self.moveWindow(a0.pos)

    def moveWindow(self, windowPos):

        if self.volets[Side.LEFT]:
            pos_y = int(self.pos().y() + self.height() / 2 - self.volets[Side.LEFT].height() / 2)
            self.volets[Side.LEFT].move(QPoint(self.pos().x() - self.volets[Side.LEFT].size().width(), pos_y))

        if self.volets[Side.TOP]:
            #title_bar_height = QApplication.style().pixelMetric(QStyle.PixelMetric.PM_TitleBarHeight)
            pos_x = int(self.pos().x() + self.width() / 2 - self.volets[Side.TOP].width() / 2)
            self.volets[Side.TOP].move(QPoint(pos_x, self.pos().y() - self.volets[Side.TOP].size().height()))

        if self.volets[Side.RIGHT]:
            pos_y = int(self.pos().y() + self.height() / 2 - self.volets[Side.RIGHT].height() / 2)
            self.volets[Side.RIGHT].move(QPoint(self.pos().x() + self.width(), pos_y))

        if self.volets[Side.BOT]:
            pos_x = int(self.pos().x() + self.width() / 2 - self.volets[Side.BOT].width() / 2)
            self.volets[Side.BOT].move(QPoint(pos_x, self.pos().y() + self.height()))

# Test
if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication, QLabel

    app = QApplication(sys.argv)
    docker  = SideDockWidget()

    left = QWidget()
    left.setWindowTitle("Émotes")
    left.setFixedSize(QSize(200, 300))

    up = QWidget()
    up.setWindowTitle("Crédits")
    up.setFixedSize(QSize(500, 150))

    right = QWidget()
    right.setWindowTitle("Données")
    right.setFixedSize(QSize(200, 300))

    bottom = QWidget()
    bottom.setWindowTitle("Maze solver")
    bottom.setFixedSize(QSize(500, 150))

    center = QLabel()
    center.setText("hello")
    center.setFixedSize(300, 500)
    center.setAlignment(Qt.AlignmentFlag.AlignCenter)
    center.setStyleSheet("background-color: yellow;")
    
    docker.setDock(left, Side.LEFT)
    docker.setDock(up, Side.TOP)
    docker.setDock(right, Side.RIGHT)
    docker.setDock(bottom, Side.BOT)
    docker.setDock(center, Side.CENTER)

    docker.setWindowTitle("Projet Marty !")
    docker.show()
    app.exec()
