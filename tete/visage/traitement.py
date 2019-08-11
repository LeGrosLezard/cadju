import numpy as np
import cv2
from PIL import Image
import os

def face_config(faceCascade, gray):
    faces = faceCascade.detectMultiScale(gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    ) 

    return faces

def eyes_config(eyesCascade, roi_gray):
    eyes = eyesCascade.detectMultiScale(roi_gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    ) 

    return eyes


def parametres_plus(liste, nombre, pos):

    counter = 0

    for i in liste[-10:]:
        if pos > i + nombre:
            counter += 1

    return counter


def parametres_moins(liste, nombre, pos):

    counter = 0

    for i in liste[-11:-1]:
        if pos < i - nombre:

            counter += 1

    return counter

def trois_parametrages(parametre1, parametre2, parametre3, mot):

    if parametre1 > 8 and parametre2 > 8 and parametre3 > 8:
        print("ouiiiiiiiiiiiiiiiiiiiiiiii" + " " + mot)


def sourciles_droit(frame, roi_color, x1, y1, w1, h1,
                    Lsourcile61, Lsourcile62, Lsourcile63):

    try:
        Lsourcile61.append(frame[y1 + 5, x1 + 5][0])
        Lsourcile62.append(frame[y1 + 5, x1 + 5][1])
        Lsourcile63.append(frame[y1 + 5, x1 + 5][2])
        
        sourcile6 = cv2.circle(roi_color, (x1 + 5, y1 + 5), 1, (0,0,0), 2)
        sourcile6 = frame[y1 + 5, x1 + 5]

        couleur1 = parametres_plus(Lsourcile61, 20, sourcile6[0])
        couleur2 = parametres_plus(Lsourcile62, 20, sourcile6[1])
        couleur3 = parametres_plus(Lsourcile63, 20, sourcile6[2])

        trois_parametrages(couleur1, couleur2, couleur3, "ici")

        couleur4 = parametres_moins(Lsourcile61, 20, sourcile6[0])
        couleur5 = parametres_moins(Lsourcile62, 20, sourcile6[1])
        couleur6 = parametres_moins(Lsourcile63, 20, sourcile6[2])

        trois_parametrages(couleur4, couleur5, couleur6, "ka")
        
    except:
        pass

    #print(sourcile6[0], sourcile6[1], sourcile6[2])




def yeux(frame, video, eyesCascade, faceCascade, gray,
         Lsourcile61, Lsourcile62, Lsourcile63):

    faces = face_config(faceCascade, gray)

    for x, y, w, h in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eyes_config(eyesCascade, roi_gray)


        oeil = 0
        
        pos1_x = 0
        pos1_y = 0

        pos2_x = 0
        pos2_y = 0
        
        for x1, y1, w1, h1 in eyes:
            
            if oeil == 0:
                #cv2.rectangle(roi_color, (x1, y1), (x1 + w1, y1 + h1),(0, 0, 255), 2)
                
                pos1_x = x1.tolist() + w1.tolist()
                pos1_y = y1.tolist()

                #SOURCILE DROIT
                sourciles_droit(frame, roi_color, x1, y1, w1, h1,
                                Lsourcile61, Lsourcile62, Lsourcile63
                )


            elif oeil == 1:
                #cv2.rectangle(roi_color, (x1, y1), (x1 + w1, y1 + h1),(0, 0, 0), 2)
                
                pos2_x = x1.tolist()
                pos2_y = y1.tolist()

                

            oeil += 1


        definition_oeil(roi_color, pos1_x, pos2_x, pos1_y, pos2_y)
































def definition_oeil(frame, pos1_x, pos2_x, pos1_y, pos2_y):

    un = 0
    deux = 0
    unun = 0
    deuxdeux = 0
    
    x = 0
    y = 0
    
    if pos1_x < pos2_x:
        un = pos1_x
        deux = pos2_x

        unun = pos1_y
        deuxdeux = pos2_y

        x = (un + deux)/2
        y = (unun + deuxdeux)/2


    elif pos1_x > pos2_x:
        deux = pos1_x
        un = pos2_x

        unun = pos2_y
        deuxdeux = pos1_y

        x = (un + deux)/2
        y = (unun + deuxdeux)/2
        y = int(round(y))

    if x == 0 or y == 0:
        pass
    else:
        entre_oeil = cv2.circle(frame, (int(round(x)), int(round(y))), 1, (255,0,0), 2)

















