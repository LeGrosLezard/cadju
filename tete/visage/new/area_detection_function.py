import os
import sys
import time
import numpy as np
import cv2
from PIL import Image
import operator
from collections import defaultdict



def face_detection(faceCascade, gray, frame):

    #Face detector
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=1,
        minSize=(60, 100),
        flags=cv2.CASCADE_SCALE_IMAGE
    )


    #Points of the detecting face
    for x, y, w, h in faces:
        frame_skin_detector = frame[y+60:y+h - 20, x+20:x+w-20]
        frame_skin_detector = cv2.GaussianBlur(frame_skin_detector,
                                               (11, 11),
                                               cv2.BORDER_DEFAULT)
        cv2.imshow("dzdzadzadazdaz", frame_skin_detector)
        return frame_skin_detector, x, y, w, h




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



def appending(tempe, patte, hear, mid, x, y, w, h):
    """We initilise list, we append points of our area in function
    of face detection"""

    #temples
    append_list(tempe,
                x, y - 20, x - 40, y + 40,
                x+w, y - 20, x+w+40, y + 40,
                2)

    #border forhead
    append_list(patte,
                x - 20, y - int(round(110 * 100 / h)), x + 30, y - int(round(50 * 100 / h)),
                x+w-20, y - int(round(110 * 100 / h)), x+w+30, y-int(round(50 * 100 / h)),
                2)
    #hears
    append_list(hear,
                x - 40, y + 70, x, y + 150,
                x+w, y + 70, x+w+40, y+150,
                2)
    #mid head
    append_list(mid,
                x + int(round(w/3)), y - int(round(150 * 100 / h)), x + int(round(w/3)) * 2, y - int(round(80 * 100 / h)),
                "", "", "", "",
                1)




def most_pixel(frame, frame_skin_detector):
    """Here we collect all pixels
    from the face detection
    and return the highter presence of pixel"""

    #while True:
    cv2.imshow("po,n", frame_skin_detector)
    dico = {}
    img = Image.fromarray(frame_skin_detector)
    for value in img.getdata():
        if value in dico.keys():
            dico[value] += 1
        else:
            dico[value] = 1

    sorted_x = sorted(dico.items(),
                      key=operator.itemgetter(1), reverse=True)


    color_dico = {}
    for i in sorted_x:
        if i[1] < 10:
            break
        else:
            if i[0][2] > i[0][1] + 10:
                color_dico[i[0]] = i[1]

    best = 0
    best_color = 0

    lower = 1000
    lower_color = 0

    for key, value in color_dico.items():
        if value > best:
            best = value
            best_color = key

        if value < lower:
            lower = value
            lower_color = key



    UPPER = best_color
    LOWER = lower_color


    print(UPPER, LOWER)


    

    return UPPER, LOWER




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
               message1, message2, MESSAGES):
    """Let's crop the differents are of our temples
    and try to see if white pixels are present.
    If we found white pixels, if want say
    skin is on it"""

    area_one = frame[y1:yh1, x1:xw1]
    area_two = frame[y2:yh2, x2:xw2]


    def analysis_pixel_crop(area_one, message, MESSAGES):
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
            displaying_message(MESSAGES, message)
            MESSAGES.append(message)

    analysis_pixel_crop(area_one, message1, MESSAGES)
    analysis_pixel_crop(area_two, message2, MESSAGES)

    

    #NB tempe droite is right temples
    #NB tempe gauche is left temples


def displaying_message(MESSAGES, message):
    if MESSAGES[-1] == message or MESSAGES[-2] == message:
        pass
    else:
        print(message)

        
def MOVEMENT_detector(frame, TEMPE, HEAR, PATTE, MID, MESSAGES, skinMask):
    """We positionning our area from the mean of points
    recuped from initialisation"""

    #temples
    y1, yh1, x1, xw1, y2, yh2, x2, xw2 = out_list(TEMPE, 2)
    detections(skinMask, y1, yh1, x1, xw1, y2, yh2, x2, xw2,
               "TEMPE droite", "TEMPE gauche", MESSAGES)
    cv2.rectangle(frame, (x1, y1), (xw1, yh1), 3)
    cv2.rectangle(frame, (x2, y2), (xw2, yh2), 3)
    #HEAR
    y1, yh1, x1, xw1, y2, yh2, x2, xw2 = out_list(HEAR, 2)
    detections(skinMask, y1, yh1, x1, xw1, y2, yh2, x2, xw2,
               "oreille droite", "oreille gauche", MESSAGES)
    cv2.rectangle(frame, (x1, y1), (xw1, yh1), 3)
    cv2.rectangle(frame, (x2, y2), (xw2, yh2), 3)
    #border forehead
    y1, yh1, x1, xw1, y2, yh2, x2, xw2 = out_list(PATTE, 2)
    detections(skinMask, y1, yh1, x1, xw1, y2, yh2, x2, xw2,
               "PATTE droite", "PATTE gauche", MESSAGES)
    cv2.rectangle(frame, (x1, y1), (xw1, yh1), 3)
    cv2.rectangle(frame, (x2, y2), (xw2, yh2), 3)
    y1, yh1, x1, xw1 = out_list(MID, 1)
    detections(skinMask, y1, yh1, x1, xw1, 0, 0, 0, 0,
               "milieu de la tete", "", MESSAGES)
    cv2.rectangle(frame, (x1, y1), (xw1, yh1), 3)
    cv2.rectangle(frame, (x2, y2), (xw2, yh2), 3)
