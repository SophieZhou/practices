import cv2
from cv2 import cvtColor
'''
Parameters
src	input image.
dst	output image of the same size and depth as src # 这个地方初看感觉有问题，大小一样没问题，但是depth不一样，这里depth和存储位数有关，和图像的channel不是一个概念。
code	color space conversion code(see cv.ColorConversionCodes).
dstCn	number of channels in the destination image; if the parameter is 0, the number of the channels is derived automatically from src and code.

void cv::cvtColor	(	InputArray 	src,
OutputArray 	dst,
int 	code,
int 	dstCn = 0 
)		
Python:
cv.cvtColor(	src, code[, dst[, dstCn]]	) ->	dst
'''



img = cv2.imread('messi.jpg')
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print (grayImg.shape)
cv2.imshow('RGB image', img)
cv2.imshow('Grayscale image', grayImg)

cv2.waitKey(0)
cv2.destroyAllWindows()

