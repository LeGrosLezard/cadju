import numpy as np
import cv2



from substractor import substractor_haut_tete
def milieu_haut_tete(frame, MILIEU_TETE, subtractor):

    cTm_x1 = int(round(sum(MILIEU_TETE[0]) / len(MILIEU_TETE[0])))
    cTm_y1 = int(round(sum(MILIEU_TETE[1]) / len(MILIEU_TETE[1])))
    cTm_x2 = int(round(sum(MILIEU_TETE[2]) / len(MILIEU_TETE[2])))
    cTm_y2 = int(round(sum(MILIEU_TETE[3]) / len(MILIEU_TETE[3])))

    coul_M = 0, 0, 255
     
    cv2.rectangle(frame, (cTm_x1, cTm_y1), (cTm_x2, cTm_y2), (coul_M), 2)

    substractor_haut_tete(frame, cTm_y2, cTm_y1, cTm_x1, cTm_x2, subtractor)


from substractor import substractor_cote_tete_droit
from substractor import substractor_cote_tete_gauche
def cotes_tete(frame, COTE_TETE, subtractor1, subtractor2):


    cTd_x1 = int(round(sum(COTE_TETE[0]) / len(COTE_TETE[0])))
    cTd_y1 = int(round(sum(COTE_TETE[1]) / len(COTE_TETE[1])))
    cTd_x2 = int(round(sum(COTE_TETE[2]) / len(COTE_TETE[2])))
    cTd_y2 = int(round(sum(COTE_TETE[3]) / len(COTE_TETE[3])))

    coul_D = 0,0,255

    cv2.rectangle(frame, (cTd_x1, cTd_y1), (cTd_x2, cTd_y2), (coul_D), 2)
    substractor_cote_tete_droit(frame, cTd_y2, cTd_y1, cTd_x1, cTd_x2,
                                 subtractor1)
    
    cTg_x1 = int(round(sum(COTE_TETE[4]) / len(COTE_TETE[4])))
    cTg_y1 = int(round(sum(COTE_TETE[5]) / len(COTE_TETE[5])))
    cTg_x2 = int(round(sum(COTE_TETE[6]) / len(COTE_TETE[6])))
    cTg_y2 = int(round(sum(COTE_TETE[7]) / len(COTE_TETE[7])))


    coul_G = 24,77,31

    cv2.rectangle(frame, (cTg_x1, cTg_y1), (cTg_x2, cTg_y2), (coul_G), 2)
    substractor_cote_tete_gauche(frame, cTg_y2, cTg_y1, cTg_x1, cTg_x2, subtractor2)


from substractor import substractor_cote_tete_frame_droit
from substractor import substractor_cote_tete_frame_gauche
def cotes_frame(frame, COTE_FRAME, subtractor1, subtractor2):
    
    cTd_x1 = int(round(sum(COTE_FRAME[0]) / len(COTE_FRAME[0])))
    cTd_y1 = int(round(sum(COTE_FRAME[1]) / len(COTE_FRAME[1])))
    cTd_x2 = int(round(sum(COTE_FRAME[2]) / len(COTE_FRAME[2])))
    cTd_y2 = int(round(sum(COTE_FRAME[3]) / len(COTE_FRAME[3])))

    coul_D = 245,66,75

    cv2.rectangle(frame, (cTd_x1, cTd_y1), (cTd_x2, cTd_y2), (coul_D), 3)
    substractor_cote_tete_frame_droit(frame, cTd_y2, cTd_y1, cTd_x1, cTd_x2,
                                      subtractor1)



    cTg_x1 = int(round(sum(COTE_FRAME[4]) / len(COTE_FRAME[4])))
    cTg_y1 = int(round(sum(COTE_FRAME[5]) / len(COTE_FRAME[5])))
    cTg_x2 = int(round(sum(COTE_FRAME[6]) / len(COTE_FRAME[6])))
    cTg_y2 = int(round(sum(COTE_FRAME[7]) / len(COTE_FRAME[7])))

    coul_G = 24,77,31

    cv2.rectangle(frame, (cTg_x1, cTg_y1), (cTg_x2, cTg_y2), (coul_G), 3)
    substractor_cote_tete_frame_gauche(frame, cTg_y2, cTg_y1, cTg_x1, cTg_x2,
                                       subtractor2)


from substractor import substractor_bouche
def bouche(frame, BOUCHE, subtractor):
    
    cTb_x1 = int(round(sum(BOUCHE[0]) / len(BOUCHE[0])))
    cTb_y1 = int(round(sum(BOUCHE[1]) / len(BOUCHE[1])))
    cTb_x2 = int(round(sum(BOUCHE[2]) / len(BOUCHE[2])))
    cTb_y2 = int(round(sum(BOUCHE[3]) / len(BOUCHE[3])))

    coul_M = 0, 0, 255

    cv2.rectangle(frame, (cTb_x1, cTb_y1), (cTb_x2, cTb_y2), (coul_M), 2)
    substractor_bouche(frame, cTb_y2, cTb_y1, cTb_x1, cTb_x2, subtractor)



from substractor import substractor_menton
def menton(frame, MENTON, subtractor):
    
    cTm_x1 = int(round(sum(MENTON[0]) / len(MENTON[0])))
    cTm_y1 = int(round(sum(MENTON[1]) / len(MENTON[1])))
    cTm_x2 = int(round(sum(MENTON[2]) / len(MENTON[2])))
    cTm_y2 = int(round(sum(MENTON[3]) / len(MENTON[3])))

    coul_M = 0, 0, 255

    cv2.rectangle(frame, (cTm_x1, cTm_y1), (cTm_x2, cTm_y2), (coul_M), 2)
    substractor_menton(frame, cTm_y2, cTm_y1, cTm_x1, cTm_x2, subtractor)

    
from substractor import substractor_buste
def buste(frame, BUSTE, subtractor):
    
    cTb_x1 = int(round(sum(BUSTE[0]) / len(BUSTE[0])))
    cTb_y1 = int(round(sum(BUSTE[1]) / len(BUSTE[1])))
    cTb_x2 = int(round(sum(BUSTE[2]) / len(BUSTE[2])))
    cTb_y2 = int(round(sum(BUSTE[3]) / len(BUSTE[3])))

    coul_M = 0, 0, 255

    cv2.rectangle(frame, (cTb_x1, cTb_y1), (cTb_x2, cTb_y2), (coul_M), 2)
    substractor_buste(frame, cTb_y2, cTb_y1, cTb_x1, cTb_x2, subtractor)

    
from substractor import substractor_epaul_droite
from substractor import substractor_epaul_gauche
def epaul(frame, EPAUL, subtractor1, subtractor2):

    cTed_x1 = int(round(sum(EPAUL[0]) / len(EPAUL[0])))
    cTed_y1 = int(round(sum(EPAUL[1]) / len(EPAUL[1])))
    cTed_x2 = int(round(sum(EPAUL[2]) / len(EPAUL[2])))
    cTed_y2 = int(round(sum(EPAUL[3]) / len(EPAUL[3])))

    cTeg_x1 = int(round(sum(EPAUL[4]) / len(EPAUL[4])))
    cTeg_y1 = int(round(sum(EPAUL[5]) / len(EPAUL[5])))
    cTeg_x2 = int(round(sum(EPAUL[6]) / len(EPAUL[6])))
    cTeg_y2 = int(round(sum(EPAUL[7]) / len(EPAUL[7])))


    coul_D = 245,66,75
    coul_G = 24,77,31

    cv2.rectangle(frame, (cTed_x1, cTed_y1), (cTed_x2, cTed_y2), (coul_D), 1)
    substractor_epaul_droite(frame, cTed_y2, cTed_y1, cTed_x1, cTed_x2,
                             subtractor1)

    
    cv2.rectangle(frame,(cTeg_x1, cTeg_y1), (cTeg_x2, cTeg_y2), (coul_G), 1)
    substractor_epaul_gauche(frame, cTeg_y2, cTeg_y1, cTeg_x1, cTeg_x2,
                             subtractor2)
    

from substractor import substractor_front
def front(frame, FRONT, subtractor):

    cTf_x1 = int(round(sum(FRONT[0]) / len(FRONT[0])))
    cTf_y1 = int(round(sum(FRONT[1]) / len(FRONT[1])))
    cTf_x2 = int(round(sum(FRONT[2]) / len(FRONT[2])))
    cTed_y2 = int(round(sum(FRONT[3]) / len(FRONT[3])))


    coul_M = 0, 0, 255
    
    cv2.rectangle(frame, (cTf_x1, cTf_y1), (cTf_x2, cTed_y2), (coul_M), 1)
    substractor_front(frame, cTed_y2, cTf_y1, cTf_x1, cTf_x2, subtractor)

    
from substractor import substractor_tempe_droite
from substractor import substractor_tempe_gauche
def tempe(frame, TEMPE, subtractor1, subtractor2):

    cTtd_x1 = int(round(sum(TEMPE[0]) / len(TEMPE[0])))
    cTtd_y1 = int(round(sum(TEMPE[1]) / len(TEMPE[1])))
    cTtd_x2 = int(round(sum(TEMPE[2]) / len(TEMPE[2])))
    cTtd_y2 = int(round(sum(TEMPE[3]) / len(TEMPE[3])))

    cTtg_x1 = int(round(sum(TEMPE[4]) / len(TEMPE[4])))
    cTtg_y1 = int(round(sum(TEMPE[5]) / len(TEMPE[5])))
    cTtg_x2 = int(round(sum(TEMPE[6]) / len(TEMPE[6])))
    cTtg_y2 = int(round(sum(TEMPE[7]) / len(TEMPE[7])))


    coul_D = 245,66,75
    coul_G = 24,77,31

    cv2.rectangle(frame, (cTtd_x1, cTtd_y1), (cTtd_x2, cTtd_y2), (coul_D), 1)
    substractor_tempe_droite(frame, cTtd_y2, cTtd_y1, cTtd_x1, cTtd_x2,
                             subtractor1)

    
    cv2.rectangle(frame,(cTtg_x1, cTtg_y1), (cTtg_x2, cTtg_y2), (coul_G), 1)
    substractor_tempe_gauche(frame, cTtg_y1, cTtg_y2, cTtg_x1, cTtg_x2,
                             subtractor2)


from substractor import substractor_oreille_droite
from substractor import substractor_oreille_gauche
def oreille(frame, OREILLE, subtractor1, subtractor2):

    cTod_x1 = int(round(sum(OREILLE[0]) / len(OREILLE[0])))
    cTod_y1 = int(round(sum(OREILLE[1]) / len(OREILLE[1])))
    cTod_x2 = int(round(sum(OREILLE[2]) / len(OREILLE[2])))
    cTod_y2 = int(round(sum(OREILLE[3]) / len(OREILLE[3])))

    cTog_x1 = int(round(sum(OREILLE[4]) / len(OREILLE[4])))
    cTog_y1 = int(round(sum(OREILLE[5]) / len(OREILLE[5])))
    cTog_x2 = int(round(sum(OREILLE[6]) / len(OREILLE[6])))
    cTog_y2 = int(round(sum(OREILLE[7]) / len(OREILLE[7])))


    coul_D = 245,66,75
    coul_G = 24,77,31

    cv2.rectangle(frame, (cTod_x1, cTod_y1), (cTod_x2, cTod_y2), (coul_D), 1)
    substractor_oreille_droite(frame, cTod_y1, cTod_y2, cTod_x1, cTod_x2,
                               subtractor1)


    cv2.rectangle(frame,(cTog_x1, cTog_y1), (cTog_x2, cTog_y2), (coul_G), 1)
    substractor_oreille_gauche(frame, cTog_y1, cTog_y2, cTog_x1, cTog_x2,
                               subtractor2)







