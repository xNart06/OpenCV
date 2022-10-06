# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 15:24:42 2022

@author: furka
"""
import cv2 as cv

img = cv.imread("IMG_0481.JPG")
img = cv.resize(img, (600,700))

img[250,70]=[0,0,0] #250.satır 70. süturdaki pikseli değiştiriyoruz
img[400,50:150]=[245,125,45] #400.satır 50.sütundan 150.sütuna kadar olan pikseli değiştri
img[400:450,50:150]=[245,125,45] #400.satırdan 450. satıra ve 50.sütundan 150.sütuna kadar olan pikseli değiştri

#kolay yol

for i in range(600):
    img[150,i]=[0,0,0]

cv.imshow("img",img)

cv.waitKey(0)
cv.destroyAllWindows()