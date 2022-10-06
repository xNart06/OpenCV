# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 07:13:46 2022

@author: furka
"""
import cv2 as cv
import numpy as np

resim = np.zeros((300,300,3), dtype="uint8") #çıktısı 000
resim2 = np.ones((300,300,3), dtype="uint8")+250 #çıktısı 111
print("zeros",resim)
print("ones",resim2)

cv.imshow("siyah",resim)
cv.imshow("beyaz",resim2)

cv.waitKey(0)
cv.destroyAllWindows()