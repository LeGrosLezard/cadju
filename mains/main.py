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

    if len(liste1) < 50:
        crop_face(frame, faceCascade, eyesCascade, BOX1,
                  liste1, liste2, liste3)

    else:
        delete_face(frame, faceCascade)
        
        image_mask = detect_skin(liste1, liste2, liste3, frame)

##        contours, hierarchy = cv2.findContours(image_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
##
##        max_area = 0
##        
##        for i in range(len(contours)):
##            cnt=contours[i]
##            area = cv2.contourArea(cnt)
##
##            if(area>max_area):
##                max_area=area
##                ci=i
##
##            
##            
##        hull = cv2.convexHull(cnt)
##
##        cnt=contours[ci]
##
##
##        drawing = np.zeros(frame.shape,np.uint8)
##
##        cv2.drawContours(drawing,[cnt],0,(0,255,0),2)



        cv2.imwrite("image1.jpg", image_mask)

        img1 = cv2.imread("image1.jpg", cv2.IMREAD_GRAYSCALE)
        img2 = cv2.imread("pouce.jpg", cv2.IMREAD_GRAYSCALE)


        orb = cv2.ORB_create()
        
        kp1, des1 = orb.detectAndCompute(img1, None)
        kp2, des2 = orb.detectAndCompute(img2, None)


        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = bf.match(des1, des2)
        matches = sorted(matches, key = lambda x:x.distance)
        matching_result = cv2.drawMatches(img1, kp1, img2, kp2, matches[:50], None, flags=2)

        print(len(matches))

        cv2.imshow("Matching result", matching_result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



        img1 = cv2.imread("image1.jpg", cv2.IMREAD_GRAYSCALE)
        img2 = cv2.imread("main.jpg", cv2.IMREAD_GRAYSCALE)


        orb = cv2.ORB_create()
        
        kp1, des1 = orb.detectAndCompute(img1, None)
        kp2, des2 = orb.detectAndCompute(img2, None)


        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = bf.match(des1, des2)
        matches = sorted(matches, key = lambda x:x.distance)
        matching_result = cv2.drawMatches(img1, kp1, img2, kp2, matches[:50], None, flags=2)

        print(len(matches))

        cv2.imshow("Matching result", matching_result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


        #cv2.imshow("image1.jpg", image_mask)
        #cv2.imshow("image10.jpg", drawing)
   










    if cv2.waitKey(1) & 0xFF == ord('q'):
        break





video.release()
cv2.destroyAllWindows()
