import cv2
import numpy as np
import threading


def original_frame(originale, kernel_blur):

    originale = cv2.resize(originale, (800, 600))
    originale=cv2.cvtColor(originale, cv2.COLOR_BGR2GRAY)
    originale=cv2.GaussianBlur(originale, (kernel_blur, kernel_blur), 0)
    kernel_dilate=np.ones((10, 10), np.uint8)

    return originale, kernel_dilate


def face_detections(cascade, frame, gray):

    detection = cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(50, 50),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for x, y, w, h in detection:
        frame[y:y+h, x:x+w] = (0, 0, 0)


def detections(cascade, frame, gray):

    detection = cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=1,
        minSize=(30, 30),
        maxSize=(100, 100),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for x, y, w, h in detection:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)



def thread(handCascade, gestCascade,
           palmCascade, closeCascade,
           closedCascade, frame, gray):

    detections(handCascade, frame, gray)
    detections(gestCascade, frame, gray)
    detections(palmCascade, frame, gray)

    detections(closeCascade, frame, gray)
    detections(closedCascade, frame, gray)



def movements_detection(gray, originale, kernel_blur, seuil,
                        kernel_dilate, frame):

    gray = cv2.GaussianBlur(gray, (kernel_blur, kernel_blur), 0)
    mask = cv2.absdiff(originale, gray)
    mask = cv2.threshold(mask, seuil, 255, cv2.THRESH_BINARY)[1]
    mask = cv2.dilate(mask, kernel_dilate, iterations=5)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE)
    frame_contour=frame.copy()

    return contours, frame_contour, gray


def drawing_movements(contours, frame_contour, frame, surface):
    
    for c in contours:
        if cv2.contourArea(c) < 100000:

            cv2.drawContours(frame_contour, [c], 0, (0, 255, 0), 5)
            if cv2.contourArea(c) < surface:
                continue
            
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)










