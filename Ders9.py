# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 07:13:46 2022

@author: furka
"""
import cv2 as cv
img = cv.imread("foto.JPG")
img = cv.resize(img,(600,700))

#pyrUP         pyrDown

ikikat = cv.pyrUp(img) #Resmi 2 kat büyütür
ikikat_k = cv.pyrDown(img) #Resmi 2 kat küçültür
ikikat_kk = cv.pyrDown(ikikat_k) #2 kat küçüğün 2 kat küçüğü
print("Normal:",img.shape,"\n2 Kat Büyük:",ikikat.shape,"\n2 Kat Küçük:",ikikat_k.shape)

cv.imshow("img",img)
cv.imshow("iki kat",ikikat)
cv.imshow("ikikat_k",ikikat_k)
cv.imshow("ikikat_kk",ikikat_kk)

cv.waitKey(0)
cv.destroyAllWindows()