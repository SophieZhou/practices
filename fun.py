# -*- coding: utf-8 -*-

# In[]
# static analysis tool,mypy 
def add(a:int,b:int)->int:
    return a+b
print (add(1,2))
print (add('s',2))

# In[]
def fun():
    print ('Hello world.')
res = fun()
print (res )

# In[]
def fun(a,b):
    res = a+b
    return res 
a =1
b = 1
res = fun(a,b)
print (res )

# In[]
def fun(a,b,*args):
    total = a+b
    n = 2
    for arg in args:
        total = total + arg 
        n  = n+1
    avg = total/n
    return total,avg
a = 0
b = 1
total, avg = fun(a,b, 2,3,4,5 ) # 
print (total)
print (avg )
# In[]
def fun(a,b):
    if a >b:
        return a 
    else :
        return b 

a = 1
b =2
res = fun(a,b)
print (res)    
# In[]
'''
variable length arguments in Python
在列表/tuple/array……前加*号，会将列表等拆分成一个一个的独立元素
'''
def fun(a,b,*args):
    res = a+b
    for arg in args:
        res = res + arg
    return res

a = 1
b = 0
alst = [2,3,4,5]
print (alst)
print (*alst)
print (fun(a,b, *alst))

# In[]
'''
dict==>(k,w)
'''
def add_dict(a,b,**kwargs):
    res = a + b
    for k in kwargs:
        res += kwargs[k]
    return res 

a = 0
b = 1
kwdict = {'k1':2,'k2':3,'k3':4,'k4':5}
print (add_dict(a,b,**kwdict))
# In[]
'''
kwargs must be after args
'''
def plus_all(a,b,*args,**kwargs):
    res = a+b
    for arg in args:
        res += arg
    for k in kwargs:
        res += kwargs[k]
    return res

a = 0
b = 1
alst = [2,3,4,5]
kwdict = {'k1':6,'k2':7,'k3':8,'k4':9}

print (plus_all(a,b,*alst,**kwdict))

# In[]
import os 
help(os.makedirs)

help (os.mkdir)

help(os.path.exists)
# In[]
import os 
dirpath = 'E:\python\code'
if not os.path.exists(dirpath):
    os.makedirs(dirpath) 

# In[]
import sys
sys.path.append('E:\python\code')
print (sys.path)

# In[]
import random
help (random.randint)
# In[]
import random 
i = random.randint(0,10)
print (i)
# In[]
import random
help (random.uniform)
u = random.uniform(0,1)
print (u)

# In[]
import random 
print (dir(random))

# In[]
help (random.betavariate)

# In[]
import random
help (random.choices)
# In[]
import random
print(random.choice('choice')) 

# In[]
import random
a = [1,2,3,4,5]
print(random.choices(a,k=6))
print(random.choices(a,weights=[0,0,1,0,0],k=6))
print(random.choices(a,weights=[1,1,1,1,1],k=6))
print(random.choices(a,cum_weights=[1,1,1,1,1],k=6))

# In[]
# module
# import modulename     # modulename.method/variable 
# from modulename import method   # you can just visit the method 
# from modulename import *  # you can visit all from modulename, but it is not recommended.
# In[]
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 12:36:49 2022

@author: Administrator
"""

# In[]

# In[]
alst = [1,2,3]
blst = [4,5,6]
clst = [4,5,6,7,8]

zipped = zip(alst,blst)     # 打包为元组的列表

for z in zipped:
    print (z)

# In[]
for a,b in zip(alst,blst):
    print (a,b)

for a,c in zip(alst,clst):
    print (a,c)

for c,a in zip(clst,alst):
    print (c,a)
    
    
# In[]
    
def square(x):
    return x ** 2
 
# 计算列表各个元素的平方
map(square, [1,2,3,4,5]) # <map at 0x17206b29630>
# 使用list()转换为列表
list(map(square, [1,2,3,4,5])) # [1, 4, 9, 16, 25]
# 使用lambda匿名函数
list(map(lambda x: x ** 2, [1, 2, 3, 4, 5])) # [1, 4, 9, 16, 25]

# In[]
'''
read txt 
'''
filename = ''
with open(filename,'r') as fn:
    lines = fn.readlines()
for line in lines:
    print (line )
# In[]
'''
read csv
'''
import csv
 
filename='test.csv'
data = []
with open(filename) as csvfile:
    csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
    #header = next(csv_reader)        # 读取第一行每一列的标题
    for row in csv_reader:            # 将csv 文件中的数据保存到data中
        data.append(row[0])           # 选择某一列加入到data数组中
    print(data)

# In[]
'''
read xlsx   the code can not run
'''
import xlrd
#打开excel
wb = xlrd.open_workbook('test.xlsx')
#按工作簿定位工作表
sh = wb.sheet_by_name('本科')
print(sh.nrows)#有效数据行数
print(sh.ncols)#有效数据列数
print(sh.cell(0,0).value)#输出第一行第一列的值
print(sh.row_values(0))#输出第一行的所有值
#将数据和标题组合成字典
print(dict(zip(sh.row_values(0),sh.row_values(1))))
#遍历excel，打印所有数据
for i in range(sh.nrows):
    print(sh.row_values(i))

# In[]
