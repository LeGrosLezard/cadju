import cv2


def face_detection(frame, gray, faceCascade):
    """We detecting the face by haarcascade"""

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(50, 50),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 10)
        return x, y, w, h


def recup_points(frame, x, y, w, h, liste_couleur):

    point = frame[y+100:y+101, x+50:x+51]

    point = point.tolist()
    point = point[0][0]

    liste_couleur.append([point[0], point[1], point[2]])
    cv2.rectangle(frame, (x+50, y+100), (x+51, y+101), (255, 0, 0), 5)
    
    return  x+50, y+100, x+51, y+101


def put_points(frame, liste_couleur, pts1, pts2, pts3, pts4,
               x, y):
    print("initialement", liste_couleur)
    print("suposé", frame[y:y+1, x:x+1])
    print("")

    cv2.rectangle(frame, (pts1, pts2), (pts3, pts4), (255, 0, 0), 5)
    cv2.rectangle(frame, (x, y), (x+1, y+1), (0, 0, 255), 5)
    


def video_capture():
    liste_couleur = []

    X = 0
    Y = 0
    W = 0
    H = 0

    faceCascade = cv2.CascadeClassifier("haar/haarcascade_frontalface_alt2.xml")
    video_capture = cv2.VideoCapture(0) 

    while True:
        _, frame = video_capture.read()
        frame = cv2.resize(frame, (800, 600))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        x, y, w, h = face_detection(frame, gray, faceCascade)


        if len(liste_couleur) < 1:
            pts1, pts2, pt3, pt4 = recup_points(frame, x, y, w, h,
                                                liste_couleur)

        else:

            x, y, w, h = face_detection(frame, gray, faceCascade)
            put_points(frame, liste_couleur, pts1, pts2, pt3, pt4,
                       x+50+(X-x), y+100+(Y-y))
        

        cv2.imshow("frame", frame)

        key = cv2.waitKey(200) & 0xFF
        if key == ord('q'):
            cv2.destroyAllWindows()
            break
                
        X = x
        Y = y
        W = x+w
        H = y+w

if __name__ == "__main__":
    video_capture()
