import numpy as np
import cv2
import time

from skin import delete_face






video = cv2.VideoCapture(0)

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")


subtractor = cv2.createBackgroundSubtractorMOG2(history=10000,
                                                varThreshold=50,
                                                detectShadows=True)

BACKGROUND = [[], []]


while(True):

    
    _, frame = video.read()
    frame = cv2.GaussianBlur(frame, (5, 5), 100)

    delete_face(frame, faceCascade)

    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    ret,thresh1 = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    cv2.imshow("image.jpg", thresh1)
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

    cv2.drawContours(drawing,[cnt],0,(0,255,0),1)

    cv2.drawContours(drawing,[hull],0,(0,0,255),1)


    for i in cnt:
        drawing[i[0][1], i[0][0]] = 0,0,0
        #BACKGROUND.a


    cv2.imshow("image.jpg", drawing)

   








    if cv2.waitKey(1) & 0xFF == ord('q'):
        break





video.release()
cv2.destroyAllWindows()
