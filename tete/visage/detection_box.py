import numpy as np
import cv2
from PIL import Image
import os

video = cv2.VideoCapture(0)

LISTE = []

while(True):


    ret, frame = video.read()
    frame = cv2.resize(frame, (600, 600))

    liste1 = []

    
    for i in range(50,100):
        for j in range(50,100):
            liste1.append(frame[i, j][0])

    liste1 = str(liste1)
    
    try:
        if sum(LISTE)/len(LISTE) + 2000 < len(liste1):
            cv2.rectangle(frame, (50, 50), (100, 100), (0,0,255), 1)
        else:
            cv2.rectangle(frame, (50, 50), (100, 100), 1)
            LISTE.append(len(liste1))
    except:
        cv2.rectangle(frame, (50, 50), (100, 100), 1)
        LISTE.append(len(liste1))


    





    cv2.imshow('FACE INITIALISATION', frame)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video.release()
cv2.destroyAllWindows()
