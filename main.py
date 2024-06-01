import sys

from PyQt6.QtWidgets import QApplication, QWidget
from SideDockWidget import SideDockWidget, Side
from switchUI import SwitchUI
from automodeUI import AutomodeUI
from martyconnect import MartyHandler 

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
    win.setWindowTitle("Marty Controller")
    win.setDock(EmoteScreen(), Side.LEFT)
    win.setDock(DataScreen(), Side.RIGHT)
    win.setDock(MainScreen(), Side.CENTER)
    win.setDock(ConnexionWidget(MartyHandler()), Side.BOT)
    win.setDock(SwitchUI(onSwitch, "Switch to automode"), Side.TOP)
    return win

def buildAutoModeWindow():
    win = SideDockWidget()
    win.setWindowTitle("Marty maze solver")
    win.setDock(SwitchUI(onSwitch, "Switch to manual mode"), Side.TOP)
    win.setDock(AutomodeUI(), Side.CENTER)
    return win

app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)

automodeWindow = QWidget()
mainWindow = buildMainWindow()
mainWindow.show()

app.exec()
