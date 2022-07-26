# -*- coding: utf-8 -*-

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
