# imports
import os,sys,time
import numpy as np
import cv2
from émotion import face_detection
from émotion import detection_emotion


camera = cv2.VideoCapture("VIDEO.mp4")
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
eyesCascade = cv2.CascadeClassifier('haarcascade_eye.xml')


master = None
while True:

    _, frame = camera.read()
    frame = cv2.resize(frame, (1200, 1000))
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=3.0,
        minNeighbors=1,
        minSize=(60, 100),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    
    
    for x1, y1, w1, h1 in faces:
        
        frame2 = frame[y1:y1+h1, x1:x1+w1]
        gray2 = gray[y1:y1+h1, x1:x1+w1]
        
        cv2.rectangle(frame, (x1,y1), (x1+w1, y1+h1),(0,0,255), 2)
        
        y1 = y1.tolist()
        y1 = y1 + 20
        h1 = h1.tolist()
        h1 = int(round(h1/2.3))
        
        roi_gray = gray[y1:y1+h1, x1:x1+w1]
        
        
        eyes = eyesCascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.6,
            minNeighbors=1,
            minSize=(40, 40),
            flags=cv2.CASCADE_SCALE_IMAGE
        )


        #ICI RECUPERER X
        for x, y, w, h in eyes:
            cv2.rectangle(roi_gray, (x,y), (x+w, y+h),(0,0,255), 2)

        
        
        


    if master is None:
        master = gray2
        continue

    try:
        frame1 = cv2.absdiff(master, gray2)

        thresh = cv2.threshold(frame1,5,100,cv2.THRESH_BINARY)[1]


        contours,hierachy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        for c in contours:

            if cv2.contourArea(c) < 600:
                    continue

            x,y,w,h = cv2.boundingRect(c)
            rx = x+int(w/2)
            ry = y+int(h/2)

            cv2.rectangle(frame2,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.circle(frame2,(rx,ry),2,(0,255,0),2)
    except:
        pass
    
    master = gray2

    try:
        cv2.imshow("Frame6: Contours",frame2)
    except:
        pass






    key = cv2.waitKey(200) & 0xFF
    if key == ord('q'):
        break


camera.release()
cv2.destroyAllWindows()
