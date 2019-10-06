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





def recup_data_mat_file(i, path):

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
            print(p[0])
            
            writting_points_into_txt(path, i, p[0])

        if one is True:
            break
        print("")


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




def acess_to_list_path(liste, path):
    #les fichiers .mat
    for i in liste:
        print("")

        print(i)
        coords = recup_data_mat_file(i, path)
        one = define_numbers_point(coords)
        numbers_of_points(one, coords, path_picture, i)




if __name__ == "__main__":
    acess_to_list_path(liste_mat, path_mat)
