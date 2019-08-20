import numpy as np
import cv2

"""#FIRT PART IS INITIALISATION
We take the current position of the face
and display box in function of the head. ^^
After we just display frame. We make a substractor
mesuring len of that (we transofrm list to str is there are movemets
there are highter numbers ^^ so we have capture movement !)"""


def detection_face(frame, faceCascade):
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=1,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    try:
        faces = faces[0].tolist()
        return faces[0], faces[1], faces[2], faces[3]

    except IndexError:
        return 1, 1, 1, 1
 

def init_mouvement(frame, faceCascade, MOUVEMENT):
    
    x, y, w, h = detection_face(frame, faceCascade)
    
    MOUVEMENT[0].append(x)
    MOUVEMENT[1].append(y)



def init_tete_haut(frame, faceCascade, MILIEU_TETE):

    x, y, w, h = detection_face(frame, faceCascade)


    dessus_milieu_1 = y - int(round(150 * 100 / h))
    dessus_milieu_2 = y - int(round(80 * 100 / h))
    
    carre = int(round(w/3))


    cTm_x1 = x + carre
    cTm_x2 = x + carre * 2
    cTm_y1 = dessus_milieu_1
    cTm_y2 = dessus_milieu_2

    coul_M = 0, 0, 255

    cv2.rectangle(frame, (cTm_x1, cTm_y1), (cTm_x2, cTm_y2), (coul_M), 2)

    liste = [cTm_x1, cTm_y1, cTm_x2, cTm_y2]

    c = 0
    for i in liste:
        MILIEU_TETE[c].append(i)
        c+=1

def init_cotes_tete(frame, faceCascade, COTE_TETE):

    x, y, w, h = detection_face(frame, faceCascade)

    cTd_x1 = x - 20
    cTd_x2 = x + 30
    cTd_y1 = y - int(round(110 * 100 / h))
    cTd_y2 = y - int(round(50 * 100 / h))

    coul_D = 245,66,75

    cv2.rectangle(frame, (cTd_x1, cTd_y1), (cTd_x2, cTd_y2), (coul_D), 2)


    cTg_x1 = x + w - 20
    cTg_x2 = x + w + 30
    cTg_y1 = y - int(round(100 * 100 / h))
    cTg_y2 = y - int(round(40 * 100 / h))

    coul_G = 24,77,31

    cv2.rectangle(frame, (cTg_x1, cTg_y1), (cTg_x2, cTg_y2), (coul_G), 2)


    liste = [cTd_x1, cTd_y1, cTd_x2, cTd_y2,
             cTg_x1, cTg_y1, cTg_x2, cTg_y2]

    c = 0
    for i in liste:
        COTE_TETE[c].append(i)
        c+=1



def init_cotes_frame(frame, faceCascade, COTE_FRAME):
    
    x, y, w, h = detection_face(frame, faceCascade)

    cTd_x1 = x - w - 30
    cTd_x2 = x - 60
    cTd_y1 = y
    cTd_y2 = y + h - 30

    coul_D = 245,66,75

    cv2.rectangle(frame, (cTd_x1, cTd_y1), (cTd_x2, cTd_y2), (coul_D), 3)

    cTg_x1 = x + w + 60
    cTg_x2 = x + w * 2 + 30
    cTg_y1 = y
    cTg_y2 = y + h - 30

    coul_G = 24,77,31

    cv2.rectangle(frame, (cTg_x1, cTg_y1), (cTg_x2, cTg_y2), (coul_G), 3)



    liste = [cTd_x1, cTd_y1, cTd_x2, cTd_y2,
             cTg_x1, cTg_y1, cTg_x2, cTg_y2]

    c = 0
    for i in liste:
        COTE_FRAME[c].append(i)
        c+=1



def init_bouche(frame, faceCascade, BOUCHE):

    x, y, w, h = detection_face(frame, faceCascade)

    carre = int(round(w/3))
    hauteur = y + h - 20

    cTb_x1 = x + carre
    cTb_y1 = hauteur
    cTb_x2 = x + carre * 2
    cTb_y2 = y + h - 5


    coul_M = 0, 0, 255
    
    cv2.rectangle(frame,(cTb_x1, cTb_y1), (cTb_x2, cTb_y2), (coul_M), 1)

    liste = [cTb_x1, cTb_y1, cTb_x2, cTb_y2]

    c = 0
    for i in liste:
        BOUCHE[c].append(i)
        c+=1
        

def init_menton(frame, faceCascade, MENTON):

    x, y, w, h = detection_face(frame, faceCascade)

    carre = int(round(w/3))
    hauteur = y + h - 40

    cTm_x1 = x + carre
    cTm_y1 = y + h + 10
    cTm_x2 = x + carre * 2
    cTm_y2 = y + h + 25


    coul_M = 0, 0, 255

    cv2.rectangle(frame,(cTm_x1, cTm_y1), (cTm_x2, cTm_y2), (coul_M), 1)

    liste = [cTm_x1, cTm_y1, cTm_x2, cTm_y2]

    c = 0
    for i in liste:
        MENTON[c].append(i)
        c+=1

def init_buste(frame, faceCascade, BUSTE):
    
    x, y, w, h = detection_face(frame, faceCascade)

    carre = int(round(w/3))
    hauteur = y + h - 40

    cTb_x1 = x
    cTb_y1 = y + h + 120
    cTb_x2 = x + w
    cTb_y2 = y + h + 180


    coul_M = 0, 0, 255

    cv2.rectangle(frame,(cTb_x1, cTb_y1), (cTb_x2, cTb_y2), (coul_M), 1)

    liste = [cTb_x1, cTb_y1, cTb_x2, cTb_y2]

    c = 0
    for i in liste:
        BUSTE[c].append(i)
        c+=1


def init_epaul(frame, faceCascade, EPAUL):

    x, y, w, h = detection_face(frame, faceCascade)

    cTed_x1 = x - 50
    cTed_y1 = y + h + 20
    cTed_x2 = x + 30
    cTed_y2 = y + h + 60

    coul_D = 245,66,75
    
    cv2.rectangle(frame, (cTed_x1, cTed_y1), (cTed_x2, cTed_y2), (coul_D), 1)


    cTeg_x1 = x + w - 30
    cTeg_y1 = y + h + 20
    cTeg_x2 = x + w + 30
    cTeg_y2 = y + h + 60

    coul_G = 24,77,31

    cv2.rectangle(frame,(cTeg_x1, cTeg_y1), (cTeg_x2, cTeg_y2), (coul_G), 1)



    liste = [cTed_x1, cTed_y1, cTed_x2, cTed_y2,
             cTeg_x1, cTeg_y1, cTeg_x2, cTeg_y2]

    c = 0
    for i in liste:
        EPAUL[c].append(i)
        c+=1



def init_front(frame, faceCascade, FRONT):

    x, y, w, h = detection_face(frame, faceCascade)

    
    dessus_milieu_1 = y - int(round(30 * 100 / h))
    dessus_milieu_2 = y - int(round(-40 * 100 / h))
    
    carre = int(round(w/3))


    cTf_x1 = x + 30
    cTf_x2 = x + w - 30
    cTf_y1 = dessus_milieu_1
    cTf_y2 = dessus_milieu_2

    coul_M = 0, 0, 255

    cv2.rectangle(frame, (cTf_x1, cTf_y1), (cTf_x2, cTf_y2), (coul_M), 2)

    liste = [cTf_x1, cTf_y1, cTf_x2, cTf_y2]

    c = 0
    for i in liste:
        FRONT[c].append(i)
        c+=1



def init_tempes(frame, faceCascade, TEMPE):
    
    x, y, w, h = detection_face(frame, faceCascade)

    cTed_x1 = x - 40
    cTed_y1 = y - 20
    cTed_x2 = x
    cTed_y2 = y + 40


    coul_D = 245,66,75
    
    cv2.rectangle(frame,(cTed_x1, cTed_y1), (cTed_x2, cTed_y2), (coul_D), 1)


    cTeg_x1 = x + w
    cTeg_y1 = y + 40
    cTeg_x2 = x + w + 40
    cTeg_y2 = y - 20 

    coul_G = 24,77,31

    cv2.rectangle(frame,(cTeg_x1, cTeg_y1), (cTeg_x2, cTeg_y2), (coul_G), 1)



    liste = [cTed_x1, cTed_y1, cTed_x2, cTed_y2,
             cTeg_x1, cTeg_y1, cTeg_x2, cTeg_y2]

    c = 0
    for i in liste:
        TEMPE[c].append(i)
        c+=1


def init_oreille(frame, faceCascade, OREILLE):
    
    x, y, w, h = detection_face(frame, faceCascade)

    cTod_x1 = x - 40
    cTod_y1 = y + 70
    cTod_x2 = x
    cTod_y2 = y + 110

    coul_D = 245,66,75
    
    cv2.rectangle(frame,(cTod_x1, cTod_y1), (cTod_x2, cTod_y2), (coul_D), 1)


    cTog_x1 = x + w + 40
    cTog_y1 = y + 70
    cTog_x2 = x + w
    cTog_y2 = y + 110

    coul_G = 24,77,31

    cv2.rectangle(frame,(cTog_x1, cTog_y1), (cTog_x2, cTog_y2), (), 1)



    liste = [cTod_x1, cTod_y1, cTod_x2, cTod_y2,
             cTog_x1, cTog_y1, cTog_x2, cTog_y2]

    c = 0
    for i in liste:
        OREILLE[c].append(i)
        c+=1

"""Now we just make mean of all of captured points.
and siplay our frame.
create a substractor with points"""


def milieu_haut_tete(frame, MILIEU_TETE, subtractor):

    cTm_x1 = int(round(sum(MILIEU_TETE[0]) / len(MILIEU_TETE[0])))
    cTm_y1 = int(round(sum(MILIEU_TETE[1]) / len(MILIEU_TETE[1])))
    cTm_x2 = int(round(sum(MILIEU_TETE[2]) / len(MILIEU_TETE[2])))
    cTm_y2 = int(round(sum(MILIEU_TETE[3]) / len(MILIEU_TETE[3])))

    coul_M = 0, 0, 255
     
    cv2.rectangle(frame, (cTm_x1, cTm_y1), (cTm_x2, cTm_y2), (coul_M), 2)

    substractor_haut_tete(frame, cTm_y2, cTm_y1, cTm_x1, cTm_x2, subtractor)



def cotes_tete(frame, COTE_TETE, subtractor1, subtractor2):


    cTd_x1 = int(round(sum(COTE_TETE[0]) / len(COTE_TETE[0])))
    cTd_y1 = int(round(sum(COTE_TETE[1]) / len(COTE_TETE[1])))
    cTd_x2 = int(round(sum(COTE_TETE[2]) / len(COTE_TETE[2])))
    cTd_y2 = int(round(sum(COTE_TETE[3]) / len(COTE_TETE[3])))

    coul_D = 0,0,255

    cv2.rectangle(frame, (cTd_x1, cTd_y1), (cTd_x2, cTd_y2), (coul_D), 2)
    substractor_cote_tete_droit(frame, cTd_y2, cTd_y1, cTd_x1, cTd_x2,
                                 subtractor1)
    
    cTg_x1 = int(round(sum(COTE_TETE[4]) / len(COTE_TETE[4])))
    cTg_y1 = int(round(sum(COTE_TETE[5]) / len(COTE_TETE[5])))
    cTg_x2 = int(round(sum(COTE_TETE[6]) / len(COTE_TETE[6])))
    cTg_y2 = int(round(sum(COTE_TETE[7]) / len(COTE_TETE[7])))


    coul_G = 24,77,31

    cv2.rectangle(frame, (cTg_x1, cTg_y1), (cTg_x2, cTg_y2), (coul_G), 2)
    substractor_cote_tete_gauche(frame, cTg_y2, cTg_y1, cTg_x1, cTg_x2, subtractor2)



def cotes_frame(frame, COTE_FRAME, subtractor1, subtractor2):
    
    cTd_x1 = int(round(sum(COTE_FRAME[0]) / len(COTE_FRAME[0])))
    cTd_y1 = int(round(sum(COTE_FRAME[1]) / len(COTE_FRAME[1])))
    cTd_x2 = int(round(sum(COTE_FRAME[2]) / len(COTE_FRAME[2])))
    cTd_y2 = int(round(sum(COTE_FRAME[3]) / len(COTE_FRAME[3])))

    coul_D = 245,66,75

    cv2.rectangle(frame, (cTd_x1, cTd_y1), (cTd_x2, cTd_y2), (coul_D), 3)
    substractor_cote_tete_frame_droit(frame, cTd_y2, cTd_y1, cTd_x1, cTd_x2,
                                      subtractor1)



    cTg_x1 = int(round(sum(COTE_FRAME[4]) / len(COTE_FRAME[4])))
    cTg_y1 = int(round(sum(COTE_FRAME[5]) / len(COTE_FRAME[5])))
    cTg_x2 = int(round(sum(COTE_FRAME[6]) / len(COTE_FRAME[6])))
    cTg_y2 = int(round(sum(COTE_FRAME[7]) / len(COTE_FRAME[7])))

    coul_G = 24,77,31

    cv2.rectangle(frame, (cTg_x1, cTg_y1), (cTg_x2, cTg_y2), (coul_G), 3)
    substractor_cote_tete_frame_gauche(frame, cTg_y2, cTg_y1, cTg_x1, cTg_x2,
                                       subtractor2)



def bouche(frame, BOUCHE, subtractor):
    
    cTb_x1 = int(round(sum(BOUCHE[0]) / len(BOUCHE[0])))
    cTb_y1 = int(round(sum(BOUCHE[1]) / len(BOUCHE[1])))
    cTb_x2 = int(round(sum(BOUCHE[2]) / len(BOUCHE[2])))
    cTb_y2 = int(round(sum(BOUCHE[3]) / len(BOUCHE[3])))

    coul_M = 0, 0, 255

    cv2.rectangle(frame, (cTb_x1, cTb_y1), (cTb_x2, cTb_y2), (coul_M), 2)
    substractor_bouche(frame, cTb_y2, cTb_y1, cTb_x1, cTb_x2, subtractor)




def menton(frame, MENTON, subtractor):
    
    cTm_x1 = int(round(sum(MENTON[0]) / len(MENTON[0])))
    cTm_y1 = int(round(sum(MENTON[1]) / len(MENTON[1])))
    cTm_x2 = int(round(sum(MENTON[2]) / len(MENTON[2])))
    cTm_y2 = int(round(sum(MENTON[3]) / len(MENTON[3])))

    coul_M = 0, 0, 255

    cv2.rectangle(frame, (cTm_x1, cTm_y1), (cTm_x2, cTm_y2), (coul_M), 2)
    substractor_menton(frame, cTm_y2, cTm_y1, cTm_x1, cTm_x2, subtractor)

    

def buste(frame, BUSTE, subtractor):
    
    cTb_x1 = int(round(sum(BUSTE[0]) / len(BUSTE[0])))
    cTb_y1 = int(round(sum(BUSTE[1]) / len(BUSTE[1])))
    cTb_x2 = int(round(sum(BUSTE[2]) / len(BUSTE[2])))
    cTb_y2 = int(round(sum(BUSTE[3]) / len(BUSTE[3])))

    coul_M = 0, 0, 255

    cv2.rectangle(frame, (cTb_x1, cTb_y1), (cTb_x2, cTb_y2), (coul_M), 2)
    substractor_buste(frame, cTb_y2, cTb_y1, cTb_x1, cTb_x2, subtractor)

    

def epaul(frame, EPAUL, subtractor1, subtractor2):

    cTed_x1 = int(round(sum(EPAUL[0]) / len(EPAUL[0])))
    cTed_y1 = int(round(sum(EPAUL[1]) / len(EPAUL[1])))
    cTed_x2 = int(round(sum(EPAUL[2]) / len(EPAUL[2])))
    cTed_y2 = int(round(sum(EPAUL[3]) / len(EPAUL[3])))

    cTeg_x1 = int(round(sum(EPAUL[4]) / len(EPAUL[4])))
    cTeg_y1 = int(round(sum(EPAUL[5]) / len(EPAUL[5])))
    cTeg_x2 = int(round(sum(EPAUL[6]) / len(EPAUL[6])))
    cTeg_y2 = int(round(sum(EPAUL[7]) / len(EPAUL[7])))


    coul_D = 245,66,75
    coul_G = 24,77,31

    cv2.rectangle(frame, (cTed_x1, cTed_y1), (cTed_x2, cTed_y2), (coul_D), 1)
    substractor_epaul_droite(frame, cTed_y2, cTed_y1, cTed_x1, cTed_x2,
                             subtractor1)

    
    cv2.rectangle(frame,(cTeg_x1, cTeg_y1), (cTeg_x2, cTeg_y2), (coul_G), 1)
    substractor_epaul_gauche(frame, cTeg_y2, cTeg_y1, cTeg_x1, cTeg_x2,
                             subtractor2)
    


def front(frame, FRONT, subtractor):

    cTf_x1 = int(round(sum(FRONT[0]) / len(FRONT[0])))
    cTf_y1 = int(round(sum(FRONT[1]) / len(FRONT[1])))
    cTf_x2 = int(round(sum(FRONT[2]) / len(FRONT[2])))
    cTed_y2 = int(round(sum(FRONT[3]) / len(FRONT[3])))


    coul_M = 0, 0, 255
    
    cv2.rectangle(frame, (cTf_x1, cTf_y1), (cTf_x2, cTed_y2), (coul_M), 1)
    substractor_front(frame, cTed_y2, cTf_y1, cTf_x1, cTf_x2, subtractor)

    

def tempe(frame, TEMPE, subtractor1, subtractor2):

    cTtd_x1 = int(round(sum(TEMPE[0]) / len(TEMPE[0])))
    cTtd_y1 = int(round(sum(TEMPE[1]) / len(TEMPE[1])))
    cTtd_x2 = int(round(sum(TEMPE[2]) / len(TEMPE[2])))
    cTtd_y2 = int(round(sum(TEMPE[3]) / len(TEMPE[3])))

    cTtg_x1 = int(round(sum(TEMPE[4]) / len(TEMPE[4])))
    cTtg_y1 = int(round(sum(TEMPE[5]) / len(TEMPE[5])))
    cTtg_x2 = int(round(sum(TEMPE[6]) / len(TEMPE[6])))
    cTtg_y2 = int(round(sum(TEMPE[7]) / len(TEMPE[7])))


    coul_D = 245,66,75
    coul_G = 24,77,31

    cv2.rectangle(frame, (cTtd_x1, cTtd_y1), (cTtd_x2, cTtd_y2), (coul_D), 1)
    substractor_tempe_droite(frame, cTtd_y2, cTtd_y1, cTtd_x1, cTtd_x2,
                             subtractor1)

    
    cv2.rectangle(frame,(cTtg_x1, cTtg_y1), (cTtg_x2, cTtg_y2), (coul_G), 1)
    substractor_tempe_gauche(frame, cTtg_y1, cTtg_y2, cTtg_x1, cTtg_x2,
                             subtractor2)



def oreille(frame, OREILLE, subtractor1, subtractor2):

    cTod_x1 = int(round(sum(OREILLE[0]) / len(OREILLE[0])))
    cTod_y1 = int(round(sum(OREILLE[1]) / len(OREILLE[1])))
    cTod_x2 = int(round(sum(OREILLE[2]) / len(OREILLE[2])))
    cTod_y2 = int(round(sum(OREILLE[3]) / len(OREILLE[3])))

    cTog_x1 = int(round(sum(OREILLE[4]) / len(OREILLE[4])))
    cTog_y1 = int(round(sum(OREILLE[5]) / len(OREILLE[5])))
    cTog_x2 = int(round(sum(OREILLE[6]) / len(OREILLE[6])))
    cTog_y2 = int(round(sum(OREILLE[7]) / len(OREILLE[7])))


    coul_D = 245,66,75
    coul_G = 24,77,31

    cv2.rectangle(frame, (cTod_x1, cTod_y1), (cTod_x2, cTod_y2), (coul_D), 1)
    substractor_oreille_droite(frame, cTod_y1, cTod_y2, cTod_x1, cTod_x2,
                               subtractor1)


    cv2.rectangle(frame,(cTog_x1, cTog_y1), (cTog_x2, cTog_y2), (coul_G), 1)
    substractor_oreille_gauche(frame, cTog_y1, cTog_y2, cTog_x1, cTog_x2,
                               subtractor2)





"""We mesuring len(str(of the crop area)
If mean > 30 there are movements ! (without movement it's 0.0)
Use function isn't cool because it take space ram but ok
"""





def substractor_haut_tete(frame, y, y1, x, x1, subtractor):

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    crop = gray[y1:y, x:x1]
    mask = subtractor.apply(crop)

    liste = []

    for i in mask:
        for j in i:
            liste.append(j)
            

    if sum(liste) / len(liste) > 30:
        print("haut de la tete, concentration ou repositionement")



def substractor_cote_tete_droit(frame, y, y1, x, x1, subtractor):

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    crop = gray[y1:y, x:x1]

    mask = subtractor.apply(crop)
    
    liste = []

    for i in mask:
        for j in i:
            liste.append(j)


    if sum(liste) / len(liste) > 30:
        print("patte de mouche droit")


def substractor_cote_tete_gauche(frame, y, y1, x, x1, subtractor):


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    crop = gray[y1:y, x:x1]
    mask = subtractor.apply(crop)

    
    liste = []

    for i in mask:
        for j in i:
            liste.append(j)
            

    if sum(liste) / len(liste) > 30:
        print("patte de mouche gauche")


def substractor_cote_tete_frame_droit(frame, y, y1, x, x1, subtractor):


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    crop = gray[y1:y, x:x1]
    mask = subtractor.apply(crop)

    
    liste = []

    for i in mask:
        for j in i:
            liste.append(j)
            

    if sum(liste) / len(liste) > 30:
        print("bras droit")


    
def substractor_cote_tete_frame_gauche(frame, y, y1, x, x1, subtractor):


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    crop = gray[y1:y, x:x1]
    mask = subtractor.apply(crop)

    
    liste = []

    for i in mask:
        for j in i:
            liste.append(j)
            

    if sum(liste) / len(liste) > 30:
        print("bras gauche")




def substractor_bouche(frame, y, y1, x, x1, subtractor):


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    crop = gray[y1:y, x:x1]
    mask = subtractor.apply(crop)

    
    liste = []

    for i in mask:
        for j in i:
            liste.append(j)
            
    if sum(liste) / len(liste) > 30:
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
            
    if sum(liste) / len(liste) > 30:
        print("buste")




def substractor_epaul_droite(frame, y, y1, x, x1, subtractor):


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    crop = gray[y1:y, x:x1]
    mask = subtractor.apply(crop)

    
    liste = []

    for i in mask:
        for j in i:
            liste.append(j)
            

    if sum(liste) / len(liste) > 30:
        print("epaul droite")




def substractor_epaul_gauche(frame, y, y1, x, x1, subtractor):


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    crop = gray[y1:y, x:x1]
    mask = subtractor.apply(crop)

    
    liste = []

    for i in mask:
        for j in i:
            liste.append(j)
            

    if sum(liste) / len(liste) > 30:
        print("épaul gauche")





def substractor_front(frame, y, y1, x, x1, subtractor):


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    crop = gray[y1:y, x:x1]
    mask = subtractor.apply(crop)

    
    liste = []

    for i in mask:
        for j in i:
            liste.append(j)
            

    if sum(liste) / len(liste) > 30:
        print("front")




def substractor_tempe_droite(frame, y, y1, x, x1, subtractor):


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    crop = gray[y1:y, x:x1]
    
    mask = subtractor.apply(crop)

    
    liste = []

    for i in mask:
        for j in i:
            liste.append(j)
            

    if sum(liste) / len(liste) > 30:
        print("tempe droite")



def substractor_tempe_gauche(frame, y, y1, x, x1, subtractor):


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    crop = gray[y1:y, x:x1]

    mask = subtractor.apply(crop)

    
    liste = []

    for i in mask:
        for j in i:
            liste.append(j)
            

    if sum(liste) / len(liste) > 30:
        print("tempe gauche")




def substractor_oreille_droite(frame, y, y1, x, x1, subtractor):


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    crop = gray[y:y1, x:x1]
    mask = subtractor.apply(crop)

    
    liste = []

    for i in mask:
        for j in i:
            liste.append(j)
            

    if sum(liste) / len(liste) > 30:
        print("oreille droite")




def substractor_oreille_gauche(frame, y, y1, x, x1, subtractor):


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    crop = gray[y:y1, x1:x]

    mask = subtractor.apply(crop)

    
    liste = []

    for i in mask:
        for j in i:
            liste.append(j)
            

    if sum(liste) / len(liste) > 30:
        print("oreille gauche")







"""Now we need it because if user moves we need to reorganize our
frames"""



def position(MOUVEMENT, x, y):

    out = False

    if x > MOUVEMENT[0][-1] + 10:
        out = True

    elif x < MOUVEMENT[0][-1] - 10:
        out = True

    elif y < MOUVEMENT[1][-1] - 10:
        out = True

    elif y < MOUVEMENT[1][-1] - 10:
        out = True


    else:
        MOUVEMENT[0].append(x)
        MOUVEMENT[1].append(y)

    return out


def tete_mouvement(frame, faceCascade, MOUVEMENT):

    init = False
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    ) 

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0,0,0), 2)

        init = position(MOUVEMENT, x.tolist(), y.tolist())

    return init, frame







