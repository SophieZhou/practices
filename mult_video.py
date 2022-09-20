# -*- coding: utf-8 -*

import operator
import csv
import time
import os
from time import ctime
from multiprocessing import Process
import cv2 
 
'''
当你有多个视频文件需要同时处理时，可以试着采用并行的形式进行，会大大提升工作效率。以下只是一个简单的示例，我只是简单地把视频都进来然后用图像形式保存了
下来，实际应用中根据需要修改。这里的cv2.imwrite，我们再单独找时间进行讲解。其中多进程并行的使用，可以参考python的相关教程。也有多线程的读视频，程序也有，但是
我感觉没有进程更明了。
'''

def read_video(video_file):
    cap = cv2.VideoCapture(video_file)
    idx = 0
    while True :
        ret, frame = cap.read()    
        if not ret:
            break         
        if ret:
            idx  = idx +1
            prefix = os.path.basename(video_file).split('.')[0]
            if idx%20==0:
                cv2.imwrite('./results/file'+prefix+str(idx)+'.jpg',frame) 
              
    cap.release()

def video_process():
    file_lists = os.listdir(r'D:\data')
    print (file_lists)

    processes = []
    for file in file_lists:
        processes.append(Process(target=read_video, args=(os.path.join(r'D:\data\\',file),)))

    for process in processes:
        process.start()

    for process in processes:  
        process.join()


if __name__=='__main__':
    video_process() 