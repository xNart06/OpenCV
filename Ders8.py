# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 16:13:02 2022

@author: furka
"""

import cv2 as cv
 
img = cv.imread("IMG_0481.JPG") 
img2 = cv.imread("foto.JPG")
img = cv.resize(img,(600,700))
img2 = cv.resize(img2,(600,700))
    
canny = cv.Canny(img2,130,150)


toplam = cv.add(img,img2) #resimleri üst üste bindirmek için kullanılan opencv fonksiyonu
agirliklitoplam = cv.addWeighted(img, 0.7, img2, 0.3, 0) #resimlerin birinin baskınlık %'sine göre agirlikli toplam

"""***addWeighted parametreleri

(src1, alpha, src2, beta, gama, dst, dtype)
       %değeri      %değeri
"""
cv.imshow("canny",canny)
cv.imshow("img",img)
cv.imshow("img2",img2)
cv.imshow("toplam",toplam)
cv.imshow("agirliklitoplam",agirliklitoplam)

cv.waitKey(0)
cv.destroyAllWindows()