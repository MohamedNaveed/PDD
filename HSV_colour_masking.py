import numpy as np
import cv2

img=cv2.imread('xray_image.jpg',1)
hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

result = cv2.bitwise_and(img, img, mask=mask_blue)

cv2.imshow('image',img)
cv2.imshow('mask_blue',mask_blue)
cv2.imshow('result', result)
k=cv2.waitKey(0) & 0xFF
if k==27:
    cv2.destroyAllWindows()
