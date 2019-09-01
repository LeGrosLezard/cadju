import numpy as np
import cv2
import time


def detection_faces(frame, faceCascade, gray):
    
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=1,
        minSize=(60, 100),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    if faces == ():
        faces = [(0,0,0,0)]

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 0), 2)

        #coupe image axe tete, ENFACE VENTRE
        cv2.rectangle(frame, (x-10, y), (x+w+10, y+h+800), (0, 255, 0), 2)
        mask_colonne = frame[y:y+h+800, x-50:x+w+50]

        return mask_colonne, y, y+h+800, x-50, x+w+50, faces

    return 0, 0, 0, 0, 0, faces



def zone2(frame):

    try:
        #coupe l'image de 70% de haut
        cv2.rectangle(frame, (0, int(round(600*70/100))), (800, 600), (0, 255, 255), 2)
        mask = frame[int(round(600*70/100)):600, 0:800]

        return mask, int(round(600*70/100)), 600, 0, 800
    except:
        return 0, 0, 0, 0, 0



def zone_extra_hemi_espace(frame, faces):

    #droite gauche du cadre
    for x, y, w, h in faces:
        cv2.rectangle(frame, (0, 0), (x, y+800), (255, 0, 0), 2)
        cv2.rectangle(frame, (x + w, 0), (x+800, y+800), (255, 0, 0), 2)

        return 0,0, x, y+800, x+w, 0, x+800, y+800


def situation_mouvement(area, x, y, y1_zon, x2_hemi1, x2_hemi2, w, x1_col, x2_col, frame):
    air = ""
    proba = 0

    liste = []
    
    if area > 30000:
        #print("GROS MOUVEMENT")
        liste.append("GROS MOUVEMENT")
        #proba = 60
        #cv2.putText(frame, str("bras " + "" + str(proba) + " %"), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255),1,cv2.LINE_AA)
        air = True
        
    if y > y1_zon:
        #print("LE CARRE EST EN BAS")
        liste.append("LE CARRE EST EN BAS")
        pass
    
    if y < y1_zon:
        #print("LE CARRE EST EN HAUT")
        liste.append("LE CARRE EST EN HAUT")
        pass
    
    if x < x2_hemi1 and y < y1_zon:
        #print("CARRE DANS LA ZONE HEMI DROITE")
        liste.append("CARRE DANS LA ZONE HEMI DROITE")
        pass
    
    if x > x2_hemi2 and y < y1_zon:
        #print("CARRE DANS LA ZONE HEMI GAUCHE")
        liste.append("CARRE DANS LA ZONE HEMI GAUCHE")
        pass
    
    if y > y1_zon and x > x1_col and x+w < x2_col:
        #print("CARRE FACE VENTRE")
        liste.append("CARRE FACE VENTRE")
        pass
    


    return liste

    """MOUVEMENT -> rectangle énorme, puis qui se rétrécit juqu'a la main -> meme zone 100%"""
    """Faut mtn analyser sa position"""
    """SUIVRE LE MOUVEMENT DES RECTANGLE SI LE MOUVEMENT EST HUMAIN LA PROBA AUGMENTE"""
    """Attention des fois des carrree apparaissent apres pres du bras ce ne sont
    pas des mains mais la proba augmentera enfaite..."""
    """Il pour dire il s'est touché la tempe ca sera le tour dapres enfaite
    et faire soustration temps pour dire la le mec s'est touché la tempe
    via la position du rectangle
    """
    """DETECTEUR DE ZONE POUR SAVOIR ???? OU APPROXIMATION DES COINS ??"""
    
    #"""ATTENTION sur cam les mouvements sont hyper élargis plus de flou ?"""
    

def possibilite_main(x, y, w, h, LISTE, aire, LISTE2,
                     etape, liste_situ, ok_petit, LISTE_CALBUTE,
                     LISTE_CALBUTE1, frame, only_hand, LISTE_MAIN):

    

    debut_analyse = ""
    hand_only = False


    
    if aire > 30000:
        try:
            #print(LISTE2[-1][0], LISTE2[-1][1],LISTE2[-1][2],LISTE2[-1][3])
            LISTE_CALBUTE.append(y+h - LISTE2[-1][3])
            if sum(LISTE_CALBUTE) > 0:
                #print(sum(LISTE_CALBUTE), "mouvement DESCENDANT", y+h)
                pass
            else:
                #print(sum(LISTE_CALBUTE), "mouvement ASCENDANT", y+h)
                pass
        except:
            pass
        
        #print([x, x+w, y, y+h, aire], "mouvement actuel")
        proba = 80
        LISTE2.append([x, x+w, y, y+h, aire, liste_situ, etape])
        cv2.putText(frame, str("Bras "  + "" + str(proba) + " %"), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255),1,cv2.LINE_AA)
        debut_analyse = True

        
    else:
        
        if ok_petit is True:

            proba = 0
            

            
            try:
                #print(LISTE[-1][0], LISTE[-1][1], LISTE[-1][2], LISTE[-1][3])
                pass
            except:
                pass
            
            if sum(LISTE_CALBUTE) > 0:
                #print(sum(LISTE_CALBUTE), "mouvement DESCENDANT", y+h)
                pass
            else:
                #print(sum(LISTE_CALBUTE), "mouvement ASCENDANT", y+h)
                pass

            
            #print("main", x, y+h, "DERNIER mouvement", LISTE2[-1][0], LISTE2[-1][3])

            if only_hand is False:
                if y+h + 70 > LISTE2[-1][3] and sum(LISTE_CALBUTE) > 0:
                    proba += 70
                    print("70%")
                    hand_only = True
                    LISTE_CALBUTE1.append(y+h)
                    
                    
                elif y+h + 80 > LISTE2[-1][3] and sum(LISTE_CALBUTE) > 0:
                    proba += 60
                    print("60%")
                    hand_only = True
                    LISTE_CALBUTE1.append(y+h)
                    
                    
                elif y+h + 90 > LISTE2[-1][3] and sum(LISTE_CALBUTE) > 0:
                    proba += 50
                    print("50%")
                    hand_only = True
                    LISTE_CALBUTE1.append(y+h)
                    

                elif y+h + 100 > LISTE2[-1][3] and sum(LISTE_CALBUTE) > 0:
                    proba += 40
                    print("40%")


                if y+h - 100 < LISTE2[-1][3] and sum(LISTE_CALBUTE) < 0:
                    proba += 40
                    print("40%")


                cv2.putText(frame, str("main "  + "" + str(proba) + " %"), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255),1,cv2.LINE_AA)
                LISTE.append([x, x+w, y, y+h, aire, liste_situ, etape])

            else:
                proba = 0
                #seconde étape on a trouvé un mouvement
                #on a trouvé une fin de mouvement
                #ON CHERCHE LES FIN DE MOUVEMENT
                #la on est de haut en bas
                #le mec peut alors les relevé, les mettre vers sont ventre
                #tendre le bras vers une extrémité
                #la laissé comme ca

                try:
                    print("main", y+h, "DERNIERE MAIN", LISTE_CALBUTE1[-1])
                except:
                    pass

                if y+h + 38 == LISTE_CALBUTE1[-1]:
                    proba += 80

                elif y+h + 56 == LISTE_CALBUTE1[-1]:
                    proba += 60


                else:
                    proba += 0



                LISTE_MAIN.append([x, x+w, y, y+h, proba])


                    
                cv2.putText(frame, str("main "  + "" + str(proba) + " %"), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255),1,cv2.LINE_AA)



                


            


            




    return debut_analyse, hand_only




def analyse_post_traumatic(LISTE1, LISTE2):
    pass




##ok au moins l'image ressemble au video je sais pas du tout comment faire réduit le seuil sinon ca detecte pas trop
##
##ok pour les zones du genre tempe faut le truk du début
##
##faire les pourcentages cm1 a la fin...
##
##------------------------------------------------
##
##skin detecteur au cas ou
##
##ou haarcascade dans le carré








