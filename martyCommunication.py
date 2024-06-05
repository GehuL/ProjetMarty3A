from martyconnect import MartyHandler
from martyconnect import MartyHandler2

gridSize = (3, 3) # x, y

# TODO : Make a method to go back to starting point after analyze ?

class Marty:
    def __init__(self, handler) -> None:
        self.handler = handler
        
        self.index = 0

        self.isFinishined = False
        self.isFinishedAnalyzed = False
        self.goLeft = False
        pass

    def analyzeTile(self) -> str:
        """Analyze one of the tile, makes Marty turn when he is on the edge of the grid. Returns the color stepped on"""

        if self.isFinishedAnalyzed:
            return None
        
        if not self.handler.isConnected():
            return None # TODO : throw exception
        connection = self.handler.getMarty()

        if self.index % gridSize[1] == 0:
            connection.walk(1,"auto",0,25,1000,False) # Forward one step
            self.goLeft = not self.goLeft
        else:
            if self.goLeft:
                connection.sidestep("left",1,35,1000,False)
            else:
                connection.sidestep("right",1,35,1000,False)

        if self.index > gridSize[0]*gridSize[1]:
            self.isFinishedAnalyzed = True
            self.index = 0
        else:
            self.index += 1

        # getColor()

        return "color"

    def isFinishedAnalyzed(self) -> bool:
        return self.isFinishedAnalyzed

    def step(self, course) -> None:
        """Makes the step associated with course[index]"""
        print("Making a step :|, n°" + self.index)
        self.index += 1
    
    def isFinished(self) -> bool:
        """Renvoie true si on à résolue le labyrinthe (plus besoin d'appeler step), false sinon"""
        return self.isFinishined

marty1 = Marty(MartyHandler())
marty2 = Marty(MartyHandler2())
info1 = []
info2 = []

def solveMaze() -> None:
    if not marty1.isFinishedAnalyzed():
        info1.append(marty1.analyzeTile())
        return None
    if not marty2.isFinishedAnalyzed():
        info2.append(marty2.analyzeTile())
        return None

    if not marty1.isFinishined():
        marty1.step(info2)
        return None
    if not marty2.isFinishined():
        marty1.step(info1)
        return None