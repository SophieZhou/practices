
import time
import cv2
import numpy as np
from os import path
import pickle


'''
关于camera id 此处需要稍微说几句。一般我们测试时，可能会通过USB使用多个摄像头，也可能是笔记本自带摄像头。这个时候，通过id号来读摄像头的图像或者视频，
就要关于摄像头的id号到底对应哪个摄像头。在ubuntu下，我们知道打开笔记本自带摄像头是用茄子命令，即cheese，而查看摄像头的的id号，一般可以通过 ls /dev/video*,
这个命令是将所有摄像头设备都打印出来，比如打印出来有/dev/video0 /dev/video1，说明该电脑识别到两个摄像头，此时假设笔记本内置摄像头是video0,注意未必一定是0，需要测试，
我自己笔记本上外接USB摄像头时，就会出现外接的摄像头是video0.此时如果我们想使用别的摄像头video1呢， cheese —device=/dev/video1，这样就打开了另外一个摄像头了。
当然你也可以通过读摄像头的属性从而读到是第几个摄像头，这个网上有资料，稍微麻烦点。具体windows下，其实差不多，windows下可以通过设备查找。
对于ubuntu下，如果想查找各个相机对应的一些详细属性，可以通过工具v4l-utils，如果系统没有安装，则需要安装一下(sudo apt install v4l-utils
)，然后可以查看系统的相机列表(v4l2-ctl --list-devices)，而后可以查看各个相机的参数,比如分辨率等。(v4l2-ctl --device=/dev/video4 --list-formats-ext
)，v4l2-ctl -d /dev/video0 --list-ctrls曝光增益等。具体可以参考官网：https://www.mankier.com/1/v4l2-ctl


'''
cam_idx = 0
#获取cap
cam_cap = cv2.VideoCapture(cam_idx)#, cv2.CAP_DSHOW)  
#设置width,height。
cam_cap.set(3, 640)
cam_cap.set(4, 480)
# cam_cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# cam_cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

'''
virtual bool cv::VideoCapture::set	(	int 	propId,
double 	value 
)		
virtual
Python:
cv.VideoCapture.set(	propId, value	) ->	retval
set函数的使用，其中propId是VideoCaptureProperties，详细很多，可以看一下官方介绍。常用的有如下几个。
CAP_PROP_POS_MSEC 
Python: cv2.CAP_PROP_POS_MSEC     Current position of the video file in milliseconds. 

CAP_PROP_POS_FRAMES 
Python: cv2.CAP_PROP_POS_FRAMES    0-based index of the frame to be decoded/captured next. 

CAP_PROP_POS_AVI_RATIO 
Python: cv2.CAP_PROP_POS_AVI_RATIO   Relative position of the video file: 0=start of the film, 1=end of the film.

CAP_PROP_FRAME_WIDTH 
Python: cv2.CAP_PROP_FRAME_WIDTH   Width of the frames in the video stream.设置video输出的宽度，这个设置只在此程序中有效，别的程序还是默认值

CAP_PROP_FRAME_HEIGHT 
Python: cv2.CAP_PROP_FRAME_HEIGHT   Height of the frames in the video stream. 设置video输出的高度，这个设置只在此程序中有效，别的程序还是默认值。

CAP_PROP_FPS 
Python: cv2.CAP_PROP_FPS    Frame rate.

CAP_PROP_FOURCC 
Python: cv2.CAP_PROP_FOURCC   4-character code of codec. see VideoWriter::fourcc. 视频写入时需要设置的

CAP_PROP_FRAME_COUNT 
Python: cv2.CAP_PROP_FRAME_COUNT   Number of frames in the video file. 注意这里是视频文件。
'''
'''
有set，就有get获取相应的属性。可以通过id号进行获取，当然也可以通过属性获取。

cv2.VideoCapture.get(0)	CV_CAP_PROP_POS_MSEC 视频文件的当前位置（播放）以毫秒为单位
cv2.VideoCapture.get(1)	CV_CAP_PROP_POS_FRAMES 基于以0开始的被捕获或解码的帧索引
cv2.VideoCapture.get(2)	CV_CAP_PROP_POS_AVI_RATIO 视频文件的相对位置（播放）：0=电影开始，1=影片的结尾。
cv2.VideoCapture.get(3)	CV_CAP_PROP_FRAME_WIDTH 在视频流的帧的宽度
cv2.VideoCapture.get(4)	CV_CAP_PROP_FRAME_HEIGHT 在视频流的帧的高度
cv2.VideoCapture.get(5)	CV_CAP_PROP_FPS 帧速率
cv2.VideoCapture.get(6)	CV_CAP_PROP_FOURCC 编解码的4字-字符代码
cv2.VideoCapture.get(7)	CV_CAP_PROP_FRAME_COUNT 视频文件中的帧数
cv2.VideoCapture.get(8)	CV_CAP_PROP_FORMAT 返回对象的格式
cv2.VideoCapture.get(9)	CV_CAP_PROP_MODE 返回后端特定的值，该值指示当前捕获模式
cv2.VideoCapture.get(10)	CV_CAP_PROP_BRIGHTNESS 图像的亮度(仅适用于照相机)
cv2.VideoCapture.get(11)	CV_CAP_PROP_CONTRAST 图像的对比度(仅适用于照相机)
cv2.VideoCapture.get(12)	CV_CAP_PROP_SATURATION 图像的饱和度(仅适用于照相机)
cv2.VideoCapture.get(13)	CV_CAP_PROP_HUE 色调图像(仅适用于照相机)
cv2.VideoCapture.get(14)	CV_CAP_PROP_GAIN 图像增益(仅适用于照相机)（Gain在摄影中表示白平衡提升）
cv2.VideoCapture.get(15)	CV_CAP_PROP_EXPOSURE 曝光(仅适用于照相机)
cv2.VideoCapture.get(16)	CV_CAP_PROP_CONVERT_RGB 指示是否应将图像转换为RGB布尔标志
cv2.VideoCapture.get(17)	CV_CAP_PROP_WHITE_BALANCE × 暂时不支持
cv2.VideoCapture.get(18)	CV_CAP_PROP_RECTIFICATION 立体摄像机的矫正标注（目前只有DC1394 v.2.x后端支持这个功能）
对应序号可以从opencv官方文件中查看得到。
enum  	cv::VideoCaptureProperties {
  cv::CAP_PROP_POS_MSEC =0,
  cv::CAP_PROP_POS_FRAMES =1,
  cv::CAP_PROP_POS_AVI_RATIO =2,
  cv::CAP_PROP_FRAME_WIDTH =3,
  cv::CAP_PROP_FRAME_HEIGHT =4,
  cv::CAP_PROP_FPS =5,
  cv::CAP_PROP_FOURCC =6,
  cv::CAP_PROP_FRAME_COUNT =7,
  cv::CAP_PROP_FORMAT =8,
  cv::CAP_PROP_MODE =9,
  cv::CAP_PROP_BRIGHTNESS =10,
  cv::CAP_PROP_CONTRAST =11,
  cv::CAP_PROP_SATURATION =12,
  cv::CAP_PROP_HUE =13,
  cv::CAP_PROP_GAIN =14,
  cv::CAP_PROP_EXPOSURE =15,
  cv::CAP_PROP_CONVERT_RGB =16,
  cv::CAP_PROP_WHITE_BALANCE_BLUE_U =17,
  cv::CAP_PROP_RECTIFICATION =18,
  cv::CAP_PROP_MONOCHROME =19,
  cv::CAP_PROP_SHARPNESS =20,
  cv::CAP_PROP_AUTO_EXPOSURE =21,
  cv::CAP_PROP_GAMMA =22,
  cv::CAP_PROP_TEMPERATURE =23,
  cv::CAP_PROP_TRIGGER =24,
  cv::CAP_PROP_TRIGGER_DELAY =25,
  cv::CAP_PROP_WHITE_BALANCE_RED_V =26,
  cv::CAP_PROP_ZOOM =27,
  cv::CAP_PROP_FOCUS =28,
  cv::CAP_PROP_GUID =29,
  cv::CAP_PROP_ISO_SPEED =30,
  cv::CAP_PROP_BACKLIGHT =32,
  cv::CAP_PROP_PAN =33,
  cv::CAP_PROP_TILT =34,
  cv::CAP_PROP_ROLL =35,
  cv::CAP_PROP_IRIS =36,
  cv::CAP_PROP_SETTINGS =37,
  cv::CAP_PROP_BUFFERSIZE =38,
  cv::CAP_PROP_AUTOFOCUS =39,
  cv::CAP_PROP_SAR_NUM =40,
  cv::CAP_PROP_SAR_DEN =41,
  cv::CAP_PROP_BACKEND =42,
  cv::CAP_PROP_CHANNEL =43,
  cv::CAP_PROP_AUTO_WB =44,
  cv::CAP_PROP_WB_TEMPERATURE =45,
  cv::CAP_PROP_CODEC_PIXEL_FORMAT =46,
  cv::CAP_PROP_BITRATE =47,
  cv::CAP_PROP_ORIENTATION_META =48,
  cv::CAP_PROP_ORIENTATION_AUTO =49,
  cv::CAP_PROP_OPEN_TIMEOUT_MSEC =53,
  cv::CAP_PROP_READ_TIMEOUT_MSEC =54
}
    '''
print (cam_cap.get(3)) # 注意返回的是浮点型数据，因此如果你要用这个返回值，注意一下数据类型。

frames = []
while (cam_cap.isOpened()):
    ret, frame = cam_cap.read()    
    if not ret:
        print ('No camera')
        break
    # import pdb 
    # pdb.set_trace()
    print (frame.shape)
    
    frame_copy = frame.copy()    
    cv2.imshow('origin', frame)
    # cv2.waitKey(0)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
    
cam_cap.release()

'''
以上程序是读视频流，直接摄像头读入数据的，如果你要读的是视频文件，那方式也差不多。只是更简单。如果视频文件不存在,ret会返回False.
'''
video_file = 'SampleVideo_1280x720_1mb.mp4'
video_cap = cv2.VideoCapture(video_file)
print ('video file width',video_cap.get(3))
print ('video file height',video_cap.get(4))
print ('video file fps',video_cap.get(cv2.CAP_PROP_FPS)) # 注意这些属性在python下使用时，没有CV_,而C++中有的。
print ('video file totoal frames.',video_cap.get(cv2.CAP_PROP_FRAME_COUNT))
'''
video file width 1280.0
video file height 720.0
video file fps 25.0
video file totoal frames. 132.0
'''
while True:
    ret, frame = video_cap.read()
    if not ret:
        break    

    cv2.imshow('video file frame',frame)
    cv2.waitKey(25)


video_cap.release()

'''
以上都是单视频读，如果想多个视频同时读，可以使用多进程的方式。具体可参考另外一个程序.
'''