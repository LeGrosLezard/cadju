import scipy
import sklearn
from sklearn.feature_extraction import image
from scipy.io import loadmat
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import numpy as np




points = scipy.io.loadmat("Buffy_1.mat")
img = cv2.imread("Buffy_1.jpg")

coords = [[], []]

for nb, i in enumerate(points["boxes"][0]):
    for j in i[0]:
        for k in j:
            coords[nb].append(k[0].tolist())
 

for i in coords:
    print(i)
    print("")



img[488,345] = 255, 255, 255
img[461,348] = 255, 255, 255
img[465,387] = 255, 255, 255
img[492,384] = 255, 255, 255


img[449,397] = 255, 255, 255
img[462,426] = 255, 255, 255
img[493,413] = 255, 255, 255
img[480,384] = 255, 255, 255

cv2.imshow("dazd", img)


















