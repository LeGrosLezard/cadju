import scipy
import sklearn
from sklearn.feature_extraction import image
from scipy.io import loadmat
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import numpy as np




points = scipy.io.loadmat("Buffy_1.mat")

coords = [[], []]

for nb, i in enumerate(points["boxes"][0]):
    for j in i[0]:
        for k in j:
            coords[nb].append(k[0].tolist())
 

for i in coords:
    print(i)
    print("")






















