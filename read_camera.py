
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
'''
cam_idx = 0
cam_cap = cv2.VideoCapture(cam_idx)#, cv2.CAP_DSHOW)  

cam_cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam_cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cam_calib = {'mtx': np.eye(3), 'dist': np.zeros((1, 5))}

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
pts = np.zeros((6 * 4, 3), np.float32)  #棋盘格尺寸6*4，下面相关地方都要修改
pts[:, :2] = np.mgrid[0:6, 0:4].T.reshape(-1, 2)  #棋盘格尺寸有关0:6, 0:4

# capture calibration frames
obj_points = []  # 3d point in real world space
img_points = []  # 2d points in image plane.
frames = []
while True:
    ret, frame = cam_cap.read()
    if not ret:
        print ('No camera')
        break

    frame_copy = frame.copy()
    # cv2.imshow('origin', frame)
    # cv2.waitKey(10)
    corners = []
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        retc, corners = cv2.findChessboardCorners(gray, (6, 4), None)
        print (corners)
        if retc:
            cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria) # 11,11是啥东西？
                # Draw and display the corners
            cv2.drawChessboardCorners(frame_copy, (6, 4), corners, ret)

            cv2.imshow('points', frame_copy)
                # s to save, c to continue, q to quit
            key = cv2.waitKey(0)
            # if cv2.waitKey(0) & 0xFF == ord('s'):
            if key == ord('s'):
                img_points.append(corners)
                obj_points.append(pts)
                frames.append(frame)
            # elif cv2.waitKey(0) & 0xFF == ord('c'):
            elif key == ord('c'):
                print('continue------')
                continue
            # elif cv2.waitKey(0) & 0xFF == ord('q'):
            elif key == ord('q'):
                print("Calibrating camera...")
                cv2.destroyAllWindows()
                break
if len(obj_points)==0:
    exit()

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, frames[0].shape[0:2], None, None)

    # check
error = 0.0
for i in range(len(frames)):
    proj_imgpoints, _ = cv2.projectPoints(obj_points[i], rvecs[i], tvecs[i], mtx, dist)
    error += (cv2.norm(img_points[i], proj_imgpoints, cv2.NORM_L2) / len(proj_imgpoints))
print("Camera calibrated successfully, total re-projection error: %f" % (error / len(frames)))

cam_calib['mtx'] = mtx
cam_calib['dist'] = dist
print("Camera parameters:")
print(cam_calib)

pickle.dump(cam_calib, open("calib_cam%d.pkl" % (cam_idx), "wb"))


