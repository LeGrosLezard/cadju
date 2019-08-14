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
    dessus_milieu_2 = y - int(round(60 * 100 / h))
    
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
    cTd_y1 = y - int(round(100 * 100 / h))
    cTd_y2 = y - int(round(10 * 100 / h))

    coul_D = 245,66,75

    cv2.rectangle(frame, (cTd_x1, cTd_y1), (cTd_x2, cTd_y2), (coul_D), 2)


    cTg_x1 = x + w - 20
    cTg_x2 = x + w + 30
    cTg_y1 = y - int(round(100 * 100 / h))
    cTg_y2 = y - int(round(10 * 100 / h))

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
    cTb_y1 = y + h + 80
    cTb_x2 = x + w
    cTb_y2 = y + h + 150


    coul_M = 0, 0, 255

    cv2.rectangle(frame,(cTb_x1, cTb_y1), (cTb_x2, cTb_y2), (coul_M), 1)

    liste = [cTb_x1, cTb_y1, cTb_x2, cTb_y2]

    c = 0
    for i in liste:
        BUSTE[c].append(i)
        c+=1





















    


