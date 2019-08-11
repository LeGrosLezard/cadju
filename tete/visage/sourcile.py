import numpy as np
import cv2
from PIL import Image
import os


def parametres_plus(liste, nombre, pos):

    counter = 0

    for i in liste[-10:]:
        if pos > i + nombre:
            counter += 1

    return counter


def parametres_moins(liste, nombre, pos):

    counter = 0

    for i in liste[-10:]:
        if pos < i - nombre:
            counter += 1

    return counter

def trois_parametrages(parametre1, parametre2, parametre3):

    out = "non"

    if parametre1 > 5 and parametre2 > 5 and parametre3 > 5:
        out = "oui"

    return out


def sourciles_gauche1(frame, roi_color, x1, y1, w1, h1,
                     Lsourcile61, Lsourcile62, Lsourcile63):

    try:

        sourcile6 = cv2.circle(roi_color, (x1 + 5, y1 + 5), 1, (0,0,0), 2)
        sourcile6 = frame[y1 + 5, x1 + 5]

        couleur1 = parametres_plus(Lsourcile61, 15, sourcile6[0])
        couleur2 = parametres_plus(Lsourcile62, 15, sourcile6[1])
        couleur3 = parametres_plus(Lsourcile63, 15, sourcile6[2])

        add1 = trois_parametrages(couleur1, couleur2, couleur3)

        couleur4 = parametres_moins(Lsourcile61, 15, sourcile6[0])
        couleur5 = parametres_moins(Lsourcile62, 15, sourcile6[1])
        couleur6 = parametres_moins(Lsourcile63, 15, sourcile6[2])

        add2 = trois_parametrages(couleur4, couleur5, couleur6)

        if add1 == "non" and add2 == "non":
            Lsourcile61.append(frame[y1 + 5, x1 + 5][0])
            Lsourcile62.append(frame[y1 + 5, x1 + 5][1])
            Lsourcile63.append(frame[y1 + 5, x1 + 5][2])

            
        return add1, add2


        
        
    except:
        pass



def sourciles_gauche2(frame, roi_color, x1, y1, w1, h1,
                     Lsourcile71, Lsourcile72, Lsourcile73):

    try:

        sourcile7 = cv2.circle(roi_color, (x1 + 15, y1 + 5), 1, (0,0,0), 2)
        sourcile7 = frame[y1 + 15, x1 + 5]

        couleur1 = parametres_plus(Lsourcile71, 30, sourcile7[0])
        couleur2 = parametres_plus(Lsourcile72, 30, sourcile7[1])
        couleur3 = parametres_plus(Lsourcile73, 30, sourcile7[2])

        add1 = trois_parametrages(couleur1, couleur2, couleur3)

        couleur4 = parametres_moins(Lsourcile71, 30, sourcile7[0])
        couleur5 = parametres_moins(Lsourcile72, 30, sourcile7[1])
        couleur6 = parametres_moins(Lsourcile73, 30, sourcile7[2])

        add2 = trois_parametrages(couleur4, couleur5, couleur6)

        if add1 == "non" and add2 == "non":
            Lsourcile71.append(frame[y1 + 15, x1 + 5][0])
            Lsourcile72.append(frame[y1 + 15, x1 + 5][1])
            Lsourcile73.append(frame[y1 + 15, x1 + 5][2])

            
        return add1, add2
        
    except:
        pass





def sourciles(frame, roi_color, x1, y1, w1, h1,
              Lsourcile61, Lsourcile62, Lsourcile63,
              Lsourcile71, Lsourcile72, Lsourcile73):

    pts_un_plus, pts_un_moins = sourciles_gauche1(frame, roi_color, x1, y1, w1, h1,
                                                  Lsourcile61, Lsourcile62, Lsourcile63
    )
    
    pts_deux_plus, pts_deux_moins = sourciles_gauche2(frame, roi_color, x1, y1, w1, h1,
                                                      Lsourcile71, Lsourcile72, Lsourcile73
    )


    if pts_un_plus == "oui" and pts_deux_plus == "oui" or\
       pts_un_moins == "oui" and pts_deux_moins == "oui":
        print("sourcile gauche")

















