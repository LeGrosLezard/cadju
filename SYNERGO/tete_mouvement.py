import cv2




def position(MOUVEMENT, x, y):

    out = False

    if x > MOUVEMENT[0][-1] + 10:
        out = True

    elif x < MOUVEMENT[0][-1] - 10:
        out = True

    elif y < MOUVEMENT[1][-1] - 10:
        out = True

    elif y < MOUVEMENT[1][-1] - 10:
        out = True


    else:
        MOUVEMENT[0].append(x)
        MOUVEMENT[1].append(y)

    return out


def tete_mouvement(frame, faceCascade, MOUVEMENT):

    init = False
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    ) 

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0,0,0), 2)

        init = position(MOUVEMENT, x.tolist(), y.tolist())

    return init, frame


    
















    
