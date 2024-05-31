import sys

from martyconnect import MartyHandler
from PyQt6.QtWidgets import QApplication
from SideDockWidget import SideDockWidget, Side
from switchUI import SwitchUI

from emotes import EmoteScreen
from datas import DataScreen
from mainscreen import MainScreen
from connexion import ConnexionWidget

def onSwitch():
    global mainWindow, automodeWindow
    if mainWindow.isVisible():
        mainWindow.close()
        automodeWindow = buildAutoModeWindow()
        automodeWindow.show()
    elif automodeWindow.isVisible():
        automodeWindow.close()
        mainWindow = buildMainWindow()
        mainWindow.show()

def buildMainWindow():
    win = SideDockWidget()
    win.setDock(EmoteScreen(), Side.LEFT)
    win.setDock(DataScreen(), Side.RIGHT)
    win.setDock(MainScreen(), Side.CENTER)
    win.setDock(ConnexionWidget(), Side.BOT)
    win.setDock(SwitchUI(onSwitch), Side.TOP)
    return win

def buildAutoModeWindow():
    win = SideDockWidget()
    win.setDock(SwitchUI(onSwitch), Side.TOP)
    return win

app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)

mainWindow = buildMainWindow()
automodeWindow = buildAutoModeWindow()

mainWindow.show()

app.exec()
