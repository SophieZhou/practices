'''
前面讲过读camera，以及读video，这次说一下如何把图像写入视频文件。
在opencv中，视频文件的写入，其实是一帧图像一帧图像进行的，因此视频流的fps和大小都需要你自己定义。
同时一个视频中，必须所有图像大小都是一样的，不可以有不同图像，或者说在写入前，你必须把所有图像resize到同一个尺寸然后才能写入到视频文件中。
'''

import cv2 
fps = 10
size = (640,480) # width,height
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
videofile = 'tmp.mp4'
VideoWriter = cv2.VideoWriter(videofile, fourcc,fps,size )

# 将文件夹中的图像保存为一个video或者将视频文件从新输出保存为一个video.
while True:
    img = cv2.imread(filepath)
    VideoWriter.write(img)

VideoWriter.release()
cv2.destroyAllWindows()