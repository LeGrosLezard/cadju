import numpy as np
import cv2
from PIL import Image
import os

from traitement_image import *








LISTE_AJUSTEMENT = []
def video_capture():

    LISTE_AJUSTEMENT = []
    video = cv2.VideoCapture(0)
    repere = 0
    
    while(True):


        left_eye = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')
        
          
        ret, frame = video.read()
        frame = cv2.resize(frame, (600, 600))
        eyes = left_eye.detectMultiScale(frame)


        if len(LISTE_AJUSTEMENT) < 100:
            pre_initialisation(repere, eyes, LISTE_AJUSTEMENT, frame)
            print("initialisation")
    
        else:
            position = position_yeux(repere, eyes, LISTE_AJUSTEMENT, frame)
            if position == None:
                pass
            else:
                print(position)

            if position in ("le mec s'est baissé", "le mec s'est levé"):
                LISTE_AJUSTEMENT = []




        cv2.imshow('YEUX CAPTURE', frame)






        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        repere += 1
    video.release()
    cv2.destroyAllWindows()









if __name__ == "__main__":

    video_capture()












