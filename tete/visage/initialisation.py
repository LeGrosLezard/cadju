import numpy as np
import cv2


def detection_face(frame, faceCascade):
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    try:
        faces = faces[0].tolist()

        return faces[0], faces[1], faces[2], faces[3]

    except IndexError:
        return 1, 1, 1, 1
 

def init_tete_haut(frame, faceCascade, MILIEU_TETE):

    x, y, w, h = detection_face(frame, faceCascade)


    dessus_milieu_1 = y - int(round(150 * 100 / h))
    dessus_milieu_2 = y - int(round(80 * 100 / h))
    
    carre = int(round(w/3))


    cTm_x1 = x + carre
    cTm_x2 = x + carre * 2
    cTm_y1 = dessus_milieu_1
    cTm_y2 = dessus_milieu_2

    coul_M = 0, 0, 255

    cv2.rectangle(frame, (cTm_x1, cTm_y1), (cTm_x2, cTm_y2), (coul_M), 2)

    liste = [cTm_x1, cTm_y1, cTm_x2, cTm_y2]

    c = 0
    for i in liste:
        MILIEU_TETE[c].append(i)
        c+=1

def init_cotes_tete(frame, faceCascade, COTE_TETE):

    x, y, w, h = detection_face(frame, faceCascade)

    cTd_x1 = x - 20
    cTd_x2 = x + 30
    cTd_y1 = y - int(round(110 * 100 / h))
    cTd_y2 = y - int(round(50 * 100 / h))

    coul_D = 245,66,75

    cv2.rectangle(frame, (cTd_x1, cTd_y1), (cTd_x2, cTd_y2), (coul_D), 2)


    cTg_x1 = x + w - 20
    cTg_x2 = x + w + 30
    cTg_y1 = y - int(round(100 * 100 / h))
    cTg_y2 = y - int(round(40 * 100 / h))

    coul_G = 24,77,31

    cv2.rectangle(frame, (cTg_x1, cTg_y1), (cTg_x2, cTg_y2), (coul_G), 2)


    liste = [cTd_x1, cTd_y1, cTd_x2, cTd_y2,
             cTg_x1, cTg_y1, cTg_x2, cTg_y2]

    c = 0
    for i in liste:
        COTE_TETE[c].append(i)
        c+=1



def init_cotes_frame(frame, faceCascade, COTE_FRAME):
    
    x, y, w, h = detection_face(frame, faceCascade)

    cTd_x1 = x - w - 30
    cTd_x2 = x - 60
    cTd_y1 = y
    cTd_y2 = y + h - 30

    coul_D = 245,66,75

    cv2.rectangle(frame, (cTd_x1, cTd_y1), (cTd_x2, cTd_y2), (coul_D), 3)

    cTg_x1 = x + w + 60
    cTg_x2 = x + w * 2 + 30
    cTg_y1 = y
    cTg_y2 = y + h - 30

    coul_G = 24,77,31

    cv2.rectangle(frame, (cTg_x1, cTg_y1), (cTg_x2, cTg_y2), (coul_G), 3)



    liste = [cTd_x1, cTd_y1, cTd_x2, cTd_y2,
             cTg_x1, cTg_y1, cTg_x2, cTg_y2]

    c = 0
    for i in liste:
        COTE_FRAME[c].append(i)
        c+=1



def init_bouche(frame, faceCascade, BOUCHE):

    x, y, w, h = detection_face(frame, faceCascade)

    carre = int(round(w/3))
    hauteur = y + h - 20

    cTb_x1 = x + carre
    cTb_y1 = hauteur
    cTb_x2 = x + carre * 2
    cTb_y2 = y + h - 5


    coul_M = 0, 0, 255
    
    cv2.rectangle(frame,(cTb_x1, cTb_y1), (cTb_x2, cTb_y2), (coul_M), 1)

    liste = [cTb_x1, cTb_y1, cTb_x2, cTb_y2]

    c = 0
    for i in liste:
        BOUCHE[c].append(i)
        c+=1
        

def init_menton(frame, faceCascade, MENTON):

    x, y, w, h = detection_face(frame, faceCascade)

    carre = int(round(w/3))
    hauteur = y + h - 40

    cTm_x1 = x + carre
    cTm_y1 = y + h + 10
    cTm_x2 = x + carre * 2
    cTm_y2 = y + h + 25


    coul_M = 0, 0, 255

    cv2.rectangle(frame,(cTm_x1, cTm_y1), (cTm_x2, cTm_y2), (coul_M), 1)

    liste = [cTm_x1, cTm_y1, cTm_x2, cTm_y2]

    c = 0
    for i in liste:
        MENTON[c].append(i)
        c+=1

def init_buste(frame, faceCascade, BUSTE):
    
    x, y, w, h = detection_face(frame, faceCascade)

    carre = int(round(w/3))
    hauteur = y + h - 40

    cTb_x1 = x
    cTb_y1 = y + h + 120
    cTb_x2 = x + w
    cTb_y2 = y + h + 180


    coul_M = 0, 0, 255

    cv2.rectangle(frame,(cTb_x1, cTb_y1), (cTb_x2, cTb_y2), (coul_M), 1)

    liste = [cTb_x1, cTb_y1, cTb_x2, cTb_y2]

    c = 0
    for i in liste:
        BUSTE[c].append(i)
        c+=1


def init_epaul(frame, faceCascade, EPAUL):

    x, y, w, h = detection_face(frame, faceCascade)

    cTed_x1 = x - 50
    cTed_y1 = y + h + 20
    cTed_x2 = x + 30
    cTed_y2 = y + h + 60

    coul_D = 245,66,75
    
    cv2.rectangle(frame, (cTed_x1, cTed_y1), (cTed_x2, cTed_y2), (coul_D), 1)


    cTeg_x1 = x + w - 30
    cTeg_y1 = y + h + 20
    cTeg_x2 = x + w + 30
    cTeg_y2 = y + h + 60

    coul_G = 24,77,31

    cv2.rectangle(frame,(cTeg_x1, cTeg_y1), (cTeg_x2, cTeg_y2), (coul_G), 1)



    liste = [cTed_x1, cTed_y1, cTed_x2, cTed_y2,
             cTeg_x1, cTeg_y1, cTeg_x2, cTeg_y2]

    c = 0
    for i in liste:
        EPAUL[c].append(i)
        c+=1



def init_front(frame, faceCascade, FRONT):

    x, y, w, h = detection_face(frame, faceCascade)

    
    dessus_milieu_1 = y - int(round(30 * 100 / h))
    dessus_milieu_2 = y - int(round(-40 * 100 / h))
    
    carre = int(round(w/3))


    cTf_x1 = x + 30
    cTf_x2 = x + w - 30
    cTf_y1 = dessus_milieu_1
    cTf_y2 = dessus_milieu_2

    coul_M = 0, 0, 255

    cv2.rectangle(frame, (cTf_x1, cTf_y1), (cTf_x2, cTf_y2), (coul_M), 2)

    liste = [cTf_x1, cTf_y1, cTf_x2, cTf_y2]

    c = 0
    for i in liste:
        FRONT[c].append(i)
        c+=1



def init_tempes(frame, faceCascade, TEMPE):
    
    x, y, w, h = detection_face(frame, faceCascade)

    cTed_x1 = x - 40
    cTed_y1 = y - 20
    cTed_x2 = x
    cTed_y2 = y + 40


    coul_D = 245,66,75
    
    cv2.rectangle(frame,(cTed_x1, cTed_y1), (cTed_x2, cTed_y2), (coul_D), 1)


    cTeg_x1 = x + w
    cTeg_y1 = y + 40
    cTeg_x2 = x + w + 40
    cTeg_y2 = y - 20 

    coul_G = 24,77,31

    cv2.rectangle(frame,(cTeg_x1, cTeg_y1), (cTeg_x2, cTeg_y2), (coul_G), 1)



    liste = [cTed_x1, cTed_y1, cTed_x2, cTed_y2,
             cTeg_x1, cTeg_y1, cTeg_x2, cTeg_y2]

    c = 0
    for i in liste:
        TEMPE[c].append(i)
        c+=1


def init_oreille(frame, faceCascade, OREILLE):
    
    x, y, w, h = detection_face(frame, faceCascade)

    cTod_x1 = x - 40
    cTod_y1 = y + 70
    cTod_x2 = x
    cTod_y2 = y + 110

    coul_D = 245,66,75
    
    cv2.rectangle(frame,(cTod_x1, cTod_y1), (cTod_x2, cTod_y2), (coul_D), 1)


    cTog_x1 = x + w + 40
    cTog_y1 = y + 70
    cTog_x2 = x + w
    cTog_y2 = y + 110

    coul_G = 24,77,31

    cv2.rectangle(frame,(cTog_x1, cTog_y1), (cTog_x2, cTog_y2), (), 1)



    liste = [cTod_x1, cTod_y1, cTod_x2, cTod_y2,
             cTog_x1, cTog_y1, cTog_x2, cTog_y2]

    c = 0
    for i in liste:
        OREILLE[c].append(i)
        c+=1










    


