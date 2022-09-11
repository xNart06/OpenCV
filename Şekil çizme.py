# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 22:16:17 2022

@author: furka
"""

import cv2
import numpy as np

#cv2.line(), cv2.circle(), cv2.rectangle(), cv2.putText()  thickness=çerçeve kalınlığı
# kullanacağımız fonksiyonlar

#Siyah bir zemin oluşturuyoruz
img = np.zeros((512,512,3), np.uint8) #512x 512y ve rgb görüntü
img_beyaz = np.zeros((512,512,3), np.uint8) + 255 #beyaz arkaplan

#dosya, başlangıç noktası, bitiş noktası, renk, kalınlık
cv2.line(img,(0,0),(511,511),(255,0,0),5) 
cv2.rectangle (img,(384,0), (510,511), (0,255,0), 3)

#merkez, yarıçap,renk, kalınlık
cv2.circle (img,(447,63),63,(0,0,255),1)
################
# yazı ekleme
font = cv2.FONT_HERSHEY_SIMPLEX #font seçimi

#dosya, yazı, konum, font-tipi, yazı boyu, renk, kalınlık, çizgi tipi/ sonuncu olmadan da çalışıyor
cv2.putText(img,'SELAM', (10,500), font, 1, (255,255,255),3,cv2.LINE_AA)
cv2.imshow("line",img)
cv2.imshow("white",img_beyaz)