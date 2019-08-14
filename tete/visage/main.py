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
from initialisation import init_epaul
from initialisation import init_front
from initialisation import init_tempes
from initialisation import init_oreille


from tete import milieu_haut_tete
from tete import cotes_tete
from tete import cotes_frame
from tete import bouche
from tete import menton
from tete import buste
from tete import epaul
from tete import front
from tete import tempe
from tete import oreille


from config import SUBSTRACTOR
from config import SUBSTRACTOR1
from config import SUBSTRACTOR2
from config import SUBSTRACTOR3
from config import SUBSTRACTOR4
from config import SUBSTRACTOR5
from config import SUBSTRACTOR6
from config import SUBSTRACTOR7
from config import SUBSTRACTOR8
from config import SUBSTRACTOR9
from config import SUBSTRACTOR10
from config import SUBSTRACTOR11
from config import SUBSTRACTOR12
from config import SUBSTRACTOR13
from config import SUBSTRACTOR14




def video_capture():


    MILIEU_TETE = [[], [], [], []]
    COTE_TETE = [[], [], [], [], [], [], [], []]
    COTE_FRAME = [[], [], [], [], [], [], [], []]
    BOUCHE = [[], [], [], []]
    MENTON = [[], [], [], []]
    BUSTE = [[], [], [], []]
    EPAUL = [[], [], [], [], [], [], [], []]
    FRONT = [[], [], [], []]
    TEMPE = [[], [], [], [], [], [], [], []]
    OREILLE = [[], [], [], [], [], [], [], []]
    
    video = cv2.VideoCapture(0)
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")

    


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
            init_epaul(frame, faceCascade, EPAUL)
            init_front(frame, faceCascade, FRONT)
            init_tempes(frame, faceCascade, TEMPE)
            init_oreille(frame, faceCascade, OREILLE)


            
        else:
            milieu_haut_tete(frame, MILIEU_TETE, SUBSTRACTOR)
            cotes_tete(frame, COTE_TETE, SUBSTRACTOR1, SUBSTRACTOR2)
            cotes_frame(frame, COTE_FRAME, SUBSTRACTOR3, SUBSTRACTOR4)
            bouche(frame, BOUCHE, SUBSTRACTOR5)
            menton(frame, MENTON, SUBSTRACTOR6)
            buste(frame, BUSTE, SUBSTRACTOR7)
            epaul(frame, EPAUL, SUBSTRACTOR8, SUBSTRACTOR9)
            front(frame, FRONT, SUBSTRACTOR10)
            tempe(frame, TEMPE, SUBSTRACTOR11, SUBSTRACTOR12)
            oreille(frame, OREILLE, SUBSTRACTOR13, SUBSTRACTOR14)

    
        cv2.imshow('FACE', frame)

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    video.release()
    cv2.destroyAllWindows()









if __name__ == "__main__":

    video_capture()












