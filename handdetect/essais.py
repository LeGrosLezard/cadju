import numpy as np
import cv2
from PIL import Image

cap=cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier("haar/haarcascade_frontalface_alt2.xml")

def original_frame(originale, kernel_blur):

    originale = cv2.resize(originale, (800, 600))
    originale=cv2.cvtColor(originale, cv2.COLOR_BGR2GRAY)
    originale=cv2.GaussianBlur(originale, (kernel_blur, kernel_blur), 0)
    kernel_dilate=np.ones((10, 10), np.uint8)

    return originale, kernel_dilate


def movements_detection(gray, frame, faceCascade):


    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(50, 50),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    try:
        print(faces)
            
        gray1 = gray[0:600, 0:faces[0][0]]
        gray2 = gray[0:600, faces[0][0]+faces[0][2]:800]

        for i in range(255):

            _, thresh1 = cv2.threshold(gray1, i, 255, cv2.THRESH_BINARY)

            _, thresh2 = cv2.threshold(gray2, i, 255, cv2.THRESH_BINARY)        

            cv2.imshow("dzad", thresh1)
            cv2.imshow("12348", thresh2)

            key=cv2.waitKey(1)&0xFF
            if key==ord('q'):
                 break

    except:
        pass

def video_capture():

    kernel_blur=43
    seuil=10
    _, originale = cap.read()
    originale, kernel_dilate = original_frame(originale, kernel_blur)
  

    while True:

        
        ret, frame=cap.read()
        frame = cv2.resize(frame, (800, 600))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        movements_detection(gray, frame, faceCascade)



        originale = gray

 

        key=cv2.waitKey(1)&0xFF
        if key==ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    video_capture()


















    
