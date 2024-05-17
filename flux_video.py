import sys 
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import cv2

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow,self).__init__()
        
        self.VBL=QVBoxLayout()
        
        self.FeedLabel=QLabel()
        self.VBL.addWidget(self.FeedLabel)
        
        self.cancel_button=QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.CancelFeed)
        self.VBL.addWidget(self.cancel_button)
        
        self.worker1= Worker1()
        self.worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        self.worker1.start()
        
        self.setLayout(self.VBL)
    
    def ImageUpdateSlot(self,Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))
        
        
    def CancelFeed(self):
        self.worker1.stop()
        
class Worker1(QThread):
    ImageUpdate=pyqtSignal(QImage)
    def run(self):
        self.ThreadActive=True
        Capture=cv2.VideoCapture(0)
        while self.ThreadActive:
            ret,frame=Capture.read()
            if ret:
                Image=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                Flipped_Image=cv2.flip(Image,1)
                Convert_To_Qtformat=QImage(Flipped_Image.data, Flipped_Image.shape[1],Flipped_Image.shape[0],QImage.Format.Format_RGB888)
                pic = Convert_To_Qtformat.scaled(300,300)
                self.ImageUpdate.emit(pic)
        
    
    def stop(self):
        self.ThreadActive=False
        self.quit()


if __name__ == "__main__":
    App=QApplication(sys.argv)
    Root= MainWindow()
    Root.show()
    App.exec()  
