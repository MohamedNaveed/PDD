import numpy as np
import cv2
import pyqrcode

img=cv2.imread('one.jpg',1)
hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#image
height, width, channels = img.shape
image_area= width*height

lower_blue = np.array([100,50,50])
upper_blue = np.array([140,255,255])

lower_orange = np.array([10,50,50])
upper_orange = np.array([45,255,255])


mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
mask_orange = cv2.inRange(hsv, lower_orange, upper_orange)

result_blue = cv2.bitwise_and(img, img, mask=mask_blue)
result_orange = cv2.bitwise_and(img, img, mask=mask_orange)

_, blue_contours, blue_hierarchy = cv2.findContours(mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
_, orange_contours, orange_hierarchy = cv2.findContours(mask_orange, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(result_blue, blue_contours, -1, (0,255,0), 5)
cv2.drawContours(result_orange, orange_contours, -1, (0,255,0), 5)

blue_area=0
orange_area=0

b_parent_var = -2
flag = False

pixelpoints_blue = cv2.findNonZero(mask_blue)
print len(pixelpoints_blue)

blue_area= float(len(pixelpoints_blue))*100/float(image_area)
print "blue area=", blue_area, "%"

pixelpoints_orange = cv2.findNonZero(mask_orange)
print len(pixelpoints_orange)
orange_area= float(len(pixelpoints_orange))*100/float(image_area)
print "orange area=", orange_area, "%"
print "image area", image_area

#qr = pyqrcode.create('Name: PDD \n Passport number: \n Weight: 100kg \n From: TRY Destination: MAS \n Content composition: \n organic % =' + str(orange_area) + '\n metal % =' +str(blue_area))
#qr = pyqrcode.create('HI'+ str(orange_area))

#qr.png('QR_tag.png', scale=5)

"""cv2.imshow('image',img)
cv2.imshow('mask_blue',mask_blue)
cv2.imshow('result', result_blue)
cv2.imshow('orange_mask', mask_orange)
cv2.imshow('result_orange',result_orange)"""

"""k=cv2.waitKey(0) & 0xFF
if k==27:
    cv2.destroyAllWindows()"""
