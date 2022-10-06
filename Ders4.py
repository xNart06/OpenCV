
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 16:13:02 2022

@author: furka
"""

import cv2 as cv

img = cv.imread("IMG_0481.JPG")
img = cv.resize(img,(600,700))

kesit = img[100:350,200:500] #100den350 y parametresi// 200 den 500 x parametresi
kesit[:,:,1]=25 #opsiyonel olarak filtre uyguladım

img[0:250,0:300] = kesit #kesit içindeki resmi, sol tarafta belirtilen 100-100 lük alana koyuyoruz
"""BURADA DİKKAT ETMEN GEREKEN BİR UNSUR VAR. KESİTİ KAÇA KAÇLIK ALDIYSAN RESİMDE YAPIŞTIRACAĞIN ALAN DA 
O BOYUTTA OLMALI"""

cv.imshow("img",img)
# cv.imshow("kesit",kesit)

cv.waitKey(0)
cv.destroyAllWindows()