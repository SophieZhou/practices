# -*- coding: utf-8 -*

import operator
import csv
import time
import os
import threading
from time import ctime
from multiprocessing import Process
import cv2 
# thread_lock = threading.Lock()
# thread_exit = False

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