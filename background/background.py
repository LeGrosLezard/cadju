import cv2
import numpy as np
import imutils
from datetime import datetime
from PIL import Image

def time():
    heure = datetime.now()
    heure = heure.hour

    return heure


def delete_visage(frame, dilate_image, faceCascade):
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )


    try:
        for x, y, w, h in faces:
            for i in range(y - 50, y + h + 400):
                for j in range(x - 50, x + w + 50):
                    dilate_image[i, j] = 0
    except:
        pass




def first_window(frame, val1, val2, val3, val4):

    greyscale_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gaussian_frame1 = cv2.GaussianBlur(greyscale_image, (val1, val2), 0)
    blur_frame1 = cv2.blur(gaussian_frame1, (val3, val4))

    return blur_frame1


def seconde_window(first_frame, blur_frame1, val):
    
    frame_delta = cv2.absdiff(first_frame, blur_frame1) 
    _, thresh = cv2.threshold(frame_delta, val, 255, cv2.THRESH_BINARY)
    dilate_image = cv2.dilate(thresh, None, iterations=1)

    return dilate_image




def contour_image(dilate_image, frame):
    
    cv2.imwrite("image_detector.jpg", dilate_image)

    image_detector = cv2.imread("image_detector.jpg")
    
    image = cv2.imread("image.jpg")
    image = cv2.resize(image, (400, 400))

    
    imgray = cv2.cvtColor(image_detector, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh,
                                           cv2.RETR_CCOMP,
                                           cv2.CHAIN_APPROX_SIMPLE)


    cv2.drawContours(image_detector, contours, -1, (0, 255, 0), 3)

    for i in range(image_detector.shape[0]):
        for j in range(image_detector.shape[1]):
            if thresh[i, j] != 0:
                image[i, j] = frame[i, j][0], frame[i, j][1], frame[i, j][2] 
                


    cv2.imshow("main2", frame)
    cv2.imshow("image", image)



























