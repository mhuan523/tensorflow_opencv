# make vedio using opencv

import cv2

img = cv2.imread('../vedio/image_1.jpg', 1)
info = img.shape

size = (info[1], info[0])

fourcc = cv2.VideoWriter.fourcc('M', 'J', 'P', 'G')
vedio_writer = cv2.VideoWriter('../vedio/2.mp4', fourcc, 15, size)

for i in range(1, 11):
    file_name = 'image_' + str(i) + '.jpg'
    frame = cv2.imread('../vedio/' + file_name, 1)
    vedio_writer.write(frame)
