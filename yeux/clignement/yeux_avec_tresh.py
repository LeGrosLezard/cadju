import numpy as np
import cv2
from PIL import Image
import os



def eyes_detection_config(roi_gray, eyescascade):
    """Eyes detection with the following configuration:
    the frame (here a crop of the frame does not gray),
    the pyragmidal image, the minimum number of neighbors,
    the size and the version of the haar"""

    eyes = eyescascade.detectMultiScale(
        roi_gray,
        scaleFactor=1.5,
        minNeighbors=1,
        minSize=(40, 40),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    return eyes


def face_detection_config(gray, facecascade):
    """Face detection with the following configuration:
    the frame (here a crop of the frame does not gray),
    the pyragmidal image, the minimum number of neighbors,
    the size and the version of the haar"""
    
    faces = facecascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=1,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    return faces




def cropage(frame, x, y, w, h, oeil):
    crop = frame[y+20:y+h-20, x:x+w]
    cv2.imwrite(oeil, crop)
    zoom(oeil)

def zoom(image):
    img = Image.open(image)
    img = img.resize((500, 500), Image.ANTIALIAS).save(image)

def modify_picture(image):
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gauss = cv2.GaussianBlur(gray, (41, 41), 0)
    ret,thresh = cv2.threshold(gauss,127,255,cv2.THRESH_BINARY)

    try:
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(image, contours, 1, (0,0,255), 3)

        cv2.imshow('RIGHT', image)
    except:
        pass








eyescascade = cv2.CascadeClassifier("haar/haarcascade_lefteye_2splits.xml")
facecascade = cv2.CascadeClassifier("haar/haarcascade_frontalface_alt2.xml")

video = cv2.VideoCapture(0)

while(True):
    ret, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detection_config(gray, facecascade)
    
    for x1, y1, w1, h1 in faces:
        roi_gray = gray[y1:y1+h1, x1:x1+w1]
        roi_color = frame[y1:y1+h1, x1:x1+w1]

        eyes = eyes_detection_config(roi_gray, eyescascade)

        counter = 0
        for x, y, w, h in eyes:
            if counter == 0:
                cropage(roi_color, x, y, w, h, "droit.jpg")
                
            elif counter == 1:
                cropage(roi_color, x, y, w, h, "gauche.jpg")
                
            counter += 1


    droite = cv2.imread("droit.jpg")
    modify_picture(droite)

    #cv2.imshow('EYES CAPTURE', frame)
    
    #cv2.imshow('LEFT', gauche)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()










