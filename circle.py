import numpy as np
import cv2
img = np.zeros((200,200,3),dtype=np.uint8)
# cv2.circle(img,(60,60),60,(0,0,255))
# cv2.imshow('img',img)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
# if cv2.waitKey(0) & 0xFF == ord('q'):
#     print ('test.')
#     cv2.destroyAllWindows()
# else:
#     print('just jump.')

# import matplotlib.pyplot as plt
# # load image using cv2....and do processing.
# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# # as opencv loads in BGR format by default, we want to show it in RGB.
# plt.show()
cv2.circle(img,(80,80),30,(0,0,255),-1)
# cv2.imshow('img',img)
# cv2.waitKey(1)
import random 
rc = random.randint(1,30)
for i in range(rc,1,-1):    
    cv2.circle(img,(80,80),i,(0,0,255),-1)
    cv2.imshow('img',img)
    cv2.waitKey(rc*10)

cv2.imshow('img',img)
cv2.waitKey(0)