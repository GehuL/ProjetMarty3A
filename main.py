import sys

from martyconnect import MartyHandler
from PyQt6.QtWidgets import QApplication
from SideDockWidget import SideDockWidget, Side

from emotes import EmoteScreen
from datas import DataScreen
from mainscreen import MainScreen
from connexion import ConnexionWidget

#MartyHandler("192.168.0.2")

app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)

mainWindow = SideDockWidget()

mainWindow.setDock(EmoteScreen(), Side.LEFT)
mainWindow.setDock(DataScreen(), Side.RIGHT)
mainWindow.setDock(MainScreen(), Side.CENTER)
mainWindow.setDock(ConnexionWidget(), Side.BOT)

mainWindow.show()

app.exec()
