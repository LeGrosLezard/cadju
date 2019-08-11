import numpy as np
import cv2
from PIL import Image
import os

from traitement import *
from initialisation import *




def video_capture():

    Lsourcile61 = []
    Lsourcile62 = []
    Lsourcile63 = []


    video = cv2.VideoCapture(0)
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
    eyesCascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    
    while(True):


        ret, frame = video.read()
        frame = cv2.resize(frame, (600, 600))

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)



        yeux(frame, video, eyesCascade, faceCascade, gray,
                Lsourcile61, Lsourcile62, Lsourcile63)
            
        #figure(frame, video, faceCascade, gray)
            
        cv2.imshow('FACE CAPTURE', frame)



        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    video.release()
    cv2.destroyAllWindows()









if __name__ == "__main__":

    video_capture()












