import numpy as np
import cv2


frame = cv2.imread("image.jpg")
height = 600 
width = 600
im2 = np.zeros((height,width,3), np.uint8)
im2[:,0:width//2] = (255,255,255)      # (B, G, R)
im2[:,width//2:width] = (255,255,255)  


imgray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours (im2, contours, -5, (0, 0, 0), 20)


cv2.imwrite("image1.jpg", im2)




frame = cv2.imread("image1.jpg", 1)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convert to grayscale
blur = cv2.blur(gray, (3, 3)) # blur the image
ret, thresh = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

hull = []

for i in range(len(contours)):
    # creating convex hull object for each contour
    hull.append(cv2.convexHull(contours[i], False))

drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)
 
# draw contours and hull points
for i in range(len(contours)):
    color_contours = (0, 255, 0) # green - color for contours
    color = (255, 0, 0) # blue - color for convex hull
    # draw ith contour
    cv2.drawContours(drawing, contours, i, color_contours, 1, 8, hierarchy)
    # draw ith convex hull object
    cv2.drawContours(drawing, hull, i, color, 1, 8)

print(hull)
cv2.imshow("imageyooo.jpg", drawing)






























