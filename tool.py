# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# In[]
print ('ceshi')
print ('bst')

# In[]
def fun(a,b,**kwargs):
    print(a)
    print (len(kwargs))
    name = {}
    for k,v in kwargs.items():
        if 'name' in k:
            name = v
    print (name)
dict_param = dict(class_names=['a','b','c'],value=['0.5','0.5','0.5'])

fun(1,2,**dict_param)



# In[]
test_str = 'testabc'
print (test_str.find('t'))
import os 
filename = 'E:\\bst_code\\temp.py'
assert(os.path.isfile(filename))

# In[]
import cv2
import numpy as np

img = cv2.imread("cards.jpg")

width,height = 250,350  #所需图像大小

#找K
pts1 = np.float32([[657,184],[812,222],[604,586],[997,627]])  #所需图像部分四个顶点的像素点坐标
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]]) #定义对应的像素点坐标
matrix_K = cv2.getPerspectiveTransform(pts1,pts2)  #使用getPerspectiveTransform()得到转换矩阵
img_K = cv2.warpPerspective(img,matrix_K,(width,height))  #使用warpPerspective()进行透视变换

#找Q
pts3 = np.float32([[63,325],[340,279],[89,634],[403,573]])
pts4 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix_Q = cv2.getPerspectiveTransform(pts3,pts4)
img_Q = cv2.warpPerspective(img,matrix_Q,(width,height))

#找J
pts5 = np.float32([[777,107],[1019,84],[842,359],[1117,332]])
pts6 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix_J = cv2.getPerspectiveTransform(pts5,pts6)
img_J = cv2.warpPerspective(img,matrix_J,(width,height))

cv2.imshow("Original Image",img)
cv2.imshow("img K",img_K)
cv2.imshow("img Q",img_Q)
# cv2.imshow("img J",img_J)

cv2.waitKey(0)
cv2.destroyAllWindows()
# In[]

import numpy as np

test = np.array([[1,2,3],[4,5,6]])
print (test[1,2])
print (test[1][2])


# In[]
import numpy as np

help(np.argmax)

# In[]


import cv2
import numpy as np
import glob
 
# 设置寻找亚像素角点的参数，采用的停止准则是最大循环次数30和最大误差容限0.001
criteria = (cv2.TERM_CRITERIA_MAX_ITER | cv2.TERM_CRITERIA_EPS, 30, 0.001)
 
# 获取标定板角点的位置
objp = np.zeros((4 * 6, 3), np.float32)
objp[:, :2] = np.mgrid[0:6, 0:4].T.reshape(-1, 2)  # 将世界坐标系建在标定板上，所有点的Z坐标全部为0，所以只需要赋值x和y
 
obj_points = []  # 存储3D点
img_points = []  # 存储2D点
 
images = glob.glob("image4/*.jpg")
i=0;
for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    size = gray.shape[::-1]
    ret, corners = cv2.findChessboardCorners(gray, (6, 4), None)
    #print(corners)
 
    if ret:
 
        obj_points.append(objp)
 
        corners2 = cv2.cornerSubPix(gray, corners, (5, 5), (-1, -1), criteria)  # 在原角点的基础上寻找亚像素角点
        #print(corners2)
        if [corners2]:
            img_points.append(corners2)
        else:
            img_points.append(corners)
 
        cv2.drawChessboardCorners(img, (6, 4), corners, ret)  # 记住，OpenCV的绘制函数一般无返回值
        i+=1;
        cv2.imwrite('conimg'+str(i)+'.jpg', img)
        cv2.waitKey(1500)
 
print(len(img_points))
cv2.destroyAllWindows()
 
# 标定
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, size, None, None)
 
print("ret:", ret)
print("mtx:\n", mtx) # 内参数矩阵
print("dist:\n", dist)  # 畸变系数   distortion cofficients = (k_1,k_2,p_1,p_2,k_3)
print("rvecs:\n", rvecs)  # 旋转向量  # 外参数
print("tvecs:\n", tvecs ) # 平移向量  # 外参数
 
print("-----------------------------------------------------")
 
img = cv2.imread(images[2])
h, w = img.shape[:2]
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))#显示更大范围的图片（正常重映射之后会删掉一部分图像）
print (newcameramtx)
print("------------------使用undistort函数-------------------")
dst = cv2.undistort(img,mtx,dist,None,newcameramtx)
x,y,w,h = roi
dst1 = dst[y:y+h,x:x+w]
cv2.imwrite('calibresult3.jpg', dst1)
print ("方法一:dst的大小为:", dst1.shape)



# In[]
 # Crop image, forward to get the param
param_lst = []
roi_box_lst = []
 
crop_policy = kvs.get('crop_policy', 'box')
for obj in objs:
    if crop_policy == 'box':
                # by face box
        roi_box = parse_roi_box_from_bbox(obj)
    elif crop_policy == 'landmark':
                # by landmarks
        roi_box = parse_roi_box_from_landmark(obj)
    else:
        raise ValueError(f'Unknown crop policy {crop_policy}')
 
    roi_box_lst.append(roi_box)
    img = crop_img(img_ori, roi_box)
    img = cv2.resize(img, dsize=(self.size, self.size), interpolation=cv2.INTER_LINEAR)
    inp = self.transform(img).unsqueeze(0)
    if self.gpu_mode:
        inp = inp.cuda(device=self.gpu_id)
        if kvs.get('timer_flag', False):
            end = time.time()
            param = self.model(inp)
            elapse = f'Inference: {(time.time() - end) * 1000:.1f}ms'
            print(elapse)
        else:
            param = self.model(inp)
 
        param = param.squeeze().cpu().numpy().flatten().astype(np.float32)
        param = param * self.param_std + self.param_mean  # re-scale
            # print('output', param)
        param_lst.append(param)
 
# In[]

def P2sRt(P):
    """ decompositing camera matrix P.
    Args:
        P: (3, 4). Affine Camera Matrix.
    Returns:
        s: scale factor.
        R: (3, 3). rotation matrix.
        t2d: (2,). 2d translation.
    """
    t3d = P[:, 3]
    R1 = P[0:1, :3]
    R2 = P[1:2, :3]
    s = (np.linalg.norm(R1) + np.linalg.norm(R2)) / 2.0
    r1 = R1 / np.linalg.norm(R1)
    r2 = R2 / np.linalg.norm(R2)
    r3 = np.cross(r1, r2)
 
    R = np.concatenate((r1, r2, r3), 0)
    return s, R, t3d
 
 
def matrix2angle(R):
    """ compute three Euler angles from a Rotation Matrix. Ref: http://www.gregslabaugh.net/publications/euler.pdf
    refined by: https://stackoverflow.com/questions/43364900/rotation-matrix-to-euler-angles-with-opencv
    todo: check and debug
     Args:
         R: (3,3). rotation matrix
     Returns:
         x: yaw
         y: pitch
         z: roll
     """
    if R[2, 0] > 0.998:
        z = 0
        x = np.pi / 2
        y = z + atan2(-R[0, 1], -R[0, 2])
    elif R[2, 0] < -0.998:
        z = 0
        x = -np.pi / 2
        y = -z + atan2(R[0, 1], R[0, 2])
    else:
        x = asin(R[2, 0])
        y = atan2(R[2, 1] / cos(x), R[2, 2] / cos(x))
        z = atan2(R[1, 0] / cos(x), R[0, 0] / cos(x))
 
    return x, y, z
 
 
def calc_pose(param):
    P = param[:12].reshape(3, -1)  # camera matrix
    s, R, t3d = P2sRt(P)
    P = np.concatenate((R, t3d.reshape(3, -1)), axis=1)  # without scale
    pose = matrix2angle(R)
    pose = [p * 180 / np.pi for p in pose]
 
    return P, pose

# In[]
import numpy as np
test = np.array([[1,2,3],[4,5,6]])
print (test[:,::-1])  # 





# In[]

filedir = 'E:\\bst\gaze\\test\gaze.pptx'

print (filedir)

# In[]

import cv2
import numpy as np

img = cv2.imread("cards.jpg")
print (img.shape)
img2 = np.transpose(img,[2,0,1])
print (img2.shape)


# In[]
import numpy as np

tmp = np.array([[1,2],[2,3]])
print (tmp)
print (tmp[:,0])

# In[]
height = 1.60
weight = 50
bmi = weight/(height*height)
print (bmi)
# In[]

from timeit import timeit 
def with_for():
    lst = []
    for i in range(100):
        lst.append(i)
    return lst 

def without_for():
    return (i for i in range(100))

print (f'with:{timeit(with_for, number=10000)}')
print (f'without:{timeit(without_for, number=10000)}')

# In[]
a = 10
print (a)