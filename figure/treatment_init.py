"""We ajust our filter, the main function is 
at the bottom"""

import cv2
import numpy as np


def adjust_gamma(image, gamma):
    """We add light to the video, we play with gamma"""

    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
            for i in np.arange(0, 256)]).astype("uint8")

    return cv2.LUT(image, table)


def detections(img, faceCascade, eyes_cascade):
    """Here we detect the faces and the eyes"""

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(60, 100),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

        crop = img[y:y+h, x:x+w]
        gray_crop = gray[y:y+h-50, x:x+w]
        
        eyes = eyes_cascade.detectMultiScale(
            gray_crop,
            scaleFactor=1.3,
            minNeighbors=4,
            minSize=(30, 30),

            flags=cv2.CASCADE_SCALE_IMAGE
        )

        return eyes, crop, faces


def make_mean(eyes):
    """We make a mean of the 2 eyes length position
    because we need to differenciate the left and right
    eyes"""
    
    mean = 0
    for x1, y1, w1, h1 in eyes:
        mean += int(x1+w1/2)

    mean = int(mean/2)

    return mean


def make_line(thresh):
    """We make line for detect more than one area
    with border, on eyelashes is paste to the border"""

    cv2.line(thresh, (0, 0), (0, thresh.shape[0]), (255, 255, 255), 5)
    cv2.line(thresh, (0, 0), (thresh.shape[1], 0), (255, 255, 255), 5)
    cv2.line(thresh, (thresh.shape[1], 0), (thresh.shape[1], thresh.shape[0]), (255, 255, 255), 5)
    cv2.line(thresh, (0,  thresh.shape[0]), (thresh.shape[1], thresh.shape[0]), (255, 255, 255), 5)


def make_thresh(nb, x1, y1, w1, h1, crop):
    """We define an area, and let the threshold run
    in a loop. If we detect the area we stop it and recup it !"""

    eyes_crop1 = crop[y1-20:y1+10, x1:x1+w1]
    eyes_crop1 = adjust_gamma(eyes_crop1, 0.5)
    gray=cv2.cvtColor(eyes_crop1, cv2.COLOR_BGR2GRAY)

    adaptive = 0
    Ocontinuer = True
    while Ocontinuer:
        if adaptive == 255:
            Ocontinuer = False

        _, thresh = cv2.threshold(gray, adaptive, 255,cv2.THRESH_BINARY)

        make_line(thresh)
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        liste = []
        for i in range(thresh.shape[0]):
            for j in range(thresh.shape[1]):
                if thresh[i, j] == 0:
                    liste.append(j)
        length = 0
        if len(liste) > 1:
            length = max(liste)  - min(liste)

        if len(contours) >= 2:
            for i in contours:
                if 1000.0 > cv2.contourArea(i) > nb and length > 30:
                    Ocontinuer = False
                    cv2.imshow("image1", thresh)
                    cv2.waitKey(0)
                    return adaptive


        adaptive += 1

        
def on_eyelashes(eyes, crop, img, facecascade, eyes_cascade):
    """We call the mean for differenciate the eyes,
    and we run the threshold"""

    mean = make_mean(eyes)
    eyes, crop, faces = detections(img, facecascade, eyes_cascade)

    thresholds_r = 0
    thresholds_l = 0

    for x1, y1, w1, h1 in eyes:

        if x1+w1 < mean:
            threshold = make_thresh(198.5, x1, y1, w1, h1, crop)
            thresholds_l = threshold

        elif x1+w1 > mean:
            threshold = make_thresh(180.5, x1, y1, w1, h1, crop)
            thresholds_r = threshold
 
    return thresholds_r, thresholds_l



def find_canny_eyes(eyes_crop, blur, value):

    ocontinue = True
    grad = 100
    min_canny = 100
    while ocontinue:

        if min_canny == 255:
            min_canny = 0
            grad += 1

        edge = cv2.Canny(blur, min_canny, grad)

        cnts, _ = cv2.findContours(edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if len(cnts) == 2:
            for i in cnts:
                if cv2.contourArea(i) >= value:
                    cv2.drawContours(eyes_crop, i, -1, (0, 0, 255), 2)
                    
                    cv2.imshow("image", edge)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    return min_canny, grad

        min_canny += 1



def eyes_init(eyes, crop):
    mean = make_mean(eyes)

    for x1, y1, h1, w1 in eyes:
        eyes_crop = crop[y1+h1-35:y1+h1-10, x1:x1+w1]
        blur = cv2.GaussianBlur(eyes_crop, (5,5), 3)

        if int(x1+w1/2) > mean:
            min_canny_r, grad_r = find_canny_eyes(eyes_crop, blur, 4.5)

        elif int(x1+w1/2) < mean:
            min_canny_l, grad_l = find_canny_eyes(eyes_crop, blur, 2.5)
  
    
    return min_canny_r, grad_r, min_canny_l, grad_l



def mouth_init(faces, img, mouthcascade):
    for x, y, w, h in faces:
        crop = img[y+h-40:y+h-10, x+55:x+w-55]
        gray=cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)

        ocontinue = True
        min_thresh = 0
 
        while ocontinue:
            _, thresh = cv2.threshold(gray, min_thresh, 255,cv2.THRESH_BINARY)
            make_line(thresh)

            liste = []
            for i in range(thresh.shape[0]):
                for j in range(thresh.shape[1]):
                    if thresh[i, j] == 0:
                        liste.append(j)
            length = 0
            if len(liste) > 1:
                length = max(liste)  - min(liste)
  
            cnts, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            for i in cnts:

                if 1000 > cv2.contourArea(i) >= 500 and length > 50:
                    cv2.drawContours(crop, i, -1, (0, 0, 255), 2)
                    cv2.imshow("zaee", thresh)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()

                    return min_thresh

            min_thresh += 1



def main():
    """We lunch it"""

    eyescascade = cv2.CascadeClassifier('haar/haarcascade_eye.xml')
    facecascade = cv2.CascadeClassifier('haar/haarcascade_frontalface_alt2.xml')
    mouthcascade = cv2.CascadeClassifier('haar/mouth.xml')


    img = cv2.imread("treat_init.jpg")
    img = adjust_gamma(img, 2.0)
    eyes, crop, faces = detections(img, facecascade, eyescascade)

    on_eyes_thresholds_r, on_eyes_thresholds_l = on_eyelashes(eyes, crop, img,
                                                              facecascade, eyescascade)

    eyes_min_canny_r, eyes_grad_r,\
    eyes_min_canny_l, eyes_grad_l = eyes_init(eyes, crop)

    mouth_thresh = mouth_init(faces, img, mouthcascade)



    cv2.imshow("image", crop)
    cv2.waitKey(0)

    return on_eyes_thresholds_r, on_eyes_thresholds_l,\
           eyes_min_canny_r, eyes_grad_r,\
           eyes_min_canny_l, eyes_grad_l,\
           mouth_thresh



