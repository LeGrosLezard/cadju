import numpy as np
import cv2 
from PIL import Image
import os


img = Image.open('image61.jpg')
img = img.resize((300, 300), Image.ANTIALIAS)
img.save("iiiiiii.jpg")


img = cv2.imread('iiiiiii.jpg', 0)
blur = cv2.blur(img,(3,3))


circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 2, 100, param1=50,
                            param2=30, minRadius=40, maxRadius=55)

circles = np.round(circles[0, :]).astype("int")

for (x, y, r) in circles:
        cv2.circle(img, (x, y), r, (0, 255, 0), 2)
        cv2.circle(img, (x, y), 2, (0, 0, 255), 3)

cv2.imwrite("yo1.jpg", img)
cv2.imshow("output", img)

cv2.waitKey(0)







liste = os.listdir()

for i in liste:
    if i == "essais_image.py":
        pass
    else:
        print(i)





















