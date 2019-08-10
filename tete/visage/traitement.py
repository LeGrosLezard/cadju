import numpy as np
import cv2
from PIL import Image
import os



def point_figure(frame, x, y, w, h):
    
    x = x.tolist()
    y = y.tolist()
    w = w.tolist()
    h = h.tolist()
    
    tempe_gauche = cv2.circle(frame,(x + w - 10 , y + 10), 1, (255,0,0), 2)
    tempe_droite = cv2.circle(frame,(x + 10, y + 10), 1, (255,0,0), 2)
    
    
    oreille_gauche = cv2.circle(frame,(x + w , y + 50), 1, (255,0,0), 2)
    oreille_droite = cv2.circle(frame,(x , y + 50), 1, (255,0,0), 2)

    cerne_droite = cv2.circle(frame, (x + 50, int(round(y + h / 2 - 5))), 1, (255,0,0), 2)
    cerne_gauche = cv2.circle(frame, (x + w - 50, int(round(y + h / 2 - 5))), 1, (255,0,0), 2)

    pomette_droite = cv2.circle(frame, (x + 40, int(round(y + h / 2 + 10))), 1, (255,0,0), 2)
    pomette_gauche = cv2.circle(frame, (x + w - 40, int(round(y + h / 2 + 10))), 1, (255,0,0), 2)




def figure(frame, video, faceCascade, gray):
    
    face = faceCascade.detectMultiScale(gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    ) 

    for x, y, w, h in face:
        rect = cv2.rectangle(frame, (x,y), (x+w, y+h),(0, 0, 255), 2)
        
        point_figure(frame, x, y, w, h)






def yeux(frame, video, eyesCascade):
    eyes = eyesCascade.detectMultiScale(frame)



    c = 0
    pos1 = 0
    pos1_y = 0
    pos2 = 0
    pos2_y = 0
    
    for x1, y1, w1, h1 in eyes:
        
        if c == 0:
            pos1 = x1.tolist() + w1.tolist()
            pos1_y = y1.tolist()
        
            sourcile6 = cv2.circle(frame, (x1 + 5, y1 + 5), 1, (0,0,0), 2)
            sourcile7 = cv2.circle(frame, (x1 + 15, y1 + 5), 1, (0,0,0), 2)
            sourcile8 = cv2.circle(frame, (x1 + 25, y1 + 5), 1, (0,0,0), 2)
            sourcile9 = cv2.circle(frame, (x1 + 35, y1 + 6), 1, (0,0,0), 2)
            sourcile10 = cv2.circle(frame, (x1 + 45, y1 + 7), 1, (0,0,0), 2)

        elif c == 1:

            pos2 = x1.tolist()
            pos2_y = y1.tolist()
            
            #cv2.rectangle(frame, (x1, y1), (x1 + w1, y1 + h1),(0, 0, 255), 2)
            sourcile1 = cv2.circle(frame, (x1 + 5, y1 + 5), 1, (0,0,0), 2)
            sourcile2 = cv2.circle(frame, (x1 + 15, y1 + 5), 1, (0,0,0), 2)
            sourcile3 = cv2.circle(frame, (x1 + 25, y1 + 5), 1, (0,0,0), 2)
            sourcile4 = cv2.circle(frame, (x1 + 35, y1 + 6), 1, (0,0,0), 2)
            sourcile5 = cv2.circle(frame, (x1 + 45, y1 + 7), 1, (0,0,0), 2)

        c += 1

        #ATTENTION A SWITCH DES YEUX


    un = 0
    deux = 0
    x = 0
    y = 0
    if pos1 < pos2:
        un = pos1
        deux = pos2

        unun = pos1_y
        deuxdeux = pos2_y

        x = (un + deux)/2
        y = (unun + deuxdeux)/2
        print(un)
        
    elif pos1 > pos2:
        deux = pos1
        un = pos2

        unun = pos2_y
        deuxdeux = pos1_y

        x = (un + deux)/2
        y = (unun + deuxdeux)/2
        y = int(round(y))


    if x == 0 or y == 0:
        pass
    else:
    
        entre_oeil = cv2.circle(frame, (int(round(x)), int(round(y))), 1, (255,0,0), 2)


        arrete_nez1 = cv2.circle(frame, (int(round(x)), int(round(y + 10))), 1, (255,0,0), 2)
        arrete_nez2 = cv2.circle(frame, (int(round(x)), int(round(y + 20))), 1, (255,0,0), 2)
        arrete_nez3 = cv2.circle(frame, (int(round(x)), int(round(y + 30))), 1, (255,0,0), 2)
        arrete_nez4 = cv2.circle(frame, (int(round(x)), int(round(y + 40))), 1, (255,0,0), 2)
        arrete_nez5 = cv2.circle(frame, (int(round(x)), int(round(y + 50))), 1, (255,0,0), 2)
        arrete_nez6 = cv2.circle(frame, (int(round(x)), int(round(y + 60))), 1, (255,0,0), 2)

        ange1 = cv2.circle(frame, (int(round(x)), int(round(y + 90))), 1, (255,0,0), 2)
        ange2 = cv2.circle(frame, (int(round(x)), int(round(y + 100))), 1, (255,0,0), 2)
        ange3 = cv2.circle(frame, (int(round(x)), int(round(y + 110))), 1, (255,0,0), 2)

























