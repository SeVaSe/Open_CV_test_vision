Проект "Open_CV_test_vision" является тестовым и включает в себя пробные версии работ, с помощью библиотек: OpenCV, Numpy, MediaPipe. Всего в проекте содержится 7 файлов, каждый из которых реализует один тестовый рабочий метод:

1. `copy&paste_photo`: Реализует функционал вырезки и вставки копируемых объектов на фотографии.
2. `cameras&videocapture`: Предоставляет возможность взаимодействия с камерой, включая вращение изображений и другие действия.
3. `videos_draw`: Позволяет рисовать различные объекты во время видео-потока.
4. `object_detection`: Обнаруживает разные объекты на изображении с помощью заранее заданных шаблонов объектов.
5. `color_detection`: Определяет цвета в видео-потоке. В данном примере осуществляется определение синего цвета.
6. `face_detections`: Распознает лица, глаза и улыбки в видео-потоке. Лица и глаза помещаются в области с подписями, а улыбки отображаются и подписываются только при их обнаружении.
7. `detected_and_workHand`: Определяет руки в видео-потоке, рисует линии между точками, а также определяет, в каких областях находятся руки. Левая рука обозначается зеленым цветом, правая - синим. Если точки присутствуют только в одной из сторон, выводится сообщение "NO CONNECTIONS".

