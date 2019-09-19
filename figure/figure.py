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


def recup_points(frame, x, y, w, h, liste):
    point = frame[y+100:y+101, x+50:x+51]
    point = point.tolist()
    point = point[0][0]
    liste.append([point[0], point[1], point[2]])
    print(liste)
    cv2.rectangle(frame, (x+50, y+100), (x+51, y+101), (255, 0, 0), 5)
    

def put_points(frame, liste, x, y, w, h):

    

   
    cv2.rectangle(frame, (x+50, y+100), (x+51, y+101), (255, 0, 0), 5)
    


def video_capture():
    liste = []
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

        print(X,Y,W,H)
        print(x, y, w, h)


        if len(liste) < 1:
            recup_points(frame, x, y, w, h, liste)

        else:
            x, y, w, h = face_detection(frame, gray, faceCascade)
            put_points(frame, liste, x, y, w, h)
        









        cv2.imshow("frame", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            cv2.destroyAllWindows()
            break
                
        X = x
        Y = y
        W = x+w
        H = y+w

if __name__ == "__main__":
    video_capture()











