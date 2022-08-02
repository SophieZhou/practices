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
img = cv2.imread('0028.jpg')
cv2.imshow('before',img)
ycrcb = cv2.cvtColor(img,cv2.COLOR_RGB2YCrCb)
ycrcb[:,:,0] = cv2.equalizeHist(ycrcb[:,:,0])
img = cv2.cvtColor(ycrcb,cv2.COLOR_YCrCb2RGB)
cv2.imshow('after',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# In[]
help(cv2.imread)
# In[]
import cv2
import numpy as np

img = cv2.imread('messi.jpg')
row,col,chan = img.shape 
cv2.imshow('origin',img)

M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(col,row))
cv2.imshow('img',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
# In[]
rows,cols = img.shape

M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
# In[]
import matplotlib.pyplot as plt
img = cv2.imread('messi.jpg')
rows,cols,ch = img.shape

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1,pts2)

dst = cv2.warpAffine(img,M,(cols,rows))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
# In[]
import matplotlib.pyplot as plt

img = cv2.imread('0028.jpg')

rows,cols,ch = img.shape

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(600,600))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

# In[]
from numpy import *
a=array([[1,2],[3,4],[5,6]])
b = a.flatten()
print (b)
# In[]

# In[]