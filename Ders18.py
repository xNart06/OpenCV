# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 18:00:19 2022

@author: furka
"""
import cv2

image = cv2.imread("C:/Users/furka/Desktop/Python/OpenCv/Youtube_Lessons/BITA.png",0)
image = cv2.resize(image, (300,400))

#görüntüleri daha kaliteli şekilde elde etmek için kullanıyoruz

#simple treshholding
ret,thresh1 = cv2.threshold(image, 160,255, cv2.THRESH_BINARY) 

#adaptive treshholding
thresh2 = cv2.adaptiveThreshold(image,255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
thresh3 = cv2.adaptiveThreshold(image,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

cv2.imshow("org",image)
cv2.imshow("thresh1",thresh1)
cv2.imshow("thresh2",thresh2)
cv2.imshow("thresh3",thresh3)

cv2.waitKey(0)
cv2.destroyAllWindows()