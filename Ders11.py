# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 16:20:48 2022

@author: furka
"""

import cv2 as cv
import numpy as np

img = np.zeros((570,960,3),dtype="uint8")

cv.line(img, (0,0),(960,570),(0,255,0),3)
cv.line(img, (0,570),(960,0),(0,0,255),3)
#img pt1 pt2 color thickness

cv.circle(img,(480,285),30,(255,0,0),2)
#img center radius color thickness

cv.putText(img, "Hello World", (615,300),cv.FONT_HERSHEY_COMPLEX, 1, (0,130,84),3)
#img text org(baslangic noktası) fontFace fontScale(yazı boyu) color thickness 
          
cv.imshow("img",img)
cv.waitKey(0)
cv.destroyAllWindows()