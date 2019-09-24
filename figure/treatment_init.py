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




def sourcile(eyes, crop):



    mean = 0
    for x1, y1, w1, h1 in eyes:
        mean += int(x1+w1/2)

    mean = int(mean/2)
    
    for x1, y1, w1, h1 in eyes:

        if x1+w1 < mean:

           
            eyes_crop1 = crop[y1-20:y1+10, x1:x1+w1]
            gray=cv2.cvtColor(eyes_crop1, cv2.COLOR_BGR2GRAY)

            adaptive = 0
            Ocontinuer = True
            while Ocontinuer:
                if adaptive == 255:
                    Ocontinuer = False
   
                _, thresh = cv2.threshold(gray, adaptive, 255,cv2.THRESH_BINARY)

                
                cv2.line(thresh, (0, 0), (0, thresh.shape[0]), (255, 255, 255), 5)
                cv2.line(thresh, (0, 0), (thresh.shape[1], 0), (255, 255, 255), 5)
                cv2.line(thresh, (thresh.shape[1], 0), (thresh.shape[1], thresh.shape[0]), (255, 255, 255), 5)
                cv2.line(thresh, (0,  thresh.shape[0]), (thresh.shape[1], thresh.shape[0]), (255, 255, 255), 5)

                contours, _ = cv2.findContours(thresh, cv2.RETR_TREE,
                                               cv2.CHAIN_APPROX_SIMPLE)

                print(len(contours))
                for i in contours:
                    print(cv2.contourArea(i))

                if len(contours) == 2:
                    for i in contours:
                        if 1000.0 > cv2.contourArea(i) > 198.5:
                            Ocontinuer = False

                            cv2.imshow("image1", thresh)
                            cv2.waitKey(0)
                #print(adaptive)
                adaptive += 1





            
        elif x1+w1 > mean:
            print("ici")
            eyes_crop2 = crop[y1-20:y1+10, x1:x1+w1]
            gray=cv2.cvtColor(eyes_crop2, cv2.COLOR_BGR2GRAY)

            adaptive = 0
            Ocontinuer = True
            while Ocontinuer:
                if adaptive == 255:
                    Ocontinuer = False

                _, thresh = cv2.threshold(gray, 156, 255,cv2.THRESH_BINARY)


                cv2.line(thresh, (0, 0), (0, thresh.shape[0]), (255, 255, 255), 5)
                cv2.line(thresh, (0, 0), (thresh.shape[1], 0), (255, 255, 255), 5)
                cv2.line(thresh, (thresh.shape[1], 0), (thresh.shape[1], thresh.shape[0]), (255, 255, 255), 5)
                cv2.line(thresh, (0,  thresh.shape[0]), (thresh.shape[1], thresh.shape[0]), (255, 255, 255), 5)


                contours, _ = cv2.findContours(thresh, cv2.RETR_TREE,
                                               cv2.CHAIN_APPROX_SIMPLE)


                cv2.imshow("image", thresh)
                cv2.waitKey(0)
                print(adaptive)

                print(len(contours))
                for i in contours:
                    print(cv2.contourArea(i))


                if len(contours) == 2:
                    for i in contours:
                        if 1000.0 > cv2.contourArea(i) > 186.5:
                            Ocontinuer = False

                            cv2.imshow("image", thresh)
                            cv2.waitKey(0)
                
                adaptive += 1





            














eyescascade = cv2.CascadeClassifier('haar/haarcascade_eye.xml')
facecascade = cv2.CascadeClassifier('haar/haarcascade_frontalface_alt2.xml')
mouthcascade = cv2.CascadeClassifier('haar/mouth.xml')


img = cv2.imread("WIN_20190924_22_35_19_Pro.jpg")

eyes, crop, faces = detections(img, facecascade, eyescascade)
sourcile(eyes, crop)


cv2.imshow("image", crop)
cv2.waitKey(0)























