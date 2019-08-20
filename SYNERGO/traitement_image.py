import numpy as np
import cv2
from PIL import Image
import os

def initialisation_pos(frame, faceCascade, eyesCascade, LISTE):
    """Phase ou on récupere un modele de pts"""

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    

    c = 0
    for x1, y1, w1, h1 in faces:
    
        roi_gray = gray[y1:y1+h1, x1:x1+w1]
        roi_color = frame[y1:y1+h1, x1:x1+w1]
        
        eyes = eyesCascade.detectMultiScale(roi_gray,
            scaleFactor=1.3,
            minNeighbors=4,
            minSize=(40, 40),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        for x, y, w, h in eyes:

            cv2.rectangle(roi_color, (x,y), (x+w, y+h),(0, 0, 255), 2)
            
            if c == 1:
                x = x.tolist()
                LISTE.append(x)
            c+=1

    return frame


def cascade_config(frame, faceCascade, eyesCascade):
    """on définit ce qu'il faut detecter avec les parametres
    de match"""

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    
    eyes = eyesCascade.detectMultiScale(gray,
        scaleFactor=1.3,
        minNeighbors=4,
        minSize=(40, 40),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    return gray, faces, eyes


def position_oeil(gauche, droite, ok, LISTE, x_droite):
    """En gros le cadre switch de gauche a droite pcqu'on parcours
    la video ? et du coup ca prend l'un ou l'autre en 1er
    du coup on dit si oeil gauche/y in a oeil droite/y
    ET que x_droite (oeil droite position x) superieur a
    la liste(ensemble de pts initialisation) alors c gauche
    car le cadre et a gauche
    sinon le cadre est a droite verifie le plus grand
    EN GROS LE CADRE SWITCH ET C CHIANT DU COUP ON VERIFIE LE CADRE
    ET SA POSITION"""

    if gauche == 0 or droite == 0:
        pass
    else:
        
        if gauche < droite - 10 and x_droite > (sum(LISTE) / len(LISTE)) + 15:
            print("gauche")
            ok = True

        if ok is True:
            pass
        else:
            if gauche < droite - 10:
                print("droite")


def position_tete_angle(frame, faceCascade, eyesCascade, LISTE):

    gray, faces, _ = cascade_config(frame, faceCascade, eyesCascade)
    
    counter = 0
    
    gauche = 0
    droite = 0

    x_gauche = 0
    x_droite = 0

    liste_x = []
    ok = False

    #on prend x...h dans le cadre face
    for x1, y1, w1, h1 in faces:
        roi_gray = gray[y1:y1+h1, x1:x1+w1]
        roi_color = frame[y1:y1+h1, x1:x1+w1]

        eyes = eyesCascade.detectMultiScale(roi_gray,
            scaleFactor=1.3,
            minNeighbors=4,
            minSize=(40, 40),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        
        for x, y, w, h in eyes:

            if len(eyes) == 1:
                pass
                #on ne trouve qu'un oeil ? on passe
            
            else:
            
                y = y.tolist()
                x = x.tolist()

                if counter == 0:
                    cv2.rectangle(roi_color, (x,y), (x+w, y+h), 2)
                    gauche = y

                    
                if counter == 1:
                    cv2.rectangle(roi_color, (x,y), (x+w, y+h),(255, 0, 0), 2)
                    droite = y
                    x_droite = x
                    
                counter += 1


        position_oeil(gauche, droite, ok, LISTE, x_droite)
    


                
    
















