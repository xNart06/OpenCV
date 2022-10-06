# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 20:59:27 2022

@author: furka
"""

"""
Bozulmuş gürültülü(karıncallı, kumlu) resimleri dügün hale getirmek için filtreleme 
işlemleri yapılır. 

MEAN FILTERING : 3x3'lük 9 pixellik (2.parametreye girilen değer) alanın etrafındaki pixelleri ortalama değerlerini 
ortadaki değere atar. Böylece komşu pixellere yakın bir renk pixeli oluşur

MEDIAN FILTERING : penceredeki tüm pixel değerleri küçükten büyüğe sıralandığı zaman ortanca eleman ortaya yazılır

GAUSE FILTERING : görüntüyü bulanıklaştırıp gürültüyü güdermeye çalışır, Mean filter'a benzer. Ancak daha karışık yapısı

"""
import cv2 as cv

img = cv.imread("C:/Users/furka/Desktop/Python/OpenCv/Youtube_Lessons/gurultulu_resim.JPG")
mean_filter = cv.blur(img,(3,3))
median_filter = cv.medianBlur(img,3) #yukardaki gibi(3,3) yazmak yerine tek 3 yazıyoruz
gauss_filter = cv.GaussianBlur(img,(3,3),0)


cv.imshow("original",img)
cv.imshow("mean_filter",mean_filter)
cv.imshow("median_filter",median_filter)
cv.imshow("gauss_filter",gauss_filter)


cv.waitKey(0)
cv.destroyAllWindows()