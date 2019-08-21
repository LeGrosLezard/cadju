"""Function are long BUT is save ram for jb search more
because sometimes i just dont understand"""

import numpy as np
import cv2
from PIL import Image
import os


def cascade_face_config(frame, faceCascade):
    """on définit ce qu'il faut detecter avec les parametres
    de match"""

    #gray frame Blue green red to one intensity pixel
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #face detector
    faces = faceCascade.detectMultiScale(
        gray,#frame
        scaleFactor=1.1,#pyramid image the coef of reduce of the picture.
        minNeighbors=1,#How many neightboor does have our detection to be conserv.
        minSize=(30, 30),#min size of our detection
        flags=cv2.CASCADE_SCALE_IMAGE#if we using an old cascade ?
    )

    return faces, gray

def cascade_eyes_config(frame, eyesCascade):

    
    eyes = eyesCascade.detectMultiScale(frame,
        scaleFactor=1.3,
        minNeighbors=1,
        minSize=(40, 40),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    return eyes



def initialisation_pos(frame, faceCascade, eyesCascade, LISTE):
    """It give us the mean position of our eyes
    with it if we detect right eyes position y > to left y eyes
    position, head is to left."""

    faces, gray = cascade_face_config(frame, faceCascade)

    c = 0
    #corner top right to corner top left, width and corner bot right
    #from detection
    for x1, y1, w1, h1 in faces:
        
        #crop color and gray frames.
        #Color for visuel.
        #Gray for eyes detector.
        roi_gray = gray[y1:y1+h1, x1:x1+w1]
        roi_color = frame[y1:y1+h1, x1:x1+w1]

        #eyes detector.
        eyes = cascade_eyes_config(roi_gray, eyesCascade)

        for x, y, w, h in eyes:
            #draw the rectangle !
            cv2.rectangle(roi_color, (x,y), (x+w, y+h),(0, 0, 255), 2)
            
            if c == 1:
                #if the eyes is the second we append x to our
                #LIST who's give us the position of the eyes.
                #x np.array to list(x)
                x = x.tolist()
                LISTE.append(x)
            c+=1
    #we return our roi fram
    return frame




def position_tete_angle(frame, faceCascade, eyesCascade, LISTE):

    counter = 0#for the eyes (0 = left, 1 = right) but care eyes detection
               #according to the position of the head changes
    gauche = 0
    droite = 0
    x_gauche = 0
    x_droite = 0#If detection change....(we got the sum of pts x. If current
                #x is > of sum who takes the left eye so we detecting right
                #blue and black frame.)

    liste_x = []
    ok = False

    faces, gray = cascade_face_config(frame, faceCascade)
    
    for x1, y1, w1, h1 in faces:
        roi_gray = gray[y1:y1+h1, x1:x1+w1]
        roi_color = frame[y1:y1+h1, x1:x1+w1]

        eyes = cascade_eyes_config(roi_gray, eyesCascade)
        
        for x, y, w, h in eyes:

            if len(eyes) == 1:
                pass
                #one eyes pass
            
            else:

                if counter == 0:#left eyes
                    cv2.rectangle(roi_color, (x,y), (x+w, y+h), 2)
                    gauche = y.tolist()

                    
                if counter == 1:#right eyes
                    cv2.rectangle(roi_color, (x,y), (x+w, y+h),(255, 0, 0), 2)
                    droite = y.tolist()
                    x_droite = x.tolist()
                    
                counter += 1


        pos = position_oeil(gauche, droite, ok, LISTE, x_droite)
        if pos != None:
            return pos


                
def position_oeil(gauche, droite, ok, LISTE, x_droite):
    """Now we search eyes position comparing to mean initialisation list"""

    #If dude move his head, we return it
    #We can cancel head area (who return without pos area movement)
    pos = ""

    #If we have no detection of eyes we pass
    if gauche == 0 or droite == 0:
        pass
    else:
        #if left < right ....   and x_right > .......
        if gauche < droite - 10 and x_droite > (sum(LISTE) / len(LISTE)) + 15:
            pos = "gauche"
            ok = True#left and we define True.
                     #(Because eyes movements go right to left, round trip)
        if ok is True:
            pass
        else:
            if gauche < droite - 10:
                pos = "droite"

    if pos:
        print(pos)
        return pos













