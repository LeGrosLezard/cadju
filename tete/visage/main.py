import numpy as np
import cv2
from PIL import Image
import os



from tete import detection_face
from tete import haut_tete
from initialisation import initialisation


def video_capture():


    BOX_ONE = []
    POSITION_TETE = []
    
    POSITION_HAUT_TETE_X = []
    POSITION_HAUT_TETE_Y1 = []
    POSITION_HAUT_TETE_W = []
    POSITION_HAUT_TETE_Y2 = []


    video = cv2.VideoCapture(0)
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
    eyesCascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    
    subtractor = cv2.createBackgroundSubtractorMOG2(history=100,
                                                    varThreshold=50,
                                                    detectShadows=True)
    while(True):


        ret, frame = video.read()
        frame = cv2.resize(frame, (600, 600))


        if len(POSITION_TETE) < 5:
            initialisation(frame, faceCascade, POSITION_TETE,
                            POSITION_HAUT_TETE_X,
                            POSITION_HAUT_TETE_Y1,
                            POSITION_HAUT_TETE_W,
                            POSITION_HAUT_TETE_Y2)
            print("initialisation")
        else:

            a = int(round(sum(POSITION_HAUT_TETE_X)/len(POSITION_HAUT_TETE_X)))
            b = int(round(sum(POSITION_HAUT_TETE_W)/len(POSITION_HAUT_TETE_W)))
            c = int(round(sum(POSITION_HAUT_TETE_Y1)/len(POSITION_HAUT_TETE_Y1)))
            d = int(round(sum(POSITION_HAUT_TETE_Y2)/len(POSITION_HAUT_TETE_Y2)))

            
            mask = haut_tete(frame, a, b, c, d, subtractor)
            
            reposition = detection_face(faceCascade, frame, BOX_ONE,
                                        POSITION_TETE)

        
            if reposition == "reposition":
                POSITION_TETE = []
                
            else:
                pass

       

            
        cv2.imshow('FACE', frame)
        try:
            cv2.imshow('MASK', mask)
        except:
            pass
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    video.release()
    cv2.destroyAllWindows()









if __name__ == "__main__":

    video_capture()












