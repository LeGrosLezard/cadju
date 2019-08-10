import numpy as np
import cv2
from PIL import Image
import os


def tempes(frame, x, y ,w ,h):
    tempe_gauche = cv2.circle(frame,(x + w - 10 , y + 10), 1, (255,0,0), 2)
    
    tempe_droite = cv2.circle(frame,(x + 10, y + 10), 1, (255,0,0), 2)


def oreilles(frame, x, y ,w ,h):
    oreille_gauche1 = cv2.circle(frame,(x + w , y + 50), 1, (255,0,0), 2)
    oreille_gauche2 = cv2.circle(frame,(x + w , y + 60), 1, (255,0,0), 2)
    oreille_gauche3 = cv2.circle(frame,(x + w , y + 70), 1, (255,0,0), 2)
    oreille_gauche4 = cv2.circle(frame,(x + w , y + 80), 1, (255,0,0), 2)
    oreille_gauche5 = cv2.circle(frame,(x + w , y + 90), 1, (255,0,0), 2)
    oreille_gauche6 = cv2.circle(frame,(x + w , y + 100), 1, (255,0,0), 2)
    
    oreille_droite1 = cv2.circle(frame,(x , y + 50), 1, (255,0,0), 2)
    oreille_droite2 = cv2.circle(frame,(x , y + 60), 1, (255,0,0), 2)
    oreille_droite3 = cv2.circle(frame,(x , y + 70), 1, (255,0,0), 2)
    oreille_droite4 = cv2.circle(frame,(x , y + 80), 1, (255,0,0), 2)
    oreille_droite5 = cv2.circle(frame,(x , y + 90), 1, (255,0,0), 2)
    oreille_droite6 = cv2.circle(frame,(x , y + 100), 1, (255,0,0), 2)
    

def cernes(frame, x, y ,w ,h):
    cerne_droite = cv2.circle(frame, (x + 40, int(round(y + h / 2 - 5))), 1, (255,0,0), 2)
    cerne_droite = cv2.circle(frame, (x + 50, int(round(y + h / 2 - 5))), 1, (255,0,0), 2)
    cerne_droite = cv2.circle(frame, (x + 60, int(round(y + h / 2 - 5))), 1, (255,0,0), 2)
    cerne_droite = cv2.circle(frame, (x + 70, int(round(y + h / 2 - 5))), 1, (255,0,0), 2)
    cerne_droite = cv2.circle(frame, (x + 80, int(round(y + h / 2 - 5))), 1, (255,0,0), 2)

    cerne_gauche = cv2.circle(frame, (x + w - 40, int(round(y + h / 2 - 5))), 1, (255,0,0), 2)
    cerne_gauche = cv2.circle(frame, (x + w - 50, int(round(y + h / 2 - 5))), 1, (255,0,0), 2)
    cerne_gauche = cv2.circle(frame, (x + w - 60, int(round(y + h / 2 - 5))), 1, (255,0,0), 2)
    cerne_gauche = cv2.circle(frame, (x + w - 70, int(round(y + h / 2 - 5))), 1, (255,0,0), 2)
    cerne_gauche = cv2.circle(frame, (x + w - 80, int(round(y + h / 2 - 5))), 1, (255,0,0), 2)


def pomettes(frame, x, y ,w ,h):
    pomette_droite = cv2.circle(frame, (x + 40, int(round(y + h / 2 + 10))), 1, (255,0,0), 2)
    pomette_gauche = cv2.circle(frame, (x + w - 40, int(round(y + h / 2 + 10))), 1, (255,0,0), 2)



def front(frame, x, y ,w ,h):
    front = cv2.rectangle(frame, (x,y), (x + w, y + 40),(0, 255, 0), 2)

def bouche(frame, x, y ,w ,h):
    bouche1 = cv2.circle(frame, (int(round(x + w / 2)), y + h - 10), 1, (255,255,0), 2)
    bouche2 = cv2.circle(frame, (int(round(x + w / 2 - 10)), y + h - 10), 1, (255,255,0), 2)
    bouche3 = cv2.circle(frame, (int(round(x + w / 2 + 10)), y + h - 10), 1, (255,255,0), 2)
    bouche4 = cv2.circle(frame, (int(round(x + w / 2 - 15)), y + h - 10), 1, (255,255,0), 2)
    bouche5 = cv2.circle(frame, (int(round(x + w / 2 + 15)), y + h - 10), 1, (255,255,0), 2)





def milieu(frame, x, y ,w ,h):
    milieu = cv2.line(frame, (int(round(x + w/2)), y), (int(round(x + w/2)), y + h), (0, 0, 255), 8)



def point_figure(frame, x, y, w, h):
    
    x = x.tolist()
    y = y.tolist()
    w = w.tolist()
    h = h.tolist()
    
    tempes(frame, x, y ,w ,h)
    oreilles(frame, x, y ,w ,h)
    cernes(frame, x, y ,w ,h)
    pomettes(frame, x, y ,w ,h)
    front(frame, x, y ,w ,h)
    bouche(frame, x, y ,w ,h)
    milieu(frame, x, y ,w ,h)
    
    
def figure(frame, video, faceCascade, gray):
    
    face = faceCascade.detectMultiScale(gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    ) 

    for x, y, w, h in face:
        #rect = cv2.rectangle(frame, (x,y), (x+w, y+h),(0, 0, 255), 2)
        point_figure(frame, x, y, w, h)




def sourciles_droit(frame, x1, y1, w1, h1):
    sourcile6 = cv2.circle(frame, (x1 + 5, y1 + 5), 1, (0,0,0), 2)
    sourcile7 = cv2.circle(frame, (x1 + 15, y1 + 5), 1, (0,0,0), 2)
    sourcile8 = cv2.circle(frame, (x1 + 25, y1 + 5), 1, (0,0,0), 2)
    sourcile9 = cv2.circle(frame, (x1 + 35, y1 + 6), 1, (0,0,0), 2)
    sourcile10 = cv2.circle(frame, (x1 + 45, y1 + 7), 1, (0,0,0), 2)


def sourciles_gauche(frame, x1, y1, w1, h1):
    sourcile1 = cv2.circle(frame, (x1 + 5, y1 + 5), 1, (0,0,0), 2)
    sourcile2 = cv2.circle(frame, (x1 + 15, y1 + 5), 1, (0,0,0), 2)
    sourcile3 = cv2.circle(frame, (x1 + 25, y1 + 5), 1, (0,0,0), 2)
    sourcile4 = cv2.circle(frame, (x1 + 35, y1 + 6), 1, (0,0,0), 2)
    sourcile5 = cv2.circle(frame, (x1 + 45, y1 + 7), 1, (0,0,0), 2)


    
def yeux(frame, video, eyesCascade):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eyes = eyesCascade.detectMultiScale(gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE)


    oeil = 0
    
    pos1 = 0
    pos1_y = 0

    pos2 = 0
    pos2_y = 0
    
    for x1, y1, w1, h1 in eyes:
        
        if oeil == 0:
            pos1 = x1.tolist() + w1.tolist()
            pos1_y = y1.tolist()
            sourciles_droit(frame, x1, y1, w1, h1)

        elif oeil == 1:

            pos2 = x1.tolist()
            pos2_y = y1.tolist()
            sourciles_gauche(frame, x1, y1, w1, h1)
            #cv2.rectangle(frame, (x1, y1), (x1 + w1, y1 + h1),(0, 0, 255), 2)


        oeil += 1




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


























