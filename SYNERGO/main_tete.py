import numpy as np
import cv2
from PIL import Image
import os

from traitement_image import *


def video_capture_tete():

    LISTE = []

    video = cv2.VideoCapture(0)
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
    eyesCascade = cv2.CascadeClassifier('haarcascade_eye.xml')


    
    while(True):


        ret, frame = video.read()
        frame = cv2.resize(frame, (600, 600))
 
        if len(LISTE) < 50:
            initialisation_pos(frame, faceCascade, eyesCascade, LISTE)
            
        else:
            position1 = position_tete_angle(frame, faceCascade, eyesCascade, LISTE)

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

   

        
    video.release()
    cv2.destroyAllWindows()



video_capture_tete()


















