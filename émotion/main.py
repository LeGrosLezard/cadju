# imports
import os,sys,time
import numpy as np
import cv2

#uniquement la gueule
#récupérer le max de détail
#faire les émotions
#selon la région
#nettété
#et le tresh
camera = cv2.VideoCapture(0)

master = None
while True:

    _,frame = camera.rsead()
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    if master is None:
        master = gray
        continue

    frame1 = cv2.absdiff(master, gray)

    thresh = cv2.threshold(frame1,5,100,cv2.THRESH_BINARY)[1]


    contours,hierachy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:

        if cv2.contourArea(c) < 100:
                continue

        x,y,w,h = cv2.boundingRect(c)
        rx = x+int(w/2)
        ry = y+int(h/2)

        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.circle(frame,(rx,ry),2,(0,255,0),2)

    master = gray

    cv2.imshow("Frame6: Contours",frame)


    

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break


camera.release()
cv2.destroyAllWindows()
