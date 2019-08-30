import numpy as np
import cv2
from PIL import Image
import os
import time

SUBSTRACTOR = cv2.createBackgroundSubtractorMOG2(history=100,
                                                varThreshold=50,
                                                detectShadows=True)


def video_capture_visage():

    #k, j, l <- video jb


    video = cv2.VideoCapture("VIDEO.mp4")
    
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
    handCascade = cv2.CascadeClassifier("hand.xml")
    handCascade3 = cv2.CascadeClassifier("hand3.xml")
    fistCascade = cv2.CascadeClassifier("fist.xml")
    closeCascade = cv2.CascadeClassifier("close.xml")
    fist2Cascade = cv2.CascadeClassifier("fist2.xml")
    gestCascade = cv2.CascadeClassifier("gest.xml")

    
    while(True):


        ret, frame_visage = video.read()
        frame_visage = cv2.resize(frame_visage, (1000, 800))

        gray = cv2.cvtColor(frame_visage, cv2.COLOR_BGR2GRAY)
        gray1 = cv2.cvtColor(frame_visage, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(frame_visage, cv2.COLOR_BGR2GRAY)
        gray3 = cv2.cvtColor(frame_visage, cv2.COLOR_BGR2GRAY)
        gray4 = cv2.cvtColor(frame_visage, cv2.COLOR_BGR2GRAY)
        gray5 = cv2.cvtColor(frame_visage, cv2.COLOR_BGR2GRAY)
        gray6 = cv2.cvtColor(frame_visage, cv2.COLOR_BGR2GRAY)
        gray7 = cv2.cvtColor(frame_visage, cv2.COLOR_BGR2GRAY)


        faces = faceCascade.detectMultiScale(
            gray1, scaleFactor=3,
            minNeighbors=1, minSize=(60, 100),
            flags=cv2.CASCADE_SCALE_IMAGE)


        fist = fistCascade.detectMultiScale(
            gray2, scaleFactor=1.5,
            minNeighbors=1, minSize=(40, 40),
            maxSize=(100, 100),
            flags=cv2.CASCADE_SCALE_IMAGE)


        hand3 = handCascade3.detectMultiScale(
            gray3, scaleFactor=1.5,
            minNeighbors=1, minSize=(40, 40),
            maxSize=(100, 100),
            flags=cv2.CASCADE_SCALE_IMAGE)

        close = closeCascade.detectMultiScale(
            gray4, scaleFactor=1.5,
            minNeighbors=1, minSize=(40, 40),
            maxSize=(100, 100),
            flags=cv2.CASCADE_SCALE_IMAGE)


        fist2 = fist2Cascade.detectMultiScale(
            gray5, scaleFactor=1.5,
            minNeighbors=1, minSize=(40, 40),
            maxSize=(100, 100),
            flags=cv2.CASCADE_SCALE_IMAGE)


        gest = gestCascade.detectMultiScale(
            gray6, scaleFactor=1.5,
            minNeighbors=1, minSize=(40, 40),
            maxSize=(100, 100),
            flags=cv2.CASCADE_SCALE_IMAGE)

        


        for x, y, w, h in faces:
            print(x, y, w, h)
            cv2.rectangle(gray, (x,y), (x+w, y+h), (255, 255, 255), 3)



        for x, y, w, h in fist2:
            print(x, y, w, h, "2")
            cv2.rectangle(gray, (x,y), (x+w, y+h), (0,255,255), 3)



        for x, y, w, h in gest:
            print(x, y, w, h, "3")
            cv2.rectangle(gray, (x,y), (x+w, y+h), (0,0,255), 3)

  
            
        for x, y, w, h in fist:
            print(x, y, w, h, "4")
            cv2.rectangle(gray, (x,y), (x+w, y+h), (150, 150, 0), 3)

       

        for x, y, w, h in hand3:
            print(x, y, w, h, "5")
            cv2.rectangle(gray, (x,y), (x+w, y+h), (0,0,0), 3)



        for x, y, w, h in close:
            print(x, y, w, h, "6")
            cv2.rectangle(gray, (x,y), (x+w, y+h), (255,0,255), 3)



        cv2.imshow('FACE121', gray)
            

        


        

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


        
    video.release()
    cv2.destroyAllWindows()



video_capture_visage()













    
