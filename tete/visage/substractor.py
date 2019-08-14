import numpy as np
import cv2

def substractor_haut_tete(frame, y, y1, x, x1, subtractor):

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    crop = gray[y1:y, x:x1]
    mask = subtractor.apply(crop)

    liste = []

    for i in mask:
        for j in i:
            liste.append(j)
            

    if sum(liste) / len(liste) > 20:
        print("haut de la tete, concentration ou repositionement")



def substractor_cote_tete_droit(frame, y, y1, x, x1, subtractor):

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    crop = gray[y1:y, x:x1]

    mask = subtractor.apply(crop)
    
    liste = []

    for i in mask:
        for j in i:
            liste.append(j)


    if sum(liste) / len(liste) > 20:
        print("patte de mouche droit")


def substractor_cote_tete_gauche(frame, y, y1, x, x1, subtractor):


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    crop = gray[y1:y, x:x1]
    mask = subtractor.apply(crop)

    
    liste = []

    for i in mask:
        for j in i:
            liste.append(j)
            

    if sum(liste) / len(liste) > 20:
        print("patte de mouche gauche")


def substractor_cote_tete_frame_droit(frame, y, y1, x, x1, subtractor):


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    crop = gray[y1:y, x:x1]
    mask = subtractor.apply(crop)

    
    liste = []

    for i in mask:
        for j in i:
            liste.append(j)
            

    if sum(liste) / len(liste) > 20:
        print("bras droit")


    
def substractor_cote_tete_frame_gauche(frame, y, y1, x, x1, subtractor):


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    crop = gray[y1:y, x:x1]
    mask = subtractor.apply(crop)

    
    liste = []

    for i in mask:
        for j in i:
            liste.append(j)
            

    if sum(liste) / len(liste) > 20:
        print("bras gauche")




def substractor_bouche(frame, y, y1, x, x1, subtractor):


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    crop = gray[y1:y, x:x1]
    mask = subtractor.apply(crop)

    
    liste = []

    for i in mask:
        for j in i:
            liste.append(j)
            
    if sum(liste) / len(liste) > 20:
        print("bouche")


def substractor_menton(frame, y, y1, x, x1, subtractor):


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    crop = gray[y1:y, x:x1]
    mask = subtractor.apply(crop)

    
    liste = []

    for i in mask:
        for j in i:
            liste.append(j)
            

    if sum(liste) / len(liste) > 20:
        print("menton")



def substractor_buste(frame, y, y1, x, x1, subtractor):


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    crop = gray[y1:y, x:x1]
    mask = subtractor.apply(crop)
    
    liste = []

    for i in mask:
        for j in i:
            liste.append(j)
            
    if sum(liste) / len(liste) > 20:
        print("buste")




def substractor_epaul_droite(frame, y, y1, x, x1, subtractor):


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    crop = gray[y1:y, x:x1]
    mask = subtractor.apply(crop)

    
    liste = []

    for i in mask:
        for j in i:
            liste.append(j)
            

    if sum(liste) / len(liste) > 20:
        print("epaul droite")




def substractor_epaul_gauche(frame, y, y1, x, x1, subtractor):


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    crop = gray[y1:y, x:x1]
    mask = subtractor.apply(crop)

    
    liste = []

    for i in mask:
        for j in i:
            liste.append(j)
            

    if sum(liste) / len(liste) > 20:
        print("épaul gauche")





def substractor_front(frame, y, y1, x, x1, subtractor):


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    crop = gray[y1:y, x:x1]
    mask = subtractor.apply(crop)

    
    liste = []

    for i in mask:
        for j in i:
            liste.append(j)
            

    if sum(liste) / len(liste) > 20:
        print("front")




def substractor_tempe_droite(frame, y, y1, x, x1, subtractor):


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    crop = gray[y1:y, x:x1]
    
    mask = subtractor.apply(crop)

    
    liste = []

    for i in mask:
        for j in i:
            liste.append(j)
            

    if sum(liste) / len(liste) > 20:
        print("tempe droite")



def substractor_tempe_gauche(frame, y, y1, x, x1, subtractor):


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    crop = gray[y1:y, x:x1]

    mask = subtractor.apply(crop)

    
    liste = []

    for i in mask:
        for j in i:
            liste.append(j)
            

    if sum(liste) / len(liste) > 20:
        print("tempe gauche")




def substractor_oreille_droite(frame, y, y1, x, x1, subtractor):


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    crop = gray[y:y1, x:x1]
    mask = subtractor.apply(crop)

    
    liste = []

    for i in mask:
        for j in i:
            liste.append(j)
            

    if sum(liste) / len(liste) > 20:
        print("oreille droite")




def substractor_oreille_gauche(frame, y, y1, x, x1, subtractor):


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    crop = gray[y:y1, x1:x]

    mask = subtractor.apply(crop)

    
    liste = []

    for i in mask:
        for j in i:
            liste.append(j)
            

    if sum(liste) / len(liste) > 20:
        print("oreille gauche")




        
