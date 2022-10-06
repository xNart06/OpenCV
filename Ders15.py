# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 22:47:33 2022

@author: furka
"""
# morfolijik işlemler

import cv2 as cv
import numpy as np

image = cv.imread("C:/Users/furka/Desktop/Python/OpenCv/Youtube_Lessons/BITA.png")

kernal = np.ones((2,2),np.uint8) #işlem yapmak için bir kernal oluşturduk

#kesikli resimlerde fayda sağlar beyazları genişletir
dilation = cv.dilate(image, kernal, iterations=1)#yeni fonskiyon dilate, 2 renkli resimlerde beyazı baskın yapıyor kalınlığı artıyor

#arka plandaki gürültü azaltılır
erosion = cv.erode(image, kernal, iterations=1)#yeni fonksiyon erode, gürültü azaltıyor

#erosion ile beyazlar gitti aynı görseli dilate edince foto düzgün ama beyazlardan kurtulmuş halde geri gelecek
dilation2 = cv.dilate(erosion, kernal, iterations=2)


cv.imshow("img",image)
cv.imshow("dilation",dilation)
cv.imshow("erosion",erosion)
cv.imshow("dilation2",dilation2)

cv.imwrite("yeni Bita",dilation2)


cv.waitKey(0)
cv.destroyAllWindows()