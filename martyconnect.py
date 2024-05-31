from martypy import Marty

class MartyHandler(object):

    def  __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MartyHandler, cls).__new__(cls)
            cls.instance.marties = {id: None} 
        return cls.instance
    
    def __init__(self, ip=None, id=0):
        if ip != None:
            print("Connecting to marty", ip, "...")
            marty = None
            try:
                marty = Marty("wifi", ip)
                print("Connected to marty")
            except:
                print("Could not connect to marty")
            self.selected_id = id
            self.marties[id] = marty

    def getMarty(self):
        return self.marties[self.selected_id]
    
    def isConnected(self):
        print(self.marties)
        return self.marties[self.selected_id] != None and self.marties[self.selected_id].is_conn_ready()

# TEST
if __name__ == "__main__":
    marty = MartyHandler("192.168.0.102").getMarty()
    marty = MartyHandler().getMarty() # Test du singleton
    marty2 = MartyHandler("192.168.0.102", 1).getMarty()
    if MartyHandler(id=3).isConnected():
        #marty.stop("clear and stop")
        #marty.dance(blocking=True)
        print("Marty dance ou je te fume")
