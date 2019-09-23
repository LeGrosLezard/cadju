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
        gray_crop = gray[y:y+h-50, x:x+w]
        
        eyes = eyes_cascade.detectMultiScale(
            gray_crop,
            scaleFactor=1.3,
            minNeighbors=4,
            minSize=(30, 30),

            flags=cv2.CASCADE_SCALE_IMAGE
        )

        return eyes, crop, faces


def sourcile(eyes, crop):


    alpha_numeric = []
    for i in range(500):
        alpha_numeric.append([])

    new = 0
    c = 0
    for x1, y1, w1, h1 in eyes:

        #cv2.rectangle(crop, (x1, y1-20), (x1+w1, y1+20), (0, 0, 0), 2)
        eyes_crop = crop[y1-20:y1+10, x1:x1+w1]
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

        counter_pts = 0
        for i in ligne[-1]:
            if counter_pts % 10 == 0:
                cv2.circle(eyes_crop, (i[1],i[0]), 1, (0,0,255), 4)
            counter_pts += 1
        
        alpha_numeric = []
        for i in range(500):
            alpha_numeric.append([])




def mouth(faces, frame, mouthcascade):

    for x, y, w, h in faces:
        
        crop1 = frame[y+h-70:y+h, x:x+w]

        crop_g = cv2.cvtColor(crop1, cv2.COLOR_BGR2GRAY)

        mouth = mouthcascade.detectMultiScale(
            crop_g,
            scaleFactor=1.3,
            minNeighbors=6,
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        for x1, y1, w1, h1 in mouth:
            
            cv2.circle(crop1, (x1-5,y1+5), 1, (0,0,255), 5)
            cv2.circle(crop1, (x1+w1-5,y1+5), 1, (0,0,255), 5) 
            break
        
        
def eyes_localisation(eyes, crop, eyes_center_xD, eyes_center_yD,
                      eyes_center_xG, eyes_center_yG):

    counter = 0
    for x1, y1, h1, w1 in eyes:

        eyes_crop = crop[y1+h1-35:y1+h1-10, x1:x1+w1]
        blur = cv2.GaussianBlur(eyes_crop, (5,5), 3)
        edge = cv2.Canny(blur, 140, 200)

        _, thresh1 = cv2.threshold(edge, 127, 255,cv2.THRESH_BINARY)
        cnts, _ = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if len(cnts) == 0:
            cv2.circle(crop, (eyes_center_xD, eyes_center_yD), 1, (0,255,0), 5) 
            cv2.circle(crop, (eyes_center_xG, eyes_center_yG), 1, (255,0,0), 5)

        else:
            if counter == 0:
                if int(x1+w1/2) > eyes_center_xD + 20:
                    eyes_center_xG = int(x1+w1/2)
                    eyes_center_yG = int(y1+h1/2)
                else:
                    eyes_center_xD = int(x1+w1/2)
                    eyes_center_yD = int(y1+h1/2)
 
            elif counter == 1:
                if int(x1+w1/2) > eyes_center_xG - 20:
                    eyes_center_xD = int(x1+w1/2)
                    eyes_center_yD = int(y1+h1/2)
                else:
                    eyes_center_xG = int(x1+w1/2)
                    eyes_center_yG = int(y1+h1/2)
    
            cv2.drawContours(eyes_crop, cnts, -1, (0, 0, 255), 3)

        counter += 1

    
    return eyes_center_xD, eyes_center_yD, eyes_center_xG, eyes_center_yG





def video_capture():

    eyescascade = cv2.CascadeClassifier('haar/haarcascade_eye.xml')
    facecascade = cv2.CascadeClassifier('haar/haarcascade_frontalface_alt2.xml')
    mouthcascade = cv2.CascadeClassifier('haar/mouth.xml')

    eyes_center_xD = 0
    eyes_center_yD = 0
    eyes_center_xG = 0
    eyes_center_yG = 0

    video = cv2.VideoCapture(0)
    while(True):

        ret, frame = video.read()
        frame = cv2.resize(frame, (800, 600))

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        try:
            eyes, crop, faces = detections(frame, gray, facecascade, eyescascade)
            sourcile(eyes, crop)
            mouth(faces, frame, mouthcascade)
            eyes_center_xD, eyes_center_yD,\
            eyes_center_xG, eyes_center_yG\
            = eyes_localisation(eyes, crop, eyes_center_xD, eyes_center_yD,
                                eyes_center_xG, eyes_center_yG)
            
        except:
            pass


        cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    video_capture()
