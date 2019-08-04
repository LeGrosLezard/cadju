import numpy as np
import cv2 
from PIL import Image
import os



def position_yeux(nom_image, inter, debut):

    #os.remove(nom_image)
    img = Image.open(debut)
    img = img.resize((300, 300), Image.ANTIALIAS)
    img.save(inter)

    img = cv2.imread(inter, 0)
    blur = cv2.blur(img,(3,3))

    try:

        circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 2, 100, param1=50,
                                    param2=30, minRadius=40, maxRadius=55)

        circles = np.round(circles[0, :]).astype("int")

        for (x, y, r) in circles:
            if x < 61:
                pass
            else:
                cv2.circle(img, (x, y), r, (0, 0, 255), 1)
                cv2.circle(img, (x, y), 2, (0, 0, 255), 3)
                cv2.imwrite(nom_image, img)
        
    except:
        pass

            



