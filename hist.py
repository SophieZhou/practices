'''
What are histograms?
Histograms are collected counts of data organized into a set of predefined bins
When we say data we are not restricting it to be intensity values (as we saw in the previous Tutorial Histogram Equalization). 
The data collected can be whatever feature you find useful to describe your image.
Let's see an example. Imagine that a Matrix contains information of an image (i.e. intensity in the range 0−255):
What happens if we want to count this data in an organized way? Since we know that the range of information value for this case is 256 values,
 we can segment our range in subparts (called bins) like:
[0,255]=[0,15]∪[16,31]∪....∪[240,255]range=bin1∪bin2∪....∪binn=15
and we can keep count of the number of pixels that fall in the range of each bin_i. Applying this to the example 
above we get the image below ( axis x represents the bins and axis y the number of pixels in each of them).
这里其实做histogram计算，并不一定一定是某个值，通常是用像素值。但是也不是一定要用像素值。
在对像素值进行统计时，如果是灰度图，因为是单通道的，所以相对简单。但是如果是多通道的，在计算histogram时，需要指定是某个通道。
其实也好理解，histogram就是直方图，直方图就可以统计任何值的直方图分布，就是统计一下这个指标的值分布区域范围。这在统计领域常见，
图像上能看到的值，最底层的就是像素值，所以可以用像素值。
'''


'''
void cv::calcHist	(	const Mat * 	images,
int 	nimages,
const int * 	channels,
InputArray 	mask,
OutputArray 	hist,
int 	dims,
const int * 	histSize,
const float ** 	ranges,
bool 	uniform = true,
bool 	accumulate = false 
)		
Python:
cv.calcHist(	images, channels, mask, histSize, ranges[, hist[, accumulate]]	) ->	hist
从函数定义可以看到，calcHist是要区分channel的。所以常常需要用到split这个函数，把图像按照channel先进行分开，然后每个通道进行histogram的计算。
'''
'''
根据官方的解释，下面的代码分为三个步骤，每个函数都可以望文生义。split最简单，就是按照channel进行拆分，把图像分成三个通道的。
而后是calcHist计算直方图，而后是normalize进行归一化。
Use the OpenCV function cv::split to divide an image into its correspondent planes.
To calculate histograms of arrays of images by using the OpenCV function cv::calcHist
To normalize an array by using the function cv::normalize
'''

import cv2 as cv
import numpy as np
# import argparse
# parser = argparse.ArgumentParser(description='Code for Histogram Calculation tutorial.')
# parser.add_argument('--input', help='Path to input image.', default='lena.jpg')
# args = parser.parse_args()
# src = cv.imread('./data/lena.jpg')
# if src is None:
#     print('Could not open or find the image:')
#     exit(0)

# bgr_planes = cv.split(src)
# histSize = 256
# histRange = (0, 256) 
# accumulate = False
# b_hist = cv.calcHist(bgr_planes, [0], None, [histSize], histRange, accumulate=accumulate)
# g_hist = cv.calcHist(bgr_planes, [1], None, [histSize], histRange, accumulate=accumulate)
# r_hist = cv.calcHist(bgr_planes, [2], None, [histSize], histRange, accumulate=accumulate)
# hist_w = 512
# hist_h = 400
# bin_w = int(round( hist_w/histSize ))
# histImage = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)
# cv.normalize(b_hist, b_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
# cv.normalize(g_hist, g_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
# cv.normalize(r_hist, r_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
# for i in range(1, histSize):
#     cv.line(histImage, ( bin_w*(i-1), hist_h - int(b_hist[i-1]) ),
#             ( bin_w*(i), hist_h - int(b_hist[i]) ),
#             ( 255, 0, 0), thickness=2)
#     cv.line(histImage, ( bin_w*(i-1), hist_h - int(g_hist[i-1]) ),
#             ( bin_w*(i), hist_h - int(g_hist[i]) ),
#             ( 0, 255, 0), thickness=2)
#     cv.line(histImage, ( bin_w*(i-1), hist_h - int(r_hist[i-1]) ),
#             ( bin_w*(i), hist_h - int(r_hist[i]) ),
#             ( 0, 0, 255), thickness=2)

# cv.imshow('Source image', src)
# cv.imshow('calcHist Demo', histImage)
# cv.waitKey()



'''
equalizeHist(img)
What is Histogram Equalization?
It is a method that improves the contrast in an image, in order to stretch out the intensity range 
(see also the corresponding Wikipedia entry).
直方图均衡化，其实就是让图像的像素在各个值段都有出现，这样才能形成强烈对比，不能全是某个值段的值。


void cv::equalizeHist	(	InputArray 	src,
OutputArray 	dst 
)		
Python:
cv.equalizeHist(	src[, dst]	) ->	dst


'''
import cv2 as cv
src = cv.imread('./data/lena.jpg')
src = cv.cvtColor(src, cv.COLOR_BGR2GRAY) #转成灰度图，对单通道进行直方图计算，方便对比。
histSize = 256
histRange = (0, 256) 
accumulate = False
hist = cv.calcHist(src, [0], None, [histSize], histRange, accumulate=accumulate)
hist_h =hist_w = 512
cv.normalize(hist, hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
histImage = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)
bin_w = int(round( hist_w/histSize ))
for i in range(1, histSize):
    cv.line(histImage, ( bin_w*(i-1), hist_h - int(hist[i-1]) ),
            ( bin_w*(i), hist_h - int(hist[i]) ),
            ( 255, 0, 0), thickness=2)

# 均衡化直方图
dst = cv.equalizeHist(src)
#####----------------------------------
###compute the histgoram after equalizehist.
#####----------------------------------
hist_2 = cv.calcHist(dst, [0], None, [histSize], histRange, accumulate=accumulate)
cv.normalize(hist_2, hist_2, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
histImage_2 = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)
# 在图上画出来
for i in range(1, histSize):
    cv.line(histImage_2, ( bin_w*(i-1), hist_h - int(hist_2[i-1]) ),
            ( bin_w*(i), hist_h - int(hist_2[i]) ),
            ( 255, 0, 0), thickness=2)

cv.imshow('calcHist Demo', histImage)
cv.imshow('calcHist Demo_2', histImage_2) #此时的的histogram分布要比前面均匀多了，不像前面的像素值集中分布在了某一个区间内，图像上每个点的像素缺少区分度。
cv.imshow('Source image', src)
cv.imshow('Equalized Image', dst)
cv.waitKey()

# import cv2 as cv

# src = cv.imread('./data/lena.jpg')
# dst = src.copy()
# dst[:,:,0] = cv.equalizeHist(src[:,:,0])
# dst[:,:,1] = cv.equalizeHist(src[:,:,1])
# dst[:,:,2] = cv.equalizeHist(src[:,:,2])
# cv.imshow('Source image', src)
# cv.imshow('Equalized Image', dst)
# cv.waitKey()

