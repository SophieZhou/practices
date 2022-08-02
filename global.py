# -*- coding: utf-8 -*-
def add(x,y):
    if x>y:
        res = x+y
    else:
        res =  x-y
    # global  a 
    # a +=1
    print (a)
    return res 

for i in range(10):
    x = i
    y = 0
    a = i 
    res = add(x,y)
    # print (res)

mylist = iter(["apple", "banana", "cherry"])
x = next(mylist, "orange")
print(x)
x = next(mylist, "orange")
print(x)
x = next(mylist, "orange")
print(x)
x = next(mylist, "orange")
print(x)