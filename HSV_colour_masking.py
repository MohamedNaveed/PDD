import numpy as np
import cv2

img=cv2.imread('xray_image.jpg',1)
hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#image
width = 240
height = 198
image_area= width*height

lower_blue = np.array([100,0,50])
upper_blue = np.array([140,255,255])

lower_orange = np.array([10,50,50])
upper_orange = np.array([45,255,255])


mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
mask_orange = cv2.inRange(hsv, lower_orange, upper_orange)

result_blue = cv2.bitwise_and(img, img, mask=mask_blue)
result_orange = cv2.bitwise_and(img, img, mask=mask_orange)

_, blue_contours, hierarchy = cv2.findContours(mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
_, orange_contours, hierarchy = cv2.findContours(mask_orange, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, blue_contours, -1, (255,0,0), 1)
cv2.drawContours(img, orange_contours, -1, (0,0,255), 1)

blue_area=0
orange_area=0

for i in range(len(blue_contours)):
	c=blue_contours[i]
	blue_area+=cv2.contourArea(c)

for i in range(len(orange_contours)):
	c=orange_contours[i]
	orange_area+=cv2.contourArea(c)

blue_composition=blue_area*100/image_area
orange_composition=orange_area*100/image_area

print blue_area
print orange_area

print image_area
print "blue composition =", blue_composition, "%"
print "orange composition =", orange_composition, "%"

cv2.imshow('image',img)
cv2.imshow('mask_blue',mask_blue)
cv2.imshow('result', result_blue)
cv2.imshow('orange_mask', mask_orange)
cv2.imshow('result_orange',result_orange)

k=cv2.waitKey(0) & 0xFF
if k==27:
    cv2.destroyAllWindows()
