import cv2
import numpy as np

#定义全局变量
n = 0#定义鼠标按下的次数
ix = 0# x,y 坐标的临时存储
iy = 0

#鼠标回调函数
def draw_rectangle(event,x,y,flags,param):
    global n,ix,iy
    if event==cv2.EVENT_LBUTTONDOWN :
        if n == 0:#首次按下保存坐标值
            n+=1
            ix,iy = x,y
            cv2.circle(img,(x,y),2,(255,255,255),-1)#第一次打点
        else:#第二次按下显示矩形
            n = 0
            cv2.rectangle(img,(ix,iy),(x,y),(255,255,255),3)#第二次画矩形



# 创建图像与窗口并将窗口与回调函数绑定
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_rectangle)

#显示并延时
while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20)&0xFF==27:
        break
#销毁所有窗口
cv2.destroyAllWindows()

res = tuple([1,2])
print (res)