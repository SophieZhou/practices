import time
import multiprocessing as mp
import threading
import cv2
from PIL import Image
import base64
import json
from io import BytesIO
import numpy as np
import requests

"""
Source: Yonv1943 2018-06-17
https://github.com/Yonv1943/Python
https://zhuanlan.zhihu.com/p/38136322
OpenCV official demo
https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
海康、大华IpCamera RTSP地址和格式（原创，旧版）- 2014年08月12日 23:01:18 xiejiashu
rtsp_path_hikvison = "rtsp://%s:%s@%s/h265/ch%s/main/av_stream" % (user, pwd, ip, channel)
rtsp_path_dahua = "rtsp://%s:%s@%s/cam/realmonitor?channel=%d&subtype=0" % (user, pwd, ip, channel)
https://blog.csdn.net/xiejiashu/article/details/38523437
最新（2017）海康摄像机、NVR、流媒体服务器、回放取流RTSP地址规则说明 - 2017年05月13日 10:51:46 xiejiashu
rtsp_path_hikvison = "rtsp://%s:%s@%s//Streaming/Channels/%d" % (user, pwd, ip, channel)
https://blog.csdn.net/xiejiashu/article/details/71786187
"""
indx = 0
def image_put(q, rtsp):
    global indx 
    ret, cap = cv2.VideoCapture(rtsp)
    while True:
        q.put(cap.read()[1])
        indx += 1
        q.get() if q.qsize() > 1 else time.sleep(0.01)


def image_get(q, window_name):
    cv2.namedWindow(window_name, flags=cv2.WINDOW_FREERATIO)
    while True:
        frame = q.get()
        frame = process(frame)
        # put_rtmp(frame, p)
        # cv2.imshow(window_name, frame)
        # cv2.waitKey(1)

def process(frame):
    # frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    img = Image.fromarray(frame)
    # output_buffer = BytesIO()  # 创建一个BytesIO
    cv2.imwrite('./results/file'+str(indx)+'.jpg',img)  # 写入output_buffer    
    # cv2.imshow("thread", img)


    return img



def run_single_camera(rtsp):
    # user_name, user_pwd, camera_ip = "admin", "admin123456", "[fe80::3aaf:29ff:fed3:d260]"
    #
    # mp.set_start_method(method='spawn')  # init
    # queue = mp.Queue(maxsize=2)
    # processes = [mp.Process(target=image_put, args=(queue, user_name, user_pwd, camera_ip)),
    #              mp.Process(target=image_get, args=(queue, camera_ip))]
    #
    # [process.start() for process in processes]
    # [process.join() for process in processes]

    user_name, user_pwd, camera_ip = "admin", "admin123456", "[fe80::3aaf:29ff:fed3:d260]"

    mp.set_start_method(method='spawn')  # init
    queue = mp.Queue(maxsize=2)
    threads = [threading.Thread(target=image_put, args=(queue, rtsp)),
                 threading.Thread(target=image_get, args=(queue, 'fire'))]

    [thread.start() for thread in threads]

def run(rtsp):
    run_single_camera(rtsp)  # quick, with 2 threads
    pass


if __name__ == '__main__':
    # rtsp = "rtsp://admin:a1234567@192.168.20.87:554/h264/ch1/main/av_stream"
    import sys
    rtsp = r'D:\\data\\WIN_20220701_15_23_22_Pro.mp4' #sys.argv[1]
    run(rtsp)

