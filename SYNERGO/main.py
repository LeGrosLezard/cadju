import cv2
import time
import datetime
import imutils
import numpy as np



from mains.traitement_hand import delete_visage
from mains.traitement_hand import first_window
from mains.traitement_hand import seconde_window
from mains.traitement_hand import contour_image
from mains.traitement_hand import hull_function
from mains.traitement_hand import time
from mains.traitement_hand import points_main
from mains.traitement_hand import points
from mains.traitement_hand import hand_function


def video_capture():
    #We call Haarcascade
    #Face Cascade
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")


    video_capture = cv2.VideoCapture(0)

    first_frame = None
    
    while True:


        _, frame = video_capture.read()
        grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        drawing, first_frame = hand_function(frame, grayscale_frame, first_frame, faceCascade)


        windows = {"dazdza":drawing, "yeux":frame, "tete":frame, "visage":frame}
 
        for nom, fenetre in windows.items():
            cv2.imshow(nom, fenetre)




        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            cv2.destroyAllWindows()
            break


                    
    video.release()
    cv2.destroyAllWindows()
        





















if __name__ == "__main__":
    video_capture()
