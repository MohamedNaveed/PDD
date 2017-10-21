import numpy as np
import cv2

img=cv2.imread('heir.jpg',1)

gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray_img,127,255,cv2.THRESH_BINARY)
_, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0,255,0), 5)

cv2.imshow('image', img)
cv2.imshow('gray image', gray_img)
cv2.imshow('thresh', thresh)

for i in range(len(contours)):
    c=contours[i]
    print i, cv2.contourArea(c), hierarchy[0,i,3]

#print hierarchy
area = 0
parent_var = -2
flag = False
for i in range(len(contours)):
    c=contours[i]
    if(flag==False):
        if (parent_var == hierarchy[0,i,3]):
            area-=cv2.contourArea(c)
        else:
            area+=cv2.contourArea(c)

    else:
        if (parent_var == hierarchy[0,i,3]):
            area+=cv2.contourArea(c)
        else:
            area-=cv2.contourArea(c)

    if(i<(len(contours)-1) and i==hierarchy[0,i+1,3]):
        parent_var= i
        if(i>0):
            flag=~flag
    print area

k=cv2.waitKey(0) & 0xFF
if k==27:
    cv2.destroyAllWindows()
