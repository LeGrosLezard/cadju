import numpy as np
import cv2
from PIL import Image
import os



from tete import detection_face

def video_capture():


    BOX_ONE = []

    video = cv2.VideoCapture(0)
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
    eyesCascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    
    while(True):


        ret, frame = video.read()
        frame = cv2.resize(frame, (600, 600))

        detection_face(faceCascade, frame, BOX_ONE)

        
        cv2.imshow('FACE', frame)




        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    video.release()
    cv2.destroyAllWindows()









if __name__ == "__main__":

    video_capture()












