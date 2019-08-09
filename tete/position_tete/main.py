import numpy as np
import cv2
from PIL import Image
import os

from traitement_image import *


def video_capture():

    LISTE = []

    
    video = cv2.VideoCapture(0)
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
    eyes = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')
    
    while(True):


        ret, frame = video.read()
        frame = cv2.resize(frame, (600, 600))
        if len(LISTE) < 50:
            initialisation(video, frame, faceCascade, eyes, LISTE)
            
        else:
            position1 = position_tete(video, frame, faceCascade, eyes, LISTE)

        


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    video.release()
    cv2.destroyAllWindows()









if __name__ == "__main__":

    video_capture()












