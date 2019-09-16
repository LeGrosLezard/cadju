import cv2
import numpy as np
from PIL import Image
import imutils
import time


def eyes(frame, gray, facecascade, eyescascade):
    """We make an average of our list.
    It give us There may be good eye detection.
    We escape detection leap.
    then we crop the current frame with this points.
    """

    crop1 = False
    crop2 = False

    faces = facecascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for x1, y1, w1, h1 in faces:
        roi_gray = gray[y1:y1+h1, x1:x1+w1]
        roi_color = frame[y1:y1+h1, x1:x1+w1]


        eyes = eyescascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.3,
            minNeighbors=4,
            minSize=(30, 30),
            maxSize=(45, 45),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        eye = 0
        for x, y, w, h in eyes:
            if eye == 0:
                crop1 = roi_color[y:y+h, x:x+w]
                cv2.rectangle(roi_color, (x, y), (x+w, y+h), (50, 255, 50), 5)
            elif eye == 1:
                crop2 = roi_color[y:y+h, x:x+w]
                cv2.rectangle(roi_color, (x, y), (x+w, y+h), (255, 0, 0), 5)
            eye += 1

        return crop1, crop2, faces



def automatic_thresh(crop):
    """We increment a variable of +1
    and verify the area into the last crop. If the area
    if > 1200 we stop the loop (max value i can got).
    We have got an potential eye.
    We add + 20 to the min tresh for a better detection.
    """

    counter = 0
    area_seuil_min = 1200

    while True:

        if counter == 255:
            return None

        gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (11, 11), 0)
        _, thresh = cv2.threshold(gray, counter, 255, 0)

        try:
            contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            img = cv2.drawContours(crop, contours, 1, (0,255,0), 3)
            center_detection(crop, contours)
            for c in contours:
                if cv2.contourArea(c) >= area_seuil_min:
                    thresh_min = counter + 20
                    return thresh_min, contours
        except:
            pass

        counter += 1


def center_detection(frame, contours):
    """Here we detection the center of our last detections"""

    for contour in contours:
        M = cv2.moments(contour)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        cv2.circle(frame, (cX, cY), 1, (0, 0, 255), 5)



def head_movement(frame, faces, liste_position):
    """Here we detect the head. Thank to this
    we can re initializing in cas where the personn
    moves his head.
    """

    for x, y, w, h in faces:

        #x movements and y movements
        try:
            if x > liste_position[0][-1] + 15:
                print("person moves to left")
            elif x < liste_position[0][-1] - 15:
                print("person moves to right")
            if y > liste_position[1][-1] + 15:
                print("person moves to bot")
            elif y < liste_position[1][-1] - 15:
                print("person moves to top")
        except IndexError:
            pass


        liste_position[0].append(x)
        liste_position[1].append(y)

        cv2.rectangle(frame, (x, y), (x+w, y+h), 3)



eyescascade = cv2.CascadeClassifier('haar/haarcascade_eye.xml')
facecascade = cv2.CascadeClassifier('haar/haarcascade_frontalface_alt2.xml')
def video_capture():


    video = cv2.VideoCapture(0)
    head_position = [[], [], [], []]

    while(True):

        ret, frame = video.read()
        frame = cv2.resize(frame, (800, 600))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        try:
            crop_eye_right, crop_eye_left,\
                            faces = eyes(frame, gray, facecascade,
                                         eyescascade)

            #INITIALIZATION THRESHOLD
            tresh_min_right, contours = automatic_thresh(crop_eye_right)
            tresh_min_left, contours = automatic_thresh(crop_eye_left)

            faces = head_movement(frame, faces, head_position)
        except:
            pass

   

        cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    video.release()
    cv2.destroyAllWindows()






if __name__ == "__main__":
    video_capture()
