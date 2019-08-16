import numpy as np
import cv2

from skin import crop_face
from skin import detect_skin
from skin import delete_face


video = cv2.VideoCapture(0)

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
eyesCascade = cv2.CascadeClassifier('haarcascade_eye.xml')

subtractor = cv2.createBackgroundSubtractorMOG2(history=10000,
                                                varThreshold=50,
                                                detectShadows=True)

BOX1 = []

liste1 = []
liste2 = []
liste3 = []


while(True):

    
    _, frame = video.read()
    frame = cv2.GaussianBlur(frame,(5,5),100)
    

    if len(liste1) < 50:
        crop_face(frame, faceCascade, eyesCascade, BOX1,
                  liste1, liste2, liste3)

    else:
        try:
            delete_face(frame, faceCascade)
        except:
            pass
        
        image_mask = detect_skin(liste1, liste2, liste3, frame)
        
        blur = cv2.GaussianBlur(image_mask,(5,5),0)
        ret,thresh1 = cv2.threshold(blur,100,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


        max_area = 0
        for i in range(len(contours)):
            cnt=contours[i]
            area = cv2.contourArea(cnt)
            if(area>max_area):
                max_area=area
                ci=i
        hull = cv2.convexHull(cnt)

        
        cnt=contours[ci]
        drawing = np.zeros(frame.shape,np.uint8)
        cv2.drawContours(drawing,[cnt],0,(0,255,0),2)
        cv2.drawContours(drawing,[hull],0,(0,0,255),2)



        cv2.imshow('frame', image_mask)
        cv2.imshow('frame', thresh1)
        cv2.imshow("image.jpg", drawing)


    
    


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break





video.release()
cv2.destroyAllWindows()
