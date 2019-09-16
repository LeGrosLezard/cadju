import os
import sys
import time
import numpy as np
import cv2
from PIL import Image
import operator
from collections import defaultdict



def face_detection(faceCascade, gray, frame):
    """Here we detecting the face thank to haarcascade.
    We trying to detect the face from gray frame.
    We make the pyramid scale to 1.3,
    we define the minimum neighbour to 1, the minimum size to 60x40
    and the flags for the old cascade."""

    #Face detector
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=1,
        minSize=(60, 100),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    """We crop, we only focus on the detection face,
    for collect after, the main pixels and make our skin detector
    of the face. We postulates skin face == skin arm for example
    """

    #Points of the detecting face
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), 3)
        frame_skin_detector = frame[y + 20:y+h - 20, x+20:x+w-20]

        """This function serves us many times so we return
        frame_skin_detector for focusing on the face,
        we return also the points of the detection
        """

        return frame_skin_detector, x, y, w, h



def most_pixel(frame_skin_detector):
    """Here we collect all pixels
    from the face detection
    and return the highter presence of pixel"""

    dico = {}
    img = Image.fromarray(frame_skin_detector)
    for value in img.getdata():
        if value in dico.keys():
            dico[value] += 1
        else:
            dico[value] = 1

    sorted_x = sorted(dico.items(),
                      key=operator.itemgetter(1), reverse=True)

    upper = sorted_x[0][0][0], sorted_x[0][0][1], sorted_x[0][0][2] + 40
    lower = sorted_x[-1][0][0], sorted_x[-1][0][1], sorted_x[-1][0][2]

    return upper, lower


def append_list(liste, x1, y1, w1, h1, x2, y2, w2, h2, mode):
    """Here we add to the list some points
    thank to the face detection for make our temples"""

    if mode == 2:

        #right
        liste[0].append(x1)
        liste[1].append(y1)
        liste[2].append(w1)
        liste[3].append(h1)

        #left
        liste[4].append(x2)
        liste[5].append(y2)
        liste[6].append(w2)
        liste[7].append(h2)


    elif mode == 1:
        liste[0].append(x1)
        liste[1].append(y1)
        liste[2].append(w1)
        liste[3].append(h1)



def out_list(liste, mode):
    """Here we make the mean of our points of the temples"""

    if mode == 2:
        y1 = round(int(sum(liste[1]) / len(liste[1])))
        yh1 = round(int(sum(liste[3]) / len(liste[3])))
        x1 = round(int(sum(liste[0]) / len(liste[0])))
        xw1 = round(int(sum(liste[2]) / len(liste[2])))

        y2 = round(int(sum(liste[5]) / len(liste[5])))
        yh2 = round(int(sum(liste[7]) / len(liste[7])))
        x2 = round(int(sum(liste[4]) / len(liste[4])))
        xw2 = round(int(sum(liste[6]) / len(liste[6])))

        return y1, yh1, x1, xw1, y2, yh2, x2, xw2
 
    elif mode == 1:
        y1 = round(int(sum(liste[1]) / len(liste[1])))
        yh1 = round(int(sum(liste[3]) / len(liste[3])))
        x1 = round(int(sum(liste[0]) / len(liste[0])))
        xw1 = round(int(sum(liste[2]) / len(liste[2])))

        return y1, yh1, x1, xw1



def detections(frame, y1, yh1, x1, xw1,
               y2, yh2, x2, xw2,
               message1, message2, messages):
    """Let's crop the differents are of our temples
    and try to see if white pixels are present.
    If we found white pixels, if want say
    skin is on it"""

    area_one = frame[y1:yh1, x1:xw1]
    area_two = frame[y2:yh2, x2:xw2]


    def analysis_pixel_crop(area_one, message, messages):
        """This is a function of a function
        here we watch into the crop (into area temples)
        if there are 100 whites pixel
        if yes it want say user have touch his temples"""

        counter_pixel = 0
        for i in range(area_one.shape[0]):
            for j in range(area_one.shape[1]):
                if area_one[i, j] == 255:
                    counter_pixel += 1

        if counter_pixel > 100:
            displaying_message(messages, message)
            messages.append(message)

    analysis_pixel_crop(area_one, message1, messages)
    analysis_pixel_crop(area_two, message2, messages)

    

    #NB tempe droite is right temples
    #NB tempe gauche is left temples

def displaying_message(messages, message):
    if messages[-1] == message or messages[-2] == message:
        pass
    else:
        print(message)

        

