import cv2
import numpy as np
image = cv2.imread('blue.jpg',1)
new_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow('image',new_image)
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,252,255])

mask = cv2.inRange(new_image,lower_blue,upper_blue)
cv2.imshow('mask',mask)
res = cv2.bitwise_and(image,image,mask=mask)
cv2.imshow('res',res)
blue = np.uint8([[[255,0,0]]])
hsv_blue = cv2.cvtColor(blue,cv2.COLOR_BGR2HSV)
print(hsv_blue)
cv2.waitKey(0)
cv2.destroyWindow()