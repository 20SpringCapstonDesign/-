import cv2
import numpy

img=cv2.imread('test8.jpg')

B,G,R= cv2.split(img)

img2=cv2.imread('test8_1.jpg')
B1,G1,R1= cv2.split(img2)

B2,G2,R2=B-B1,G-G1,R-R1
BGR = cv2.merge((B2, G2, R2))
cv2.imshow('merge',BGR)
