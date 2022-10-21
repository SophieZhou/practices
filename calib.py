# -*- coding:utf-8 -*-
import cv2
import numpy as np
 
 
class Chessboard:
    def __init__(self):
        # 背景颜色
        self.background_color = [255, 255, 255]
        # 棋盘颜色
        self.foreground_color = [0, 0, 0]
        # 每个棋盘格占像素个数
        self.block_size_pixel = 8
 
    def gen_chessboard_image(self, pattern_size_hw):
 
        height, width = pattern_size_hw
        # 图像大小
        image_height = self.block_size_pixel * (height + 1)
        image_width = self.block_size_pixel * (width + 1)
        # 生成图像
        image = np.zeros((image_height, image_width, 3), dtype=np.uint8)
 
        image[:] = self.background_color
        if self.block_size_pixel != 0 and 0 not in pattern_size_hw:
            for j in range(height + 1):
                for i in range(width + 1):
                    if (i + j) % 2 != 0:
                        x1 = i * self.block_size_pixel
                        x2 = (i + 1) * self.block_size_pixel
                        y1 = j * self.block_size_pixel
                        y2 = (j + 1) * self.block_size_pixel
                        image[y1: y2, x1: x2, :] = self.foreground_color
        return image
 
 
if __name__ == '__main__':
    calibration_board = Chessboard()
    board_pic = calibration_board.gen_chessboard_image(pattern_size_hw=[4, 6])
 
    cv2.namedWindow('cb', 0)
    cv2.imshow('cb', board_pic)
    cv2.waitKey()