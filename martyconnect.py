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
            self.calibaration={"red":(0,0,0),"pink":(0,0,0),"blue":(0,0,0),"yellow":(0,0,0),"lightblue":(0,0,0),"green":(0,0,0),"black":(0,0,0)}

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
    
    
    


    def calibrate(self,color):#a appeler pour faire la calibration
        r=marty.get_color_sensor_value_by_channel("left","red")
        g=marty.get_color_sensor_value_by_channel("left","green")
        b=marty.get_color_sensor_value_by_channel("left","red")
        self.calibration[color][0]=r
        self.calibration[color][1]=g
        self.calibration[color][2]=b
        
    def getColor(self):#a appeler pour detecter une couleur, donc en permanence en fait, dans la fonction update je crois
        #renvoie une chaine de caracteres: la couleur detectee
        margin=0.1*255
        r=marty.get_color_sensor_value_by_channel("left","red")
        g=marty.get_color_sensor_value_by_channel("left","green")
        b=marty.get_color_sensor_value_by_channel("left","red")
        colors=[i for i in self.calibration.keys()]
        for i in range(7):
            if abs(r-self.calibaration[i(0)])<margin:
                if abs(r-self.calibaration[i(1)])<margin:
                    if abs(r-self.calibaration[i(2)])<margin:
                        return colors[i]
        return "black"

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
