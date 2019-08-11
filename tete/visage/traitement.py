import cv2
import numpy as np

def cote1(frame, x, y, w, h):

    pass


def decoupage(frame, faceCascade):
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.3, 5)
    
    for x, y, w, h in faces:

        x = x.tolist()
        y = y.tolist()
        w = w.tolist()
        h = h.tolist()

        crop = frame[y:y+100, x-30:x+w+30]
    

        blur = cv2.GaussianBlur(crop,(5,5),0)
        gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
        retval2,thresh1 = cv2.threshold(gray,70,255, cv2.THRESH_OTSU)

    try:
        cv2.imshow("treshold detector", thresh1)
    except:
        pass
