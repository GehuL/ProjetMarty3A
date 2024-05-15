import sys

from PyQt6.QtWidgets import QApplication
from SideDockWidget import SideDockWidget, Side

from emotes import EmoteScreen
from datas import DataScreen
from mainscreen import MainScreen

app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)

mainWindow = SideDockWidget()

mainWindow.setDock(EmoteScreen(), Side.LEFT)
mainWindow.setDock(DataScreen(), Side.RIGHT)
mainWindow.setDock(MainScreen(), Side.CENTER)

mainWindow.show()

app.exec()
