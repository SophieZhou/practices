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
Point 	center,
int 	radius,
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
'''



#Tips:此处注意，是两个点，但是很多数据集给的标注信息是左上角的点和宽高，所以你要转换一次。