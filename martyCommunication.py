gridSize = (3, 3)

class Marty1:
    def __init__(self) -> None:
        self.isFinishined = False
        self.isFinishedAnalyzed = False
        pass

    def analyzeTile(self, index):
        """Analyze one of the tile, makes Marty turn when he is on the edge of the grid"""
        return "color"

    def isFinishedAnalyzed(self):
        return self.isFinishedAnalyzed


    def step(self, course, index):
        """Makes the step associated with course[index]"""
        print("Making a step :|, n°" + index)
    
    def isFinished(self) -> bool:
        """Renvoie true si on à résolue le labyrinthe (plus besoin d'appeler step), false sinon"""
        return self.isFinishined
    
class Marty2:
    def __init__(self) -> None:
        self.isFinishined = false
        pass

    def analyzeTile(self, index):
        """Analyze one of the tile, makes Marty turn when he is on the edge of the grid"""
        return "color"

    def step(self, course, index):
        """Makes the step associated with course[index]"""
        print("Making a step :|, n°" + index)
    
    def isFinished(self) -> bool:
        """Renvoie true si on à résolue le labyrinthe (plus besoin d'appeler step), false sinon"""
        return self.isFinishined

def solveMaze():
    pass