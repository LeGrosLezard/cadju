import numpy as np
import cv2

from CONFIG import EYES_RIGHT
from CONFIG import EYES_LEFT



def video_main(video):
    #Main frame
    ret, main_frame = video.read()
    frame = cv2.resize(main_frame, (200, 200))

    cv2.imshow('MAIN', frame)



def video_left(video, d):
    #Eyes left

    left_eye = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')
  
    ret, frame = video.read()
    left = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    left = cv2.resize(frame, (400, 400))

    
    eyes = left_eye.detectMultiScale(left)
    
    c = 0
    for (ex, ey, ew, eh) in eyes:
        if c % 2 == 0:
            pass
        else:
            cv2.rectangle(left, (ex,ey), (ex+ew, ey+eh), 0)
            left = left[ey:ey+eh, ex:ex+ew]
            path = r"C:\Users\jeanbaptiste\Desktop\cadju\yeux\clignement\image\{0}"
            image = "image" + str(d) + ".jpg"
            image = path.format(image)
            cv2.imwrite(image, left)


            
        c += 1

    

    cv2.imshow('LEFT', left)




def video_right(video):
    #Eyes right



    right_eye = cv2.CascadeClassifier("haarcascade_lefteye_2splits.xml")
    
    ret, frame = video.read()
    right = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    right = cv2.resize(right, (400, 400))

    eyes = right_eye.detectMultiScale(right)

    c = 0
    for (ex, ey, ew, eh) in eyes:
        
        if c % 2 == 0:
            cv2.rectangle(right, (ex,ey), (ex+ew, ey+eh), 0)
            right = right[ey:ey+eh, ex:ex+ew]

        else:
            pass
    
        c += 1

    


    cv2.imshow('RIGHT', right)

    


def video_capture():

    
    video = cv2.VideoCapture(0)
    
    image_numero = 0
    while(True):

        
        
        #video_main(video)
        video_left(video, image_numero)
        #video_right(video)

        if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        image_numero += 1

    video.release()

    cv2.destroyAllWindows()









if __name__ == "__main__":

    video_capture()












