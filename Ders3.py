# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 16:13:02 2022

@author: furka
"""

import cv2 as cv

img = cv.imread("IMG_0481.JPG")
img,img2,img3 = cv.resize(img,(600,700)),cv.resize(img,(600,700)),cv.resize(img,(600,700))


img[:,:,0]=255 #resmin tamamına mavi filtre uyguluyoruz 0 1 2 değerleri alır son parametre. BGR BLUE GREEN RED mantığı ile sıralanır
img2[:,:,1]=255 # yeşil filtre uyguladık
img3[100:350,200:505,2]=255 # resmin bu değerler arasındaki yerine gri filtre uyguladık
img3[100:350,200:505,1]=120

"""
Birden fazla filtreyi aynı resme uygulayabiliriz. Bunun için:
    img[:,:,0]=255
    img[:,:,1]=255
yapabilirz. blue ve green renk filtresini karıştırıp bize yeni bi filtre sunacak
"""

cv.imshow("img",img)
cv.imshow("img2",img2) 
cv.imshow("img3",img3) 

cv.waitKey(0)
cv.destroyAllWindows()