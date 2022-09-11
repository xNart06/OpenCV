# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 20:51:25 2022

@author: furka
"""

import cv2


cap = cv2.VideoCapture(0) #isim yazarsan videoyu alır, 0 gibi rakamlar ise 0,1,2 webcamlar

while(True): #cap.isOpened() hazır video için kullan

    ret, frame = cap.read() #her döngüde görüntüyü okuyup frame değişkenine atacayacak, ret ise true veya false değerlerini döndürecek
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #aynı görğntüyü gri'ye çevirme
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #aynı görğntüyü gri'ye çevirme
    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    blur = cv2.GaussianBlur(frame,(13,13), cv2.BORDER_DEFAULT)
    canny = cv2.Canny(frame,125,175)
    cv2.imshow("webcam",frame) #burda bize her frame i gösterecek
    cv2.imshow("gri",gray)
    cv2.imshow("hsv",hsv)
    cv2.imshow("rgb",rgb)
    cv2.imshow("canny",canny)
    cv2.imshow("blur",blur)
    
    a = cv2.waitKey(1) #esc ile çıkış için değişkene atadık waitKey(1) her karenin ekranda kaç mili saniye duracağını belirler
    if a == 27:
        break
    
cap.release() #tutulan videoyu bırak

cv2.destroyAllWindows()
