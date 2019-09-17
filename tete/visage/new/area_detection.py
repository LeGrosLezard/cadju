"""FIRST -> we recup the face detection
            we positioning our area (temples, HEARs...) in function of face
            we add this points into our list
       
  SECOND -> we recup pixel colours of the face detection
            we apply this on the current frame
            we recup only our skin pixels

  THIRD -> we do the mean of the step one of our list of points
           we crop it from the frame
           we want see if there are whites pixels
           if yes we say it
"""
           
            


import os
import sys
import time
import numpy as np
import cv2
from PIL import Image
import operator
from collections import defaultdict

from area_detection_function import *




def video_capture():

    TEMPE = [[], [], [], [], [], [], [], []]
    PATTE = [[], [], [], [], [], [], [], []]
    HEAR = [[], [], [], [], [], [], [], []]
    MID = [[], [], [], []]

    MOVEMENT = []
    MESSAGES = ["", ""]

    cap=cv2.VideoCapture(0)
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")#face detection


    counter = 0
    while True:

        ret, frame =cap.read()
        frame = cv2.resize(frame, (800, 600))
        gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        #Initialization
        if len(TEMPE[0]) < 5:
            _, x, y, w, h = face_detection(faceCascade, gray, frame)
            appending(TEMPE, PATTE, HEAR, MID, x, y, w, h)


        #Skin detection
        if counter == 10:
            frame_skin_detector, _, _, _, _ = face_detection(faceCascade, gray, frame)
            UPPER, LOWER = most_pixel(frame_skin_detector)
            


        #Area  detection
        elif len(TEMPE[0]) >= 5 and counter >= 10:

            try:
                _, x, y, w, h = face_detection(faceCascade, gray, frame)

                skinMask = cv2.inRange(frame, np.array([LOWER], dtype = "uint8"),
                                       np.array([UPPER], dtype = "uint8"))
                print(LOWER, UPPER)
                if MOVEMENT[-1] > x + 5 or MOVEMENT[-1] < x - 5:
                    TEMPE = [[], [], [], [], [], [], [], []]
                    HEAR = [[], [], [], [], [], [], [], []]
                    PATTE = [[], [], [], [], [], [], [], []]
                    MID = [[], [], [], []]

                else:
                    MOVEMENT_detector(frame, TEMPE, HEAR, PATTE, MID, MESSAGES, skinMask)
                    cv2.imshow("skinMask1", skinMask)

            except:
                pass

            

        cv2.imshow("skinMask", frame)
        



        counter+=1
        MOVEMENT.append(x)



        key=cv2.waitKey(1)&0xFF
        if key==ord('q'):
            break


if __name__ == "__main__":
    video_capture()

