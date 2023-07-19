import cv2
import numpy as np

cap = cv2.VideoCapture(0)


while True:
    # real cam
    ret_real, real_frame = cap.read()


    # detect blue
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90, 50, 50]) # светлый синий
    upper_blue = np.array([130, 250, 250]) # темно синий

    mask = cv2.inRange(hsv, lower_blue, upper_blue) # маска - часть кадра, в которой только серые оттенки
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('detection BLUE', result) # вывод только синих объектовый
    cv2.imshow('real', real_frame) # вывод реального изобр
    cv2.imshow('mask', mask) # вывод маски

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

















