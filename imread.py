'''
Mat cv::imread	(	const String & 	filename,
int 	flags = IMREAD_COLOR 
)		
Python:
retval	=	cv.imread(	filename[, flags]	)
官方的文档是这么说的，
The function imread loads an image from the specified file and returns it. If the image cannot be read (because of missing file,
improper permissions, unsupported or invalid format), the function returns an empty matrix ( Mat::data==NULL )
这里要特别注意，当文件没被读取到，返回的是NULL。
首先看一下参数，文件名不能少，其它的都不是必须的。
这个函数看着简单，其实那都是表象，我们来一一看看官方的文档。
The function determines the type of an image by the content, not by the file extension.
此函数是根据图像的内容来决定其类型，而不是根据文件的扩展名。
In the case of color images, the decoded images will have the channels stored in B G R order.
当图像是彩色图时，图像解码后输出的维度是BGR的顺序。
When using IMREAD_GRAYSCALE, the codec's internal grayscale conversion will be used, if available. 
Results may differ to the output of cvtColor()
当使用参数'IMREAD_GRAYSCALE',解码器的内置灰度图转换可能会被调用，这个转换可能和opencv的cvtColor()这个函数得到的结果不一样。
On Microsoft Windows* OS and MacOSX*, the codecs shipped with an OpenCV image
 (libjpeg, libpng, libtiff, and libjasper) are used by default.
So, OpenCV can always read JPEGs, PNGs, and TIFFs. 
On MacOSX, there is also an option to use native MacOSX image readers.
But beware that currently these native image loaders give images with different pixel values because of the color management embedded into MacOSX.
此处解释了WINDOWS, MacOSX的解码，太详细了，具体细看。

On Linux*, BSD flavors and other Unix-like open-source operating systems, 
OpenCV looks for codecs supplied with an OS image. Install the relevant packages 
(do not forget the development files, for example, "libjpeg-dev", in Debian* and Ubuntu*) to get the codec 
support or turn on the OPENCV_BUILD_3RDPARTY_LIBS flag in CMake.
Linux包括其它别的开源操作系统，opencv解码依赖系统的image操作。因此，需要安装相关软件包，比如libjpeg-dev,同时在安装时，cmake文件中
需要打开OPENCV_BUILD_3RDPARTY_LIBS 这个选项。

In the case you set WITH_GDAL flag to true in CMake and IMREAD_LOAD_GDAL to load the image, 
then the GDAL driver will be used in order to decode the image, supporting the following formats: 
Raster, Vector.
当你在cmake中打开了WITH_GDAL，那么在加载图像时将寻找GDAL驱动来解码图像。

If EXIF information is embedded in the image file, the EXIF orientation will be taken into account 
and thus the image will be rotated accordingly except if the flags IMREAD_IGNORE_ORIENTATION or 
IMREAD_UNCHANGED are passed.Use the IMREAD_UNCHANGED flag to keep the floating point values from PFM image.
如果 EXIF 这个信息被封装在图像文件中，

By default number of pixels must be less than 2^30. Limit can be set using system variable OPENCV_IO_MAX_IMAGE_PIXELS

'''
'''
filename	Name of file to be loaded.
flags	Flag that can take values of cv::ImreadModes
下面看一看ImreadModes都可以取哪些值，常用的就是前三个，其余可以参考官方文档：
enum ImreadModes
{
    IMREAD_UNCHANGED           = -1,  # If set, return the loaded image as is (with alpha channel包含alpha通道, otherwise it gets cropped).
    IMREAD_GRAYSCALE           = 0, # If set, always convert image to the single channel grayscale image.
    IMREAD_COLOR               = 1, # If set, always convert image to the 3 channel BGR color image.
    IMREAD_ANYDEPTH            = 2, 
    IMREAD_ANYCOLOR            = 4,
    IMREAD_LOAD_GDAL           = 8,
    IMREAD_REDUCED_GRAYSCALE_2 = 16,
    IMREAD_REDUCED_COLOR_2     = 17,
    IMREAD_REDUCED_GRAYSCALE_4 = 32,
    IMREAD_REDUCED_COLOR_4     = 33,
    IMREAD_REDUCED_GRAYSCALE_8 = 64,
    IMREAD_REDUCED_COLOR_8     = 65,
    IMREAD_IGNORE_ORIENTATION  = 128,
};
'''

import numpy as np
import cv2
img = cv2.imread(r"messi.jpg")  # 默认是IMREAD_COLOR
print('default image',img.shape) # (296, 474, 3)  in height, width, channel
cv2.imshow("default", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img2 = cv2.imread(r"messi.jpg",cv2.IMREAD_COLOR)  # 
print('color image',img.shape) # (296, 474, 3)  in height, width, channel
cv2.imshow("color", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
逐个像素比较一下，两者是完全相等的。
'''
num = 0
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i,j,0] != img2[i,j,0] or img[i,j,1] != img2[i,j,1] or img[i,j,2] != img2[i,j,2]:
            num +=1
            print (num)




# 读入完整图片，含alpha通道
imgwithalpha = cv2.imread('messi.jpg', cv2.IMREAD_UNCHANGED)
cv2.imshow('IMREAD_UNCHANGED+Color', imgwithalpha)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 读入彩色图片，忽略alpha通道
imgcolor = cv2.imread('messi.jpg', cv2.IMREAD_COLOR)
cv2.imshow('IMREAD_COLOR+Color', imgcolor)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
上面两种格式读进来的图，可以类似之前的做法比较一下，还是有稍微差别的。
'''

#彩色图片以灰度图片读入
imgGray = cv2.imread('messi.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('IMREAD_GRAYSCALE+Color', imgGray)
cv2.waitKey(0)
cv2.destroyAllWindows()

