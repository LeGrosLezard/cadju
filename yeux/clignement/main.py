import numpy as np
import cv2
from PIL import Image
import os

from traitement_image import *









def video_capture():

    LISTE_AJUSTEMENT = []
    LISTE_DROITE = []
    LISTE_GAUCHE = []
    
    video = cv2.VideoCapture(0)

    
    while(True):


        left_eye = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')
        
          
        ret, frame = video.read()
        frame = cv2.resize(frame, (600, 600))
        eyes = left_eye.detectMultiScale(frame)


        if len(LISTE_AJUSTEMENT) < 50:
            pre_initialisation(eyes, LISTE_AJUSTEMENT, frame, LISTE_DROITE)
            print("initialisation")
    
        else:
            position = position_yeux_verticale(eyes, LISTE_AJUSTEMENT, frame)
            position_yeux_horizontal(eyes, LISTE_DROITE, LISTE_GAUCHE, frame)
            if position == None:
                pass
            else:
                #print(position)
                pass
            if position in ("le mec s'est baissé", "le mec s'est levé"):
                LISTE_AJUSTEMENT = []




        cv2.imshow('YEUX CAPTURE', frame)






        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    video.release()
    cv2.destroyAllWindows()









if __name__ == "__main__":

    video_capture()












