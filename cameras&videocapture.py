import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# size = (600, 200, 3) # Указываем желаемый размер окна (высоту, ширину, число каналов)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    image = np.zeros(frame.shape, np.uint8)
    # (0, 0) в параметре dsize указывает на то, что размеры выходного изображения будут вычислены автоматически на основе масштабных факторов fx и fy
    smaller_image = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    # первая колонка изображений
    image[:height//2, :width//2] = cv2.rotate(smaller_image, cv2.ROTATE_180) # левая верхняя
    image[height//2:, :width//2] = smaller_image # левая нижняя
    # вторая колонка изображений
    image[:height//2, width//2:] = smaller_image # правая верхняя
    image[height//2:, width//2:] = cv2.rotate(smaller_image, cv2.ROTATE_180)# правая нижняя


    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


















