import numpy as np
import cv2

from skin import crop_face
from skin import detect_skin
from skin import delete_face


video = cv2.VideoCapture(0)

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
eyesCascade = cv2.CascadeClassifier('haarcascade_eye.xml')

subtractor = cv2.createBackgroundSubtractorMOG2(history=100,
                                                varThreshold=50,
                                                detectShadows=True)

BOX1 = []

liste1 = []
liste2 = []
liste3 = []


while(True):



    _, frame = video.read()

    if len(liste1) < 1:
        crop_face(frame, faceCascade, eyesCascade, BOX1,
                  liste1, liste2, liste3)

    else:
        image_mask = detect_skin(liste1, liste2, liste3, frame)

        delete_face(frame, faceCascade)

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(5,5),0)
        ret,thresh1 = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)


        img2 = cv2.imread("main.jpg", cv2.IMREAD_GRAYSCALE)

        orb = cv2.ORB_create()
        kp1, des1 = orb.detectAndCompute(thresh1, None)
        kp2, des2 = orb.detectAndCompute(img2, None)


        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = bf.match(des1, des2)
        matches = sorted(matches, key = lambda x:x.distance)
        matching_result = cv2.drawMatches(thresh1, kp1, img2, kp2, matches[:50], None, flags=2)



        cv2.imshow("Matching result", matching_result)
        
        cv2.imshow("image.jpg", thresh1)
        cv2.imshow("image1.jpg", image_mask)










    if cv2.waitKey(1) & 0xFF == ord('q'):
        break





video.release()
cv2.destroyAllWindows()
