from martypy import Marty

# Premier marty
class BaseHandler(object):

    def  __new__(cls):
        if not hasattr(cls, 'instance'):
            print(cls)
            cls.instance = super(BaseHandler, cls).__new__(cls)
            cls.instance.marty = None
            cls.instance.ip = None
        return cls.instance
    
    def __init__(self, ip=None):
        if ip != None:
            self.marty = None
            self.connect(ip)

    def connect(self, ip):
        print("Connecting to marty", ip, "...")
        try:
            self.ip = ip
            self.marty = Marty("wifi", ip)
            print("Connected to marty")
        except:
            print("Could not connect to marty")

    def getMarty(self):
        return self.marty
    
    def isConnected(self):
        return self.marty != None and self.marty.is_conn_ready()

# Premier marty
class MartyHandler(BaseHandler):

    def __new__(cls, *args, **kwargs):
        return super(MartyHandler, cls).__new__(cls)

    def __init__(self, ip=None):
        super().__init__(ip)
   
# Deuxième marty
class MartyHandler2(BaseHandler):

    def __new__(cls, *args, **kwargs):
        return super(MartyHandler2, cls).__new__(cls)

    def __init__(self, ip=None):
        super().__init__(ip)

if __name__ == "__main__":
    MartyHandler()
    MartyHandler("192.168.0.108")
    marty = MartyHandler2("192.168.0.107").getMarty()
    marty = MartyHandler2().getMarty() # Test du singleton
    if marty is not None:
        #marty.stop("clear and stop")
        #marty.dance(blocking=True)
        print("Marty dance ou je te fume")
