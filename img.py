# -*- coding: utf-8 -*-

# In[]
def fun(a,b,*args):
    res = a+b
    for arg in args:
        res = res + arg
    return res

a = 1
b = 0
alst = [2,3,4,5]
blst = *alst
print (fun(a,b, *alst))

# In[]

