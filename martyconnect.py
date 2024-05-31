from martypy import Marty

# Premier marty
class MartyHandler(object):

    def  __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MartyHandler, cls).__new__(cls)
            cls.instance.marty = None
        return cls.instance
    
    def __init__(self, ip=None):
        if ip != None:
            print("Connecting to marty", ip, "...")
            self.marty = None
            self.connect(ip)

    def connect(self, ip):
        try:
            self.marty = Marty("wifi", ip)
            print("Connected to marty")
        except:
            print("Could not connect to marty")

    def getMarty(self):
        return self.marty
    
    def isConnected(self):
        return self.marty != None and self.marty.is_conn_ready()

# Deuxième marty
class MartyHandler2(MartyHandler):
    def __init__(self, ip=None):
        super().__init__(ip)

if __name__ == "__main__":
    marty = MartyHandler2("192.168.0.102").getMarty()
    marty = MartyHandler2().getMarty() # Test du singleton
    if marty is not None:
        #marty.stop("clear and stop")
        #marty.dance(blocking=True)
        print("Marty dance ou je te fume")
