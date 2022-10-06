# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 16:58:46 2022

@author: furka
"""
import cv2 as cv


cap = cv.VideoCapture(0) #Kamera erişim

while True:
    ret,frame = cap.read() #ret kamera çalışıp çalışmadığını kontrol edecek ve cap.read ile kamere görüntüleri okunup frame e aktarılacak
     
    cv.imshow("kamera",frame) #ekranda gösterme
    
    if cv.waitKey(1) & 0xFF==27: #30ms de bir görüntü alacak ve belirli tuşa basarsa çıkarsa
        break #27 = esc
        
cap.release() #kamerayı serbest bırakcak
cv.destroyAllWindows() 


""" Video için
cap = cv.VideoCapture("video.mp4") #Kamera erişim

while True:
    ret,frame = cap2.read() #ret kamera çalışıp çalışmadığını kontrol edecek ve cap.read ile kamere görüntüleri okunup frame e aktarılacak
     
    cv.imshow("kamera",frame) #ekranda gösterme
    
    if cv.waitKey(1) & 0xFF==27: #30ms de bir görüntü alacak ve belirli tuşa basarsa çıkarsa
        break #27 = esc
        
cap.release() #kamerayı serbest bırakcak
"""