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