# -*- coding: utf-8 -*-
'''
今天来看看opencv中的resize方法。
就打个tag: opencv resize 
先看看官方定义
void cv::resize	(	InputArray 	src,
OutputArray 	dst,
Size 	dsize,
double 	fx = 0,
double 	fy = 0,
int 	interpolation = INTER_LINEAR 
)		

Python:
dst	=	cv.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]]	)
各个参数可以参考c++版本的数据类型。简单解释如下：
参数	类型	是否必须指定	具体含义
src	numpy.ndarray	是	     原图像
dsize	tuple<int>	是	     缩放后的图像大小
dst  	无所谓	 否	          目标图像，但是在 Python 里面没有任何意义。一般不传参或者设成 None
fx, fy	数值类型	否	    x 和 y 方向上的缩放比例
interpolation	int	否	插值方式表示代码，本质是一个 int 数值，一般用 OpenCV 内置的参数代号以提高可读性。
具体可以参考官方的这个解释：
enum  	cv::InterpolationFlags {
  cv::INTER_NEAREST = 0,
  cv::INTER_LINEAR = 1,
  cv::INTER_CUBIC = 2,
  cv::INTER_AREA = 3,
  cv::INTER_LANCZOS4 = 4,
  cv::INTER_LINEAR_EXACT = 5,
  cv::INTER_NEAREST_EXACT = 6,
  cv::INTER_MAX = 7,
  cv::WARP_FILL_OUTLIERS = 8,
  cv::WARP_INVERSE_MAP = 16
}

因此在使用时，可以写代号也可以写出来方法名字。
使用方法从参数来看，可以设置resize后图像的大小，也可以通过设置方法比例进行resize。
从参数列别可以看到，参数src, dsize是必须有的参数，后面的参数都是可选，或者是有默认值的参数。因此，就是你指定了fx,fy，也必须
同时给dsize赋值（可以为None），否则会报错。但是当你指定dsize的大小了，可以不用管fx,fy.
此处要特别注意，从参数顺序就能看到，此处显示x方向再是y方向的，也就是说先是宽度，再是高度。
此处主要还是要看官方的一个地方是参数的设置，
To shrink an image, it will generally look best with INTER_AREA interpolation, whereas to enlarge an image, 
it will generally look best with c::INTER_CUBIC (slow) or INTER_LINEAR (faster but still looks OK).
这里的意思是，如果resize后，图像变小了，推荐插值算法用INTER_AREA，而如果resize后，图像大小变大了，推荐用INTER_LINEAR或者慢点
但是效果更好的方式INTER_CUBIC (slow)。因此，如果你确定大多数图像resize前后都是增大还是减小，那就可以相应选择对应的插值方法。
'''


'''
first, let me see the img shape. When you using img.shape, it is height, width, channel. Remember this. 
'''
import numpy as np
import cv2
img = cv2.imread(r"messi.jpg")
print('origin image',img.shape) # (296, 474, 3)  in height, width, channel
cv2.imshow("messi", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

rimg = cv2.resize(img,dsize=None,fx=2,fy=2,interpolation=cv2.INTER_LINEAR)# 放大了两倍,此处dsize不可以省略，必须指定的参数
cv2.imshow("resize messi", rimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

rwidth = img.shape[1]*2
rheight = img.shape[0]*2
# 放大了两倍,此处dsize必须是先width再height.
rimg2 = cv2.resize(img,dsize=(rwidth, rheight),interpolation=cv2.INTER_LINEAR)
cv2.imshow("resize messi2", rimg2)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 当dsize和fx,fy不一致，而且两者又都是有效的，优先选择dsize作为参数，而忽略fx,fy。
rwidth = img.shape[1]*3
rheight = img.shape[0]*3
rimg3 = cv2.resize(img,dsize=(rwidth, rheight),fx=1,fy=1,interpolation=cv2.INTER_LINEAR)
cv2.imshow("resize messi3", rimg3)
print ('resize image3: ',rimg3.shape) # (888, 1422, 3)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 当resize后，图像变小了，那么插入方式建议INTER_AREA。
rwidth = int(img.shape[1]*0.5)
rheight = int(img.shape[0]*0.5)
rimg4 = cv2.resize(img,dsize=(rwidth, rheight),fx=1,fy=1,interpolation=cv2.INTER_AREA)
cv2.imshow("resize messi4", rimg4)
print ('resize image4: ',rimg4.shape) # (148, 237, 3)
cv2.waitKey(0)
cv2.destroyAllWindows()

#tips:容易犯错的地方,img.shape给出来的结果是(h,w)，但是resize时，dsize传入的顺序是(w,h)
