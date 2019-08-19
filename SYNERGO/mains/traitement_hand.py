import cv2
import numpy as np
import imutils
from datetime import datetime

def time():
    """We import time. The light isn't the same
    during a day. So we can adapt light for threshold
    background. Could work for you or not. We must adapt
    treshold parameters. It the base of this file."""

    heure = datetime.now()
    heure = heure.hour

    return heure


def first_window(grayscale_frame, val1, val2):

    gaussian_frame1 = cv2.GaussianBlur(grayscale_frame, (val1, val1), 0)
    blur_frame1 = cv2.blur(gaussian_frame1, (val2, val2))

    return blur_frame1


def seconde_window(first_frame, blur_frame1, val):
 
    frame_delta = cv2.absdiff(first_frame, blur_frame1) 
    _, thresh = cv2.threshold(frame_delta, val, 255, cv2.THRESH_BINARY)
    dilate_image = cv2.dilate(thresh, None, iterations=1)

    return dilate_image




def delete_visage(grayscale_frame, dilate_image, faceCascade):
    
    faces = faceCascade.detectMultiScale(
        grayscale_frame,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )


    try:
        faces = faces.tolist()
        for i in range(faces[0][1] - 50, faces[0][1] + faces[0][3] + 400):
            for j in range(faces[0][0] - 50, faces[0][0] + faces[0][2] + 50):
                dilate_image[i, j] = 0
    except:
        pass




def contour_image(dilate_image):
    
    cv2.imwrite("detector.jpg", dilate_image)

    image = cv2.imread("detector.jpg", cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(image, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP,
                                           cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

    return contours, thresh, hierarchy




def hull_function(contours, thresh, hierarchy):
    
    hull = []
     
    for i in range(len(contours)):
        hull.append(cv2.convexHull(contours[i], False))

    drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)

    for i in range(len(contours)):
        if len(contours[i]) < 200:
            pass
        else:
            cv2.drawContours(drawing, contours, i, (0, 255, 0), 1, 8, hierarchy)
            cv2.drawContours(drawing, hull, i, (255, 0, 0), 1, 8)
            
    return drawing, hull



def points_main(drawing, hull):

    image = cv2.imread("detector.jpg")
    pts_x = [[], [], []]
    pts_y = [[], [], []]
    dico = {}

    for i in hull:
        i = i.tolist()
        for j in i:
            dico[j[0][0]] = j[0][1]
            pts_x[0].append(j[0][0])
            pts_y[0].append(j[0][1])
   
    return pts_x, pts_y



def points(pts_x, pts_y, drawing):

    image = cv2.imread("detector.jpg")

    l = image.shape[1]
    h = int(round(image.shape[0] - h * 20 / 100))

    for i in range(2):
        for i in range(len(pts_x[0])):
            try:
                if pts_x[0][i] >= pts_x[0][i + 1] and\
                   pts_x[0][i] <= pts_x[0][i + 1] + 4 or\
                   pts_x[0][i] + 3 >= pts_x[0][i + 1] and\
                   pts_x[0][i] <= pts_x[0][i + 1] + 1 or\
                   pts_y[0][i] >= pts_y[0][i + 1] and\
                   pts_y[0][i] <= pts_y[0][i + 1] + 8:
                    pass
                elif pts_y[0][i] > h:
                    pass
                else:
                    pts_x[1].append(pts_x[0][i])
                    pts_y[1].append(pts_y[0][i])
            except:
                pass


    for i in range(len(pts_x[1])):
        cv2.circle(drawing, (pts_x[1][i], pts_y[1][i]), 3, (0,0,255), 3)

    return drawing






def hand_function(frame, grayscale_frame, first_frame, faceCascade):
    """We want detect hand and their significations.
    For that, we must first of all define the current hour.
    Indeed, the day light is very hight.
    So we need to ajust parameter of thresholding.
    """

    heure = time()
    
    def hour_depending(frame, heure, v1, v2, v3, first_frame):
        #we make it flou, it delete some contrasts, details.
        blur_frame1 = first_window(grayscale_frame, v1, v2)

        if first_frame is None:
            first_frame = blur_frame1
 
        #We dilate picture for details.
        dilate_image = seconde_window(first_frame, blur_frame1, v3)

        return blur_frame1, first_frame, dilate_image


  
    if 20 > heure > 10:
        blur_frame1, first_frame, dilate_image =\
                     hour_depending(frame, heure, 3, 3, 15, first_frame)
    else:
        blur_frame1, first_frame, dilate_image =\
                     hour_depending(frame, heure, 21, 5, 90, first_frame)


    delete_visage(grayscale_frame, dilate_image, faceCascade)

    contours, thresh, hierarchy = contour_image(dilate_image)
    drawing, hull = hull_function(contours, thresh, hierarchy)
    pts_x, pts_y = points_main(drawing, hull)
    drawing = points(pts_x, pts_y, drawing)

    return drawing, first_frame














