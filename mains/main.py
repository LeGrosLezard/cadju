import numpy as np
import cv2

from skin import crop_face
from skin import detect_skin
from skin import delete_face


video = cv2.VideoCapture(0)

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
eyesCascade = cv2.CascadeClassifier('haarcascade_eye.xml')

subtractor = cv2.createBackgroundSubtractorMOG2(history=100,
                                                varThreshold=50,
                                                detectShadows=True)

BOX1 = []

liste1 = []
liste2 = []
liste3 = []


while(True):

    
    
    _, frame = video.read()

    if len(liste1) < 1:
        crop_face(frame, faceCascade, eyesCascade, BOX1,
                  liste1, liste2, liste3)
        cv2.imshow("mask", frame)
        
    else:
        image_mask = detect_skin(liste1, liste2, liste3, frame)
        cv2.imshow('FACE', image_mask)
    

##    contours =  cv2.findContours(frame,
##                                 cv2.RETR_TREE,
##                                 cv2.CHAIN_APPROX_SIMPLE)[-2]
##    
##    for i in contours:
##        cv2.drawContours(frame, i, -1, (0, 0, 255), 3)


    


    
    


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break





video.release()
cv2.destroyAllWindows()
