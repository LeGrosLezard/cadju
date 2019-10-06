import cv2
import numpy as np
import csv


import scipy
import sklearn
from sklearn.feature_extraction import image
from scipy.io import loadmat
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import numpy as np


from config import liste_mat
from config import path_mat
from config import liste_picture
from config import path_picture



def resize_coordinate(width, height, points):

    dw = 1./width
    dh = 1./height

    coords = [[], []]

    for i in range(len(points)):
        try:
            x = (points[i][0][0] + points[i][0][1])/2.0
            y = (points[i][1][0] + points[i][1][1])/2.0
            w = points[i][0][1] - points[i][0][0]
            h = points[i][1][1] - points[i][1][0]
            x = x * dw
            w = w * dw
            y = y * dh
            h = h * dh

            coords[i].append(x);coords[i].append(w);
            coords[i].append(y);coords[i].append(h);
        except IndexError:
            pass

    return coords



def recup_data_mat_file(i, path, width, height):

    #ouverture fichier .mat
    points = scipy.io.loadmat(path.format(str(i)))

    coords = [[], []]



    #recuperation des pts du .mat
    for nb, i in enumerate(points["boxes"][0]):
        for j in i[0]:
            for k in j:
                try:
                    if k[0] == "R" or k[0] == "L":
                        pass
                    else:
                        coords[nb].append(k[0].tolist())
                except:
                    pass

    coords = resize_coordinate(width, height, coords)

    return coords



def define_numbers_point(coords):

    #des fois y'a qu'un seul point qu'on definit par one
    one = False
    for lst in coords:
        if lst == []:
            one = True

    return one


def numbers_of_points(one, coords, path, i):

    #si pas one on recup les 2 pts
    #sinon on stop

    first = True
    
    for nb, pts in enumerate(coords):
        print(nb)

        if nb == 1:
            first = False

        writting_annotation_to_picture(path, i, first)
        
        for p in pts:
            writting_points_into_txt(path, i, p)

        if one is True:
            break



    #faut définir tous les pts en txt.


def writting_annotation_to_picture(path, i, first):

    i = str(i[:-4]) + ".txt"

    print(path.format(i))

    with open(path.format(i), "a") as file:
        if first is False:
            file.write(str("\n"))
        file.write("0")


def writting_points_into_txt(path, i, p):

    i = str(i[:-4]) + ".txt"
    
    with open(path.format(i), "a") as file:
        file.write(" ")
        file.write(str(p))




def acess_to_list_path(liste, path, path_picture):
    #les fichiers .mat
    for i in liste:
        print("")

        print(i)

        img = cv2.imread(path_picture.format(str(i[:-4]) + ".jpg"))
        width = img.shape[1]
        height = img.shape[0]

        coords = recup_data_mat_file(i, path, width, height)
        one = define_numbers_point(coords)
        numbers_of_points(one, coords, path_picture, i)



if __name__ == "__main__":
    acess_to_list_path(liste_mat, path_mat, path_picture)












