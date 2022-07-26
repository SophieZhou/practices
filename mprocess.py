# -*- coding: utf-8 -*-
# In[]
'''
数据并行
'''
from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))

# In[]
'''
多进程
'''
from multiprocessing import Process

def f(name):
    print('hello', name)

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()

# In[]
from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()

# In[]
'''
在 Unix 上通过 spawn 和 forkserver 方式启动多进程会同时启动一个 资源追踪 进程，
负责追踪当前程序的进程产生的、并且不再被使用的命名系统资源(如命名信号量以及 SharedMemory 对象)。
当所有进程退出后，资源追踪会负责释放这些仍被追踪的的对象。通常情况下是不会有这种对象的，
但是假如一个子进程被某个信号杀死，就可能存在这一类资源的“泄露”情况。
（泄露的信号量以及共享内存不会被释放，直到下一次系统重启，对于这两类资源来说，
这是一个比较大的问题，
因为操作系统允许的命名信号量的数量是有限的，而共享内存也会占据主内存的一片空间）.
要选择一个启动方法，你应该在主模块的 if __name__ == '__main__' 子句中调用 set_start_method() .
'''
import multiprocessing as mp

def foo(q):
    q.put('hello')

if __name__ == '__main__':
    mp.set_start_method('spawn')
    q = mp.Queue()
    p = mp.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()
# In[]
'''
在程序中 set_start_method() 不应该被多次调用。

或者，你可以使用 get_context() 来获取上下文对象。
上下文对象与 multiprocessing 模块具有相同的API，
并允许在同一程序中使用多种启动方法。:
'''
