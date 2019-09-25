import cv2
import numpy as np
from PIL import Image
import operator
from collections import defaultdict


from treatment_init import main
#afin d'ajuster les seuil mettre une image genreu n tigre et compter les tache

def picture_to_init():
    """Take a picture of init and adaptation of filters"""

    cap = cv2.VideoCapture(0)
    _,frame = cap.read()
    frame = cv2.resize(frame, (800, 600))
    cap.release()
    cv2.imwrite('treat_init.jpg', frame)

    return False


def make_line(thresh):
    """We make line for detect more than one area
    with border, on eyelashes is paste to the border"""

    cv2.line(thresh, (0, 0), (0, thresh.shape[0]), (255, 255, 255), 5)
    cv2.line(thresh, (0, 0), (thresh.shape[1], 0), (255, 255, 255), 5)
    cv2.line(thresh, (thresh.shape[1], 0), (thresh.shape[1], thresh.shape[0]), (255, 255, 255), 5)
    cv2.line(thresh, (0,  thresh.shape[0]), (thresh.shape[1], thresh.shape[0]), (255, 255, 255), 5)



def adjust_gamma(image, gamma):
    """We add light to the video, we play with gamma"""

    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
            for i in np.arange(0, 256)]).astype("uint8")

    return cv2.LUT(image, table)



def detections(frame, gray,
               faceCascade, eyes_cascade,
               frame1):
    """We detecting face and eyes"""

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
        crop1 = frame1[y:y+h, x:x+w]
        gray_crop = gray[y:y+h-50, x:x+w]
        
        eyes = eyes_cascade.detectMultiScale(
            gray_crop,
            scaleFactor=1.3,
            minNeighbors=4,
            minSize=(30, 30),

            flags=cv2.CASCADE_SCALE_IMAGE
        )

        return eyes, crop, faces, crop1



#------------------------------------------------------------------------------------------eyelashes_top()
    
def build_list():
    """We build a list for append each x of threshold
    and have the borders"""

    alpha_numeric = []
    for i in range(500):
        alpha_numeric.append([])

    return alpha_numeric


def make_mean(eyes):
    """This mean give us the position of
    the detection if the eyes is right or left"""

    mean = 0
    if len(eyes) == 2:
        for x1, y1, w1, h1 in eyes:
            mean += int(x1+w1/2)

    mean = int(mean/2)
    return mean


def threshold_building(x1, w1, mean, eyes_crop,
                       on_eyes_thresholds_l,
                       on_eyes_thresholds_r):
    """We building a filter for recup the on eyes"""

    gray=cv2.cvtColor(eyes_crop, cv2.COLOR_BGR2GRAY)

    if (x1+w1/2) < mean:
        _, thresh = cv2.threshold(gray, on_eyes_thresholds_l,
                                  255, cv2.THRESH_BINARY)


    elif (x1+w1/2) > mean:
        _, thresh = cv2.threshold(gray, on_eyes_thresholds_r,
                                  255, cv2.THRESH_BINARY)


    return thresh



def points_of_thresh(alpha_numeric, thresh):
    """We recup each points of the thresh (x and y position of x axis)
    In case one day we'll ive need of the y axis"""

    new = 0

    for i in range(thresh.shape[0]):
        for j in range(thresh.shape[1]):

            if j == thresh.shape[1] - 1:
                new += 1

            if thresh[i, j] == 0:
                alpha_numeric[new].append([i, j])


def x_points_in_treated_list(alpha_numeric):
    """We recup only x position"""

    len_x = 0
    row = []
    for i in alpha_numeric:
        if i != []:
            if len(i) > len_x:
                len_x = len(i)
                row.append(i)
    return row


def drawing_point_from_list(ligne, eyes_crop):
    """We dawing the points"""

    counter_pts = 0
    row = 0

    for i in ligne[-1]:
        if counter_pts % 10 == 0:
            cv2.circle(eyes_crop, (i[1],i[0]), 1, (0,0,255), 4)
            row = i[0]
        counter_pts += 1

    return row



def on_eyes_detection(rowD, rowG):
    """If the two on eyes are min 15 we display it"""

    if rowD != 0 or rowG != 0:
        if rowD < 15 and rowG < 15:
           print("levé")



def eyelashes_top(eyes, crop, on_eyes_thresholds_r, on_eyes_thresholds_l):
    """ - eyes for eyes detection
        - crop the crop of the face
        - on_eyes_thresholds_r automatic by init
        - on_eyes_thresholds_l automatic by init
    
        -----> top eyelashes detection
    """

    rowD = 0
    rowG = 0

    alpha_numeric = build_list() #built a list of list
    mean = make_mean(eyes) #make a mean of the x position of eyes

    for x1, y1, w1, h1 in eyes:

        eyes_crop = crop[y1-20:y1+10, x1:x1+w1]#crop frame focus on on eyes

        thresh = threshold_building(x1, w1, mean, eyes_crop,
                                    on_eyes_thresholds_l,
                                    on_eyes_thresholds_r)#build thresh
        
        points_of_thresh(alpha_numeric, thresh)#add list to thresh points
        ligne = x_points_in_treated_list(alpha_numeric)#only take x axis

        row = drawing_point_from_list(ligne, eyes_crop)#draw points

        if (x1+w1/2) < mean:
            rowD = row #We need to know if it's right eyes
                
        elif (x1+w1/2) > mean:
            rowG = row #We need to know if it's left eyes

    on_eyes_detection(rowD, rowG)#Displaying in case of detection

#----------------------------------------------------------------------------------------------------eyelashes_top()




#----------------------------------------------------------------------------------------------------eyelashes_down()

def down_detection(gray, min_thresh, detection, eyes_crop):
    """
        -> Make thresh
        -> Recup max y points () the one that is the lowest
        -> if this last point < the last points of the last loop -> it fallen
    """

    _, thresh = cv2.threshold(gray, min_thresh, 255,cv2.THRESH_BINARY)
    make_line(thresh)   #Doing lines on each length and width of the rectangle

    liste = []
    for i in range(int(thresh.shape[0])):  #Recup y points
        for j in range(int(thresh.shape[1]/2)):
            if thresh[i, j] == 0:
               liste.append(j)

    position = max(liste)   #Recup the smallest point on y axis

    if position > detection + 2:    #it is superior of the last detection ?
        print("baisse")

    #Draw the points
    cv2.circle(eyes_crop, (position, int(thresh.shape[0]/2)), 1, (0, 0, 0), 5)

    return position


def eyelashes_down(eyes, crop1, lenght_detectionD, lenght_detectionG,
                    on_eyes_thresholds_r, on_eyes_thresholds_l):
    """
        We search the smaller points for know if eyelashes has fallen

        -----> down eyelashes detection
    """

    mean = make_mean(eyes)  #Mean for know if it's right or left points

    for x1, y1, w1, h1 in eyes:
        eyes_crop = crop1[y1-20:y1+20, x1+10:x1+w1]  #Only focus on this eyelashes area
        gray=cv2.cvtColor(eyes_crop, cv2.COLOR_BGR2GRAY)


        if (x1+w1/2) < mean: #right, we search the smaller y point
            y_position_eyelashes_down_R = down_detection(gray, on_eyes_thresholds_r,
                                                         lenght_detectionD, eyes_crop)

        elif (x1+w1/2) > mean: #left
            y_position_eyelashes_down_L = down_detection(gray, on_eyes_thresholds_l,
                                                         lenght_detectionG, eyes_crop)

    #We return this points and compare it each loop
    return y_position_eyelashes_down_R, y_position_eyelashes_down_L



#----------------------------------------------------------------------------------------------------eyelashes_down()





#----------------------------------------------------------------------------------------------------eyes()

def make_canny(x1, w1, mean, blur,
               eyes_min_canny_r, eyes_grad_r,
               eyes_min_canny_l, eyes_grad_l):

    if int(x1+w1/2) > mean:
        edge = cv2.Canny(blur, eyes_min_canny_r, eyes_grad_r)
    elif int(x1+w1/2) < mean:
        edge = cv2.Canny(blur, eyes_min_canny_l, eyes_grad_l)

    return edge


def close_eyes(cnts, crop, eyes_center_xD, eyes_center_yD,
               eyes_center_xG, eyes_center_yG):

    cv2.circle(crop, (eyes_center_xD, eyes_center_yD), 1, (0,255,0), 10) 
    cv2.circle(crop, (eyes_center_xG, eyes_center_yG), 1, (255,0,0), 10)

def in_case_close_eye(x1, w1, y1, h1, mean,
                      eyes_center_xG, eyes_center_yG,
                      eyes_center_xD, eyes_center_yD):


    if int(x1+w1/2) > mean: #In case close eyes
        eyes_center_xG = int(x1+w1/2)
        eyes_center_yG = int(y1+h1/2)

    else:
        eyes_center_xD = int(x1+w1/2)
        eyes_center_yD = int(y1+h1/2)

    return eyes_center_xG, eyes_center_yG,\
           eyes_center_xD, eyes_center_yD



def eyes_localisation(eyes, crop, eyes_center_xD, eyes_center_yD,
                      eyes_center_xG, eyes_center_yG,
                      eyes_min_canny_r, eyes_grad_r,
                      eyes_min_canny_l, eyes_grad_l):


    mean = make_mean(eyes)

    for x1, y1, h1, w1 in eyes:

        if len(eyes) == 2:
            eyes_crop = crop[y1+h1-35:y1+h1-10, x1:x1+w1]
            blur = cv2.GaussianBlur(eyes_crop, (5,5), 3)


            edge = make_canny(x1, w1, mean, blur,
                              eyes_min_canny_r, eyes_grad_r,
                              eyes_min_canny_l, eyes_grad_l)

            _, thresh1 = cv2.threshold(edge, 127, 255,cv2.THRESH_BINARY)
            cnts, _ = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


            if len(cnts) == 0:
                close_eyes(cnts, crop, eyes_center_xD, eyes_center_yD,
                           eyes_center_xG, eyes_center_yG)

            for i in cnts:
                if cv2.contourArea(i) > 2.0:
                    cv2.drawContours(eyes_crop, i, -1, (0, 0, 255), 3)

            else:
                eyes_center_xG, eyes_center_yG,\
                eyes_center_xD, eyes_center_yD =\
                in_case_close_eye(x1, w1, y1, h1, mean,
                                  eyes_center_xG, eyes_center_yG,
                                  eyes_center_xD, eyes_center_yD)


    if eyes_center_xG > mean and eyes_center_xD < mean and len(eyes) == 2:
        return eyes_center_xD, eyes_center_yD, eyes_center_xG, eyes_center_yG




#----------------------------------------------------------------------------------------------------eyes()





#----------------------------------------------------------------------------------------------------mouth()

def mouth(faces, frame, mouthcascade, mouth_pts1_x):

    for x, y, w, h in faces:
        
        crop1 = frame[y+h-50:y+h, x+50:x+w-50]
        crop_g = cv2.cvtColor(crop1, cv2.COLOR_BGR2GRAY)

        square = int(w/3)
        crop = frame[y+h-40:y+h, x+square:x+w-square]


        mouth = mouthcascade.detectMultiScale(
            crop_g,
            scaleFactor=1.1,
            minNeighbors=5,
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        for x1, y1, w1, h1 in mouth:

            if x1+w1 < mouth_pts1_x - 10:
                print("ooooooh")
            else:
                mouth_pts1_x = x1+w1

    return mouth_pts1_x

#----------------------------------------------------------------------------------------------------mouth()


#----------------------------------------------------------------------------------------------------smyling()
def smyling_list_thresh(crop_window, thresh1):

    x_liste = []
    y_liste = []

    for i in range(crop_window.shape[0]):
        for j in range(crop_window.shape[1]):
            if thresh1[i, j] != 255:
                x_liste.append(i)
                y_liste.append(j)

    return x_liste, y_liste


def border_point_mouth(y_liste, x_liste, crop_frame):

    coin_dx = min(y_liste)
    coin_dy = x_liste[y_liste.index(min(y_liste))]

    coin_gx = max(y_liste)
    coin_gy = x_liste[y_liste.index(max(y_liste))]


    cv2.circle(crop_frame, (coin_dx, coin_dy), 1, (0, 0, 0), 10)
    cv2.circle(crop_frame, (coin_gx, coin_gy), 1, (0, 0, 0), 10)

    return coin_dx, coin_dy, coin_gx, coin_gy



def center_y_min_mouth(coin_dx, coin_gx, thresh1, crop_window,
               crop_frame, coin_dy, coin_gy):

    mid = int((coin_dx + coin_gx) / 2)

    liste_mid_top = []
    for i in range(crop_window.shape[0]):
        for j in range(mid):
            if thresh1[i, j] == 0:
                liste_mid_top.append(i)

    cv2.circle(crop_frame, (mid, max(liste_mid_top)), 1, (255, 0, 255), 5)
    cv2.line(crop_frame, (mid, max(liste_mid_top)), (coin_dx, coin_dy), (0, 0, 255))
    cv2.line(crop_frame, (mid, max(liste_mid_top)), (coin_gx, coin_gy), (0, 0, 255))



def smyling(frame, faces, mouth_thresh):

    for x, y, w, h in faces:

        crop1 = frame[y+h-50:y+h-30, x+55:x+w-55]
        crop_frame = crop1
        crop1 = adjust_gamma(crop1, 0.6)

        gray=cv2.cvtColor(crop1, cv2.COLOR_BGR2GRAY)
        _, thresh1 = cv2.threshold(gray, mouth_thresh, 255,cv2.THRESH_BINARY)
        cv2.imshow("dazdaz", thresh1)


        crop_window = thresh1[int(thresh1.shape[0]/5.5):int(thresh1.shape[0]/1.3), 0:thresh1.shape[1]]


        x_liste, y_liste = smyling_list_thresh(crop_window, thresh1)


        coin_dx, coin_dy, coin_gx, coin_gy\
        = border_point_mouth(y_liste, x_liste, crop_frame)

        center_y_min_mouth(coin_dx, coin_gx, thresh1, crop_window,
                           crop_frame, coin_dy, coin_gy)
 

#----------------------------------------------------------------------------------------------------smyling()
  


#----------------------------------------------------------------------------------------------------nose()
def nose(frame, faces):

    for x, y, w, h in faces:

        square = int(w/3)

        crop = frame[y+int(270*100/y):y+h-60, x+square:x+w-square]
        gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        edge = cv2.Canny(gray, 0, 255)
        
        cnts, _ = cv2.findContours(edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        cv2.drawContours(crop, cnts, -1, (0, 0, 255), 3)
        if cnts:
            print("He smelling you bro or he asks concentration")
#----------------------------------------------------------------------------------------------------nose()



#----------------------------------------------------------------------------------------------------teeth()
def teeth(frame, faces):
    for x, y, w, h in faces:

        crop1 = frame[y+h-50:y+h-20, x+55:x+w-55]
        gray = cv2.cvtColor(crop1, cv2.COLOR_BGR2GRAY)
        edge = cv2.Canny(gray, 0, 255)

        cnts, _ = cv2.findContours(edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for i in cnts:
            if cv2.contourArea(i) > 95:
                print("teeth appears or something on the mouse")
 
#----------------------------------------------------------------------------------------------------teeth()



def video_capture(on_eyes_thresholds_r, on_eyes_thresholds_l,\
                   eyes_min_canny_r, eyes_grad_r,\
                   eyes_min_canny_l, eyes_grad_l,\
                   mouth_thresh):

    eyescascade = cv2.CascadeClassifier('haar/haarcascade_eye.xml')
    facecascade = cv2.CascadeClassifier('haar/haarcascade_frontalface_alt2.xml')
    mouthcascade = cv2.CascadeClassifier('haar/mouth.xml')

    eyes_center_xD = 0
    eyes_center_yD = 0
    eyes_center_xG = 0
    eyes_center_yG = 0

    listeD = []
    listeG = []

    lenght_detectionD = 1000
    lenght_detectionG = 1000



    mouth_pts1_x = -10000

    video = cv2.VideoCapture(0)
    while(True):

        ret, frame = video.read()
        frame = cv2.resize(frame, (800, 600))
        frame1 = cv2.resize(frame, (800, 600))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        try:
            eyes, crop, faces, crop1 = detections(frame, gray,
                                                 facecascade, eyescascade,
                                                 frame1)


            eyelashes_top(eyes, crop, on_eyes_thresholds_r, on_eyes_thresholds_l)

            teeth(frame, faces)

            mouth_pts1_x = mouth(faces, frame, mouthcascade,
                                 mouth_pts1_x)
            smyling(frame, faces, mouth_thresh)

            eyes_center_xD, eyes_center_yD,\
            eyes_center_xG, eyes_center_yG\
            = eyes_localisation(eyes, crop, eyes_center_xD, eyes_center_yD,
                                eyes_center_xG, eyes_center_yG,
                                eyes_min_canny_r, eyes_grad_r,
                                eyes_min_canny_l, eyes_grad_l)
            
            lenght_detectionD, lenght_detectionG\
            = eyelashes_down(eyes, crop,
                            lenght_detectionD, lenght_detectionG,
                            on_eyes_thresholds_r, on_eyes_thresholds_l)

  

            nose(frame, faces)


        except:
            pass




        cv2.imshow("frame", frame)
        

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":

    #picture_to_init()

    on_eyes_thresholds_r, on_eyes_thresholds_l,\
    eyes_min_canny_r, eyes_grad_r,\
    eyes_min_canny_l, eyes_grad_l,\
    mouth_thresh = main()

    print(on_eyes_thresholds_r, on_eyes_thresholds_l,
           eyes_min_canny_r, eyes_grad_r,
            eyes_min_canny_l, eyes_grad_l, mouth_thresh)

    video_capture(on_eyes_thresholds_r, on_eyes_thresholds_l,\
                   eyes_min_canny_r, eyes_grad_r,\
                   eyes_min_canny_l, eyes_grad_l,\
                   mouth_thresh)
    
