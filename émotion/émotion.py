import cv2

def face_detection(faceCascade, frame):
    

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    

    c = 0
    for x1, y1, w1, h1 in faces:
    
        roi_gray = gray[y1:y1+h1, x1:x1+w1]
        roi_color = frame[y1:y1+h1, x1:x1+w1]
        
        eyes = eyesCascade.detectMultiScale(roi_gray,
            scaleFactor=1.3,
            minNeighbors=4,
            minSize=(40, 40),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        for x, y, w, h in eyes:

            cv2.rectangle(roi_color, (x,y), (x+w, y+h),(0, 0, 255), 2)
            
            if c == 1:
                x = x.tolist()
                LISTE.append(x)
            c+=1

    cv2.imshow('FACE CAPTURE', frame)
