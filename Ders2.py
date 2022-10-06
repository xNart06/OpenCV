# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 15:24:42 2022

@author: furka
"""
import cv2 as cv

img = cv.imread("IMG_0481.JPG")
img = cv.resize(img, (600,700))

cv.imshow("img",img)

print(img[(230,50)])#girilen(230,50) noktasına ait bgr değerini gösterir

print("Resim Boyutu:"+str(img.size))
print("Resim Özellikleri"+str(img.shape)) #str=değerleri string ifadeye çevirir
print("Resim veri tipi"+str(img.dtype))

cv.waitKey(0)
cv.destroyAllWindows()