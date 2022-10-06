# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 13:14:00 2022

@author: furka
"""

# morfolijik işlemler

import cv2 as cv
import numpy as np

image = cv.imread("morfoloji_foto.jpg")

kernal = np.ones((5,5),np.uint8)

dilation = cv.dilate(image, kernal, iterations=1)
erosion = cv.erode(image, kernal, iterations=1)
dilation2 = cv.dilate(erosion, kernal, iterations=1)

#Yukardaki gibi dilate ve erode yerine sadece opening işlemi ile tekte temiz görüntü alabiliyoruz
opening = cv.morphologyEx(image, cv.MORPH_OPEN, kernal)
#kopuklu, kesikli fotoğraflar için
closing = cv.morphologyEx(image, cv.MORPH_CLOSE, kernal)
#dilation-erosion=gradyan anlamına gelir
gradyan = cv.morphologyEx(image, cv.MORPH_GRADIENT, kernal)
#bu ise image-opening=tophat anlamına gelir
tophat = cv.morphologyEx(image, cv.MORPH_TOPHAT, kernal)
#image-closing=blackhat
blackhat = cv.morphologyEx(image, cv.MORPH_BLACKHAT, kernal)



cv.imshow("img",image)
# cv.imshow("dilation",dilation)
# cv.imshow("erosion",erosion)
# cv.imshow("dilation2",dilation2)
cv.imshow("opening", opening)
cv.imshow("closing",closing)
cv.imshow("gradyan", gradyan)
cv.imshow("tophat",tophat)
cv.imshow("blackhat",blackhat)

cv.waitKey(0)
cv.destroyAllWindows()