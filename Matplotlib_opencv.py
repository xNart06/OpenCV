# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 19:56:24 2022

@author: furka
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("foto.jpg",0) #resmi okuduk, sıfır parametresi ile resmi gri yaptık
plt.imshow(img) #resim okuma
plt.show() #plt gösterim


cv2.waitKey(0)
cv2.destroyAllWindows()