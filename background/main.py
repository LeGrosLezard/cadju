import cv2
import time
import datetime
import imutils
import numpy as np


from background import *




def motion_detection():
    
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
    
    video_capture = cv2.VideoCapture(0) 

    first_frame = None

    while True:

        
        _, frame = video_capture.read()
        frame = cv2.resize(frame, (400, 400))
        heure = time()
         
        if 20 > heure > 10:
            blur_frame1 = first_window(frame, 3, 3, 3, 3)

            if first_frame is None:
                first_frame = blur_frame1

            dilate_image = seconde_window(first_frame, blur_frame1, 15)


        else:
            blur_frame1 = first_window(frame, 21, 21, 5, 5)

            if first_frame is None:
                first_frame = blur_frame1

            dilate_image = seconde_window(first_frame, blur_frame1, 90)


        contour_image(dilate_image, frame)

        
        


        

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            cv2.destroyAllWindows()
            break
                



motion_detection()



















