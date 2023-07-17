import cv2

img = cv2.imread('assets/photo1.jpg')
img2 = cv2.imread('assets/photo1.jpg')

for i in range(30):
    for j in range(img.shape[2]):
        img[i][j] = [255, 55, 255]
        img[i][100] = [25, 55, 255]



tgk = img[40:60, 60:80] # копируем фрагмент картинки
img2[10:30, 70:90] = tgk # вставляем скопируемый фрагмент

cv2.imshow('Image', img)
cv2.waitKey(0) # ждем бесконечно, пока не нажмется клавиша
cv2.imshow('1', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

