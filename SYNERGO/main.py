import cv2

from mains.traitement_hand import delete_visage
from mains.traitement_hand import first_window
from mains.traitement_hand import seconde_window
from mains.traitement_hand import contour_image
from mains.traitement_hand import hull_function
from mains.traitement_hand import points_main
from mains.traitement_hand import points
from mains.traitement_hand import hand_function


from head_position.head_inclinaison import initialisation
from head_position.head_inclinaison import position_oeil
from head_position.head_inclinaison import position_tete




def video_capture():
    
    #We call Face Haarcascade
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
    #We call Eyes Haarcascade
    eyesCascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    
    #Container of inclinaison_head
    LISTE = []
    
    video_capture = cv2.VideoCapture(0)

    first_frame = None
    
    while True:

        _, frame = video_capture.read()
        frame = cv2.resize(frame, (600, 600))
        
        grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        drawing, first_frame = hand_function(frame, grayscale_frame,
                                             first_frame, faceCascade)

        windows = {"dazdza":drawing, "yeux":frame, "tete":frame}
 
        for nom, fenetre in windows.items():
            cv2.imshow(nom, fenetre)



        if len(LISTE) < 5:
            initialisation(grayscale_frame, faceCascade, eyesCascade, LISTE)
            
        else:
            position1 = position_tete(frame, grayscale_frame, faceCascade, eyesCascade, LISTE)













        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            cv2.destroyAllWindows()
            break
     
    video.release()
    cv2.destroyAllWindows()
        





















if __name__ == "__main__":
    video_capture()

















