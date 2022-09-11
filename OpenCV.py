# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 19:56:24 2022

@author: furka
"""
import cv2
import numpy as np

img = cv2.imread("foto.jpg",0) #resmi okuduk, sıfır parametresi ile resmi gri yaptık

cv2.imwrite("foto_gri.jpg",img) #resmi aynı dizin içine yeni hali ile kayıt ediyoruz

cv2.imshow("img",img) #görseli ekranda gösteriyoruz

cv2.waitKey(0)
cv2.destroyAllWindows()