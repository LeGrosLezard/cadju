import cv2
import numpy as np
from PIL import Image




eyescascade = cv2.CascadeClassifier('haar/haarcascade_eye.xml')
facecascade = cv2.CascadeClassifier('haar/haarcascade_frontalface_alt2.xml')
def video_capture():


    video = cv2.VideoCapture(0)
    liste = [[], [], [], []]
    
    while(True):

        ret, frame = video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        def detection(gray, frame, facecascade, eyescascade, liste):

            eyes = eyescascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=2,
                minSize=(40, 40),
                flags=cv2.CASCADE_SCALE_IMAGE
            )
            

            c = 0
            for x, y, w, h in eyes:

                if c == 0:

                    liste[0].append(x)
                    liste[1].append(y)
                    liste[2].append(x+w)
                    liste[3].append(y+h)
                    
                    cv2.rectangle(frame, (x, y), (x+w, y+h), 3)
                elif c == 1:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 3)

                c+=1

                
        if len(liste[0]) < 50:
            detection(gray, frame, facecascade, eyescascade, liste)

            
        else:

            def eyes(frame):

                a = int(round(sum(liste[0]) / len(liste[0])))
                b = int(round(sum(liste[1]) / len(liste[1])))
                c = int(round(sum(liste[2]) / len(liste[2])))
                d = int(round(sum(liste[3]) / len(liste[3])))

                crop = frame[b:d, a:c]

                cv2.imshow("frame1", crop)

            eyes(frame)

            

                
        cv2.imshow("frame", frame)
        


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    video.release()
    cv2.destroyAllWindows()






if __name__ == "__main__":
    video_capture()
