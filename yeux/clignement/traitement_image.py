import numpy as np
import cv2 
from PIL import Image
import os




def pre_initialisation(eyes, liste, frame):
    """Ici si repere est inférieur a 100
    on ajoute les lignes dans la liste"""


    for (ex, ey, ew, eh) in eyes:

        cv2.rectangle(frame, (ex,ey), (ex+ew, ey+eh), 0)
        
        ey = ey.tolist()
        liste.append(ey)

        
def position_yeux_verticale(eyes, liste, frame):
    """Si repere est superieur a 100
    c'est qu'on a fini la premiere initialisation"""

    
    for (ex, ey, ew, eh) in eyes:

        cv2.rectangle(frame, (ex,ey), (ex+ew, ey+eh), 2)

        if ey < sum(liste)/len(liste) - 90:
            return "le mec s'est levé"
            
        elif ey > sum(liste)/len(liste) + 90: 
            return "le mec s'est baissé"

        elif ey < sum(liste)/len(liste) - 20:
            return "le mec à levé la tete"
            
        elif ey > sum(liste)/len(liste) + 20: 
            return "le mec à baisser la tete"

        elif ey < sum(liste)/len(liste) - 5:
            return "le mec regarde en HAUT"
        
        elif ey > sum(liste)/len(liste) + 5: 
            return "le mec regarde en bas"


def qualibrage(LISTE_QUALIBRAGE):
    if LISTE_QUALIBRAGE[-10:] in ("le mec regarde en HAUT",
                                  "le mec regarde en bas"):
        return "qualibration"


def position_yeux_horizontal(eyes, LISTE_DROITE_GAUCHE, frame):

    c = 0

    if len(eyes) == 1:
        pass
    else:
    
        for (ex, ey, ew, eh) in eyes:

            cv2.rectangle(frame, (ex,ey), (ex+ew, ey+eh), 2)
                
            cv2.circle(frame, (round(int(ex+(ew/2))),
                        round(int(ey+(eh/2+5)))), 3, (0, 0, 255), 5)


            if c == 0:
                #On prend uniquement pour l'oeil droit

                ex = ex.tolist()
                ew = ew.tolist()
                LISTE_DROITE_GAUCHE.append(round(int(ex+(ew/2))))

                try:


                    if LISTE_DROITE_GAUCHE[-2] == "retour":
                        pass
                        #On evite le retour de l'oeil

                    else:

                        if round(int(ex+(ew/2))) < LISTE_DROITE_GAUCHE[-2] - 3 or\
                           round(int(ex+(ew/2))) > LISTE_DROITE_GAUCHE[-2] + 4:
                            pass
                            #car a + 3 et - 4 on considere que c'est la tete qui bouge
                        
                        else:

                            if round(int(ex+(ew/2))) < LISTE_DROITE_GAUCHE[-2] - 1:
                                LISTE_DROITE_GAUCHE.append("retour")
                                return "gauche"
                            
                            elif round(int(ex+(ew/2))) > LISTE_DROITE_GAUCHE[-2] + 1:
                               LISTE_DROITE_GAUCHE.append("retour")
                               return "droite"
                except:
                    pass



            c+=1






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

