import numpy as np
import cv2
from PIL import Image
import os



from tete import detection_face
from initialisation import initialisation


def video_capture():


    BOX_ONE = []
    POSITION_TETE = []


    video = cv2.VideoCapture(0)
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
    eyesCascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    
    while(True):


        ret, frame = video.read()
        frame = cv2.resize(frame, (600, 600))


        if len(POSITION_TETE) < 20:
            initialisation(frame, faceCascade, POSITION_TETE)
            print("initialisation")
        else:
            reposition = detection_face(faceCascade, frame,
                                         BOX_ONE, POSITION_TETE)

            if reposition == "reposition":
                POSITION_TETE = []
            else:
                pass

        
        cv2.imshow('FACE', frame)




        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    video.release()
    cv2.destroyAllWindows()









if __name__ == "__main__":

    video_capture()












