# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 16:13:02 2022

@author: furka
"""

import cv2 as cv
 
img = cv.imread("IMG_0481.JPG")
img = cv.resize(img,(600,700))
    
# 2 ayrı pixel seçim pixel ağırlığı bulcaz

print(img[120,240]) #konumdaki pixel değerinin bgr kodu
print(img[50,420]) #konumdaki pixel değerinin bgr kodu

print(img[120,240]+img[50,420]) #2 pixel'in bgr değerini topladık. 255 den sonra 0 olup devam ediyor toplam

x = img[120,240]+img[50,420] #belirlenen pixel ağırlıklarını x değişkenine atadık

img[120:200,60:100] = x #ağırlık rengini daha rahat görebilmek için ekranda çizdik

cv.imshow("img",img)

cv.waitKey(0)
cv.destroyAllWindows()