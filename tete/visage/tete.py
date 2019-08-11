import numpy as np
import cv2

def detect_box(x, y, y1,y2, w,
               BOX, frame):

    liste1 = []

    for i in range(y1, y2):
        for j in range(x, x+w):
            liste1.append(frame[i,j][0])

    liste1 = str(liste1)

    
    try:
        if sum(BOX)/len(BOX) + 1000 < len(liste1):
            cv2.rectangle(frame, (x, y1),
                          (x+w, y2), (0,0,255), 1)
            print("MAIN AU DESSUS DE LA TETE")
            
        elif sum(BOX)/len(BOX) - 1000 > len(liste1):
            cv2.rectangle(frame, (x, y1),
                          (x+w, y2), (255,0,255), 1)
            
        else:
            cv2.rectangle(frame, (x, y1),
                          (x+w, y2), 1)
            BOX.append(len(liste1))

    except:
        cv2.rectangle(frame, (x, y1),
                      (x+w, y2), 1)
        BOX.append(len(liste1))
            

def tete_haut(faceCascade, frame, x, y, h, w, BOX_ONE):
    
    x = x.tolist()
    y = y.tolist()
    h = h.tolist()
    w = w.tolist()

    dessus_visage1 = int(round(60 * 100 / h))
    dessus_visage2 = int(round(150 * 100 / h))


    #cv2.rectangle(frame, (x, y-dessus_visage2), (x+w, y-dessus_visage1),
    #              (0, 0, 255), 2)

    detect_box(x, y, y-dessus_visage2,
               y-dessus_visage1, w, BOX_ONE, frame)




def detection_face(faceCascade, frame, BOX_ONE):
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

        tete_haut(faceCascade, frame, x, y, h, w, BOX_ONE)
























