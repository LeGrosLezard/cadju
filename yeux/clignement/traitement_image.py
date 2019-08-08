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
        cv2.circle(frame, (round(int(ex+(ew/2))), round(int(ey+(eh/2+5)))), 3, (0, 0, 255), 5)
        
        ey = ey.tolist()

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





        
















