# -*- coding: utf-8 -*-
# In[]
#https://pep8.org/
# In[]
# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# More indentation included to distinguish this from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Hanging indents should add a level.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)

# In[]
# 79 characters
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
help(zip)
# In[]
alst = [1,2,3]
blst = [4,5,6]
clst = [4,5,6,7,8]
zipped = zip(alst,blst)     # 打包为元组的列表
for z in zipped:
    print (z)
# In[]    
unziped = zip(*zipped)
print ((unziped))
for u in unziped:
    print (u)
# In[]
for a,b in zip(alst,blst):
    print (a,b)

for a,c in zip(alst,clst):
    print (a,c)

for c,a in zip(clst,alst):
    print (c,a)

# In[]
# f-string 
import datetime
name = 'Fred'
age = 50
anniversary = datetime.date(1991, 10, 12)
print (f'My name is {name}, my age next year is {age+1}, my anniversary is {anniversary:%A, %B %d, %Y}.')
print (f'He said his name is {name!r}.')

# In[]
# f-string用大括号 {} 表示被替换字段，其中直接填入替换内容：
# >>> 
name = 'Eric'
print (f'Hello, my name is {name}')
number = 7
print (f'My lucky number is {number}')

price = 19.99
print (f'The price of this book is {price}')

# In[]
# 表达式求值与函数调用
#f-string的大括号 {} 可以填入表达式或调用函数，Python会求出其结果并填入返回的字符串内：
print (f'A total number of {24 * 8 + 4}')
print (f'Complex number {(2 + 2j) / (2 - 3j)}')
name = 'ERIC'
print (f'My name is {name.lower()}')
import math
print (f'The answer is {math.log(math.pi)}')

# In[]
# f-string大括号外如果需要显示大括号，则应输入连续两个大括号 {{ 和 }}：
print (f'5 {"{stars}"}')

# In[]
print (f"Hello!" \
    f"I'm {name}." \
    f"I'm {age}."
"Hello!I'm Eric.I'm 27.")

# In[]
print (f"""Hello!
... I'm {name}.
... I'm {age}.""")

# In[]
a = 123.456
print (f'a is {a:6.2f}')
print (f'a is {a:8.2f}')
print (f'a is {a:6.0f}')
print (f'a is {a:.0f}')
b = 1000
print (f'b is {b:6}')
print (f'b is {b:8}')

# In[]
# 自定义格式：对齐、宽度、符号、补零、精度、进制等
#f-string采用 {content:format} 设置字符串格式，其中 content 是替换并填入字符串的内容，
#可以是变量、表达式或函数等，format是格式描述符。
#采用默认格式时不必指定 {:format}，如上面例子所示只写 {content} 即可。

# In[]
alst = [1,2,3,4]
def fun(alst,i,j):
    tmp = alst[j] 
    alst[j] = alst[i]
    alst[i] = tmp 
    i = j 

i = 1
fun(alst,i,0)
print (alst )

# https://pythontutor.com/render.html#mode=display

# In[]
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017261630425888

test_dict = {1:5, 2:4, 3:3, 4:2, 5:1}
print ({k:v for k, v in test_dict.items() if v >=3})

# In[]
# os error  unable to lock file  no locks available

# 这一问题通常是由于在 NFS 文件系统中的问题，
# 直接在 ~/.bashrc 文件中加入
export HDF5_USE_FILE_LOCKING=FALSE
# 然后 
source ~/.bashrc

# In[]
