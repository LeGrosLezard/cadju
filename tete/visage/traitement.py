import numpy as np
import cv2
from PIL import Image
import os



def point_figure(frame, x, y, w, h):
    x = x.tolist()
    y = y.tolist()
    w = w.tolist()
    h = h.tolist()
    
    tempe_droite = cv2.circle(frame,(x + 10, y + 10), 5, (255,0,0), 5)
    tempe_gauche = cv2.circle(frame,(x + w - 10 , y + 10), 5, (255,0,0), 5)

    oreille_droite = cv2.circle(frame,(x , y + 60), 5, (255,0,0), 5)
    oreille_gauche = cv2.circle(frame,(x + w , y + 60), 5, (255,0,0), 5)




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
    
    for x1, y1, w1, h1 in eyes:
        cv2.rectangle(frame, (x1,y1), (x1+w1, y1+h1),(0, 0, 255), 2)
