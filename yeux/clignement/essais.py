import cv2
import numpy as np
from PIL import Image
import imutils



eyescascade = cv2.CascadeClassifier('haar/haarcascade_eye.xml')
facecascade = cv2.CascadeClassifier('haar/haarcascade_frontalface_alt2.xml')
def video_capture():


    video = cv2.VideoCapture(0)
    liste = [[], [], [], []]
    liste1 = [[], [], [], []]
    counter = 0
    
    while(True):

        ret, frame = video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        def detection(gray, frame, facecascade, eyescascade, liste):

            eyes = eyescascade.detectMultiScale(
                gray,
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

                    liste1[0].append(x)
                    liste1[1].append(y)
                    liste1[2].append(x+w)
                    liste1[3].append(y+h)
                    
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

                e = int(round(sum(liste1[0]) / len(liste1[0])))
                f = int(round(sum(liste1[1]) / len(liste1[1])))
                g = int(round(sum(liste1[2]) / len(liste1[2])))
                h = int(round(sum(liste1[3]) / len(liste1[3])))

                crop = frame[b+10:d-10, a+5:c-5]
                crop1 = frame[f+10:h-10, e+5:g-5]
                
                return crop, crop1


  
            crop, crop_g = eyes(frame)

        
            gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
            _, thresh = cv2.threshold(gray, 127, 255, 0)



            gray1 = cv2.cvtColor(crop_g, cv2.COLOR_BGR2GRAY)
            _, thresh1 = cv2.threshold(gray1, 127, 255, 0)



            try:
                contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                img = cv2.drawContours(crop, contours, 1, (0,255,0), 3)

                contours1, hierarchy1 = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                img1 = cv2.drawContours(crop_g, contours1, 1, (0,255,0), 3)



    ##            for c in cnts:
    ##     
    ##                M = cv2.moments(c)
    ##                cX = int(M["m10"] / M["m00"])
    ##                cY = int(M["m01"] / M["m00"])
             

                
                cv2.imshow("p111oj11", thresh)
                cv2.imshow("p111oj", thresh1)
            except:
                pass
            
        cv2.imshow("frame", frame)
        


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    video.release()
    cv2.destroyAllWindows()






if __name__ == "__main__":
    video_capture()
