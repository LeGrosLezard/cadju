    for x, y, w, h in faces:

        y1 = int(150*100/y+h)
        
        crop1 = frame[y1:y+h, x+50:x+w-50]
        crop_g = cv2.cvtColor(crop1, cv2.COLOR_BGR2GRAY)
        crop_g = adjust_gamma(crop_g, 2.5)
        edge = cv2.Canny(crop_g, 40, 10)
