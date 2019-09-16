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
        cv2.rectangle(frame, (x1, y1), (x1+w1, y1+h1), (0,0,255), 5)
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

        return crop1, crop2



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
            return True, None

        gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (11, 11), 0)
        _, thresh = cv2.threshold(gray, counter, 255, 0)

        try:
            contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            img = cv2.drawContours(crop, contours, 1, (0,255,0), 3)
            for c in contours:
                if cv2.contourArea(c) >= area_seuil_min:
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

    kernel = np.ones((5,5), np.uint8) 

    gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (11, 11), 0)
    erosion = cv2.erode(gray, kernel, iterations=1) 
    _, thresh = cv2.threshold(erosion, thresh_min, 255, 0)


    try:
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        img = cv2.drawContours(crop, contours, 1, (0,255,0), 3)

        for c in contours:
            area = cv2.contourArea(c)
            M = cv2.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.circle(crop, (cX, cY), 1, (0, 0, 255), 1)
    except:
        pass



def no_detection(tresh_min_right, tresh_min_left):
    """if we havn't got any detection from the threshold
    filter we return False and re start an initialization
    in case right and left are None.
    If only left is none we make left filter = right filter.
    """

    if tresh_min_right != None and tresh_min_left != None:
        return True, tresh_min_right, tresh_min_left

    elif tresh_min_right == None and tresh_min_left == None:
        return False, tresh_min_right, tresh_min_left

    elif tresh_min_left == None:
        tresh_min_left = tresh_min_right
        return True, tresh_min_right, tresh_min_left



def head_movement(frame, gray, facecascade, liste_position):
    """Here we detect the head. Thank to this
    we can re initializing in cas where the personn
    moves his head.
    """

    init = False

    faces = facecascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=4,
        minSize=(30, 30),
    )


    for x, y, w, h in faces:

        #x movements and y movements
        try:
            if x > liste_position[0][-1] + 15:
                print("person moves to left")
                init = True
            elif x < liste_position[0][-1] - 15:
                print("person moves to right")
                init = True
            if y > liste_position[1][-1] + 15:
                print("person moves to bot")
                init = True
            elif y < liste_position[1][-1] - 15:
                print("person moves to top")
                init = True
        except IndexError:
            pass


        liste_position[0].append(x)
        liste_position[1].append(y)

        cv2.rectangle(frame, (x, y), (x+w, y+h), 3)

        return init




eyescascade = cv2.CascadeClassifier('haar/haarcascade_eye.xml')
facecascade = cv2.CascadeClassifier('haar/haarcascade_frontalface_alt2.xml')
def video_capture():


    video = cv2.VideoCapture(0)
    
    eye_list_one = [[], [], [], []]
    eye_list_two = [[], [], [], []]
    head_position = [[], [], [], []]


    counter = 0
    
    STOP_INIT = False


    while(True):

        ret, frame = video.read()
        frame = cv2.resize(frame, (800, 600))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        try:
            crop_eye_right, crop_eye_left = eyes(frame, gray, facecascade,
                                                 eyescascade)

            #INITIALIZATION THRESHOLD
            _, tresh_min_right = automatic_thresh(crop_eye_right)
            STOP_INIT, tresh_min_left = automatic_thresh(crop_eye_left)

        except:
            pass


##            STOP_INIT, tresh_min_right, tresh_min_left =\
##                       no_detection(tresh_min_right, tresh_min_left)

##                #INITIALIZATION THRESHOLD FAILED
##                if STOP_INIT is False:
##                        eye_list_one = [[], [], [], []]
##                        eye_list_two = [[], [], [], []]
##
##
##
##
##            #WE HAVE MATCH WITH THRESHOLD
##            if STOP_INIT is True:
##
##                faces = head_movement(frame, gray, facecascade,
##                                      head_position)
##
##                detecting_eye(crop_eye_right, tresh_min_right)
##                detecting_eye(crop_eye_left, tresh_min_left)





        cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    video.release()
    cv2.destroyAllWindows()






if __name__ == "__main__":
    video_capture()
