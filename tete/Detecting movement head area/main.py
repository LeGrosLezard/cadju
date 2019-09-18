import os
import cv2
import numpy as np
from PIL import Image


from config.config import SUBSTRACTOR1
from config.config import SUBSTRACTOR2
from config.config import SUBSTRACTOR3
from config.config import SUBSTRACTOR4
from config.config import SUBSTRACTOR5
from config.config import SUBSTRACTOR6
from config.config import SUBSTRACTOR7

from config.config import msg1
from config.config import msg2
from config.config import msg3
from config.config import msg4
from config.config import msg5
from config.config import msg6
from config.config import msg7
from config.config import msg8
from config.config import msg9

def face_detection(frame, gray, faceCascade):
    """We detecting the face by haarcascade"""

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(50, 50),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for x, y, w, h in faces:
        return x, y, w, h



def initialization(HEAD_MID, HEAD_SIDE, HEARS, TEMPLES,
                   x, y, w, h):
    """the initilization serves us to position our zones.
    In effect, we perform a variable set of these points
    (previously constructed) by adding to the figure"""


    def area_buiding(liste, x, y, w, h,
                     x1, y1, w1, h1, mode):
        """We insert into our list. mode 2 for hears for example.
        1 for the middle of the head"""

        if mode == 2:
            
            liste[0].append(x)
            liste[1].append(y)
            liste[2].append(w)
            liste[3].append(h)

            liste[4].append(x1)
            liste[5].append(y1)
            liste[6].append(w1)
            liste[7].append(h1)

        elif mode == 1:

            liste[0].append(x)
            liste[1].append(y)
            liste[2].append(w)
            liste[3].append(h)


    #MIDDLE OF THE HEAD
    area_buiding(HEAD_MID, x + int(round(w/3)), y - int(round(180 * 100 / h)),
                 x + int(round(w/3)) * 2, y - int(round(100 * 100 / h)),
                 "", "", "", "", 1)

    #HEAD_SIDE
    area_buiding(HEAD_SIDE, x - 20,
                 y - int(round(130 * 100 / h)),
                 x + 30,
                 y - int(round(70 * 100 / h)),
                 x+w-20,
                 y - int(round(130 * 100 / h)), x+w+30,
                 y-int(round(70 * 100 / h)), 2)

    #HEARS
    area_buiding(HEARS, x - 60, y + 70, x-20, y + 150,
                 x+w+20, y + 70, x + w + 60, y + 150, 2)

    #TEMPLES
    area_buiding(TEMPLES, x - 60, y - 20, x - 20, y + 40,
                 x+w + 20, y - 20, x + w + 60, y + 40, 2)



def area_built(liste, mode):
    """Here we make the mean of our points for positioning
    In case where our initialization is > 1"""

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


def crop_substrator(gray, y1, yh1, x1, xw1, subtractor):
    """We croping our area and make a substraction of the
    background. If movements are detected it will
    make appear some pixels. Without movement
    the area is egal to 0. With a minimum of movement
    the area have more than sum + 50 pixels."""

    crop = gray[y1:yh1, x1:xw1]
    mask = subtractor.apply(crop)

    liste = []

    for i in mask:
        for j in i:
            liste.append(j)

    if sum(liste) / len(liste) > 50 and\
       sum(liste) / len(liste) != 127.0:
        return True


def analysing_touch(middle, right_side, left_side, right_temple,
                    left_temple, right_hear, left_hear,
                    DISPLAY_MESSAGE):
    """We define the area to a message"""

    out = False

    if middle is True:
        if right_side is True or right_temple is True or right_hear is True:
            out = msg1
        elif left_side is True or left_temple is True or left_hear is True:
            out = msg2
        else:
            out = msg3

    elif right_side is True:
        out = msg4

    elif left_side is True:
        out = msg5

    elif right_temple is True:
        out = msg6

    elif left_temple is True:
        out = msg7

    elif right_hear is True:
        out = msg8

    elif left_hear is True:
        out = msg9

    DISPLAY_MESSAGE.append(out)



def analysing_display_message(DISPLAY_MESSAGE):
    """Here we choose the message to display.
    for touch mid head we must pass
    by hear and temples. For that we define
    mid head to 0 value. If personn touch hear (who's egal to 2)
    and touch temples (who's egal to 1)
    and finnaly mid (who's egal to 0), we take the lower
    value who's here 0.

    We return true if nothing is detecte it raise the list"""

    dico = {msg1:0, msg2:0, msg3:0,
            msg4:1, msg5:1,
            msg6:2, msg7:2,
            msg8:3, msg9:3}

    if DISPLAY_MESSAGE[-1] == False and len(DISPLAY_MESSAGE) > 2:

        lower_value = 10
        lower_msg = ""

        DISPLAY_MESSAGE = set(DISPLAY_MESSAGE)
        for i in DISPLAY_MESSAGE:
            if i not in("", False):
                for key, value in dico.items():
                    if i == key and value < lower_value :
                        lower_value = value
                        lower_msg = key

        if lower_msg != "":
            print(lower_msg)
        return True



def area_detection(frame, gray,
                   HEAD_MID, HEAD_SIDE, TEMPLES, HEARS,
                   SUBSTRACTOR1, SUBSTRACTOR2, SUBSTRACTOR3,
                   SUBSTRACTOR4, SUBSTRACTOR5, SUBSTRACTOR6,
                   SUBSTRACTOR7, DISPLAY_MESSAGE):
    """Here we have built our area, now we apply the substractor in
    the crop"""


    #mid
    y1, yh1, x1, xw1 = area_built(HEAD_MID, 1)
    middle = crop_substrator(gray, y1, yh1, x1, xw1, SUBSTRACTOR1)
    cv2.rectangle(frame, (x1, y1), (xw1, yh1), 3)

    #head side
    y1, yh1, x1, xw1, y2, yh2, x2, xw2 = area_built(HEAD_SIDE, 2)
    right_side = crop_substrator(gray, y1, yh1, x1, xw1, SUBSTRACTOR2)
    left_side = crop_substrator(gray, y2, yh2, x2, xw2, SUBSTRACTOR3)
    cv2.rectangle(frame, (x1, y1), (xw1, yh1), 3)
    cv2.rectangle(frame, (x2, y2), (xw2, yh2), 3)

    #temples
    y1, yh1, x1, xw1, y2, yh2, x2, xw2 = area_built(TEMPLES, 2)
    right_temple = crop_substrator(gray, y1, yh1, x1, xw1, SUBSTRACTOR4)
    left_temple = crop_substrator(gray, y2, yh2, x2, xw2, SUBSTRACTOR5)
    cv2.rectangle(frame, (x1, y1), (xw1, yh1), 3)
    cv2.rectangle(frame, (x2, y2), (xw2, yh2), 3)

    #hears
    y1, yh1, x1, xw1, y2, yh2, x2, xw2 = area_built(HEARS, 2)
    right_hear = crop_substrator(gray, y1, yh1, x1, xw1, SUBSTRACTOR6)
    left_hear = crop_substrator(gray, y2, yh2, x2, xw2, SUBSTRACTOR7)
    cv2.rectangle(frame, (x1, y1), (xw1, yh1), 3)
    cv2.rectangle(frame, (x2, y2), (xw2, yh2), 3)


    analysing_touch(middle, right_side, left_side, right_temple,
                    left_temple, right_hear, left_hear,
                    DISPLAY_MESSAGE)





def video_capture():
    """Lunch all functions and the camera capture

        INITIALIZATION = face_detection(),
                        initialization(),
                        area_buiding()

        Re initialization = face_detection()

        area_detection = area_built(),
                        crop_substrator(),
                        analysing_touch(),
                        area_detection(),
                        analysing_display_message()
    """

    HEAD_MID = [[], [], [], []]
    HEAD_SIDE = [[], [], [], [], [], [], [], []]
    TEMPLES = [[], [], [], [], [], [], [], []]
    HEARS = [[], [], [], [], [], [], [], []]
    HEAD_MOVEMENT = 0
    DISPLAY_MESSAGE = [""]
    

    video = cv2.VideoCapture(0)
    faceCascade = cv2.CascadeClassifier("haar/haarcascade_frontalface_alt2.xml")

    counter = 0
    
    while(True):
        
        ret, frame = video.read()
        frame = cv2.resize(frame, (800, 600))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #Inizialisation
        if len(HEAD_MID[0]) < 1:
            try:
                x, y, w, h = face_detection(frame, gray, faceCascade)
                initialization(HEAD_MID, HEAD_SIDE, HEARS, TEMPLES,
                               x, y, w, h)
            except:
                pass
            #no face detection


        #Initialization Succed
        else:

            try:
                #Re initialization
                x, _, _, _ = face_detection(frame, gray, faceCascade)
                if HEAD_MOVEMENT > x + 5 or HEAD_MOVEMENT < x - 5:
                    HEAD_MID = [[], [], [], []]
                    HEAD_SIDE = [[], [], [], [], [], [], [], []]
                    TEMPLES = [[], [], [], [], [], [], [], []]
                    HEARS = [[], [], [], [], [], [], [], []]


                #No initialization
                else:
                    area_detection(frame, gray,
                                    HEAD_MID, HEAD_SIDE, TEMPLES, HEARS,
                                    SUBSTRACTOR1, SUBSTRACTOR2, SUBSTRACTOR3,
                                    SUBSTRACTOR4, SUBSTRACTOR5, SUBSTRACTOR6,
                                    SUBSTRACTOR7, DISPLAY_MESSAGE)

            except TypeError:
                pass
            #no face detection
       

        try:
            HEAD_MOVEMENT = x
        except:
            pass

        #Traiting message to display
        raise_list = analysing_display_message(DISPLAY_MESSAGE)
        if raise_list is True:
            DISPLAY_MESSAGE = [""]


        cv2.imshow('FACE', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        

    video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    video_capture()
