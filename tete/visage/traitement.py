import numpy as np
import cv2
from PIL import Image
import os

#on récupere la couleur des pixels ici
def initialisation_tempe(Ltempe_gauche, Ltempe_droite, x, y, h, w, frame):
    Ltempe_gauche.append(frame[y + 10, x + w - 10])
    Ltempe_droite.append(frame[y + 10, x + 10])


def initialisation_oreille_gauche(Loreille_gauche1, Loreille_gauche2,
                                  Loreille_gauche3, Loreille_gauche4,
                                  Loreille_gauche5, Loreille_gauche6,
                                  Ltempe_droite, x, y, h, w, frame):

    Loreille_gauche1.append(frame[y + 50, x + w])
    Loreille_gauche2.append(frame[y + 60, x + w])
    Loreille_gauche3.append(frame[y + 70, x + w])
    Loreille_gauche4.append(frame[y + 80, x + w])
    Loreille_gauche5.append(frame[y + 90, x + w])
    Loreille_gauche6.append(frame[y + 100, x + w])


def initialisation_oreille_droite(Loreille_droite1, Loreille_droite2,
                                  Loreille_droite3, Loreille_droite4,
                                  Loreille_droite5, Loreille_droite6,
                                  x, y, h, w, frame):

    Loreille_droite1.append(frame[y + 50, x])
    Loreille_droite2.append(frame[y + 60, x])
    Loreille_droite3.append(frame[y + 70, x])
    Loreille_droite4.append(frame[y + 80, x])
    Loreille_droite5.append(frame[y + 90, x])
    Loreille_droite6.append(frame[y + 100, x])


def initialisation_cerne_droite(Lcerne_droite1, Lcerne_droite2,
                                Lcerne_droite3, Lcerne_droite4,
                                Lcerne_droite5,
                                x, y, h, w, frame):

    Lcerne_droite1.append(frame[int(round(y + h / 2 - 5)), x + 40])
    Lcerne_droite2.append(frame[int(round(y + h / 2 - 5)), x + 50])
    Lcerne_droite3.append(frame[int(round(y + h / 2 - 5)), x + 60])
    Lcerne_droite4.append(frame[int(round(y + h / 2 - 5)), x + 70])
    Lcerne_droite5.append(frame[int(round(y + h / 2 - 5)), x + 80])



def initialisation_cerne_gauche(Lcerne_gauche1, Lcerne_gauche2,
                                Lcerne_gauche3, Loreille_droite4,
                                Loreille_droite5,
                                x, y, h, w, frame):

    Lcerne_gauche1.append(frame[int(round(y + h / 2 - 5)), x + w - 40])
    Lcerne_gauche2.append(frame[int(round(y + h / 2 - 5)), x + w - 50])
    Lcerne_gauche3.append(frame[int(round(y + h / 2 - 5)), x + w - 60])
    Loreille_droite4.append(frame[int(round(y + h / 2 - 5)), x + w - 70])
    Loreille_droite5.append(frame[int(round(y + h / 2 - 5)), x + w - 80])


def initialisation_pomette(Lpomette_droite, Lpomette_gauche, x, y, h, w, frame):
    Lpomette_droite.append(frame[int(round(y + h / 2 + 10)), x + 40])
    Lpomette_gauche.append(frame[int(round(y + h / 2 + 10)), x + w - 40])


def initialisation_front(Lfront1, Lfront2,
                         Lfront3, Lfront4,
                         x, y, h, w, frame):
    
    Lfront1.append(frame[y + 5, x + 40:x + w - 40])
    Lfront2.append(frame[y + 10, x + 40:x + w - 40])
    Lfront3.append(frame[y + 15, x + 40:x + w - 40])
    Lfront4.append(frame[y + 20, x + 40:x + w - 40])

def initialisation_bouche(frame, Lbouche1, Lbouche2,
                          Lbouche3, Lbouche4, Lbouche5,
                          x, y, h, w):
    Lbouche1.append(frame[y + h - 10, int(round(x + w / 2))])
    Lbouche2.append(frame[y + h - 10, int(round(x + w / 2 - 10))])
    Lbouche3.append(frame[y + h - 10, int(round(x + w / 2 + 10))])
    Lbouche4.append(frame[y + h - 10, int(round(x + w / 2 - 15))])
    Lbouche5.append(frame[y + h - 10, int(round(x + w / 2 + 15))])
    
def initialisation_milieu(Lmillieu, x, y, h, w, frame):
    Lmillieu.append(frame[y:y + h, int(round(x + w/2))])
    

def initialisation_sourcile_droit(frame, sourcile6, sourcile7,
                                  sourcile8, sourcile9,
                                  sourcile10
                                  x, y, h, w):
    sourcile6.append(frame[y1 + 5, x1 + 5])
    sourcile7.append(frame[y1 + 5, x1 + 15])
    sourcile8.append(frame[y1 + 5, x1 + 25])
    sourcile9.append(frame[y1 + 6, x1 + 35])
    sourcile10.append(frame[y1 + 7, x1 + 45])


def initialisation_sourcile_gauche(frame, sourcile1, sourcile2,
                                   sourcile3, sourcile4,
                                   sourcile5
                                   x, y, h, w):
    sourcile1.append(frame[y1 + 5, x1 + 5])
    sourcile2.append(frame[y1 + 5, x1 + 15])
    sourcile3.append(frame[y1 + 5, x1 + 25])
    sourcile4.append(frame[y1 + 6, x1 + 35])
    sourcile5.append(frame[y1 + 7, x1 + 45])


def initialisation(frame, video, faceCascade, gray,
                   Ltempe_gauche, Ltempe_droite,
                   Loreille_gauche1, Loreille_gauche2,
                   Loreille_gauche3, Loreille_gauche4,
                   Loreille_gauche5, Loreille_gauche6,
                   Loreille_droite1, Loreille_droite2,
                   Loreille_droite3, Loreille_droite4,
                   Loreille_droite5, Loreille_droite6,
                   Lcerne_droite1, Lcerne_droite2,
                   Lcerne_droite3, Lcerne_droite4,
                   Lcerne_droite5, Lcerne_gauche1,
                   Lcerne_gauche2, Lcerne_gauche3,
                   Lcerne_gauche4, Lcerne_gauche5,
                   Lpomette_droite, Lpomette_gauche,
                   Lfront1, Lfront2, Lfront3, Lfront4,
                   Lbouche1, Lbouche2, Lbouche3, Lbouche4,
                   Lbouche5, Lmillieu, sourcile6, sourcile7,
                   sourcile8, sourcile9, sourcile10, sourcile1,
                   sourcile2, sourcile3, sourcile4, sourcile5):



    face = faceCascade.detectMultiScale(gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    ) 

    for x, y, w, h in face:

        x = x.tolist()
        y = y.tolist()
        w = w.tolist()
        h = h.tolist()


        initialisation_tempe(Ltempe_gauche, Ltempe_droite, x, y, h, w, frame)

        
        initialisation_oreille_gauche(Loreille_gauche1, Loreille_gauche2,
                                        Loreille_gauche3, Loreille_gauche4,
                                        Loreille_gauche5, Loreille_gauche6,
                                        Ltempe_droite, x, y, h, w, frame)


        initialisation_oreille_droite(Loreille_droite1, Loreille_droite2,
                                        Loreille_droite3, Loreille_droite4,
                                        Loreille_droite5, Loreille_droite6,
                                        x, y, h, w, frame)


        initialisation_cerne_droite(Lcerne_droite1, Lcerne_droite2,
                                    Lcerne_droite3, Lcerne_droite4,
                                    Lcerne_droite5,
                                    x, y, h, w, frame)


        initialisation_cerne_gauche(Lcerne_gauche1, Lcerne_gauche2,
                                    Lcerne_gauche3, Loreille_droite4,
                                    Loreille_droite5,
                                    x, y, h, w, frame)


        initialisation_pomette(Lpomette_droite, Lpomette_gauche, x, y, h, w, frame)


        initialisation_front(Lfront1, Lfront2,
                             Lfront3, Lfront4,
                             x, y, h, w, frame)

        initialisation_bouche(frame, Lbouche1, Lbouche2,
                                  Lbouche3, Lbouche4, Lbouche5,
                                  x, y, h, w)

        initialisation_milieu(Lmillieu, x, y, h, w, frame)
        

        initialisation_sourcile_droit(frame, sourcile6, sourcile7,
                                          sourcile8, sourcile9,
                                          sourcile10
                                          x, y, h, w)

        initialisation_sourcile_gauche(frame, sourcile1, sourcile2,
                                           sourcile3, sourcile4,
                                           sourcile5
                                           x, y, h, w)


def tempes(frame, x, y ,w ,h):
##    tempe_gauche = cv2.circle(frame,(x + w - 10 , y + 10), 1, (255,0,0), 2)
##    tempe_droite = cv2.circle(frame,(x + 10, y + 10), 1, (255,0,0), 2)

    

def oreilles(frame, x, y ,w ,h):
##    oreille_gauche1 = cv2.circle(frame,(x + w , y + 50), 1, (255,0,0), 2)
##    oreille_gauche2 = cv2.circle(frame,(x + w , y + 60), 1, (255,0,0), 2)
##    oreille_gauche3 = cv2.circle(frame,(x + w , y + 70), 1, (255,0,0), 2)
##    oreille_gauche4 = cv2.circle(frame,(x + w , y + 80), 1, (255,0,0), 2)
##    oreille_gauche5 = cv2.circle(frame,(x + w , y + 90), 1, (255,0,0), 2)
##    oreille_gauche6 = cv2.circle(frame,(x + w , y + 100), 1, (255,0,0), 2)
##    
##    oreille_droite1 = cv2.circle(frame,(x , y + 50), 1, (255,0,0), 2)
##    oreille_droite2 = cv2.circle(frame,(x , y + 60), 1, (255,0,0), 2)
##    oreille_droite3 = cv2.circle(frame,(x , y + 70), 1, (255,0,0), 2)
##    oreille_droite4 = cv2.circle(frame,(x , y + 80), 1, (255,0,0), 2)
##    oreille_droite5 = cv2.circle(frame,(x , y + 90), 1, (255,0,0), 2)
##    oreille_droite6 = cv2.circle(frame,(x , y + 100), 1, (255,0,0), 2)


def cernes(frame, x, y ,w ,h):
##    cerne_droite1 = cv2.circle(frame, (x + 40, int(round(y + h / 2 - 5))), 1, (255,0,0), 2)
##    cerne_droite2 = cv2.circle(frame, (x + 50, int(round(y + h / 2 - 5))), 1, (255,0,0), 2)
##    cerne_droite3 = cv2.circle(frame, (x + 60, int(round(y + h / 2 - 5))), 1, (255,0,0), 2)
##    cerne_droite4 = cv2.circle(frame, (x + 70, int(round(y + h / 2 - 5))), 1, (255,0,0), 2)
##    cerne_droite5 = cv2.circle(frame, (x + 80, int(round(y + h / 2 - 5))), 1, (255,0,0), 2)
##
##    cerne_gauche1 = cv2.circle(frame, (x + w - 40, int(round(y + h / 2 - 5))), 1, (255,0,0), 2)
##    cerne_gauche2 = cv2.circle(frame, (x + w - 50, int(round(y + h / 2 - 5))), 1, (255,0,0), 2)
##    cerne_gauche3 = cv2.circle(frame, (x + w - 60, int(round(y + h / 2 - 5))), 1, (255,0,0), 2)
##    cerne_gauche4 = cv2.circle(frame, (x + w - 70, int(round(y + h / 2 - 5))), 1, (255,0,0), 2)
##    cerne_gauche5 = cv2.circle(frame, (x + w - 80, int(round(y + h / 2 - 5))), 1, (255,0,0), 2)


def pomettes(frame, x, y ,w ,h):
##    pomette_droite = cv2.circle(frame, (x + 40, int(round(y + h / 2 + 10))), 1, (255,0,0), 2)
##    pomette_gauche = cv2.circle(frame, (x + w - 40, int(round(y + h / 2 + 10))), 1, (255,0,0), 2)


def front(frame, Lfront1, Lfront2,
          Lfront3, Lfront4,
          x, y ,w ,h):
    
##    front1 = cv2.line(img, (x + 40, y + 5), (x + w - 40, y + 5), (0,0,0), 2)
##    front2 = cv2.line(img, (x + 40, y + 10), (x + w - 40, y + 10), (0,0,0), 2)
##    front3 = cv2.line(img, (x + 40, y + 15), (x + w - 40, y + 15), (0,0,0), 2)
##    front4 = cv2.line(img, (x + 40, y + 20), (x + w - 40, y + 20), (0,0,0), 2)


def bouche(frame, x, y ,w ,h):
##    bouche1 = cv2.circle(frame, (int(round(x + w / 2)), y + h - 10), 1, (255,255,0), 2)
##    bouche2 = cv2.circle(frame, (int(round(x + w / 2 - 10)), y + h - 10), 1, (255,255,0), 2)
##    bouche3 = cv2.circle(frame, (int(round(x + w / 2 + 10)), y + h - 10), 1, (255,255,0), 2)
##    bouche4 = cv2.circle(frame, (int(round(x + w / 2 - 15)), y + h - 10), 1, (255,255,0), 2)
##    bouche5 = cv2.circle(frame, (int(round(x + w / 2 + 15)), y + h - 10), 1, (255,255,0), 2)


def milieu(frame, x, y ,w ,h):
##milieu = cv2.line(frame, (int(round(x + w/2)), y), (int(round(x + w/2)), y + h), (0, 0, 255), 8)

    
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
##    sourcile6 = cv2.circle(frame, (x1 + 5, y1 + 5), 1, (0,0,0), 2)
##    sourcile7 = cv2.circle(frame, (x1 + 15, y1 + 5), 1, (0,0,0), 2)
##    sourcile8 = cv2.circle(frame, (x1 + 25, y1 + 5), 1, (0,0,0), 2)
##    sourcile9 = cv2.circle(frame, (x1 + 35, y1 + 6), 1, (0,0,0), 2)
##    sourcile10 = cv2.circle(frame, (x1 + 45, y1 + 7), 1, (0,0,0), 2)


def sourciles_gauche(frame, x1, y1, w1, h1):
##    sourcile1 = cv2.circle(frame, (x1 + 5, y1 + 5), 1, (0,0,0), 2)
##    sourcile2 = cv2.circle(frame, (x1 + 15, y1 + 5), 1, (0,0,0), 2)
##    sourcile3 = cv2.circle(frame, (x1 + 25, y1 + 5), 1, (0,0,0), 2)
##    sourcile4 = cv2.circle(frame, (x1 + 35, y1 + 6), 1, (0,0,0), 2)
##    sourcile5 = cv2.circle(frame, (x1 + 45, y1 + 7), 1, (0,0,0), 2)


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


























