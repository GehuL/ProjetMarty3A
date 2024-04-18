from PyQt6.QtCore import QSize, Qt, QPoint
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QStyle
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
        self.setFixedSize(400, 600)
    
    def setDock(self, widget, side : Side):
        self.volets[side] = widget
        widget.setParent(self)
    
        if side is not Side.CENTER:
            widget.setWindowFlag(Qt.WindowType.Window | Qt.WindowType.FramelessWindowHint)

        widget.show()
    
    def getDock(self, side: Side):
        return self.volets[side]

    def moveEvent(self, a0):
        height = QApplication.style().pixelMetric(QStyle.PixelMetric.PM_TitleBarHeight)

        if self.volets[Side.LEFT]:
            pos_y = int(self.pos().y() + self.height() / 2 - self.volets[Side.LEFT].height() / 2)
            self.volets[Side.LEFT].move(QPoint(self.pos().x() - self.volets[Side.LEFT].size().width(), pos_y))

        if self.volets[Side.TOP]:
            pos_x = int(self.pos().x() + self.width() / 2 - self.volets[Side.TOP].width() / 2)
            self.volets[Side.TOP].move(QPoint(pos_x, a0.pos().y() - height - self.volets[Side.TOP].size().height()))

        if self.volets[Side.RIGHT]:
            pos_y = int(self.pos().y() + self.height() / 2 - self.volets[Side.RIGHT].height() / 2)
            self.volets[Side.RIGHT].move(QPoint(self.pos().x() + self.width(), pos_y))

        if self.volets[Side.BOT]:
            pos_x = int(self.pos().x() + self.width() / 2 - self.volets[Side.BOT].width() / 2)
            self.volets[Side.BOT].move(QPoint(pos_x, a0.pos().y() + self.height()))

# Test
if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication, QLabel

    app = QApplication(sys.argv)
    docker  = SideDockWidget()

    left = QWidget()
    left.setWindowTitle("Émotes")
    left.setMaximumSize(QSize(200, 300))
    
    up = QWidget()
    up.setWindowTitle("Crédits")
    up.setMaximumSize(QSize(500, 150))

    right = QWidget()
    right.setWindowTitle("Données")
    right.setMaximumSize(QSize(200, 300))

    bottom = QWidget()
    bottom.setWindowTitle("Maze solver")
    bottom.setMaximumSize(QSize(500, 150))

    center = QLabel()
    center.setText("hello")
    center.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
    center.setScaledContents(True)
    
    docker.setDock(left, Side.LEFT)
    docker.setDock(up, Side.TOP)
    docker.setDock(right, Side.RIGHT)
    docker.setDock(bottom, Side.BOT)
    docker.setDock(center, Side.CENTER)

    docker.setWindowTitle("Projet Marty !")
    docker.show()
    app.exec()
