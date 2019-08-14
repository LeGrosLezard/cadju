import numpy as np
import cv2


def detection_face(frame, faceCascade):
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h),(0, 0, 0), 2)


    try:
        x = x.tolist()
        w = w.tolist()

        return x, w
    
    except:
        pass
    #pas de détection de tete



def position_haut_tete(faceCascade, frame,
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
                        POSITION_HAUT_TETE_Y2_3):

    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    

    for x, y, w, h in faces:
        
        cv2.rectangle(frame, (x,y), (x+w, y+h),(0, 0, 255), 2)
        

        liste1 = []
        x = x.tolist()
        y = y.tolist()
        h = h.tolist()
        w = w.tolist()

        dessus_visage1 = int(round(60 * 100 / h))
        dessus_visage2 = int(round(150 * 100 / h))

        carre = int(round(w/3))

        cv2.rectangle(frame,(x-20 ,y-dessus_visage1), (x + carre-20, y - dessus_visage2),
                      (0,255,0), 1)
        
        cv2.rectangle(frame,(x + carre, y-dessus_visage1),
                      (x + carre*2, y - dessus_visage2), (255,0,0), 1)
        
        cv2.rectangle(frame,(x+ carre*2 + 15, y-dessus_visage1),
                      ((x + carre*3) + 15, y - dessus_visage2), (0,0,255), 1)


        POSITION_HAUT_TETE_X_1.append(x-20)
        POSITION_HAUT_TETE_Y1_1.append(y-dessus_visage1)
        POSITION_HAUT_TETE_W_1.append(x + carre-20)
        POSITION_HAUT_TETE_Y2_1.append(y-dessus_visage2)
        
        POSITION_HAUT_TETE_X_2.append(x + carre)
        POSITION_HAUT_TETE_Y1_2.append(y-dessus_visage1)
        POSITION_HAUT_TETE_W_2.append(x + carre*2)
        POSITION_HAUT_TETE_Y2_2.append(y-dessus_visage2)
        
        POSITION_HAUT_TETE_X_3.append(x + carre*2 + 15)
        POSITION_HAUT_TETE_Y1_3.append(y-dessus_visage1)
        POSITION_HAUT_TETE_W_3.append(x + carre*3 + 15)
        POSITION_HAUT_TETE_Y2_3.append(y-dessus_visage2)      

        

def initialisation(frame, faceCascade, POSITION_TETE,
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
                    POSITION_HAUT_TETE_Y2_3):

    try:
        x, w = detection_face(frame, faceCascade)

        POSITION_TETE.append(x + w)
        position_haut_tete(faceCascade, frame,
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
        
    except:
        pass
    #pas de détection de tete





















    


