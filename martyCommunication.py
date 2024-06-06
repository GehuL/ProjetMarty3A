from martyconnect import MartyHandler
from martyconnect import MartyHandler2


gridSize = (3, 3) # x, y

# TODO : Make a method to go back to starting point after analyze ?

class Marty:
    def __init__(self, handler) -> None:
        self._handler = handler
        
        self._index = 1

        self._isFinishined = False
        self._isFinishedAnalyzed = False
        self._goLeft = False
        pass

    def analyzeTile(self) -> str:
        """Analyze one of the tile, makes Marty turn when he is on the edge of the grid. Returns the color stepped on. After measuring, we establish that to go from the middle of a cell to another, we need to do 4 sidestep or 3 forward"""

        if self._isFinishedAnalyzed:
            return None
        
        if not self._handler.isConnected():
            return None
        connection = self._handler.getMarty()

        print(self._index)

        if self._index % gridSize[1] == 0:
            connection.walk(3,"auto",0,25,1000,False) # Forward one step
            self._goLeft = not self._goLeft
        else:
            if self._goLeft:
                connection.sidestep("left",4,35,1000,False)
            else:
                connection.sidestep("right",4,35,1000,False)

        if self._index > gridSize[0]*gridSize[1] + 1:
            self._isFinishedAnalyzed = True
            self._index = 0
        else:
            self._index += 1

        # getColor()

        return "color"

    def isFinishedAnalyzed(self) -> bool:
        return self._isFinishedAnalyzed

    def step(self, course) -> None:
        """Makes the step associated with course[index]"""
        print("Making a step :|, n°" + str(self._index))
        self._index += 1
    
    def isFinished(self) -> bool:
        """Renvoie true si on à résolue le labyrinthe (plus besoin d'appeler step), false sinon"""
        return self._isFinishined

marty1 = Marty(MartyHandler())
#marty2 = Marty(MartyHandler2())
info1 = []
info2 = []

def solveMaze() -> None:

    if not marty1.isFinishedAnalyzed():
        info1.append(marty1.analyzeTile())
        return None
    #if not marty2.isFinishedAnalyzed():
    #    info2.append(marty2.analyzeTile())
    #    return None

    if not marty1.isFinished():
        marty1.step(info2)
        return None
    #if not marty2.isFinishined():
    #    marty1.step(info1)
    #    return None
    