import numpy as np
import cv2
from PIL import Image
import os

video = cv2.VideoCapture(0)

subtractor = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50, detectShadows=True)

liste = []

liste1 = []
while(True):

    ret, frame = video.read()
    frame = cv2.resize(frame, (600, 600))

    cv2.rectangle(frame, (201, 201), (250,250), (0,0,255), 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    crop = gray[200:250, 200:250]
    mask = subtractor.apply(crop)




    for i in mask:
        liste1 = []
        for j in i:
            liste1.append(j)

    print(sum(liste1) / len(liste1))



    
            
    
    cv2.imshow("Frame", frame)
    cv2.imshow("mask", mask)
    



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video.release()
cv2.destroyAllWindows()
