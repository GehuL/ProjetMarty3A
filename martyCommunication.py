from martyconnect import MartyHandler
from martyconnect import MartyHandler2


gridSize = (3, 3) # x, y

class MartyAnalyzer:
    def __init__(self, handler) -> None:
        self._handler = handler
        
        self._course = []

        for i in range(0, gridSize[1]):
            self._course.append([])
            for _ in range(0, gridSize[0]):
                self._course[i].append("")

        self._x = 0
        self._y = 0

        self._isFinishined = False

    def analyzeTile(self) -> None:
        """Analyze the cell of the grid (one for each call), and internally stores it. After measuring, we establish that to go from the middle of a cell to another, we need to do 4 sidestep or 3 forward"""

        if self._isFinishined:
            return None
        
        if not self._handler.isConnected():
            return None
        connection = self._handler.getMarty()

        if self._y % 2 == 0:
            xEnd = gridSize[0]
            xStep = 1
        else:
            xStep = -1


        if self._x == xEnd:
            connection.walk(3, "auto", 0, 25, 1000, False)
            self._y += 1
        else:
            connection.sidestep("right", 4, 35, 1000, False)
            self._x += xStep

        if self._y == gridSize[1] and self._x == xEnd:
            self._isFinishined = True

        self._course[self._x][self._y] = self._handler.getColor()

        return None

    def isFinished(self) -> bool:
        return self._isFinishined

    
    def isFinished(self) -> bool:
        """Renvoie true si on à finie d'analyser le labyrinthe labyrinthe (plus besoin d'appeler step), false sinon"""
        return self._isFinishined
    
    def getCourse(self):
        return self._course

def combineCourse(course1, course2):
    for y in range(0, gridSize[1]):
        for x in range(0, gridSize[0]):
            if course1[y][x] == "noir":
                course1[y][x] = course2[y][x]
    
    return course1

class MartyParkour:
    def __init__(self, course, handler) -> None:
        self._handler = handler

        self._course = course
        self._x = 0
        self._y = 0
        self._isFinishined = False

        for y in range(0, gridSize[1]):
            for x in range(0, gridSize[0]):
                if self._course[y][x] == "lightblue":
                    self._x = x
                    self._y = y

    def step(self) -> None:
        """Makes the step associated with course[index]"""
        if self._isFinishined == True:
            return None

        if not self._handler.isConnected():
            return None
        connection = self._handler.getMarty()

        if self._course[self._index] == "red":
            self._isFinishined = True
        elif self._course[self._index] == "green":
            connection.walk(3, "auto", 0, 25, 1000, False)
            self._y += 1
        elif self._course[self._index] == "yellow":
            connection.walk(3,"auto", 0, -25, 1000, False)
            self._y -= 1
        elif self._course[self._index] == "blue":
            connection.sidestep("right", 4, 35, 1000, False)
            self._x += 1
        elif self._course[self._index] == "pink":
            connection.sidestep("left", 4, 35, 1000, False)
            self._x -= 1
    
    def isFinished(self) -> bool:
        """Renvoie true si on à résolue le labyrinthe (plus besoin d'appeler step), false sinon"""
        return self._isFinishined

analalyzer1 = MartyAnalyzer(MartyHandler())
analalyzer2 = MartyAnalyzer(MartyHandler2())

parkour = None

def analyze() -> None:
    analalyzer1.analyzeTile()
    analalyzer2.analyzeTile()

def initSolve() -> None:
    global parkour
    parkour = MartyParkour(combineCourse(analalyzer1.getCourse(), analalyzer2.getCourse()), MartyHandler())

def solve() -> None:
    parkour.step()
