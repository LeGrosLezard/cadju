import cv2
import numpy as np
from PIL import Image
import operator
from collections import defaultdict


from config import alpha_numeric
#afin d'ajuster les seuil mettre une image genreu n tigre et compter les tache

def picture_to_init():
    cap = cv2.VideoCapture(0)
    _,frame = cap.read()
    frame = cv2.resize(frame, (800, 600))
    cap.release()
    cv2.imwrite('treat_init.jpg', frame)


    return False

def adjust_gamma(image, gamma):
    """We add light to the video, we play with gamma"""

    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
            for i in np.arange(0, 256)]).astype("uint8")

    return cv2.LUT(image, table)


def detections(frame, gray,
               faceCascade, eyes_cascade,
               frame1):
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





def sourcile(eyes, crop):

    rowD = 0
    rowG = 0

    centerD = 0
    centerG = 0

    alpha_numeric = []
    for i in range(500):
        alpha_numeric.append([])

    new = 0
    c = 0
    mean = 0
    mean_y = 0

    if len(eyes) == 2:
        for x1, y1, w1, h1 in eyes:
            mean += int(x1+w1/2)
            mean_y += int(y1+h1/2)

    mean = int(mean/2)
    mean_y = int(mean_y/2)
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

        cv2.imshow("azevcnbv,", thresh)
        len_x = 0
        ligne = []
        for i in alpha_numeric:
            if i != []:
                if len(i) > len_x:
                    len_x = len(i)
                    ligne.append(i)

        
        counter_pts = 0
        row = 0
        last = 0
        for i in ligne[-1]:
            if counter_pts % 10 == 0:
                cv2.circle(eyes_crop, (i[1],i[0]), 1, (0,0,255), 4)
                row = i[0]
                last = i[1]
            counter_pts += 1
        
        alpha_numeric = []
        for i in range(500):
            alpha_numeric.append([])


        if (x1+w1/2) < mean:
            rowD = row
 
        elif (x1+w1/2) > mean:
            rowG = row

    if rowD != 0 or rowG != 0 or centerD != 0 or centerG != 0:

        if rowD < 25 and rowG < 25:
           print("levé")





def sourcile_position(eyes, crop1, lenght_detectionD, lenght_detectionG):

    mean = 0
    for x, y, w, h in eyes:
        mean += x+w/2

    mean = int(mean/2)


    for x1, y1, w1, h1 in eyes:
        eyes_crop = crop1[y1-20:y1+20, x1+10:x1+w1]
        gray=cv2.cvtColor(eyes_crop, cv2.COLOR_BGR2GRAY)


        if x1 < mean:#droite

            _, thresh = cv2.threshold(gray, 150, 255,cv2.THRESH_BINARY)
            right = cv2.line(thresh, (0, 0), (0, thresh.shape[0]), (255, 255, 255), 5)

            liste = []
            for i in range(int(thresh.shape[0])):
                for j in range(int(thresh.shape[1]/2)):
                    if thresh[i, j] == 0:
                       liste.append(j)

            a = max(liste)

            if a > lenght_detectionD + 2:
                print("baisse")

            cv2.circle(eyes_crop, (a, int(thresh.shape[0]/2)), 1, (0, 0, 0), 5)


        
        elif x1 > mean:


            _, thresh = cv2.threshold(gray, 150, 255,cv2.THRESH_BINARY)
 
            liste = []
            for i in range(int(thresh.shape[0])):
                for j in range(int(thresh.shape[1]/2)):
                    if thresh[i, j] == 0:
                       liste.append(j)

            b = max(liste)
            if b > lenght_detectionG + 2:
                print("baisse")
            cv2.circle(eyes_crop, (b, int(thresh.shape[0]/2)), 1, (0, 0, 0), 5)

    return a, b



def eyes_localisation(eyes, crop, eyes_center_xD, eyes_center_yD,
                      eyes_center_xG, eyes_center_yG):

    counter = 0
    mean = 0
    if len(eyes) == 2:
        for x1, y1, h1, w1 in eyes:
            mean += int(x1+w1/2)
        mean = int(mean /2)

    for x1, y1, h1, w1 in eyes:

        if len(eyes) == 2:
            eyes_crop = crop[y1+h1-35:y1+h1-10, x1:x1+w1]
            blur = cv2.GaussianBlur(eyes_crop, (5,5), 3)
            edge = cv2.Canny(blur, 140, 200)

            _, thresh1 = cv2.threshold(edge, 127, 255,cv2.THRESH_BINARY)
            cnts, _ = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            if len(cnts) == 0:
                cv2.circle(crop, (eyes_center_xD, eyes_center_yD), 1, (0,255,0), 10) 
                cv2.circle(crop, (eyes_center_xG, eyes_center_yG), 1, (255,0,0), 10)

            else:

                if int(x1+w1/2) > mean:
                    eyes_center_xG = int(x1+w1/2)
                    eyes_center_yG = int(y1+h1/2)

                else:
                    eyes_center_xD = int(x1+w1/2)
                    eyes_center_yD = int(y1+h1/2)


                cv2.drawContours(eyes_crop, cnts, -1, (0, 0, 255), 3)

        counter += 1



    if eyes_center_xG > mean and eyes_center_xD < mean and len(eyes) == 2:
        return eyes_center_xD, eyes_center_yD, eyes_center_xG, eyes_center_yG




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

            #cv2.circle(crop1, (x1,y1), 1, (0,0,255), 5)
            #cv2.circle(crop1, (x1+w1,y1), 1, (0,0,255), 5)
            #cv2.rectangle(crop1, (x1, y1), (x1+w1, y1+h1), 3)

            
            if x1+w1 < mouth_pts1_x - 10:
                print("ooooooh")
            else:
                mouth_pts1_x = x1+w1


    return mouth_pts1_x





def smyling(frame, faces):

    for x, y, w, h in faces:

        crop1 = frame[y+h-50:y+h-20, x+55:x+w-55]
        crop_frame = crop1
        crop1 = adjust_gamma(crop1, 0.6)

        gray=cv2.cvtColor(crop1, cv2.COLOR_BGR2GRAY)
        _, thresh1 = cv2.threshold(gray, 60, 255,cv2.THRESH_BINARY)

        x_liste = []
        y_liste = []


        crop_window = thresh1[int(thresh1.shape[0]/5.5):int(thresh1.shape[0]/1.3), 0:thresh1.shape[1]]

        for i in range(crop_window.shape[0]):
            for j in range(crop_window.shape[1]):
                if thresh1[i, j] != 255:
                    x_liste.append(i)
                    y_liste.append(j)


        coin_dx = min(y_liste)
        coin_dy = x_liste[y_liste.index(min(y_liste))]

        coin_gx = max(y_liste)
        coin_gy = x_liste[y_liste.index(max(y_liste))]


        cv2.circle(crop_frame, (coin_dx, coin_dy), 1, (0, 0, 0), 10)
        cv2.circle(crop_frame, (coin_gx, coin_gy), 1, (0, 0, 0), 10)



        mid = int((coin_dx + coin_gx) / 2)

        liste_mid_top = []
        for i in range(crop_window.shape[0]):
            for j in range(mid):
                if thresh1[i, j] == 0:
                    liste_mid_top.append(i)

        cv2.circle(crop_frame, (mid, max(liste_mid_top)), 1, (255, 0, 255), 5)
        cv2.line(crop_frame, (mid, max(liste_mid_top)), (coin_dx, coin_dy), (0, 0, 255))
        cv2.line(crop_frame, (mid, max(liste_mid_top)), (coin_gx, coin_gy), (0, 0, 255))

  
##        cv2.imshow("zaee", thresh1)
##        cv2.imshow("eazeazezaeza", crop1)
##        if cv2.waitKey(1) & 0xFF == ord('q'):
##            o = input("sauve.")
##            cv2.imwrite(o, thresh1)






def nose(frame, faces):

    for x, y, w, h in faces:

        square = int(w/3)

        y2 = 0
        
        crop = frame[y+int(270*100/y):y+h-60, x+square:x+w-square]
        gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        edge = cv2.Canny(gray, 0, 255)
        
        cnts, _ = cv2.findContours(edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        cv2.drawContours(crop, cnts, -1, (0, 0, 255), 3)
        if cnts:
            print("He smelling you bro or he asks concentration")

##        cv2.imshow("azeze1111", crop)
##        cv2.imshow("dazdqsd1111", edge)
##
##        if cv2.waitKey(1) & 0xFF == ord('q'):
##            o = input("sauve.")
##            cv2.imwrite(o, crop)



def teeth(frame, faces):
    for x, y, w, h in faces:

        crop1 = frame[y+h-50:y+h-20, x+55:x+w-55]
        gray = cv2.cvtColor(crop1, cv2.COLOR_BGR2GRAY)
        edge = cv2.Canny(gray, 0, 255)

        cnts, _ = cv2.findContours(edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for i in cnts:
            if cv2.contourArea(i) > 95:
                print("teeth appears or something on the mouse")
 
##
##        cv2.imshow("azeze1111", crop1)
##        cv2.imshow("dazdqsd1111", edge)




def video_capture():

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

            sourcile(eyes, crop)

            teeth(frame, faces)

            mouth_pts1_x = mouth(faces, frame, mouthcascade,
                                 mouth_pts1_x)
            smyling(frame, faces)

            eyes_center_xD, eyes_center_yD,\
            eyes_center_xG, eyes_center_yG\
            = eyes_localisation(eyes, crop, eyes_center_xD, eyes_center_yD,
                                eyes_center_xG, eyes_center_yG)
            
            a, b = sourcile_position(eyes, crop,
                                lenght_detectionD, lenght_detectionG)

            lenght_detectionD = a
            lenght_detectionG = b

            nose(frame, faces)

            
            
            #si fermeture yeux alors affiche pas sourcile
        except:
            pass



        cv2.imshow("frame", frame)
        

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    Ocontinue = True
    while Ocontinue:
        Ocontinue = picture_to_init()

    video_capture()
    
