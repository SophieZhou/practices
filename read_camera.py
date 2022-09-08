
import time
import cv2
import numpy as np
from os import path
import pickle

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


