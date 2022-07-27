# -*- coding: utf-8 -*-

# In[]
def fun(a,b,*args):
    res = a+b
    for arg in args:
        res = res + arg
    return res

a = 1
b = 0
alst = [2,3,4,5]
print (alst)
print (*alst)
print (fun(a,b, *alst))

# In[]
'''
 Preferable interpolation methods are cv2.INTER_AREA for shrinking 缩小
 and cv2.INTER_CUBIC (slow) & cv2.INTER_LINEAR for zooming放大. By default, 
 interpolation method used is cv2.INTER_LINEAR for all resizing purposes.
'''
import cv2
import numpy as np

img = cv2.imread('messi.jpg')
res = cv2.resize(img, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
#OR
height, width = img.shape[:2]
res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)


# In[]
import cv2
img = cv2.imread('messi.jpg')
