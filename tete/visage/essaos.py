import numpy as np
import cv2

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
eyesCascade = cv2.CascadeClassifier('haarcascade_eye.xml')

img = cv2.imread("tete_de_teube.jpg")
img = cv2.resize(img, (800, 700))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

LISTE = []

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags=cv2.CASCADE_SCALE_IMAGE
)

for x, y, w, h in faces:
    cv2.rectangle(img, (x+50,y), (x+w-50, y+h),(0, 0, 255), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    


    eyes = eyesCascade.detectMultiScale(
        roi_gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    
    for x1, y1, w1, h1 in eyes:
        cv2.rectangle(roi_color, (x1,y1), (x1+w1, y1+h1),(0, 0, 255), 2)
        for i in range(y1-10, y1+h1):
            for j in range(x1, x1 + w1):
                roi_color[i, j] = 0,0,255


    for i in range(y, y+h):
        for j in range(x+50, x+w-50):
            if img[i,j][0] == 0 and\
               img[i,j][1] == 0 and\
               img[i,j][2] == 255:
                pass
            else:
                LISTE.append(img[i,j])
                


    liste1 = []
    liste2 = []
    liste3 = []

    for i in LISTE:
        i = i.tolist()
        
        liste1.append(i[0])
        liste2.append(i[1])
        liste3.append(i[2])


    print(sum(liste1) / len(liste1))
    print(sum(liste2) / len(liste2))
    print(sum(liste3) / len(liste3))








            
cv2.imshow("jb", img)
