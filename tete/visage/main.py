import numpy as np
import cv2
from PIL import Image
import os


from initialisation import init_tete_haut
from initialisation import init_cotes_tete
from initialisation import init_cotes_frame
from initialisation import init_bouche
from initialisation import init_menton
from initialisation import init_buste


from tete import milieu_haut_tete
from tete import cotes_tete
from tete import cotes_frame
from tete import bouche
from tete import menton
from tete import buste



def video_capture():


    MILIEU_TETE = [[], [], [], []]
    COTE_TETE = [[], [], [], [], [], [], [], []]
    COTE_FRAME = [[], [], [], [], [], [], [], []]
    BOUCHE = [[], [], [], []]
    MENTON = [[], [], [], []]
    BUSTE = [[], [], [], []]
    
    video = cv2.VideoCapture(0)
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
    
    subtractor = cv2.createBackgroundSubtractorMOG2(history=100,
                                                    varThreshold=50,
                                                    detectShadows=True)

    while(True):


        ret, frame = video.read()
        frame = cv2.resize(frame, (600, 600))



        if len(MILIEU_TETE[0]) < 1:
            init_tete_haut(frame, faceCascade, MILIEU_TETE)
            init_cotes_tete(frame, faceCascade, COTE_TETE)
            init_cotes_frame(frame, faceCascade, COTE_FRAME)
            init_bouche(frame, faceCascade, BOUCHE)
            init_menton(frame, faceCascade, MENTON)
            init_buste(frame, faceCascade, BUSTE)
            
        else:
            milieu_haut_tete(frame, MILIEU_TETE)
            cotes_tete(frame, COTE_TETE)
            cotes_frame(frame, COTE_FRAME)
            bouche(frame, BOUCHE)
            menton(frame, MENTON)
            buste(frame, BUSTE)


        
       
        cv2.imshow('FACE', frame)

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    video.release()
    cv2.destroyAllWindows()









if __name__ == "__main__":

    video_capture()












