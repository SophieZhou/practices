'''
本次来学习基于opencv进行各种画图操作，以前只习惯用matplotlib，最近开始用opencv，觉得也很好用。
 cv.line(), cv.circle() , cv.rectangle(), cv.ellipse(), cv.putText() 
 In all the above functions, you will see some common arguments as given below:
img : The image where you want to draw the shapes
color : Color of the shape. for BGR, pass it as a tuple, eg: (255,0,0) for blue. For grayscale, just pass the scalar value.
thickness : Thickness of the line or circle etc. If -1 is passed for closed figures like circles, it will fill the shape. default thickness = 1
lineType : Type of line, whether 8-connected, anti-aliased line etc. By default, it is 8-connected. cv.LINE_AA gives anti-aliased line which looks great for curves.
'''
######################################
# cv2.line 官方的解释如下
'''
void cv::line	(	InputOutputArray 	img,
Point 	pt1,
Point 	pt2,
const Scalar & 	color,
int 	thickness = 1,
int 	lineType = LINE_8,
int 	shift = 0 
)		
Python:
cv.line(img, pt1, pt2, color[, thickness[, lineType[, shift]]]	) ->	img
各个参数的含义如下：

img	Image.
pt1	First point of the line segment.
pt2	Second point of the line segment.
color	Line color.  BGR顺序
thickness	Line thickness.
lineType	Type of the line. See LineTypes.
shift	Number of fractional bits in the point coordinates.

'''
import cv2 as cv
# Create a black image
img = cv.imread('messi.jpg')
# Draw a diagonal blue line with thickness of 5 px
cv.line(img,(0,0),(511,511),(255,0,0),lineType = cv.LINE_AA,shift =0)
cv.imshow('img line ',img)
if cv.waitKey(0) & 0xff==ord('q'):
    cv.destroyAllWindows()
##################
#rectangle 官方解读如下
'''
void cv::rectangle	(	InputOutputArray 	img,
Point 	pt1,
Point 	pt2,
const Scalar & 	color,
int 	thickness = 1,
int 	lineType = LINE_8,
int 	shift = 0 
)		
Python:
cv.rectangle(	img, pt1, pt2, color[, thickness[, lineType[, shift]]]	) ->	img
cv.rectangle(	img, rec, color[, thickness[, lineType[, shift]]]	) ->	img

img	Image.
pt1	Vertex of the rectangle.
pt2	Vertex of the rectangle opposite to pt1 .
color	Rectangle color or brightness (grayscale image).
thickness	Thickness of lines that make up the rectangle. Negative values, like FILLED, mean that the function has to draw a filled rectangle.
lineType	Type of the line. See LineTypes
shift	Number of fractional bits in the point coordinates.   
我喜欢首先通过C++版本的函数来看函数，因为输入输出数据类型一目了然。从参数来看，输入第一个参数是图像，第2，3个参数是坐标点，
严格来说是矩形左上角、右下角的两点，紧接着是颜色，这里也是，如果是灰度可以只有一个scalar,如果是彩色，按照BGR顺序传参。
接着的参数thickness是线的厚度，肯定是这个数越大，画出来的线越宽。然后是线的类型，可以看一下一下几种可选，其中LINE_8是默认的。
这里线的类型和我们普通意义上的是实线、虚线等这种不一样，由于我们这里画线其实是改变了image像素点的颜色，因此这里的线的类型是这个
意义，就是都是怎么改变像素点颜色的算法，具体可以参考官方文档。
LINE_4 Python: cv.LINE_4 4-connected line
LINE_8 Python: cv.LINE_8 8-connected line
LINE_AA Python: cv.LINE_AA antialiased line

'''

import cv2
img = cv2.imread(r'messi.jpg')
print(img.shape)  
cv2.rectangle(img, (120, 10), (240, 100), (0, 255, 0), 2)
cv2.imshow("rectangle", img)
if cv.waitKey(0) & 0xff==ord('q'):
    cv.destroyAllWindows()


'''
circle
void cv::circle	(	InputOutputArray 	img,
Point 	center,  # 圆心
int 	radius,  # 半径
const Scalar & 	color,
int 	thickness = 1,
int 	lineType = LINE_8,
int 	shift = 0 
)		
Python:
cv.circle(	img, center, radius, color[, thickness[, lineType[, shift]]]	) ->	img
'''
cv2.circle(img,(80,80),30,(0,0,255),-1)

cv2.imshow('img',img)

if cv.waitKey(0) & 0xff==ord('q'):
    cv.destroyAllWindows()

'''
text
void cv::putText	(	InputOutputArray 	img,
const String & 	text,
Point 	org,
int 	fontFace,
double 	fontScale,
Scalar 	color,
int 	thickness = 1,
int 	lineType = LINE_8,
bool 	bottomLeftOrigin = false 
)		
Python:
cv.putText(	img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]]	) ->	img
该函数的每个字段数据类型可以从c++的函数定义中看到，在使用时最好保证每个输入字段都是数据类型严格一致的，否则容易出莫名其妙的错。
C++版本的函数定义中，无法明显看到该函数的返回值，其实也可以明白，因为输入的是具有指针意义的Array，在函数内部做操作时，是会改变
其本身的。而python版本的函数指出了返回的也是img。就是是在图上写文字，因此改变了图像本身。其实opencv这几个函数和matplotlib等的
绘制矩形框的方式不太一样，那个是把图加载到画板上，矩形框和字体也是加载到画板上，图像本身是可以不发生变化的。
所以在使用opencv进行这些形状和文字的描写时一定要注意，图是会发生变化的，因此如果后续会继续使用原图，请一定使用copy()把原图备份了。
'''
import time 
import cv2
cap = cv2.VideoCapture(0)
while (1):  
    ret, img = cap.read()

    text = 'camera is ready.'
    import random 
    indx = random.randint(0,len(text))
    # 图片 添加的文字（字符串） 位置（整型，x,y） 字体 字体大小 字体颜色(BGR顺序) 字体粗细
    cv2.putText(img, text, (5,5+indx*10 ), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
    cv2.imshow("image", img)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
cap.release()  
cv2.destroyAllWindows()  

#Tips:此处注意，是两个点，但是很多数据集给的标注信息是左上角的点和宽高，所以你要转换一次。
# 同时各个地方坐标点是整数值，这个可千万要记住，否则提示很多错误。其实也很好理解，这几种方法是通过改变图像像素点像素值来进行画图的，因此必须是整数。
# 另外一个地方，其实也挺出乎意料的，putText函数中第二个参数，要求是字符串，这里使用时一定要是字符串，如果是int类型，一定要
#显示转换一下，否则报错。所以我们在使用时，如果你不确定你的数据是符合数据类型的，最好转换一下。