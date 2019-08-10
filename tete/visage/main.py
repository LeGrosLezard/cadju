import numpy as np
import cv2
from PIL import Image
import os

from traitement import figure
from traitement import yeux





def video_capture():

    LISTE = []

    Ltempe_gauche = []
    Ltempe_droite = []
    
    Loreille_gauche1 = []
    Loreille_gauche2 = []
    Loreille_gauche3 = []
    Loreille_gauche4 = []
    Loreille_gauche5 = []
    Loreille_gauche6 = []
    
    Loreille_droite1 = []
    Loreille_droite2 = []
    Loreille_droite3 = []
    Loreille_droite4 = []
    Loreille_droite5 = []
    Loreille_droite6 = []

    Lcerne_droite1 = []
    Lcerne_droite2 = []
    Lcerne_droite3 = []
    Lcerne_droite4 = []
    Lcerne_droite5 = [] 

    Lcerne_gauche1 = []
    Lcerne_gauche2 = []
    Lcerne_gauche3 = []
    Lcerne_gauche4 = []
    Lcerne_gauche5 = []

    Lpomette_droite = []
    Lpomette_gauche = []

    Lfront1 = []
    Lfront2 = []
    Lfront3 = []
    Lfront4 = []

    Lbouche1 = []
    Lbouche2 = []
    Lbouche3 = []
    Lbouche4 = []
    Lbouche5 = []


    Lmillieu = []

    sourcile6 = []
    sourcile7 = []
    sourcile8 = []
    sourcile9 = []
    sourcile10 = []


    sourcile1 = []
    sourcile2 = []
    sourcile3 = []
    sourcile4 = []
    sourcile5 = []




    
    video = cv2.VideoCapture(0)
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
    eyesCascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    
    while(True):


        ret, frame = video.read()
        frame = cv2.resize(frame, (600, 600))

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if len(sourcile1) < 50:
            initialisation(frame, video, faceCascade, gray)
        else:

            yeux(frame, video, eyesCascade)
            figure(frame, video, faceCascade, gray)
            
            cv2.imshow('FACE CAPTURE', frame)



        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    video.release()
    cv2.destroyAllWindows()









if __name__ == "__main__":

    video_capture()












