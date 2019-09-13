import cv2
import numpy as np
from PIL import Image
import imutils



eyescascade = cv2.CascadeClassifier('haar/haarcascade_eye.xml')
facecascade = cv2.CascadeClassifier('haar/haarcascade_frontalface_alt2.xml')


def detection_initialization(frame, gray, facecascade, eyescascade,
                             eye_list_one, eye_list_two):
    """First we detect the eyes thanks
        to a haarcascade in xml.

        Second we add each new position
        on a list.

        After we make a sum for have an average
        of the last points detected.
    """

    eyes = eyescascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=4,
        minSize=(30, 30),
        maxSize=(50, 50),
    )

    #eye = 0 for right and 1 for left
    eye = 0 
    for x, y, w, h in eyes:

        if eye == 0:
            eye_list_one[0].append(x)
            eye_list_one[1].append(y)
            eye_list_one[2].append(x+w)
            eye_list_one[3].append(y+h)
            cv2.rectangle(frame, (x, y), (x+w, y+h), 3)

        elif eye == 1:
            eye_list_two[0].append(x)
            eye_list_two[1].append(y)
            eye_list_two[2].append(x+w)
            eye_list_two[3].append(y+h)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 3)

        eye += 1


def eyes(frame, liste1, liste2):
    """We make an average of our list.
    It give us There may be good eye detection.
    We escape detection leap.
    then we crop the current frame with this points.
    """

    pts1 = int(round(sum(liste1[0]) / len(liste1[0])))
    pts2 = int(round(sum(liste1[1]) / len(liste1[1])))
    pts3 = int(round(sum(liste1[2]) / len(liste1[2])))
    pts4 = int(round(sum(liste1[3]) / len(liste1[3])))

    pts5 = int(round(sum(liste2[0]) / len(liste2[0])))
    pts6 = int(round(sum(liste2[1]) / len(liste2[1])))
    pts7 = int(round(sum(liste2[2]) / len(liste2[2])))
    pts8 = int(round(sum(liste2[3]) / len(liste2[3])))

    crop1 = frame[pts2 + 10:pts4, pts1:pts3]
    crop2 = frame[pts6 + 10:pts8, pts5:pts7]
    
    return crop1, crop2



def automatic_thresh(crop):
    """We increment a variable of +1
    and verify the area into the last crop. If the area
    if > 1200 we stop the loop (max value i can got).
    We have got an potential eye.
    We add + 20 to the min tresh for a better detection.
    """
    
    counter = 0
    ocontinuer = True
    while ocontinuer:

        if counter == 255:
            counter = 0
        
        gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (11, 11), 0)
        _, thresh = cv2.threshold(gray, counter, 255, 0)


        try:
            contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            img = cv2.drawContours(crop, contours, 1, (0,255,0), 3)
            for c in contours:
                if cv2.contourArea(c) >= 1200:
                    thresh_min = counter + 20
                    return True, thresh_min
        except:
            pass

        counter += 1


def detecting_eye(crop, thresh_min):
    """Here we detecting by treshold
    the eye. We display on the current frame
    the contour and take the center of this
    contour.
    This center will say to us if the eye has
    moved.
    """

    gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (11, 11), 0)
    _, thresh = cv2.threshold(gray, thresh_min, 255, 0)


    try:
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        img = cv2.drawContours(crop, contours, 1, (0,255,0), 3)

        for c in contours:
            M = cv2.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.circle(crop, (cX, cY), 1, (0, 0, 255), 1)
    except:
        pass


                    
                
def video_capture():


    video = cv2.VideoCapture(0)
    
    eye_list_one = [[], [], [], []]
    eye_list_two = [[], [], [], []]

    counter = 0
    
    STOP_INIT = False


    while(True):

        ret, frame = video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        #INITIALIZATION SITUATION EYES
        if len(eye_list_two[0]) < 30:
            detection_initialization(frame, gray, facecascade, eyescascade,
                                     eye_list_one, eye_list_two)

        else:
            crop_eye_right, crop_eye_left = eyes(frame,eye_list_one,
                                                 eye_list_two)


            #INITIALIZATION THRESHOLD
            if STOP_INIT is False:

                _, tresh_min_right = automatic_thresh(crop_eye_right)
                STOP_INIT, tresh_min_left = automatic_thresh(crop_eye_left)

                print(tresh_min_right, tresh_min_left)



            if STOP_INIT is True:

                detecting_eye(crop_eye_right, tresh_min_right)
                detecting_eye(crop_eye_left, tresh_min_left)


                
        cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    video.release()
    cv2.destroyAllWindows()






if __name__ == "__main__":
    video_capture()
