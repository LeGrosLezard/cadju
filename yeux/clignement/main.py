import numpy as np
import cv2

from CONFIG import PATH_Y_G
from CONFIG import PATH_Y_D

from traitement_image import position_yeux

def video_main(video):
    #Main frame
    ret, main_frame = video.read()
    frame = cv2.resize(main_frame, (200, 200))

    cv2.imshow('MAIN', frame)



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

            try:
                position_yeux()
            except:
                pass
            
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
                position_yeux()
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
    
    while(True):

        video_main(video)
        video_left(video)
        video_right(video)


        if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        
    video.release()
    cv2.destroyAllWindows()









if __name__ == "__main__":

    video_capture()












