# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 17:38:49 2022

@author: furka
"""

#pixel değeri eşik değerinden küçükse 0'a ayarlanır. Aksi takdirde max değere ayarlanır.

import cv2

image = cv2.imread("foto.JPG",0)
image = cv2.resize(image, (300,400))

ret,thresh1 = cv2.threshold(image, 127,255, cv2.THRESH_BINARY) #2 parametre alır. pixel değeri 127 altında olanı 0 a eşitler diğerlerini 255 e 
ret,thresh2 = cv2.threshold(image, 127,255,cv2.THRESH_BINARY_INV) #yukardakinin  aynısı zıt renkler
ret,thresh3 = cv2.threshold(image, 127,255,cv2.THRESH_TRUNC) #orjinalın solmuş hali
ret,thresh4 = cv2.threshold(image, 127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(image, 127,255,cv2.THRESH_TOZERO_INV)

cv2.imshow("org",image)
cv2.imshow("THRESH_BINARY", thresh1) 
cv2.imshow("THRESH_BINARY_INV", thresh2)
cv2.imshow("THRESH_TRUNC", thresh3)
cv2.imshow("THRESH_TOZERO", thresh4)
cv2.imshow("THRESH_TOZERO_INV", thresh5)

cv2.waitKey(0)
cv2.destroyAllWindows()