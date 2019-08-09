import numpy as np
import cv2
from PIL import Image
import os

from traitement_image import *


def video_capture():

    LISTE_POS_INI_X = []
    LISTE_POS_INI_Y_H = []
    LISTE_LARGEUR = []
    
    video = cv2.VideoCapture(0)
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")

    
    while(True):


        ret, frame = video.read()
        frame = cv2.resize(frame, (600, 600))
        
 
        if len(LISTE_POS_INI_X) < 100:
            initialisation(video, frame, faceCascade, LISTE_POS_INI_X,
                           LISTE_POS_INI_Y_H, LISTE_LARGEUR)
            print("initialisation")

        else:
            position = position_tete(video, frame, faceCascade, LISTE_POS_INI_X,
                          LISTE_POS_INI_Y_H, LISTE_LARGEUR)
            
            if position == "autofocus":
                LISTE_POS_INI_X = []
                LISTE_POS_INI_Y_H = []
                LISTE_LARGEUR = []
                
            elif position == "tete gauche":
                print("tete gauche")
        

        #x -
        #y + h +


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    video.release()
    cv2.destroyAllWindows()









if __name__ == "__main__":

    video_capture()












