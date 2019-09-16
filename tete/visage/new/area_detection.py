"""FIRST -> we recup the face detection
            we positioning our area (temples, hears...) in function of face
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

from temples_function import *



#Sometimes video begening by effect we want to be sure
#to have the good pixels so we define counter
counter = 0
#temples list
tempe = [[], [], [], [], [], [], [], []]
patte = [[], [], [], [], [], [], [], []]
hear = [[], [], [], [], [], [], [], []]
mid = [[], [], [], []]

#movement list, if the person moves his head
movement = []
messages = ["", ""]

cap=cv2.VideoCapture("yo.mp4")#current video
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")#face detection


def appending(tempe, hear, mid, x, y, w, h):
    """We initilise list, we append points of our area in function
    of face detection"""

    #temples
    append_list(tempe, x, y - 20, x - 40, y + 40, x+w, y - 20, x+w+40, y + 40, 2)
    #border forhead
    append_list(patte, x - 20, y - int(round(110 * 100 / h)), x + 30, y - int(round(50 * 100 / h)),
                x+w-20, y - int(round(110 * 100 / h)), x+w+30, y-int(round(50 * 100 / h)), 2)
    #hears
    append_list(hear, x - 40, y + 70, x, y + 150, x+w, y + 70, x+w+40, y+150, 2)
    #mid head
    append_list(mid, x + int(round(w/3)), y - int(round(150 * 100 / h)), x + int(round(w/3)) * 2, y - int(round(80 * 100 / h)), "", "", "", "", 1)


def movement_detector(tempe, hear, patte, mid):
    """We positionning our area from the mean of points
    recuped from initialisation"""

    #temples
    y1, yh1, x1, xw1, y2, yh2, x2, xw2 = out_list(tempe, 2)
    detections(skinMask, y1, yh1, x1, xw1, y2, yh2, x2, xw2,
               "tempe droite", "tempe gauche", messages)
    #hear
    y1, yh1, x1, xw1, y2, yh2, x2, xw2 = out_list(hear, 2)
    detections(skinMask, y1, yh1, x1, xw1, y2, yh2, x2, xw2,
               "oreille droite", "oreille gauche", messages)
    #border forehead
    y1, yh1, x1, xw1, y2, yh2, x2, xw2 = out_list(patte, 2)
    detections(skinMask, y1, yh1, x1, xw1, y2, yh2, x2, xw2,
               "patte droite", "patte gauche", messages)
    y1, yh1, x1, xw1 = out_list(mid, 1)
    detections(skinMask, y1, yh1, x1, xw1, 0, 0, 0, 0,
               "milieu de la tete", "", messages)



while True:

    ret, frame =cap.read()
    frame = cv2.resize(frame, (800, 600))
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    #Initialization
    if len(tempe[0]) < 5:
        _, x, y, w, h = face_detection(faceCascade, gray, frame)
        appending(tempe, hear, mid, x, y, w, h)

    #Skin detection
    if counter == 5:
        frame_skin_detector, _, _, _, _ = face_detection(faceCascade, gray, frame)
        UPPER, LOWER = most_pixel(frame_skin_detector)

    #Area  detection
    elif len(tempe[0]) >= 5 and counter > 5:

        _, x, y, w, h = face_detection(faceCascade, gray, frame)

        skinMask = cv2.inRange(frame, np.array([LOWER], dtype = "uint8"),
                               np.array([UPPER], dtype = "uint8"))

        if movement[-1] > x + 5 or movement[-1] < x - 5:
            tempe = [[], [], [], [], [], [], [], []]
            hear = [[], [], [], [], [], [], [], []]
            patte = [[], [], [], [], [], [], [], []]
            mid = [[], [], [], []]

        else:
            movement_detector(tempe, hear, patte, mid)

        cv2.imshow("skinMask", frame)



    counter+=1
    movement.append(x)



    key=cv2.waitKey(1)&0xFF
    if key==ord('q'):
        break
