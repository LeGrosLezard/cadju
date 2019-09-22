import cv2
import numpy as np
from PIL import Image

from config import alpha_numeric

def adjust_gamma(image, gamma):
    """We add light to the video, we play with gamma"""

    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
            for i in np.arange(0, 256)]).astype("uint8")

    return cv2.LUT(image, table)



def detections(frame, gray, faceCascade, eyes_cascade):
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(60, 100),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

        crop = frame[y:y+h, x:x+w]
        gray_crop = gray[y:y+h, x:x+w]
        
        eyes = eyes_cascade.detectMultiScale(
            gray_crop,
            scaleFactor=1.3,
            minNeighbors=2,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        return eyes, crop


def sourcile(eyes, crop, alpha_numeric):

    new = 0
    c = 0
    for x1, y1, w1, h1 in eyes:

        #cv2.rectangle(crop, (x1, y1-20), (x1+w1, y1+20), (0, 0, 0), 2)
        eyes_crop = crop[y1-20:y1+20, x1:x1+w1]
        gray=cv2.cvtColor(eyes_crop, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 150, 255,cv2.THRESH_BINARY)

        for i in range(thresh.shape[0]):
            for j in range(thresh.shape[1]):

                if j == thresh.shape[1] - 1:
                    new += 1

                if thresh[i, j] == 0:
                    alpha_numeric[new].append([i, j])

        len_x = 0
        ligne = []

        for i in alpha_numeric:
            if i != []:
                if len(i) > len_x:
                    len_x = len(i)
                    ligne.append(i)

        for i in ligne[-1]:
            cv2.circle(eyes_crop, (i[1],i[0]), 1, (0,0,255), -1)

        
        alpha_numeric = []
        for i in range(500):
            alpha_numeric.append([])



def video_capture():

    eyescascade = cv2.CascadeClassifier('haar/haarcascade_eye.xml')
    facecascade = cv2.CascadeClassifier('haar/haarcascade_frontalface_alt2.xml')
    video = cv2.VideoCapture(0)
    while(True):

        ret, frame = video.read()
        frame = cv2.resize(frame, (800, 600))

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        try:
            eyes, crop = detections(frame, gray, facecascade, eyescascade)
            sourcile(eyes, crop, alpha_numeric)
        except:
            pass



        cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite("yoyoy.jpg")
            break

    video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    video_capture()
