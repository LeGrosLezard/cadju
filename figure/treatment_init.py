"""We ajust our filter, the main function is 
at the bottom"""

import cv2
import numpy as np

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
    gray=cv2.cvtColor(eyes_crop1, cv2.COLOR_BGR2GRAY)

    adaptive = 0
    Ocontinuer = True
    while Ocontinuer:
        if adaptive == 255:
            Ocontinuer = False

        _, thresh = cv2.threshold(gray, adaptive, 255,cv2.THRESH_BINARY)

        make_line(thresh)
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if len(contours) >= 2:
            for i in contours:
                if 1000.0 > cv2.contourArea(i) > nb:
                    Ocontinuer = False

                    cv2.imshow("image1", thresh)
                    cv2.waitKey(0)
                    return adaptive

        #print(adaptive)
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
                    return min_canny, grad

        min_canny += 1



def eyes_init(eyes, crop):
    mean = make_mean(eyes)

    for x1, y1, h1, w1 in eyes:
        eyes_crop = crop[y1+h1-35:y1+h1-10, x1:x1+w1]
        blur = cv2.GaussianBlur(eyes_crop, (5,5), 3)
        
        
        if int(x1+w1/2) > mean:
            min_canny, grad = find_canny_eyes(eyes_crop, blur, 4.5)

        elif int(x1+w1/2) < mean:
            min_canny, grad = find_canny_eyes(eyes_crop, blur, 2.5)
  







        

def main():
    """We lunch it"""

    eyescascade = cv2.CascadeClassifier('haar/haarcascade_eye.xml')
    facecascade = cv2.CascadeClassifier('haar/haarcascade_frontalface_alt2.xml')
    mouthcascade = cv2.CascadeClassifier('haar/mouth.xml')


    img = cv2.imread("WIN_20190925_13_48_04_Pro.jpg")

    eyes, crop, faces = detections(img, facecascade, eyescascade)
    thresholds_r, thresholds_l = on_eyelashes(eyes, crop, img, facecascade, eyescascade)

    eyes_init(eyes, crop)

    cv2.imshow("image", crop)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()




















