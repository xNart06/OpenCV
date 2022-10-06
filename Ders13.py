# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 19:51:03 2022

@author: furka
"""
import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    
    ret,frame = cap.read()
    
    cv.rectangle(frame, (125,90),(570,350),(0,255,0),3) #videoya dikdörtgen ekledik
    cv.putText(frame, "FURKAN",(120,80),cv.FONT_HERSHEY_COMPLEX, 1, (0,0,255),1)
    
    cv.imshow("video",frame)
    
    if cv.waitKey(1) & 0xff==27:
        break

cap.release()
cv.destroyAllWindows()