import cv2
import numpy as np


img = cv2.resize(cv2.imread('assets/photo2.jpg'), (0, 0), fx=0.5, fy=0.5)
temp = cv2.resize(cv2.imread('assets/perch.jpg'), (0, 0), fx=0.5, fy=0.5)
temp1 = cv2.resize(cv2.imread('assets/bool.jpg'), (0, 0), fx=0.5, fy=0.5)
height, width, _ = temp.shape
h, w, _= temp1.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]


for method in methods:
    img2 = img.copy()

    res = cv2.matchTemplate(img2, temp, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    res1 = cv2.matchTemplate(img2, temp1, method)
    min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(res1)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
        location1 = min_loc1
    else:
        location = max_loc
        location1 = max_loc1


    bottom_loc = (location[0] + width, location[1] + height)
    bottom_loc1 = (location1[0] + w, location1[1] + h)
    img2 = cv2.rectangle(img2, location, bottom_loc, (0, 0, 255), 4)
    img2 = cv2.rectangle(img2, location1, bottom_loc1, (255, 0, 0), 4)
    cv2.imshow('Detected', img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()































