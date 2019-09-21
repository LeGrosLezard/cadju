import cv2
import numpy as np


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


def skin_detector(frame, x, y, w, h):

    frame[y:y+h, x:x+w]#haut






    


def video_capture():
    init = False


    faceCascade = cv2.CascadeClassifier("haar/haarcascade_frontalface_alt2.xml")
    video_capture = cv2.VideoCapture(0) 

    while True:

        _, frame = video_capture.read()
        frame = cv2.resize(frame, (800, 600))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        lower = np.array([0, 48, 80], dtype = "uint8")
        upper = np.array([20, 255, 255], dtype = "uint8")
        converted = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        skinMask = cv2.inRange(converted, lower, upper)

        skin = cv2.bitwise_and(frame, frame, mask = skinMask)


        cv2.imshow("frame", frame)
        cv2.imshow("images", skin)


        key = cv2.waitKey(200) & 0xFF
        if key == ord('q'):
            cv2.destroyAllWindows()
            break
                


if __name__ == "__main__":
    video_capture()











