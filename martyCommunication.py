class Info:
    """On stockera les informations que les Marty doivent se passer entre ici"""
    def __init__(self) -> None:
        self.foo = "bar"

class Marty1:
    def __init__(self) -> None:
        pass

    def start() -> Info:
        """Commence à résoudre le labyrinthe (c'est toujours Marty1 qui commence), renvoie une instance de Info à transmettre à Marty2"""
        return Info()
    
    def step(info: Info) -> Info:
        """Fait une autre étape de la résolution du labyrinthe à l'aide des infos transmises par Marty2, renvoie une instance de Info à transmettre à Marty2"""
        return Info()
    
    def isFinished() -> bool:
        """Renvoie true si on à résolue le labyrinthe (plus besoin d'appeler step), false sinon"""
        return False
    
class Marty2:
    def __init__(self) -> None:
        pass
    
    def step(info: Info) -> Info:
        """Fait une autre étape de la résolution du labyrinthe à l'aide des infos transmises par Marty1, renvoie une instance de Info à transmettre à Marty1"""
        return Info()
    
    def isFinished() -> bool:
        """Renvoie true si on à résolue le labyrinthe (plus besoin d'appeler step), false sinon"""
        return False