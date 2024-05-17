import cv2
import numpy as np
#besoin d'etre connecte a marty 

def video_capture():#parametres? Marty?
    cap=cv2.VideoCapture(0)#capture la webcam du pc, a voir comment on capture celle de marty
    while True:
        ret,frame=cap.read()
        cv2.imshow("frame",frame)#possiblite de resize ici 
        if cv2.waitKey(1)==ord("q"):#exit when q is pressed 
            break
    cap.release()
    cv2.destroyAllWindows()
    
video_capture()



