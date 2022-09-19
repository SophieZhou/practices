import cv2
import numpy as np

#定义全局变量
n = 0#定义鼠标按下的次数
ix = 0# x,y 坐标的临时存储
iy = 0

#鼠标回调函数
def click_cicle(event,x,y,flags,param):
    global n,ix,iy
    if event==cv2.EVENT_LBUTTONUP :
        file_dir = 'D:/data/images/'
        #the pos clicking. 
        # cv2.circle(img,(x,y),2,(255,255,255),-1)
        cv2.imwrite(file_dir+str(n)+'.jpg',img)
        n=n+1


cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    img_copy = img.copy()
    # img=np.zeros((512,512,3),np.uint8)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image',click_cicle)
    
    cv2.imshow('image',img)
    key = cv2.waitKey(1)
    if key  & 0xFF==27:
        break
 
    
#销毁所有窗口
cv2.destroyAllWindows()
    