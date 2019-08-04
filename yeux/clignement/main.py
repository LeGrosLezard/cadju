import numpy as np
import cv2
from PIL import Image
import os


from CONFIG import PATH_Y_G
from CONFIG import PATH_Y_D

from traitement_image import position_yeux



def video_oeil_gauche(video):
    #Main frame

    try:
        
        im = cv2.imread("gauche_oeil.jpg")
        cv2.imshow('gauche_oeil', im)
 
    except:
        pass

def video_oeil_droit(video):
    #Main frame

    try:
        
        im1 = cv2.imread("droite_oeil.jpg")
        cv2.imshow('droite_oeil', im1)

 
    except:
        pass

    
def video_left(video):
    #Eyes left


    left_eye = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')
    
  
    ret, frame = video.read()
    left = cv2.resize(frame, (400, 400))
    eyes = left_eye.detectMultiScale(left)
    
    c = 0
    for (ex, ey, ew, eh) in eyes:
        if c % 2 == 0:
            pass
        else:
            cv2.rectangle(left, (ex,ey), (ex+ew, ey+eh), 0)
            left = left[ey:ey+eh, ex:ex+ew]
            
            cv2.imwrite(PATH_Y_G, left)

          
            position_yeux("gauche_oeil.jpg", "iiiiiii.jpg", "image_position_yeux_gauche.jpg")

            
        c += 1

    
    try:
        cv2.imshow('LEFT', left)
    except:
        pass



def video_right(video):
    #Eyes right

 
    right_eye = cv2.CascadeClassifier("haarcascade_lefteye_2splits.xml")
    
    ret, frame = video.read()
    right = cv2.resize(frame, (400, 400))
    eyes = right_eye.detectMultiScale(right)

    c = 0
    for (ex, ey, ew, eh) in eyes:
        
        if c % 2 == 0:
            cv2.rectangle(right, (ex,ey), (ex+ew, ey+eh), 0)
            right = right[ey:ey+eh, ex:ex+ew]
            
            cv2.imwrite(PATH_Y_D, right)

            try:
                position_yeux("droite_oeil.jpg", "jjj.jpg", "image_position_yeux_droit.jpg")
            except:
                pass

        else:
            pass
    
        c += 1

    

    try:
        cv2.imshow('RIGHT', right)
    except:
        pass
    





def video_capture():

    GLOBAL = []
    video = cv2.VideoCapture(0)
    repere = 0
    while(True):
        if repere % 10 == 0:
            print("REPEREEEEEEEEEEEEEEEE")
        if repere % 30 == 0:

            liste = ["iiiiiii.jpg", "jjj.jpg", "droite_oeil.jpg", "gauche_oeil.jpg"]
            for i in liste:
                os.remove(i)
            
                new_im = Image.new('RGB', (300,300), (255,255,255))
                new_im.save(i, "jpeg")

            
        video_oeil_gauche(video)
        video_oeil_droit(video)
        video_left(video)
        video_right(video)


        if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        repere += 1
    video.release()
    cv2.destroyAllWindows()









if __name__ == "__main__":

    video_capture()












