from PyQt6.QtWidgets import QWidget, QGridLayout
from connexion import ConnexionWidget
from martyconnect import MartyHandler, MartyHandler2

class AutomodeUI(QWidget):
    def __init__(self):
        super().__init__()

        grid = QGridLayout(self)

        q1 = ConnexionWidget(MartyHandler())
        q1.setParent(self) # 1e marty
        q2 = ConnexionWidget(MartyHandler2())
        q2.setParent(self) # 2e marty

        grid.addWidget(q1)
        grid.addWidget(q2)
