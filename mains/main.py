import cv2
import time
import datetime
import imutils
import numpy as np


from traitement_hand import delete_visage
from traitement_hand import first_window
from traitement_hand import seconde_window
from traitement_hand import contour_image
from traitement_hand import hull_function



def motion_detection():
    
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
    
    video_capture = cv2.VideoCapture(0) 

    first_frame = None

    while True:

        
        _, frame = video_capture.read()


        blur_frame1 = first_window(frame)

        if first_frame is None:
            first_frame = blur_frame1 


        dilate_image = seconde_window(first_frame, blur_frame1)

        delete_visage(frame, dilate_image, faceCascade)

        contours, thresh, hierarchy = contour_image(dilate_image)
        drawing = hull_function(contours, thresh, hierarchy)
    

        cv2.imshow("main", drawing)
        cv2.imshow('frame', frame)
        cv2.imshow('mask', dilate_image)



        

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            cv2.destroyAllWindows()
            break
                


if __name__=='__main__':    
    motion_detection()
