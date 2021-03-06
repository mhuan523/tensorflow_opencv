# for basic function of opencv

import  cv2

img = cv2.imread('../picture/mountain.jpg', 1)

# jpg format: lossy compression, compression ratio : 0 - 100
cv2.imwrite('../picture/mountain1.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 50])

# png format: lossless compression, compression ratio： 0 - 9
cv2.imwrite('../picture/mountain1.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 0])

# manipulate pixels
(b, g, r) = img[100, 100]
print(b, g, r)
for i in range(100):
    img[i, 100] = (255, 255, 0)
cv2.imwrite('../picture/mountain3.jpg', img)
