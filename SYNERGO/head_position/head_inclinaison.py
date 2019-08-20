import numpy as np
import cv2


def face_detection(faceCascade, gray):
    
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    return faces
    

def eyes_detection(eyesCascade, roi_gray):
    eyes = eyesCascade.detectMultiScale(roi_gray,
        scaleFactor=1.3,
        minNeighbors=4,
        minSize=(40, 40),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    return eyes


def initialisation(grayscale_frame, faceCascade, eyesCascade, LISTE):
    """Phase ou on récupere un modele de pts"""

    faces = face_detection(faceCascade, grayscale_frame)
    
    c = 0
    for x1, y1, w1, h1 in faces:
        roi_gray = grayscale_frame[y1:y1+h1, x1:x1+w1]

        eyes = eyes_detection(eyesCascade, roi_gray)

        for x, y, w, h in eyes:
            cv2.rectangle(roi_gray, (x,y), (x+w, y+h),(0, 0, 255), 2)

            if c == 1:
                LISTE.append(x.tolist())
            c+=1

    cv2.imshow('FACE CAPTURE', grayscale_frame)




def position_oeil(gauche, droite, ok, LISTE, x_droite):
    

    if gauche < droite - 10 and x_droite > (sum(LISTE) / len(LISTE)) + 15:
        print("gauche")
        ok = True
        
    if ok is not True and gauche < droite - 10:
        print("droite")


def position_tete(frame, grayscale_frame, faceCascade, eyesCascade, LISTE):

    faces = face_detection(faceCascade, grayscale_frame)
    
    counter, gauche, droite, x_gauche, x_droite = 0


    liste_x = []
    ok = False


    for x1, y1, w1, h1 in faces:
        roi_gray = grayscale_frame[y1:y1+h1, x1:x1+w1]
        roi_color = frame[y1:y1+h1, x1:x1+w1]

        eyes = eyes_detection(eyesCascade, roi_gray)
        
        for x, y, w, h in eyes:

            if len(eyes) != 1:

                if counter == 0:
                    cv2.rectangle(roi_color, (x,y), (x+w, y+h), 2)
                    gauche = y.tolist()

                    
                if counter == 1:
                    cv2.rectangle(roi_color, (x,y), (x+w, y+h),(255, 0, 0), 2)
                    droite = y.tolist()
                    x_droite = x.tolist()
                    
                counter += 1


        position_oeil(gauche, droite, ok, LISTE, x_droite)
    


            
        
    cv2.imshow('FACE CAPTURE', frame)


