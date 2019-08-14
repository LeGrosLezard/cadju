import numpy as np
import cv2
from PIL import Image
import os



from tete import milieu_haut_tete


from initialisation import init_tete_haut




def video_capture():


    MILIEU_TETE = [[], [], [], []]
    COTE_TETE = [[], [], [], [], [], [], [], []]

    video = cv2.VideoCapture(0)
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
    
    subtractor = cv2.createBackgroundSubtractorMOG2(history=100,
                                                    varThreshold=50,
                                                    detectShadows=True)

    while(True):


        ret, frame = video.read()
        frame = cv2.resize(frame, (600, 600))



        if len(MILIEU_TETE[0]) < 10:
            init_tete_haut(frame, faceCascade, MILIEU_TETE)
            
        else:
            milieu_haut_tete(frame, MILIEU_TETE)


        
       
        cv2.imshow('FACE', frame)

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    video.release()
    cv2.destroyAllWindows()









if __name__ == "__main__":

    video_capture()












