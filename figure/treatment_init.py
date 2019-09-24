import cv2




def detections(img, faceCascade, eyes_cascade):
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(60, 100),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

        crop = img[y:y+h, x:x+w]
        gray_crop = gray[y:y+h-50, x:x+w]
        
        eyes = eyes_cascade.detectMultiScale(
            gray_crop,
            scaleFactor=1.3,
            minNeighbors=4,
            minSize=(30, 30),

            flags=cv2.CASCADE_SCALE_IMAGE
        )

        return eyes, crop, faces



def crop_mode(mode, x1, y1, w1, h1):

    if mode == "left":
        eyes_crop = crop[y1-20:y1+10, x1:x1+w1]
    elif mode == "right":
        eyes_crop = crop[y1-20:y1+10, x1:x1+w1]

    return eyes_crop

def contours_init(contours, th_min, thresh):
    if len(contours) == 2:
        for i in contours:
            if cv2.contourArea(i) == th_min:
                Ocontinuer = False

                cv2.imshow("image1", thresh)
                cv2.waitKey(0)


                        
def find_thresh(mode, x1, y1, w1, h1, th_min):


    eyes_crop = crop_mode(mode, x1, y1, w1, h1)
    gray=cv2.cvtColor(eyes_crop, cv2.COLOR_BGR2GRAY)

    adaptive = 0
    Ocontinuer = True
    while Ocontinuer:
        if adaptive == 255:
            Ocontinuer = False


        _, thresh = cv2.threshold(gray, adaptive, 255,cv2.THRESH_BINARY)
        if mode == "left":
            cv2.line(thresh, (0, 0), (0, thresh.shape[0]), (255, 255, 255), 5)
        elif mode == "right":
            cv2.line(thresh, (thresh.shape[1], 0),
                    (thresh.shape[1], thresh.shape[0]),
                    (255, 255, 255), 5)

        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE,
                                       cv2.CHAIN_APPROX_SIMPLE)

        contours_init(contours, th_min, thresh)


        adaptive += 1


def sourcile(eyes, crop):



    mean = 0
    for x1, y1, w1, h1 in eyes:
        mean += int(x1+w1/2)

    mean = int(mean/2)
    
    for x1, y1, w1, h1 in eyes:

        if x1+w1 < mean:
            find_thresh("left", x1, y1, w1, h1, 198.5)

        elif x1+w1 > mean:
            find_thresh("right", x1, y1, w1, h1, 186.5)
            


            














eyescascade = cv2.CascadeClassifier('haar/haarcascade_eye.xml')
facecascade = cv2.CascadeClassifier('haar/haarcascade_frontalface_alt2.xml')
mouthcascade = cv2.CascadeClassifier('haar/mouth.xml')


img = cv2.imread("treat_init.jpg")

eyes, crop, faces = detections(img, facecascade, eyescascade)
sourcile(eyes, crop)


cv2.imshow("image", crop)
cv2.waitKey(0)























