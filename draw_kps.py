import cv2
import numpy as np
 
 
def SIFT(img):
    I = cv2.imread(img)
    descriptor = cv2.xfeatures2d.SIFT_create()  # 在2004年，不列颠哥伦比亚大学的D.Lowe在他的论文中提出了一种新的算法，即尺度不变特征变换（SIFT）
    (kps, features) = descriptor.detectAndCompute(I, None)
    cv2.drawKeypoints(I, kps, I, (0, 255, 255), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow('img', I)
    cv2.waitKey(0)
    cv2.imwrite('sift_keypoints.jpg', I)
    cv2.destroyAllWindows()
 
 
if __name__ == '__main__':
    SIFT('left.png')