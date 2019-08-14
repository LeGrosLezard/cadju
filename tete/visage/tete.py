import numpy as np
import cv2




def milieu_haut_tete(frame, MILIEU_TETE):

    cTm_x1 = int(round(sum(MILIEU_TETE[0]) / len(MILIEU_TETE[0])))
    cTm_y1 = int(round(sum(MILIEU_TETE[1]) / len(MILIEU_TETE[1])))
    cTm_x2 = int(round(sum(MILIEU_TETE[2]) / len(MILIEU_TETE[2])))
    cTm_y2 = int(round(sum(MILIEU_TETE[3]) / len(MILIEU_TETE[3])))

    coul_M = 0, 0, 255
     
    cv2.rectangle(frame, (cTm_x1, cTm_y1), (cTm_x2, cTm_y2), (coul_M), 2)




def cotes_tete(frame, x, y, w, h):


    cTd_x1 = x - 20
    cTd_x2 = x + 30
    cTd_y1 = y - int(round(100 * 100 / h))
    cTd_y2 = y - int(round(10 * 100 / h))

    coul_D = 245,66,75

    cv2.rectangle(frame, (cTd_x1, cTd_y1), (cTd_x2, cTd_y2), (coul_D), 2)


    cTg_x1 = x + w - 20
    cTg_x2 = x + w + 30
    cTg_y1 = y - int(round(100 * 100 / h))
    cTg_y2 = y - int(round(10 * 100 / h))

    coul_G = 24,77,31

    cv2.rectangle(frame, (cTg_x1, cTg_y1), (cTg_x2, cTg_y2), (coul_G), 2)



def cotes_frame(frame, x, y, w, h):
    
    cTd_x1 = x - w - 10
    cTd_x2 = x - 30
    cTd_y1 = y
    cTd_y2 = y + h

    coul_D = 245,66,75

    cv2.rectangle(frame, (cTd_x1, cTd_y1), (cTd_x2, cTd_y2), (coul_D), 3)

    cTg_x1 = x + w + 30
    cTg_x2 = x + w * 2
    cTg_y1 = y
    cTg_y2 = y + h

    coul_G = 24,77,31

    cv2.rectangle(frame, (cTg_x1, cTg_y1), (cTg_x2, cTg_y2), (coul_G), 3)


    










