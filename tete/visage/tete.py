import numpy as np
import cv2


def position_tete(x, w, POSITION_TETE):

    if x + w > sum(POSITION_TETE) / len(POSITION_TETE) + 40:
        print("le mec s'est rapproché")
        return "reposition"

    elif x + w < sum(POSITION_TETE) / len(POSITION_TETE) - 40:
        print("le mec s'est éloigné")
        return "reposition"

    else:
        POSITION_TETE.append(x+w)




def detection_face(faceCascade, frame, BOX_ONE, POSITION_TETE):


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )



    for x, y, w, h in faces:
        
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 2)
        
        reposition = position_tete(x, w, POSITION_TETE)

        liste1 = []
        x = x.tolist()
        y = y.tolist()
        h = h.tolist()
        w = w.tolist()


        if reposition == "reposition":
            out = "reposition"
        else:
            out = None

        return out


def haut_tete(frame, a, b, c, d, subtractor):
    
    cv2.rectangle(frame, (a,c), (b, d),(0, 0, 255), 2)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    crop = gray[d:c, a:b]

    mask = subtractor.apply(crop)

    liste1 = []
    for i in mask:
        for j in i:
            liste1.append(j)


    print(sum(liste1) / len(liste1))


  
    return mask
  
        






















