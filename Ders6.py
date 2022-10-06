# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 16:13:02 2022

@author: furka
"""

import cv2 as cv
 
img = cv.imread("IMG_0481.JPG")
img = cv.resize(img,(600,700))

#dikdörtgen çizme
#sol üst-sağ alt sıralaması ile çizilir

cv.rectangle(img,(180,85),(504,350),[0,0,255],2)

cv.imshow("Rectangle",img)

cv.waitKey(0)
cv.destroyAllWindows()