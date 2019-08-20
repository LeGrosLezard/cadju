import cv2
import numpy as np



from tete import init_tete_haut
from tete import init_cotes_tete
from tete import init_cotes_frame
from tete import init_bouche
from tete import init_menton
from tete import init_buste
from tete import init_epaul
from tete import init_front
from tete import init_tempes
from tete import init_oreille
from tete import init_mouvement

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

from tete import tete_mouvement

from config import *




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
##    try:
##        cv2.imshow('FACE POSITIONEMENT', POS)
##    except:
##        pass





LISTE = []
from traitement_image import position_tete_angle
from traitement_image import initialisation_pos

def head_position(LISTE, frame, eyesCascade, faceCascade):
    """Here we want find the meaning of head.
    Indeed empathy is that leans to the left.
    the head that leans to the right represents
    the reason. So we just get position of eyes.
    If one of them is lower of the other
    it want say the head is on this direction.
    For have this direction we can take the sum
    by initialisation."""
    
    if len(LISTE) < 10:
        initialisation_pos(frame, faceCascade, eyesCascade, LISTE)
            
    else:
        position1 = position_tete_angle(frame, faceCascade, eyesCascade, LISTE)

    cv2.imshow('FACE POSITION', frame)





LISTE_AJUSTEMENT = []
LISTE_DROITE_GAUCHE = []
LISTE_QUALIBRAGE = []
from traitement_image_yeux import pre_initialisation
from traitement_image_yeux import position_yeux_verticale
from traitement_image_yeux import qualibrage
from traitement_image_yeux import position_yeux_horizontal
from traitement_image_yeux import association


def eyes_position(eyes, frame, LISTE_AJUSTEMENT,
                  LISTE_DROITE_GAUCHE, LISTE_QUALIBRAGE):

    if len(LISTE_AJUSTEMENT) < 10:
        pre_initialisation(eyes, LISTE_AJUSTEMENT, frame)

    else:
        position1 = position_yeux_verticale(eyes, LISTE_AJUSTEMENT, frame)
        position2 = position_yeux_horizontal(eyes, LISTE_DROITE_GAUCHE, frame)

        association(position1, position2, LISTE_AJUSTEMENT)


        LISTE_QUALIBRAGE.append(position1)
        qualibration = qualibrage(LISTE_QUALIBRAGE)
        if qualibration == "qualibration":
            LISTE_AJUSTEMENT = []

        if position1 in ("le mec s'est baissé", "le mec s'est levé",
                         "le mec à levé la tete", "le mec à baisser la tete"):
            LISTE_AJUSTEMENT = []




    cv2.imshow('YEUX CAPTURE', frame)



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
        frame3 = cv2.resize(frame, (600, 600))
        
        face_area(frame, frame1, faceCascade)
        head_position(LISTE, frame2, eyesCascade, faceCascade)
        eyes_position(eyesCascade, frame3, LISTE_AJUSTEMENT,
                      LISTE_DROITE_GAUCHE, LISTE_QUALIBRAGE)

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    video.release()
    cv2.destroyAllWindows()






if __name__ == "__main__":
    video()








