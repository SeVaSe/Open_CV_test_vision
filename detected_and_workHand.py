import cv2
import numpy as np
import mediapipe as mp


cap = cv2.VideoCapture(1)
mpHands = mp.solutions.hands #  Здесь мы создаем объект mpHands, который представляет собой модель для обнаружения рук из библиотеки Mediapipe
hands = mpHands.Hands() # Объект для обнаружения рук в пространстве
mpDraw = mp.solutions.drawing_utils # объект mpDraw, который содержит инструменты для рисования различных элементов (например, точек, линий) на кадрах изображения

while True:
    ret, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # из BGR в RGB, тк MediaPipe работает ток с RGB
    res = hands.process(imgRGB) # передаем результат в объект для обнаруж РУК, process() выполняет обнаружение рук на переданном изображении и возвращает результаты этой обработки

    coord8gr = None
    coord8bl = None

    if res.multi_hand_landmarks: # проверяет - есть ли руки на данном кадре. multi_hand_landmarks - список всех обнаруж РУК

        for handLandMark in res.multi_hand_landmarks:
            for id, lm in enumerate(handLandMark.landmark): # enumerate - возращает результат списка в виде: 1:индекс, 2:значение
                #print(f'[ID:{id} | mark:{lm}]')
                h, w, channel = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(f'[ID:{id} | mark:{lm}]')


                if cx > w // 2:
                    if id == 8:
                        coord8gr = (cx, cy)
                    cv2.circle(img, (cx, cy), 10, (0, 255, 0), -1)
                else:
                    if id == 8:
                        coord8bl = (cx, cy)
                    cv2.circle(img, (cx, cy), 10, (255, 0, 0), -1)


                if coord8gr and coord8bl:
                    cv2.line(img, coord8gr, coord8bl, (0, 100, 250), 2)


                mpDraw.draw_landmarks(img, handLandMark, mpHands.HAND_CONNECTIONS)

                # if id == 4:
                #     # print(f'Coord 4: {cx}, {cy}')
                #     coord4 = (cx, cy)
                #     print(f'Coord 4: {coord4}')
                #     cv2.circle(img, (coord4), 10, (0,255,0), -1)
                #
                # if hand_id == 1:
                #     if id == 8:
                #         coord8 = (cx, cy)
                #         print(f'Coord 8: {coord8}')
                #         cv2.circle(img, (coord8), 10, (0, 255, 0), -1)
                #
                # if coord4: # and coord8
                #     cv2.line(img, coord4, (coord8), (255,0,0), 2)




    if not coord8gr or not coord8bl:
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(img, 'NO CONNECTIONS', (50, 50), font, 2, (150, 20, 255), 3)

    cv2.imshow('Hands Detected',cv2.resize(img, (800, 600)))

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




































