import numpy as np
import cv2


def position_tete(x, w, POSITION_TETE):

    if x + w > sum(POSITION_TETE) / len(POSITION_TETE) + 40:
        print("le mec s'est rapproché")
        return "reposition"

    elif x + w < sum(POSITION_TETE) / len(POSITION_TETE) - 40:
        print("le mec s'est éloigné")
        return "reposition"

    else:
        POSITION_TETE.append(x+w)




def detection_face(faceCascade, frame, BOX_ONE, POSITION_TETE):


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )



    for x, y, w, h in faces:

        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 2)
        
        x = x.tolist()
        w = w.tolist()
        
        reposition = position_tete(x, w, POSITION_TETE)
        
        if reposition == "reposition":
            out = "reposition"
        else:
            out = None

        return out


def haut_tete(frame, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p,
              subtractor, DEBUT, timmer, LISTE, PRE_INIT):

    

    cv2.rectangle(frame, (e,g), (f, h),(0, 255, 255), 2)    
    cv2.rectangle(frame, (i,k), (j, l),(255, 0, 255), 2)
    cv2.rectangle(frame, (m,o), (n, p),(255, 255, 255), 2)

    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    crop1 = gray[h:g, e:f]
    crop2 = gray[l:k, i:j]
    crop3 = gray[p:o, m:n]


    mask1 = subtractor.apply(crop1)
    mask2 = subtractor.apply(crop2)
    mask3 = subtractor.apply(crop3)
    

    liste2 = []
    liste3 = []
    liste4 = []


    for i in mask1:
        for j in i:
            liste2.append(j)
    for i in mask2:
        for j in i:
            liste3.append(j)
    for i in mask3:
        for j in i:
            liste4.append(j)

    if DEBUT == 1:
        pass
    else:
        
        if sum(liste2) / len(liste2) > 100:
            LISTE[0].append([1, timmer])
            print("droite")

        if sum(liste2) / len(liste2) > 50:
            PRE_INIT.append(sum(liste2) / len(liste2))
            
        if sum(liste2) / len(liste2) == 0.0:
            PRE_INIT = []
        
        if sum(liste3) / len(liste3) > 100:
            LISTE[1].append([2, timmer])
            print("milieu")
        if sum(liste4) / len(liste4) > 100:
            LISTE[2].append([3, timmer])
            print("gauche")

        






















