import numpy as np
import cv2


def detect_face(frame, faceCascade):
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    try:
        return faces, gray
    except IndexError:
        pass



def detect_eyes(eyesCascade, roi_gray):
    
    eyes = eyesCascade.detectMultiScale(
        roi_gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )


    return eyes


def cache_oeil(eyes, roi_color):
    
    for x1, y1, w1, h1 in eyes:
        cv2.rectangle(roi_color, (x1,y1), (x1+w1, y1+h1),(0, 0, 255), 2)
        for i in range(y1, y1+h1):
            for j in range(x1, x1 + w1):
                roi_color[i, j] = 0,0,255



def recup_couleur(frame, BOX1, x, y, h, w,
                  liste1, liste2, liste3):
    
    for i in range(y, y + h):
        for j in range(x + 50, x + w - 50):
            if frame[i, j][0] == 0 and\
               frame[i, j][1] == 0 and\
               frame[i, j][2] == 255:
                pass
            else:
                BOX1.append(frame[i, j])

    for i in BOX1:
        i = i.tolist()
        liste1.append(i[0])
        liste2.append(i[1])
        liste3.append(i[2])

    
def crop_face(frame, faceCascade, eyesCascade, BOX1,
              liste1, liste2, liste3):
    
    faces, gray = detect_face(frame, faceCascade)

    for x, y, w, h in faces:

        x1 = x + 50
        y1 = y
        x2 = x + w - 50
        y2 = y + h
        c = 0, 0, 255

        cv2.rectangle(frame, (x1, y1), (x2, y2),(c), 2)
        roi_gray = gray[y:y, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = detect_eyes(eyesCascade, roi_gray)
        cache_oeil(eyes, roi_color)
        recup_couleur(frame, BOX1, x, y, h, w,
                      liste1, liste2, liste3)

                    


def delete_face(frame, faceCascade):

    try:
        faces , _ = detect_face(frame, faceCascade)

        x = faces[0][0].tolist()
        y = faces[0][1].tolist()
        w = faces[0][2].tolist()
        h = faces[0][3].tolist()

        for i in range(y - 40, y + h + 400):
            for j in range(x - 30, x + w + 30):
                frame[i, j] = 0, 0, 255

    except:
        pass

def detect_skin(liste1, liste2, liste3, frame):
    
    a = int(round(sum(liste1) / len(liste1) + 40))
    b = int(round(sum(liste2) / len(liste2) + 40))
    c = int(round(sum(liste3) / len(liste3) + 40))
    d = int(round(sum(liste1) / len(liste1) - 30))
    e = int(round(sum(liste2) / len(liste2) - 30))
    f = int(round(sum(liste3) / len(liste3) - 30))
    
    upper =  np.array([a, b, c])
    lower =  np.array([d, e, f])


    image_mask = cv2.inRange(frame, lower, upper)

    return image_mask

























