import cv2
import numpy as np
import imutils
from datetime import datetime

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




def contour_image(dilate_image):
    
    cv2.imwrite("image_detector.jpg", dilate_image)

    image_detector = cv2.imread("image_detector.jpg")

    imgray = cv2.cvtColor(image_detector, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh,
                                           cv2.RETR_CCOMP,
                                           cv2.CHAIN_APPROX_SIMPLE)


    cv2.drawContours(image_detector, contours, -1, (0, 255, 0), 3)



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
            color_contours = (0, 255, 0) 
            color = (255, 0, 0) 
    
            cv2.drawContours(drawing, contours, i, color_contours, 1, 8, hierarchy)
            cv2.drawContours(drawing, hull, i, color, 1, 8)
            
    return drawing, hull



def points_main(drawing, hull):

    image_detector = cv2.imread("image_detector.jpg")
    pts_x = [[], [], []]
    pts_y = [[], [], []]
    dico = {}
    c = 0
    for i in hull:
        i = i.tolist()
        for j in i:
            dico[j[0][0]] = j[0][1]
            pts_x[0].append(j[0][0])
            pts_y[0].append(j[0][1])

    return pts_x, pts_y



def points(pts_x, pts_y, drawing):

    image_detector = cv2.imread("image_detector.jpg")

    l = h = image_detector.shape[1]
    h = image_detector.shape[0]
    h1 = int(round(h * 20 / 100))

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
                elif pts_y[0][i] > h-h1:
                    pass
                else:
                    pts_x[1].append(pts_x[0][i])
                    pts_y[1].append(pts_y[0][i])
            except:
                pass


    for i in range(len(pts_x[1])):
        cv2.circle(drawing, (pts_x[1][i], pts_y[1][i]), 3, (0,0,255), 3)
        




    return drawing






















