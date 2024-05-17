from martypy import Marty

class MartyHandler(object):

    def  __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MartyHandler, cls).__new__(cls)
            print("Connecting to marty...")
            marty = None
            try:
                marty = Marty("wifi", args[0])
                print("Connected to marty")
            except:
                print("Could not connect to marty")
            cls.instance.marty = marty
        return cls.instance
    
    def __init__(self, ip=None):
        pass

    def getMarty(self):
        return self.marty

if __name__ == "__main__":
    marty = MartyHandler("192.168.0.2").getMarty()
    marty = MartyHandler().getMarty() # Test du singleton
    if marty is not None:
        marty.stop("clear and stop")
        marty.dance(blocking=True)
        print("Marty dance ou je te fume")
