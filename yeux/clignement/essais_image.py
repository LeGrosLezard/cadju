import numpy as np
import cv2 


left_eye = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')
img = cv2.imread('test.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


eyes = left_eye.detectMultiScale(gray)

c = 0
for (ex, ey, ew, eh) in eyes:
    if c % 2 == 0:
        pass
    else:
        cv2.rectangle(gray, (ex,ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        crop_img = gray[ey:ey+eh, ex:ex+ew]
    c+=1







    
cv2.imshow('LEFT', crop_img)
