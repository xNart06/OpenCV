# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 14:56:20 2022

@author: furka
"""

import cv2 as cv

img = cv.imread("IMG_0481.JPG")
img = cv.resize(img, (600,700))
cv.imshow("img",img)

print(img)
print(img.shape) 
print(img.dtype)
print(img.size)
cv.waitKey(0)
cv.destroyAllWindows()