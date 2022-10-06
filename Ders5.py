
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 16:13:02 2022

@author: furka
"""

import cv2 as cv

img = cv.imread("IMG_0481.JPG")
img = cv.resize(img,(300,350))

"""HEPSİNDE copyMakeBorder(src,top,bottom,lef,right,cv.BORDER_xxxxxx) ifadesi kullanılacak"""


#AYNALAMA  ===>  cv.BORDER_REFLECT  
aynalama = cv.copyMakeBorder(img,300,300,700,700,cv.BORDER_REFLECT)

#UZATILAN ==> cv.BORDER_REPLICATE
uzatılan = cv.copyMakeBorder(img,100,100,150,150,cv.BORDER_REPLICATE)

#TEKRAR ==>cv.BORDER_WRAP
tekrar = cv.copyMakeBorder(img,300,300,700,700,cv.BORDER_WRAP)

#çerçeve ==>cv.BORDER_CONSTANT + value=(0,0,0) ekleyip renk verebiliriz
cerceve = cv.copyMakeBorder(img,5,5,5,5,cv.BORDER_CONSTANT, value=(255,12,124))


cv.imshow("aynalama",aynalama)
cv.imshow("Uzatılan",uzatılan)
cv.imshow("Tekrar",tekrar)
cv.imshow("cerceve",cerceve)

cv.waitKey(0)
cv.destroyAllWindows()