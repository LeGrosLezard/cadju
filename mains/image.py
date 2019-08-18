import numpy as np
import cv2


image_detector = cv2.imread("image_detector.jpg")



imgray = cv2.cvtColor(image_detector, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh,
                                       cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_SIMPLE)


cv2.drawContours(image_detector, contours, -1, (0, 255, 0), 3)


hull = []
 

for i in range(len(contours)):
    hull.append(cv2.convexHull(contours[i], False))

drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)

for i in range(len(contours)):
    if len(contours[i]) < 150:
        pass
    else:
        color_contours = (0, 255, 0) 
        color = (255, 0, 0) 

        cv2.drawContours(drawing, contours, i, color_contours, 1, 8, hierarchy)
        cv2.drawContours(drawing, hull, i, color, 1, 8)




pts = []
dico = {}
c = 0
for i in hull:
    i = i.tolist()
    for j in i:
        dico[j[0][0]] = j[0][1]


print(dico)





        
#cv2.circle(drawing, (j[0][0], j[0][1]), 3, (0,0,255),3)
        
        





cv2.imshow("yoyo.jpg", drawing)

















