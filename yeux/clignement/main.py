import numpy as np
import cv2


from image_processing import pre_initialisation
from image_processing import y_eye_position
from image_processing import qualibrage
from image_processing import x_eye_position
from image_processing import association
from image_processing import pre_initialisation


def video_capture_yeux():
    """Here we lunch the video display (pc cam) with VideoCapture"""

    #We initialize list
    FIT_LIST = []
    LIST_RIGHT_LEFT = []
    QUALIFER_LIST = []

    video = cv2.VideoCapture("video/yeux.mp4")

    while(True):

        #Eyes haarcascade
        left_eye = cv2.CascadeClassifier('haar/haarcascade_lefteye_2splits.xml')
        facesa = cv2.CascadeClassifier('haar/haarcascade_frontalface_alt2.xml')

        #We define the current frame and resize it
        ret, frame = video.read()
        frame = cv2.resize(frame, (600, 600))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = facesa.detectMultiScale(
            gray, 1.3, 5)

        for (x,y,w,h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

        #We try to detect eyes into the frame 
        eyes = left_eye.detectMultiScale(roi_gray,
                                         minSize=(40, 40),
                                         minNeighbors=2)

        #we fill in our list of the current position
        #of the eyes in order to make an average of
        #them and then to be able to continue them.
        if len(FIT_LIST) < 50:
            pre_initialisation(eyes, FIT_LIST, roi_color)
            print("initialisation")

        #Now we catch the current position and
        #if the eyes move by -5 pixels for example
        #(on the y-axis) it is because the person looked up.
        else:
            pos_y = y_eye_position(eyes, FIT_LIST, roi_color)
            pos_x = x_eye_position(eyes, LIST_RIGHT_LEFT, roi_color)

            association(pos_y, pos_x, FIT_LIST)

            if pos_y!= None:
                QUALIFER_LIST.append(pos_y)
            qualibration = qualibrage(QUALIFER_LIST)
            if qualibration == "qualibration":
                FIT_LIST = []


            #If the person bent down, got up ...
            #We empty the list to re-initialize
            if pos_y in ("the person bent down",
                         "the person got up",
                         "the person lifted his head",
                         "the person has dropped his head"):

                FIT_LIST = []


        cv2.imshow('EYES CAPTURE', frame)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()






if __name__ == "__main__":
    video_capture_yeux()
