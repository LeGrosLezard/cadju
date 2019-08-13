import numpy as np
import cv2


def detection_face(frame, faceCascade):
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h),(0, 0, 0), 2)

    try:
        x = x.tolist()
        w = w.tolist()

        return x, w
    
    except:
        pass
    #pas de détection de tete

def initialisation(frame, faceCascade, POSITION_TETE):

    try:
        x, w = detection_face(frame, faceCascade)

        POSITION_TETE.append(x + w)
    except:
        pass
    #pas de détection de tete





















    


