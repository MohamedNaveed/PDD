import numpy as np
import cv2

img=cv2.imread('im1.jpg',1)
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
#calculation of blue
"""
for i in range(len(blue_contours)):
	c=blue_contours[i]
	if(flag==False):
		if (b_parent_var == blue_hierarchy[0,i,3]):
			blue_area-=cv2.contourArea(c)
		else:
			blue_area+=cv2.contourArea(c)

	else:
		if (b_parent_var == blue_hierarchy[0,i,3]):
			blue_area+=cv2.contourArea(c)
		else:
			blue_area-=cv2.contourArea(c)

	if(i<(len(blue_contours)-1) and i==blue_hierarchy[0,i+1,3]):
		b_parent_var= i
		if(i>0):
			flag=~flag
	print blue_area

flag = False
o_parent_var=-2
#calculation of orange
for i in range(len(orange_contours)):
	c=orange_contours[i]
	if(flag==False):
		if (o_parent_var == orange_hierarchy[0,i,3]):
			orange_area-=cv2.contourArea(c)
		else:
			orange_area+=cv2.contourArea(c)

	else:
		if (o_parent_var == orange_hierarchy[0,i,3]):
			orange_area+=cv2.contourArea(c)
		else:
			orange_area-=cv2.contourArea(c)

	if(i<(len(orange_contours)-1) and i==orange_hierarchy[0,i+1,3]):
		o_parent_var= i
		if(i>0):
			flag=~flag
	print "orange =", orange_area


blue_composition=(blue_area*100)/image_area
orange_composition=(orange_area*100)/image_area

print blue_area
print orange_area

print image_area
print "blue composition =", blue_composition, "%"
print "orange composition =", orange_composition, "%"
"""
cv2.imshow('image',img)
cv2.imshow('mask_blue',mask_blue)
cv2.imshow('result', result_blue)
cv2.imshow('orange_mask', mask_orange)
cv2.imshow('result_orange',result_orange)

k=cv2.waitKey(0) & 0xFF
if k==27:
    cv2.destroyAllWindows()
