import numpy as np
import cv2
import threading

cap=cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier("haar/haarcascade_frontalface_alt2.xml")
handCascade = cv2.CascadeClassifier("haar/palm.xml")
gestCascade = cv2.CascadeClassifier("haar/agest.xml")
closeCascade = cv2.CascadeClassifier("haar/close.xml")
closedCascade = cv2.CascadeClassifier("haar/closed.xml")
palmCascade = cv2.CascadeClassifier("haar/palm.xml")


from traitement_hand import *



def video_capture():
    kernel_blur=43
    seuil=10
    surface=3000

    _, originale = cap.read()
    originale, kernel_dilate = original_frame(originale, kernel_blur)


    while True:

        
        ret, frame=cap.read()
        frame = cv2.resize(frame, (800, 600))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        face_detections(faceCascade, frame, gray)

        thread(handCascade, gestCascade,
               palmCascade, closeCascade,
               closedCascade, frame, gray)


        contours, frame_contour, gray\
                  = movements_detection(gray, originale,
                                        kernel_blur, seuil,
                                        kernel_dilate, frame)

        drawing_movements(contours, frame_contour, frame, surface)

        
        originale = gray

        
        cv2.imshow("frame", frame)     

        key=cv2.waitKey(1)&0xFF
        if key==ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    video_capture()
    
