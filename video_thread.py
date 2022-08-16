import numpy as np
import cv2
import threading
from copy import deepcopy

thread_lock = threading.Lock()
thread_exit = False
indx = 0
class myThread(threading.Thread):
    def __init__(self, video_file, img_height, img_width):
        super(myThread, self).__init__()
        self.video_file = video_file
        self.img_height = img_height
        self.img_width = img_width
        self.frame = np.zeros((img_height, img_width, 3), dtype=np.uint8)

    def get_frame(self):        
        return deepcopy(self.frame)

    def run(self):
        global indx
        global thread_exit
        cap = cv2.VideoCapture(self.video_file)
        while not thread_exit:
            ret, frame = cap.read()            
            if ret:
                indx = indx +1
                frame = cv2.resize(frame, (self.img_width, self.img_height))
                thread_lock.acquire()
                self.frame = frame
                print (indx )
                cv2.imwrite('./results/file'+str(indx)+'.jpg',self.frame)
                thread_lock.release()
            else:
                thread_exit = True
        cap.release()

def main():
    global thread_exit
    video_file =  r'D:\\data\\WIN_20220701_15_23_22_Pro.mp4' #'SampleVideo_1280x720_1mb.mp4'
    img_height = 720
    img_width = 1280
    thread = myThread(video_file, img_height, img_width)
    thread.start()

    while not thread_exit:
        thread_lock.acquire()
        frame = thread.get_frame()
        thread_lock.release()

        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            thread_exit = True
    thread.join()

if __name__ == "__main__":
    main()
