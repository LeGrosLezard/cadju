import numpy as np
import cv2
from PIL import Image
import os

from traitement import figure
from traitement import yeux


def video_capture():

    LISTE = []

    
    video = cv2.VideoCapture(0)
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
    eyesCascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    
    while(True):


        ret, frame = video.read()
        frame = cv2.resize(frame, (600, 600))

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        figure(frame, video, faceCascade, gray)
        yeux(frame, video, eyesCascade)
        
        cv2.imshow('FACE CAPTURE', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    video.release()
    cv2.destroyAllWindows()









if __name__ == "__main__":

    video_capture()












