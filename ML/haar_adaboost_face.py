# detect faces and eyes using opencv haar adaboost

import cv2

img = cv2.imread('../picture/lena.jpg', 1)

face_xml = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_xml = cv2.CascadeClassifier('haarcascade_eye.xml')

cv2.imshow('src', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_xml.detectMultiScale(gray, 1.2, 5)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
    eye_roi = gray[x: x + w, y: y + h]
    eye_color = img[x: x + w, y: y + h]
    eyes = eye_xml.detectMultiScale(eye_roi, 1.2, 5)
    for (e_x, e_y, e_w, e_h) in eyes:
        cv2.rectangle(eye_color, (e_x, e_y), (e_x + e_w, e_y + e_h), (255, 0, 0), 2)

cv2.imshow('dst', img)
cv2.waitKey(0)
