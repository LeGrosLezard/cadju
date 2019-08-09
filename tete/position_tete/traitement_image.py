import numpy as np
import cv2
from PIL import Image
import os


def initialisation(video, frame, faceCascade, LISTE_POS_INI_X,
                   LISTE_POS_INI_Y_H, LISTE_LARGEUR):
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);
    
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        
        x = x.tolist()
        y = y.tolist()
        h = h.tolist()
        w = w.tolist()

        LISTE_POS_INI_X.append(x)
        LISTE_POS_INI_Y_H.append(y + h)
        LISTE_LARGEUR.append(w)
        
    cv2.imshow('FACE CAPTURE', frame)


def position_tete(video, frame, faceCascade, LISTE_POS_INI_X,
                  LISTE_POS_INI_Y_H, LISTE_LARGEUR):

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);
    
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )


    for (x, y, w, h) in faces:

        x = x.tolist()
        y = y.tolist()
        h = h.tolist()
        w = w.tolist()

        if x < sum(LISTE_POS_INI_X)/len(LISTE_POS_INI_X) - 1 and\
           sum(LISTE_POS_INI_Y_H)/len(LISTE_POS_INI_Y_H) + 10 < y + w\
           > sum(LISTE_POS_INI_Y_H)/len(LISTE_POS_INI_Y_H) + 1 and\
           sum(LISTE_LARGEUR)/len(LISTE_LARGEUR) + 1 < w\
           > sum(LISTE_LARGEUR)/len(LISTE_LARGEUR) + 1:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            return "tete gauche"

        elif y + w > sum(LISTE_POS_INI_Y_H)/len(LISTE_POS_INI_Y_H) + 10 and\
           w > sum(LISTE_LARGEUR)/len(LISTE_LARGEUR) + 10:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            return "autofocus"
 
        else:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            LISTE_POS_INI_X.append(x)
            LISTE_POS_INI_Y_H.append(y + h)
            LISTE_LARGEUR.append(w)



    cv2.imshow('FACE CAPTURE', frame)



#si trop rouge approché













