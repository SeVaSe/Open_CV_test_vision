import cv2
import numpy as np

cap = cv2.VideoCapture(1)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') # загр каскад лица
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml') # загр каскад глаз
mouth_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml') # загр каскад рта

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # переводим в серый цвет картинку
    faces = face_cascade.detectMultiScale(gray, 1.3, 6) # определяем лицо
    font = cv2.FONT_HERSHEY_PLAIN # шрифт

    # вывод лица
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x-25, y-25), (x+w+25, y+h+25), (255,0,0), 4) # рисуем квадрат во круг лица, верхний левый угол, и нижний правый угол прямоугольника
        cv2.putText(frame, 'Face', (x-40, y-40), font, 2, (200,0,40), 2) # приписка, что это лицо
        roy_grey = gray[y:y+h, x:x+w] # это подмножество изображения содержит только пиксели, охватывающие область лица в сером цвете
        roy_color = frame[y:y+h, x:x+w]  # это подмножество изображения содержит только пиксели, охватывающие область лица в цвете

        # вывод глаз
        eyes = eye_cascade.detectMultiScale(roy_grey, 1.1, 20) # определиение глаз
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roy_color, (ex, ey), (ex+ew, ey+eh), (0,0,255), 2)
            cv2.putText(roy_color, 'Eyes', (ex - 25, ey - 10), font, 1, (0, 0, 255), 2)  # приписка, что это улыбка

        # вывод улыбки
        smiles = mouth_cascade.detectMultiScale(roy_grey, 1.8, 20)  # определиение рта
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roy_color, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 2)
            cv2.putText(roy_color, 'Smile', (sx - 25, sy - 10), font, 1.5, (0, 255, 0), 2)  # приписка, что это улыбка


    cv2.imshow('Face Detection', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()