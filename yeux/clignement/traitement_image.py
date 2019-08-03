import numpy as np
import cv2 
from PIL import Image
import os



def position_yeux():

    liste = os.listdir()

    for i in liste:
        if i in ('CONFIG.py', 'essais', 'haarcascade_frontalface_default.xml',
                 'haarcascade_lefteye_2splits.xml', 'main.py',
                 'traitement_image', '__pycache__', "traitement_image.py"
                 "iiiiiii.jpg"):
            pass

        
        else:
            #On resize les yeux
            img = Image.open(i)
            img = img.resize((300, 300), Image.ANTIALIAS)
            img.save("iiiiiii.jpg")

            #On lit l'image resize et on la blur
            img = cv2.imread('iiiiiii.jpg', 0)
            blur = cv2.blur(img,(3,3))

            #On test de voir si y'a un rond
            try:
                
                circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 2, 100, param1=50,
                                            param2=30, minRadius=40, maxRadius=55)

                circles = np.round(circles[0, :]).astype("int")


            
                for (x, y, r) in circles:

                    cv2.circle(img, (x, y), 2, (0, 0, 255), 3)
               
                  
                    #des fois y'a des faux cercles en haut a gauche
                    #le matching se fera toujours dans la régions des 100y

                    if x < 100:
                        pass
                    else:
                        if x < 120:
                            print("regarde vers le haut")

                    #cv2.imshow("dzadza", img)
            except TypeError:
                pass

##    try:
##        os.remove("image_position_yeux_gauche.jpg")
##        os.remove("image_position_yeux_droite.jpg")
##
##    except:
##        pass












