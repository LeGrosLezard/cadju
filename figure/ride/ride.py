import cv2
import numpy as np
from PIL import Image

def adjust_gamma(image, gamma):
    """We add light to the video, we play with gamma"""

    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
            for i in np.arange(0, 256)]).astype("uint8")

    return cv2.LUT(image, table)

def make_line(thresh):
    """We make line for detect more than one area
    with border, on eyelashes is paste to the border"""

    cv2.line(thresh, (0, 0), (0, thresh.shape[0]), (0, 0, 0), 1)
    cv2.line(thresh, (0, 0), (thresh.shape[1], 0), (0, 0, 0), 1)
    cv2.line(thresh, (thresh.shape[1], 0), (thresh.shape[1], thresh.shape[0]), (0, 0, 0), 1)
    cv2.line(thresh, (0,  thresh.shape[0]), (thresh.shape[1], thresh.shape[0]), (0, 0, 0), 1)

    return thresh


facecascade = cv2.CascadeClassifier('../haar/haarcascade_frontalface_alt2.xml')
eyescascade = cv2.CascadeClassifier('../haar/haarcascade_eye.xml')

img = cv2.imread("WIN_20190925_13_48_04_Pro.jpg")
img = adjust_gamma(img, 0.6)

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

            counter = 0
            continuer = True
            while continuer:
            
                eyes_crop_l = crop[y1:y1+w1+20, x1:x1+w1]
                gray=cv2.cvtColor(eyes_crop_l, cv2.COLOR_BGR2GRAY)
                
                blur = cv2.GaussianBlur(gray, (11, 11), 0)
                _, thresh = cv2.threshold(gray, 28, 255, 0)


                contours, _ = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                for i in contours:

                    if 1000 >= cv2.contourArea(i) >= 60.0:
                        M = cv2.moments(i)
                        cX = int(M["m10"] / M["m00"])
                        cY = int(M["m01"] / M["m00"])

                        cv2.circle(eyes_crop_l,(cX, cY), 2, (0,0,255), 5)

                        continuer = False


                counter += 1


                edge_l = cv2.Canny(eyes_crop_l, 0, 0)
                cv2.imwrite("eyes_crop_l.png", edge_l)
                image_pil = Image.open("eyes_crop_l.png").resize((200,200), Image.ANTIALIAS)
                image_pil.save("eyes_crop_l.png")
     

     
            else:
                eyes_crop_r = crop[y1:y1+w1, x1:x1+w1]
                edge_r = cv2.Canny(eyes_crop_r, 40, 0)
                cv2.imwrite("eyes_crop_r.png", edge_r)
                image_pil = Image.open("eyes_crop_r.png").resize((200,200), Image.ANTIALIAS)
                image_pil.save("eyes_crop_r.png")









img = cv2.imread("eyes_crop_l.png")
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,thresh2 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
thresh2 = make_line(thresh2)

contours, _ = cv2.findContours(thresh2, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for i in contours:
    if 30000 > cv2.contourArea(i) > 200:
        print(cv2.contourArea(i))
        cv2.drawContours(img, [i], -1, (0,0,255), 1)
    
cv2.imwrite("eyes_crop_l.png", img)



img = cv2.imread("eyes_crop_l.png")
cv2.imshow("image", img)









