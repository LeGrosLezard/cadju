import cv2
import numpy as np
from PIL import Image


"""
maintenant faut faire comme dans la video, soit test de
récup le pourtoure soit mtn récupere
la position de x avant, puis x et y mtn (l'oeil du coup va sauter !!!!)
on dit si x ou y a bouger de temps et que mtn t'as ste position de l'oeil
on peut replacer l'oeil via le saut de tete,
faire justement le quadrant et repérer l'oeil !!!!!!
et c mieux !
"""








#---------------------------------------------------------DETECTION FUNCTIONS
def face_detection_config(gray, facecascade):
    """Face detection with the following configuration:
    the frame (here a crop of the frame does not gray),
    the pyragmidal image, the minimum number of neighbors,
    the size and the version of the haar"""
    
    faces = facecascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=1,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    return faces


def eyes_detection_config(roi_gray, eyescascade):
    """Eyes detection with the following configuration:
    the frame (here a crop of the frame does not gray),
    the pyragmidal image, the minimum number of neighbors,
    the size and the version of the haar"""

    eyes = eyescascade.detectMultiScale(
        roi_gray,
        scaleFactor=1.3,
        minNeighbors=1,
        minSize=(40, 40),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    return eyes


#---------------------------------------------------------IMAGE FUNCTIONS
def eye_save(frame, eye, nom, counter, x, y, w, h):

    crop = frame[y:y+h, x:x+w]
    if eye == counter:
        cv2.imwrite(nom, crop)



def detection(frame, gray, facecascade, eyescascade):
    
    faces = face_detection_config(gray, facecascade)

    for x1, y1, w1, h1 in faces:
        roi_gray = gray[y1:y1+h1, x1:x1+w1]
        roi_color = frame[y1:y1+h1, x1:x1+w1]
        
        eyes = eyes_detection_config(roi_gray, eyescascade) 

        eye = 0
        for x, y, w, h in eyes:
            eye_save(roi_color, eye, "droite.jpg", 0, x, y, w, h)
            eye_save(roi_color, eye, "gauche.jpg", 1, x, y, w, h)

            eye += 1

            cv2.rectangle(roi_color, (x, y), (x+w, y+h), (0, 0, 255), 2) 


def resizer(image):
    img = Image.open(image)
    img = img.resize((500, 500), Image.ANTIALIAS).save(image)



def circle(image):
    
    img = cv2.imread(image, 0)
    gauss = cv2.GaussianBlur(img, (41, 41), 0)


    try:
        circles = cv2.HoughCircles(gauss, cv2.HOUGH_GRADIENT, 2, 100, param1=50,
                                    param2=30, minRadius=40, maxRadius=55)

        circles = np.round(circles[0, :]).astype("int")

        for (x, y, r) in circles:
            if x < 61:
                pass
            else:
                cv2.circle(img, (x, y), r, (0, 0, 255), 1)
                cv2.circle(img, (x, y), 2, (0, 0, 255), 3)
                cv2.imshow("image", img)
        
    except:
        pass



eyescascade = cv2.CascadeClassifier('haar/haarcascade_eye.xml')
facecascade = cv2.CascadeClassifier('haar/haarcascade_frontalface_alt2.xml')
def video_capture():

    video = cv2.VideoCapture(0)

    while(True):

        ret, frame = video.read()        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        detection(frame, gray, facecascade, eyescascade)
        resizer("droite.jpg")
        circle("droite.jpg")
       
        cv2.imshow("frame", frame)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    video.release()
    cv2.destroyAllWindows()









video_capture()
