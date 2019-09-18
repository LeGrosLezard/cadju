import cv2
import numpy as np
import threading


def original_frame(originale, kernel_blur):
    """Make a first 'picture' for define the
    what we must raise and what we must take in consideration.
    We raise the background"""

    originale = cv2.resize(originale, (800, 600))
    originale=cv2.cvtColor(originale, cv2.COLOR_BGR2GRAY)
    originale=cv2.GaussianBlur(originale, (kernel_blur, kernel_blur), 0)
    kernel_dilate=np.ones((10, 10), np.uint8)

    return originale, kernel_dilate


def face_detections(cascade, frame, gray):
    """We make a face detection"""

    detection = cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=4,
        minSize=(40, 40),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for x, y, w, h in detection:
        return x, y, w, h
        

def detections(cascade, frame, gray, mode):
    """We make a general function for detect palm and fist.
    We make a rectangle and fill it for accelerate
    the detection into the movement detection."""

    detection = cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=1,
        minSize=(30, 30),
        maxSize=(100, 100),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for x, y, w, h in detection:
        if mode == 0:
            frame[y:y+h, x:x+w] = 255,0,0
        elif mode == 1:
            frame[y:y+h, x:x+w] = 255,255,0


def all_detections(handCascade, gestCascade,
                   palmCascade, closeCascade,
                   closedCascade, frame, gray):
    """We call detections function for
    run all this haar"""

    detections(handCascade, frame, gray, 0)
    detections(gestCascade, frame, gray, 0)
    detections(palmCascade, frame, gray, 0)

    detections(closeCascade, frame, gray, 1)
    detections(closedCascade, frame, gray, 1)



def movements_detection(gray, originale, kernel_blur, seuil,
                        kernel_dilate, frame):
    """This is our current frame in comparaison with
    original frame. We make a threshold, dilate it for
    and find the contours."""

    gray = cv2.GaussianBlur(gray, (kernel_blur, kernel_blur), 0)
    mask = cv2.absdiff(originale, gray)
    mask = cv2.threshold(mask, seuil, 255, cv2.THRESH_BINARY)[1]
    mask = cv2.dilate(mask, kernel_dilate, iterations=5)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE)
    frame_contour=frame.copy()

    return contours, frame_contour, gray


def detect(message):
    """We displaying right or left hand/fist"""

    if x1 < 350:
        print("right " + message)
    elif x1 > 450:
        print("left "  + message) 



def drawing_movements(contours, frame_contour, frame,
                      x, y, w, h):
    """We drawing in a rectangle the movement.
    This movement area beetween 10 000 and 500000.
    In this rectangle we search 255, 0, 0 and
    255, 255, 0 pixels."""


    stop = False
    for c in contours:

        if cv2.contourArea(c) > 10000 and\
           cv2.contourArea(c) < 50000:
            x1, y1, w1, h1 = cv2.boundingRect(c)

            if x1 > x and y1 > y and x1+w1 < x+w:
                pass
            else:
                cv2.rectangle(frame, (x1, y1), (x1+w1, y1+h1), (0, 0, 255), 2)

                liste = []
                crop = frame[y1:y1+w1, x1:x1+w1]
                liste.append(str(crop))
                find_hand = str(liste).find("255   0   0")
                find_fist = str(liste).find("255 255   0")

                if find_hand >= 0:
                    detect("hand")

                elif find_fist >= 0:
                    detect("fist")
