# -*- coding: utf-8 -*-
import argparse
# # 1、创建 ArgumentParser() 对象
# #
# # 2、调用 add_argument() 方法添加参数
# #
# # 3、使用 parse_args() 解析添加的参数
parser = argparse.ArgumentParser()

parser.add_argument("--square", help="display a square of a given number", type=int)
parser.add_argument("--cubic", help="display a cubic of a given number", type=int)
parser.add_argument("--test-hand", help="display a hand of a given number", type=int)
#from:https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument 
# Any internal - characters will be converted to _ characters to make sure the string is a valid attribute name. 

args = parser.parse_args()

if args.square:
    print(args.square ** 2)
if args.cubic:
    print(args.cubic ** 3)

if args.test_hand:
    print ('no different')

# In[]
import random
print (random.randint(3,5))
# In[]
import random

# 随机数不一样
random.seed()
print('随机数1：',random.random())
random.seed()
print('随机数2：',random.random())

# 随机数一样
random.seed(1)
print('随机数3：',random.random())
random.seed(1)
print('随机数4：',random.random())
random.seed(2)
print('随机数5：',random.random())

'''
随机数1： 0.7643602170615428
随机数2： 0.31630323818329664
随机数3： 0.13436424411240122
随机数4： 0.13436424411240122
随机数5： 0.9560342718892494
'''
# In[]
import numpy as np

box=np.array([0,1,2,3])
center = (box[0:2]+box[2:4])/2
print (center)
