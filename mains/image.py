import numpy as np
import cv2


image_detector = cv2.imread("image_detector.jpg")


height = image_detector.shape[0]
width = image_detector.shape[1]



##for i in range(image_detector.shape[0]):
##    for j in range(image_detector.shape[1]):
##        if image_detector[i, j][0] == 255:
##            print(image_detector[i, j])


imgray = cv2.cvtColor(image_detector,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(image_detector, contours, -1, (0,255,0), 3)



hull = []
 
# calculate points for each contour
for i in range(len(contours)):
    # creating convex hull object for each contour
    hull.append(cv2.convexHull(contours[i], False))


drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)
 
# draw contours and hull points
for i in range(len(contours)):
    if len(contours[i]) < 200:
        pass
    else:
        color_contours = (0, 255, 0) # green - color for contours
        color = (0, 0, 255) # blue - color for convex hull
        # draw ith contour
        cv2.drawContours(drawing, contours, i, color_contours, 1, 8, hierarchy)
        # draw ith convex hull object
        cv2.drawContours(drawing, hull, i, color, 1, 8)

















cv2.imshow('Security', drawing)
