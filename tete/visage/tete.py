import numpy as np
import cv2




def milieu_haut_tete(frame, MILIEU_TETE):

    cTm_x1 = int(round(sum(MILIEU_TETE[0]) / len(MILIEU_TETE[0])))
    cTm_y1 = int(round(sum(MILIEU_TETE[1]) / len(MILIEU_TETE[1])))
    cTm_x2 = int(round(sum(MILIEU_TETE[2]) / len(MILIEU_TETE[2])))
    cTm_y2 = int(round(sum(MILIEU_TETE[3]) / len(MILIEU_TETE[3])))

    coul_M = 0, 0, 255
     
    cv2.rectangle(frame, (cTm_x1, cTm_y1), (cTm_x2, cTm_y2), (coul_M), 2)




def cotes_tete(frame, COTE_TETE):


    cTd_x1 = int(round(sum(COTE_TETE[0]) / len(COTE_TETE[0])))
    cTd_y1 = int(round(sum(COTE_TETE[1]) / len(COTE_TETE[1])))
    cTd_x2 = int(round(sum(COTE_TETE[2]) / len(COTE_TETE[2])))
    cTd_y2 = int(round(sum(COTE_TETE[3]) / len(COTE_TETE[3])))

    coul_D = 245,66,75

    cv2.rectangle(frame, (cTd_x1, cTd_y1), (cTd_x2, cTd_y2), (coul_D), 2)

    
    cTg_x1 = int(round(sum(COTE_TETE[4]) / len(COTE_TETE[4])))
    cTg_y1 = int(round(sum(COTE_TETE[5]) / len(COTE_TETE[5])))
    cTg_x2 = int(round(sum(COTE_TETE[6]) / len(COTE_TETE[6])))
    cTg_y2 = int(round(sum(COTE_TETE[7]) / len(COTE_TETE[7])))


    coul_G = 24,77,31

    cv2.rectangle(frame, (cTg_x1, cTg_y1), (cTg_x2, cTg_y2), (coul_G), 2)



def cotes_frame(frame, COTE_FRAME):
    
    cTd_x1 = int(round(sum(COTE_FRAME[0]) / len(COTE_FRAME[0])))
    cTd_y1 = int(round(sum(COTE_FRAME[1]) / len(COTE_FRAME[1])))
    cTd_x2 = int(round(sum(COTE_FRAME[2]) / len(COTE_FRAME[2])))
    cTd_y2 = int(round(sum(COTE_FRAME[3]) / len(COTE_FRAME[3])))

    coul_D = 245,66,75

    cv2.rectangle(frame, (cTd_x1, cTd_y1), (cTd_x2, cTd_y2), (coul_D), 3)

    cTg_x1 = int(round(sum(COTE_FRAME[4]) / len(COTE_FRAME[4])))
    cTg_y1 = int(round(sum(COTE_FRAME[5]) / len(COTE_FRAME[5])))
    cTg_x2 = int(round(sum(COTE_FRAME[6]) / len(COTE_FRAME[6])))
    cTg_y2 = int(round(sum(COTE_FRAME[7]) / len(COTE_FRAME[7])))

    coul_G = 24,77,31

    cv2.rectangle(frame, (cTg_x1, cTg_y1), (cTg_x2, cTg_y2), (coul_G), 3)


def bouche(frame, BOUCHE):
    
    cTb_x1 = int(round(sum(BOUCHE[0]) / len(BOUCHE[0])))
    cTb_y1 = int(round(sum(BOUCHE[1]) / len(BOUCHE[1])))
    cTb_x2 = int(round(sum(BOUCHE[2]) / len(BOUCHE[2])))
    cTb_y2 = int(round(sum(BOUCHE[3]) / len(BOUCHE[3])))

    coul_M = 0, 0, 255

    cv2.rectangle(frame, (cTb_x1, cTb_y1), (cTb_x2, cTb_y2), (coul_M), 2)



def menton(frame, MENTON):
    
    cTm_x1 = int(round(sum(MENTON[0]) / len(MENTON[0])))
    cTm_y1 = int(round(sum(MENTON[1]) / len(MENTON[1])))
    cTm_x2 = int(round(sum(MENTON[2]) / len(MENTON[2])))
    cTm_y2 = int(round(sum(MENTON[3]) / len(MENTON[3])))

    coul_M = 0, 0, 255

    cv2.rectangle(frame, (cTm_x1, cTm_y1), (cTm_x2, cTm_y2), (coul_M), 2)


def buste(frame, BUSTE):
    
    cTb_x1 = int(round(sum(BUSTE[0]) / len(BUSTE[0])))
    cTb_y1 = int(round(sum(BUSTE[1]) / len(BUSTE[1])))
    cTb_x2 = int(round(sum(BUSTE[2]) / len(BUSTE[2])))
    cTb_y2 = int(round(sum(BUSTE[3]) / len(BUSTE[3])))

    coul_M = 0, 0, 255

    cv2.rectangle(frame, (cTb_x1, cTb_y1), (cTb_x2, cTb_y2), (coul_M), 2)
























