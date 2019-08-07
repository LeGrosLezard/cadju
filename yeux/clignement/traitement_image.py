import numpy as np
import cv2 
from PIL import Image
import os




def pre_initialisation(repere, eyes, liste, frame):
    """Ici si repere est inférieur a 100
    on ajoute les lignes dans la liste"""


    for (ex, ey, ew, eh) in eyes:
        
        cv2.rectangle(frame, (ex,ey), (ex+ew, ey+eh), 0)
        ey = ey.tolist()
        liste.append(ey)




def position_yeux(repere, eyes, liste, frame):
    """Si repere est superieur a 100
    c'est qu'on a fini la premiere initialisation"""


    for (ex, ey, ew, eh) in eyes:

        cv2.rectangle(frame, (ex,ey), (ex+ew, ey+eh), 0)
        ey = ey.tolist()
        liste.append(ey)


        if ey < sum(liste)/len(liste) - 100:
            return "le mec s'est levé"
            

        elif ey > sum(liste)/len(liste) + 100: 
            return "le mec s'est baissé"


        if ey < sum(liste)/len(liste) - 20:
            return "le mec à levé la tete"
            
        elif ey > sum(liste)/len(liste) + 20: 
            return "le mec à baisser la tete"

        
        elif ey < sum(liste)/len(liste) - 5:
            return "le mec regarde en HAUT"
        
        elif ey > sum(liste)/len(liste) + 5: 
            return "le mec regarde en bas"




        























