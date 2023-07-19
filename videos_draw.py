import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.line(frame, (0, 0), (width, height), (43, 0, 0), 10) #линия1 # (0)frame - наше изображение, (1)координата верхнего левого угла, (2)нижнего правого угла, (3)цвет, (4)толщина
    img = cv2.line(img, (0, width), (height, 0), (0, 24, 200), 5) #линия2
    img = cv2.rectangle(img, (0, 0), (50, 100), (210, 23, 200), 10) #прямоугольник # (1)координата верхней правой точки, (2)координата нижней левой точки, после прямоугольник заполняется сам
    img = cv2.circle(img, (300, 300), 40, (32, 200, 200), -1) #круг # (1)координата где он стоит, (2)радиус круга (4)-1 заполняетя круг цветом

    # текст
    font = cv2.FONT_HERSHEY_PLAIN
    img = cv2.putText(img, 'Sevase is Great!!!', (200, height-10), font, 2, (0, 0, 0), 3, cv2.LINE_AA) #текст # (4) маштаб шрифта

    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

























