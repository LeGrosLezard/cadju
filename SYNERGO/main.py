import cv2
import numpy as np


#------------------------------------------Side
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
from initialisation import init_mouvement


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


from tete_mouvement import tete_mouvement

from traitement_image import *



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
MOUVEMENT = [[], []]

LISTE = []

def reconfig(MILIEU_TETE, COTE_TETE, COTE_FRAME,
             BOUCHE, MENTON, BUSTE, EPAUL, FRONT,
             TEMPE, OREILLE, MOUVEMENT):
    
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
    MOUVEMENT = [[], []]

    
def face_area(frame_visage, frame_positionnement, faceCascade):
    

    if len(MILIEU_TETE[0]) < 1:
        init_mouvement(frame_visage, faceCascade, MOUVEMENT)
        init_tete_haut(frame_visage, faceCascade, MILIEU_TETE)
        init_cotes_tete(frame_visage, faceCascade, COTE_TETE)
        init_cotes_frame(frame_visage, faceCascade, COTE_FRAME)
        init_bouche(frame_visage, faceCascade, BOUCHE)
        init_menton(frame_visage, faceCascade, MENTON)
        init_buste(frame_visage, faceCascade, BUSTE)
        init_epaul(frame_visage, faceCascade, EPAUL)
        init_front(frame_visage, faceCascade, FRONT)
        init_tempes(frame_visage, faceCascade, TEMPE)
        init_oreille(frame_visage, faceCascade, OREILLE)

    else:
        INIT, POS = tete_mouvement(frame_positionnement, faceCascade, MOUVEMENT)

        if INIT is True:
            reconfig(MILIEU_TETE, COTE_TETE, COTE_FRAME,
                     BOUCHE, MENTON, BUSTE, EPAUL, FRONT,
                     TEMPE, OREILLE, MOUVEMENT)

        else:
            milieu_haut_tete(frame_visage, MILIEU_TETE, SUBSTRACTOR)
            cotes_tete(frame_visage, COTE_TETE, SUBSTRACTOR1, SUBSTRACTOR2)
            cotes_frame(frame_visage, COTE_FRAME, SUBSTRACTOR3, SUBSTRACTOR4)
            bouche(frame_visage, BOUCHE, SUBSTRACTOR5)
            menton(frame_visage, MENTON, SUBSTRACTOR6)
            buste(frame_visage, BUSTE, SUBSTRACTOR7)
            epaul(frame_visage, EPAUL, SUBSTRACTOR8, SUBSTRACTOR9)
            front(frame_visage, FRONT, SUBSTRACTOR10)
            tempe(frame_visage, TEMPE, SUBSTRACTOR11, SUBSTRACTOR12)
            oreille(frame_visage, OREILLE, SUBSTRACTOR13, SUBSTRACTOR14)


    cv2.imshow('FACE AREA', frame_visage)
    try:
        cv2.imshow('FACE POSITIONEMENT', POS)
    except:
        pass


def head_position(LISTE, frame, eyesCascade, faceCascade):
    if len(LISTE) < 50:
        initialisation_pos(frame, faceCascade, eyesCascade, LISTE)
            
    else:
        position1 = position_tete_angle(frame, faceCascade, eyesCascade, LISTE)

    cv2.imshow('FACE POSITION', frame)


def video():
    video = cv2.VideoCapture(0)
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
    eyesCascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    
    while(True):
        
        INIT = False
        _, frame = video.read()
        frame = cv2.resize(frame, (600, 600))
        frame1 = cv2.resize(frame, (600, 600))
        frame2 = cv2.resize(frame, (600, 600))
        
        face_area(frame, frame1, faceCascade)
        head_position(LISTE, frame2, eyesCascade, faceCascade)

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    video.release()
    cv2.destroyAllWindows()






if __name__ == "__main__":
    video()








