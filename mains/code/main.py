import cv2
import numpy as np
import csv
import os

import scipy
import sklearn
from sklearn.feature_extraction import image
from scipy.io import loadmat
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import numpy as np


from config import model
from config import config
from config import data


liste = os.listdir(r"C:\Users\jeanbaptiste\Desktop\cadju\mains\HAND\images\main_image\annotations")
path = "../images/main_image/annotations/{}"


#les fichiers .mat
for i in liste:
    print("")
    print(i)

    #ouverture fichier .mat
    points = scipy.io.loadmat(path.format(str(i)))
    coords = [[], []]

    #recuperation des pts du .mat
    for nb, i in enumerate(points["boxes"][0]):
        for j in i[0]:
            for k in j:
                coords[nb].append(k[0].tolist())

    #des fois y'a qu'un seul point qu'on definit par one
    one = False
    for lst in coords:
        if lst == []:
            one = True

    #si pas one on recup les 2 pts
    #sinon on stop
    for nb, pts in enumerate(coords):
        print(nb)
        for p in pts:
            print(p)
        if one is True:
            break
        print("")


    #faut définir tous les pts en txt.






















































