import numpy as np
import cv2
from PIL import Image
import os

from traitement_image import *


def video_capture():

    LISTE = []

    video = cv2.VideoCapture(0)
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
    eyesCascade = cv2.CascadeClassifier('haarcascade_eye.xml')


    
    while(True):


        ret, frame = video.read()
        frame = cv2.resize(frame, (600, 600))
 
        if len(LISTE) < 50:
            initialisation(video, frame, faceCascade, eyesCascade, LISTE)
            
        else:
            position1 = position_tete(video, frame, faceCascade, eyesCascade, LISTE)

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

   

        
    video.release()
    cv2.destroyAllWindows()









if __name__ == "__main__":

    video_capture()












