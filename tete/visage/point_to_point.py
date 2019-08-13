import numpy as np
import cv2
from PIL import Image
import os
import time



video = cv2.VideoCapture(0)

BOX1 = []
BOX2 = []
BOX3 = []
BOX4 = []

pos = []
time = []

c = 0
tempo = [0]


START = False

while(True):


    ret, frame = video.read()
    frame = cv2.resize(frame, (600, 600))


    cv2.rectangle(frame,(100,100), (150, 150), (0,0,255), 1)
    cv2.rectangle(frame,(300,100), (350, 150), (0,0,255), 1)
    cv2.rectangle(frame,(400,100), (450, 150), (0,0,255), 1)


    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'start puis carree puis stop',(20,20), font, 1,(255,255,255),2,cv2.LINE_AA)


    if START is False:
        cv2.rectangle(frame,(500,500), (550, 550), (255,0,0), 1)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,'STOP',(500,550), font, 1,(255,255,255),2,cv2.LINE_AA)
    if START is True:
        cv2.rectangle(frame,(500,500), (550, 550), (0,0,255), 1)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,'START',(500,550), font, 1,(255,255,255),2,cv2.LINE_AA)

 
    liste1 = []

    for i in range(100, 150):
        for j in range(100, 150):
            liste1.append(frame[i,j][0])

    liste2 = []

    for i in range(100, 150):
        for j in range(300, 350):
            liste2.append(frame[i,j][0])


    liste3 = []

    for i in range(100, 150):
        for j in range(400,450):
            liste3.append(frame[i,j][0])
            
    liste4 = []

    for i in range(500, 550):
        for j in range(500,550):
            liste4.append(frame[i,j][0])


    
    liste1 = str(liste1)
    liste2 = str(liste2)
    liste3 = str(liste3)
    liste4 = str(liste4)

    
    try:
        if sum(BOX1)/len(BOX1) + 1000 < len(liste1) or\
           sum(BOX1)/len(BOX1) - 1000 > len(liste1):
            cv2.rectangle(frame,(100,100), (150, 150), (255,0,255), 1)
            pos.append(1)
            time.append(c)
  
        if sum(BOX2)/len(BOX2) + 1000 < len(liste2) or\
           sum(BOX2)/len(BOX2) - 1000 > len(liste2):
            cv2.rectangle(frame,(300,100), (350, 150), (255,0,255), 1)
            pos.append(2)
            time.append(c)

        if sum(BOX3)/len(BOX3) + 500 < len(liste3) or\
           sum(BOX3)/len(BOX3) - 500 > len(liste3):
            cv2.rectangle(frame,(400,100), (450, 150), (255,0,255), 1)
            pos.append(3)
            time.append(c)

        
        if sum(BOX4)/len(BOX4) + 80 < len(liste4) or\
           sum(BOX4)/len(BOX4) - 80 > len(liste4):
            if tempo[-1] + 20 < c:
                if START == False:
                    START = True
                    tempo.append(c)
                    
                elif START == True:
                    START = False
                    tempo.append(c)
                    liste = [[],[],[]]

                    d = 0

                    for i in pos:
                        if i == 1:
                            liste[0].append([i, time[d]])
                        elif i == 2:
                            liste[1].append([i, time[d]])
                        elif i == 3:
                            liste[2].append([i, time[d]])
                            
                        d+=1
                        
                    a = []
                    o = []
                    dico = {}


                    for i in liste:
                        a.append(i[-1])
                        dico[i[-1][0]] = i[-1][1]


                    aaaa = 0
                    for i in a:
                        o.append(a[aaaa][1])
                        aaaa += 1

                    o = sorted(o)

                    for i in o:
                        for cle, valeur in dico.items():
                            if i == valeur:
                                print(cle)
            else:
                pass

    
    except:
        pass



    BOX1.append(len(liste1))
    BOX2.append(len(liste2))
    BOX3.append(len(liste3))
    BOX4.append(len(liste4))
    

##    try:
##        print(pos)
##    except:
##        pass

    cv2.imshow('point', frame)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    c+=1
video.release()
cv2.destroyAllWindows()
