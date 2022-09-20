#!/usr/bin/env python3

# --------------------------------------------------------
# All the codes refers to a lot of materials from webs and other works.
# --------------------------------------------------------

from subprocess import call
import cv2
import numpy as np
from os import path
import pickle 

def cam_calibrate(cam_idx, cap, cam_calib):

    # termination criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    # here we use chessboard with size 6x4 and the distance between two corners are 21mm but here we do not use it.
    pts = np.zeros((6 * 4, 3), np.float32)
    pts[:, :2] = np.mgrid[0:6, 0:4].T.reshape(-1, 2)#*

    # capture calibration frames
    obj_points = []  # 3d point in real world space
    img_points = []  # 2d points in image plane.
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            print ('No images.')
            return 

        frame_copy = frame.copy()
        cv2.imshow('image', frame)
        cv2.waitKey(0)

        corners = []
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            retc, corners = cv2.findChessboardCorners(gray, (6, 4), None) # 6x4 chessboard, if your chessboard is not 6x4, please change it freely, may be 9x6 or others.
            if retc:
                cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria) # (11,11)亚像素角点检测窗口大小,不需要太精确可删除
                # Draw and display the corners
                cv2.drawChessboardCorners(frame_copy, (6, 4), corners, ret)
               
                cv2.imshow('points', frame_copy)
                # s to save, c to continue, q to quit
                if cv2.waitKey(0) & 0xFF == ord('s'):
                    img_points.append(corners)
                    obj_points.append(pts)
                    frames.append(frame)
                elif cv2.waitKey(0) & 0xFF == ord('c'):
                    continue
                elif cv2.waitKey(0) & 0xFF == ord('q'):
                    print("Calibrating camera...")
                    cv2.destroyAllWindows()
                    break

    # compute calibration matrices

    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, frames[0].shape[0:2], None, None)

    # check the error after calibration, according to the projectpoints. proj_imgpoints is the prediction results on image after calibration,
    # they should be very near to img_points and the error should be very little may be far smaller than 1.
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


#################################
# Start camera
#################################

cam_idx = 0

cam_cap = cv2.VideoCapture(cam_idx)
cam_cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam_cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# calibrate camera
cam_calib = {'mtx': np.eye(3), 'dist': np.zeros((1, 5))}
print("Calibrate camera once. Print pattern.png, paste on a clipboard, show to camera and capture non-blurry images in which points are detected well.")
print("Press s to save frame and the frame will be used in the future to do calibration, c to continue to next frame and q to quit collecting data and proceed to calibration.")
cam_calibrate(cam_idx, cam_cap, cam_calib)
cam_cap.release()