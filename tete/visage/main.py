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
    TIME = []
    POS = []
    LISTE = [[],[],[]]
    PRE_INIT = []

    POSITION_HAUT_TETE_X = []
    POSITION_HAUT_TETE_Y1 = []
    POSITION_HAUT_TETE_W = []
    POSITION_HAUT_TETE_Y2 = []
    
    POSITION_HAUT_TETE_X_1 = []
    POSITION_HAUT_TETE_Y1_1 = []
    POSITION_HAUT_TETE_W_1 = []
    POSITION_HAUT_TETE_Y2_1 = []

    POSITION_HAUT_TETE_X_2 = []
    POSITION_HAUT_TETE_Y1_2 = []
    POSITION_HAUT_TETE_W_2 = []
    POSITION_HAUT_TETE_Y2_2 = []

    POSITION_HAUT_TETE_X_3 = []
    POSITION_HAUT_TETE_Y1_3 = []
    POSITION_HAUT_TETE_W_3 = []
    POSITION_HAUT_TETE_Y2_3 = []


    DEBUT = 0

    video = cv2.VideoCapture(0)
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
    eyesCascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    
    subtractor = cv2.createBackgroundSubtractorMOG2(history=100,
                                                    varThreshold=50,
                                                    detectShadows=True)

    timmer = 0
    while(True):


        ret, frame = video.read()
        frame = cv2.resize(frame, (600, 600))


        try:

            if len(PRE_INIT) > 15:
                POSITION_TETE = []
                
                POSITION_HAUT_TETE_X_1 = []
                POSITION_HAUT_TETE_Y1_1 = []
                POSITION_HAUT_TETE_W_1 = []
                POSITION_HAUT_TETE_Y2_1 = []

                POSITION_HAUT_TETE_X_2 = []
                POSITION_HAUT_TETE_Y1_2 = []
                POSITION_HAUT_TETE_W_2 = []
                POSITION_HAUT_TETE_Y2_2 = []

                POSITION_HAUT_TETE_X_3 = []
                POSITION_HAUT_TETE_Y1_3 = []
                POSITION_HAUT_TETE_W_3 = []
                POSITION_HAUT_TETE_Y2_3 = []
                BOX_ONE = []
                POSITION_TETE = []
                TIME = []
                POS = []
                LISTE = [[],[],[]]
                PRE_INIT = []


                
        except:
            pass

        

        if len(POSITION_TETE) < 1:
            initialisation(frame, faceCascade, POSITION_TETE,
                            POSITION_HAUT_TETE_X,
                            POSITION_HAUT_TETE_Y1,
                            POSITION_HAUT_TETE_W,
                            POSITION_HAUT_TETE_Y2,
                            POSITION_HAUT_TETE_X_1,
                            POSITION_HAUT_TETE_Y1_1,
                            POSITION_HAUT_TETE_W_1,
                            POSITION_HAUT_TETE_Y2_1,
                            POSITION_HAUT_TETE_X_2,
                            POSITION_HAUT_TETE_Y1_2, 
                            POSITION_HAUT_TETE_W_2, 
                            POSITION_HAUT_TETE_Y2_2,
                            POSITION_HAUT_TETE_X_3,
                            POSITION_HAUT_TETE_Y1_3, 
                            POSITION_HAUT_TETE_W_3, 
                            POSITION_HAUT_TETE_Y2_3)
            DEBUT = 0
            print("initialisation")



        elif LISTE[0] != [] and LISTE[1] != [] and LISTE[2] != [] and timmer > 20 :
            
            a = []
            o = []
            dico = {}


            for i in LISTE:
                a.append(i[-1])
                dico[i[-1][0]] = i[-1][1]


            aaaa = 0
            for i in a:
                o.append(a[aaaa][1])
                aaaa += 1

            o = sorted(o)
            print(dico)
            for i in o:
                for cle, valeur in dico.items():
                    if i == valeur:
                        print(cle)

            LISTE = [[],[],[]]
            timmer = 0
   

            
        else:

            a = int(round(sum(POSITION_HAUT_TETE_X_1)/len(POSITION_HAUT_TETE_X_1)))
            b = int(round(sum(POSITION_HAUT_TETE_W_1)/len(POSITION_HAUT_TETE_W_1)))
            c = int(round(sum(POSITION_HAUT_TETE_Y1_1)/len(POSITION_HAUT_TETE_Y1_1)))
            d = int(round(sum(POSITION_HAUT_TETE_Y2_1)/len(POSITION_HAUT_TETE_Y2_1)))


            e = int(round(sum(POSITION_HAUT_TETE_X_1)/len(POSITION_HAUT_TETE_X_1)))
            f = int(round(sum(POSITION_HAUT_TETE_W_1)/len(POSITION_HAUT_TETE_W_1)))
            g = int(round(sum(POSITION_HAUT_TETE_Y1_1)/len(POSITION_HAUT_TETE_Y1_1)))
            h = int(round(sum(POSITION_HAUT_TETE_Y2_1)/len(POSITION_HAUT_TETE_Y2_1)))

            i = int(round(sum(POSITION_HAUT_TETE_X_2)/len(POSITION_HAUT_TETE_X_2)))
            j = int(round(sum(POSITION_HAUT_TETE_W_2)/len(POSITION_HAUT_TETE_W_2)))
            k = int(round(sum(POSITION_HAUT_TETE_Y1_2)/len(POSITION_HAUT_TETE_Y1_2)))
            l = int(round(sum(POSITION_HAUT_TETE_Y2_2)/len(POSITION_HAUT_TETE_Y2_2)))


            m = int(round(sum(POSITION_HAUT_TETE_X_3)/len(POSITION_HAUT_TETE_X_3)))
            n = int(round(sum(POSITION_HAUT_TETE_W_3)/len(POSITION_HAUT_TETE_W_3)))
            o = int(round(sum(POSITION_HAUT_TETE_Y1_3)/len(POSITION_HAUT_TETE_Y1_3)))
            p = int(round(sum(POSITION_HAUT_TETE_Y2_3)/len(POSITION_HAUT_TETE_Y2_3)))

            
            mask = haut_tete(frame, a, b, c, d, e, f, g, h, i,
                             j, k, l, m, n, o, p,
                             subtractor, DEBUT, timmer, LISTE, PRE_INIT)
            DEBUT += 1
            
            reposition = detection_face(faceCascade, frame, BOX_ONE,
                                        POSITION_TETE)

        
            if reposition == "reposition":
                POSITION_TETE = []
                
                POSITION_HAUT_TETE_X_1 = []
                POSITION_HAUT_TETE_Y1_1 = []
                POSITION_HAUT_TETE_W_1 = []
                POSITION_HAUT_TETE_Y2_1 = []

                POSITION_HAUT_TETE_X_2 = []
                POSITION_HAUT_TETE_Y1_2 = []
                POSITION_HAUT_TETE_W_2 = []
                POSITION_HAUT_TETE_Y2_2 = []

                POSITION_HAUT_TETE_X_3 = []
                POSITION_HAUT_TETE_Y1_3 = []
                POSITION_HAUT_TETE_W_3 = []
                POSITION_HAUT_TETE_Y2_3 = []
                
            else:
                pass

       

            
        cv2.imshow('FACE', frame)
        try:
            cv2.imshow('MASK', mask)
        except:
            pass
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        timmer += 1

    video.release()
    cv2.destroyAllWindows()









if __name__ == "__main__":

    video_capture()












