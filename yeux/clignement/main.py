import numpy as np
import cv2
from PIL import Image
import os

from traitement_image import *


def video_capture():

    LISTE_AJUSTEMENT = []
    LISTE_DROITE_GAUCHE = []
    LISTE_GAUCHE = []
    
    video = cv2.VideoCapture(0)

    
    while(True):


        left_eye = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')
        
          
        ret, frame = video.read()
        frame = cv2.resize(frame, (600, 600))
        eyes = left_eye.detectMultiScale(frame)


        if len(LISTE_AJUSTEMENT) < 50:
            pre_initialisation(eyes, LISTE_AJUSTEMENT, frame)
            print("initialisation")
    
        else:
            position1 = position_yeux_verticale(eyes, LISTE_AJUSTEMENT, frame)
            position2 = position_yeux_horizontal(eyes, LISTE_DROITE_GAUCHE, frame)

            if position1 == None:
                pass

            if position2 == None:
                pass


            if position1 and position2:
                if position1 == "le mec regarde en HAUT" and\
                   position2 == "gauche":
                    print("le mec a regarder en haut a gauche")
                elif position1 == "le mec regarde en HAUT" and\
                     position2 == "droite":
                    print("le mec a regarder en haut a droite")
                elif position1 == "le mec regarde en bas" and\
                     position2 == "droite":
                    print("le mec a regarder en bas a droite")
                elif position1 == "le mec regarde en bas" and\
                     position2 == "gauche":
                    print("le mec a regarder en bas a gauche")
     

            elif position1:
                print(position1)

            elif position2:
                print(position2)




            if position1 in ("le mec s'est baissé", "le mec s'est levé",
                             "le mec à levé la tete", "le mec à baisser la tete"):
                LISTE_AJUSTEMENT = []




        cv2.imshow('YEUX CAPTURE', frame)






        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    video.release()
    cv2.destroyAllWindows()









if __name__ == "__main__":

    video_capture()












