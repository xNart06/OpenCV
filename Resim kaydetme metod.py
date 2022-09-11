# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 20:43:35 2022

@author: furka
"""

import cv2

img = cv2.imread("foto.jpg",0)
cv2.imshow("foto",img)

a=cv2.waitKey(0) #bekleme kodu

if a == 27: #27 esc tuşunun asci kodu
    cv2.destroyAllWindows()
elif a == ord('s'): #ord klavyeden veri almak için kullanılır
    cv2.imwrite("tus_ile_kaydedilen_resim.jpg",img)
    

    
    