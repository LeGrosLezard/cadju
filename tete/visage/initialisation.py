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
        pass
 

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

def init_milieu():
    pass








    


