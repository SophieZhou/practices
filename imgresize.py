# -*- coding: utf-8 -*-
'''
opencv resize 
先看看官方定义
void cv::resize	(	InputArray 	src,
OutputArray 	dst,
Size 	dsize,
double 	fx = 0,
double 	fy = 0,
int 	interpolation = INTER_LINEAR 
)		
Python:
dst	=	cv.resize(	src, dsize[, dst[, fx[, fy[, interpolation]]]]	)
使用方法从参数来看，可以设置resize后图像的大小，也可以通过设置方法比例进行resize。注意这两种方式选一种即可。
此处要特别注意，从参数顺序就能看到，此处显示x方向再是y方向的，也就是说先是宽度，再是高度。
此处主要还是要看官方的一个地方是参数的设置，
To shrink an image, it will generally look best with INTER_AREA interpolation, whereas to enlarge an image, 
it will generally look best with c::INTER_CUBIC (slow) or INTER_LINEAR (faster but still looks OK).
这里的意思是，如果resize后，图像变小了，推荐插值算法用INTER_AREA，而如果resize后，图像大小变大了，推荐用INTER_LINEAR或者慢点
但是效果更好的方式INTER_CUBIC (slow)。因此，如果你确定大多数图像resize前后都是增大还是减小，那就可以相应选择对应的插值方法。
'''

# data = cv2.resize(data,dsize=None,fx=2,fy=2,interpolation=cv2.INTER_LINEAR)
# data = cv2.resize(data,dsize=(2*height,2*width),fx=1,fy=1,interpolation=cv2.INTER_LINEAR)
# data = cv2.resize(data,dsize=(width, height),fx=1,fy=1,interpolation=cv2.INTER_LINEAR)

# https://blog.csdn.net/qq_43668591/article/details/122906293
'''
first, let me see the img shape. When you using img.shape, it is height, width, channel. Remember this. 
'''
import numpy as np
import cv2
img = cv2.imread(r"messi.jpg")
print(img.shape) # (296, 474, 3)  in height, width, channel
cv2.imshow("messi", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

rimg = cv2.resize(img,dsize=None,fx=2,fy=2,interpolation=cv2.INTER_LINEAR)# 放大了两倍
cv2.imshow("resize messi", rimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

rwidth = img.shape[1]*2
rheight = img.shape[0]*2
rimg2 = cv2.resize(img,dsize=(rwidth, rheight),interpolation=cv2.INTER_LINEAR)# 放大了两倍,dsize必须是先width再height.
cv2.imshow("resize messi2", rimg2)
cv2.waitKey(0)
cv2.destroyAllWindows()



