import numpy as np
import cv2 
from PIL import Image
import os

#-------------------------------------------------------------INITIALIZATION FUNCTIONS
def pre_initialisation(eyes, liste, frame):
    """we detect the position of the eyes"""

    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(frame, (ex,ey), (ex+ew, ey+eh), 0)
        liste.append(ey)



def qualibrage(QUALIFER_LIST):

    if QUALIFER_LIST[-10:] in ("the person looks up",
                                "the person to look down",
                                "the person bent down",
                                "the person lifted his head",
                                "the person got up",
                                "the person dropped his head"):
        return "qualibration"

#------------------------------------------------------------Y EYE FUNCTIONS
    
        
def y_eye_position(eyes, liste, frame):
    """a mark has been defined with the initialization.
    Now we continue our eyes and their position
    by contributing to the reference"""

    for (ex, ey, ew, eh) in eyes:

        cv2.rectangle(frame, (ex,ey), (ex+ew, ey+eh), 2)

        #  -100px on y axis
        if ey < sum(liste)/len(liste) - 100:
            return "the person got up"
 
        #  +100px on y axis
        elif ey > sum(liste)/len(liste) + 150: 
            return "the person bent down"

        #  -100px on y axis
        elif ey < sum(liste)/len(liste) - 20:
            return "the person lifted his head"

        #  +20px on y axis
        elif ey > sum(liste)/len(liste) + 20: 
            return "the person has dropped his head"

        #  -5px on y axis
        elif ey < sum(liste)/len(liste) - 5:
            return "the person looks up"

        #  +30px on y axis
        elif ey > sum(liste)/len(liste) + 60: 
            return "the person to look down"




#------------------------------------------------------------X EYE FUNCTIONS
def x_movement(ex, ew, LISTE_RIGHT_LEFT):
    """ """

    try:
        #We don't count the return of the eye
        if LISTE_RIGHT_LEFT[-2] != "retour":

            if round(int(ex+(ew/2))) < LISTE_RIGHT_LEFT[-2] - 3 or\
               round(int(ex+(ew/2))) > LISTE_RIGHT_LEFT[-2] + 4:
                pass
                # + 3 and - 4 are considere like a head movement

            else:
                try:
                    if LISTE_RIGHT_LEFT[-2] - 3 < round(int(ex+(ew/2))) < LISTE_RIGHT_LEFT[-2] - 1:
                        LISTE_RIGHT_LEFT.append("retour")
                        return "left"
                    
                    elif LISTE_RIGHT_LEFT[-2] + 4 > round(int(ex+(ew/2))) > LISTE_RIGHT_LEFT[-2] + 1:
                       LISTE_RIGHT_LEFT.append("retour")
                       return "right"
                except TypeError:
                    pass
    except IndexError:
        pass


def x_eye_position(eyes, LISTE_RIGHT_LEFT, frame):

    counter = 0

    if len(eyes) == 1:
        pass
    else:

        for (ex, ey, ew, eh) in eyes:

            cv2.rectangle(frame, (ex,ey), (ex+ew, ey+eh), 2)
            cv2.circle(frame, (round(int(ex+(ew/2))),
                        round(int(ey+(eh/2+5)))), 3, (0, 0, 255), 5)

            if counter == 0:
                #We only take right eye
                LISTE_RIGHT_LEFT.append(round(int(ex+(ew/2))))


                position = x_movement(ex, ew, LISTE_RIGHT_LEFT)
                if position != None:
                    return position
       

            counter += 1



#------------------------------------------------------------------MESSAGE FUNCTION
def association(position1, position2, LISTE_AJUSTEMENT):

    if position1 == None:
        pass

    if position2 == None:
        pass

    if position1 and position2:
        if position1 == "le mec regarde en HAUT" and\
           position2 == "gauche":
            print("le mec a regarder en haut a gauche")
            
        elif position1 == "le mec regarde en HAUT" and\
             position2 == "droite":
            print("le mec a regarder en haut a droite")
            
        elif position1 == "le mec regarde en bas" and\
             position2 == "droite":
            print("le mec a regarder en bas a droite")
            
        elif position1 == "le mec regarde en bas" and\
             position2 == "gauche":
            print("le mec a regarder en bas a gauche")

    
    elif position1:
        print(position1)

    elif position2:
        print(position2)

