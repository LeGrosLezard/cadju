import cv2
import numpy as np


def adjust_gamma(image, gamma):
    """We add light to the video, we play with gamma"""

    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
            for i in np.arange(0, 256)]).astype("uint8")

    return cv2.LUT(image, table)



facecascade = cv2.CascadeClassifier('../haar/haarcascade_frontalface_alt2.xml')
eyescascade = cv2.CascadeClassifier('../haar/haarcascade_eye.xml')

img = cv2.imread("WIN_20190925_13_48_04_Pro.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = facecascade.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=5,
    minSize=(60, 100),
    flags=cv2.CASCADE_SCALE_IMAGE
)

for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

    crop = img[y:y+h, x:x+w]
    gray_crop = gray[y:y+h, x:x+w]
    edge = cv2.Canny(gray_crop, 40, 10)

    eyes = eyescascade.detectMultiScale(
        gray_crop,
        scaleFactor=1.3,
        minNeighbors=4,
        minSize=(30, 30),

        flags=cv2.CASCADE_SCALE_IMAGE
        )


    mean = 0
    for x1, y1, w1, h1 in eyes:
        mean += x1+w1 / 2
    mean = int(mean /2)
    
    for x1, y1, w1, h1 in eyes:
        if x1+w1/2 < mean:
            eyes_crop_l = crop[y1:y1+w1, x1:x1+w1]
            edge_l = cv2.Canny(eyes_crop_l, 0, 0)
 
        else:
            eyes_crop_r = crop[y1:y1+w1, x1:x1+w1]
            edge_r = cv2.Canny(eyes_crop_r, 0, 0)
    

##
##cv2.imshow("edge", edge)
##cv2.imshow("image", img)


##cv2.imshow("eyes_crop_l", eyes_crop_l)
##cv2.imshow("eyes_crop_r", eyes_crop_r)
cv2.imshow("dzad", edge_l)
cv2.imshow("eyes_vwvwcrop_r", edge_r)






