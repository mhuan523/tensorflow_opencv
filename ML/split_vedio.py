# split vedio using opencv

import cv2

cap = cv2.VideoCapture('../vedio/1.mp4')
is_opened = cap.isOpened

fps = cap.get(cv2.CAP_PROP_FPS)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

i = 0
while is_opened:
    if i == 10:
        break
    else:
        i = i + 1
    (flag, frame) = cap.read()
    file_name = 'image_' + str(i) + '.jpg'
    if flag is True:
        cv2.imwrite('../vedio/' + file_name, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
