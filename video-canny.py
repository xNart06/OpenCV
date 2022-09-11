# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 22:54:22 2022

@author: furka
"""
import cv2 as cv

img = cv.imread('2a8d9b58-25d1-4cef-9193-24aa78a32423.jpg')
img = cv.resize(img, (300,500))
blur = cv.GaussianBlur(img,(7,7), cv.BORDER_DEFAULT)
canny = cv.Canny(blur,125,175)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("canny",canny)
cv.imshow("image",img)
cv.imshow("HSV",hsv)
cv.imshow("gray",gray)  

cv.waitKey(0)
cv.destroyAllWindows()
