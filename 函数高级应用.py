'''
装饰器
Python 语言中，装饰器是“用一个函数装饰另外一个函数并为其提供额外的能力”的语法现象。
装饰器本身是一个函数，它的参数是被装饰的函数，它的返回值是一个带有装饰功能的函数。
'''
import random
import time

def download(filename):
    print(f'开始下载{filename}')
    time.sleep(random.random()*6)
    print(f'{filename}下载完成')

def upload(filename):
    print(f'开始上传{filename}')
    time.sleep(random.random()*8)
    print(f'{filename}上传完成')

def record_time(func):

    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(f'{func.__name__}执行时间:{end-start:.2f}秒')
        return result

    return wrapper

print(time.time())
download=record_time(download)
upload=record_time(upload)
download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')

'''
递归调用
'''

def time_record(func):

    def warpper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(f'{func.__name__}执行时间：{end-start:.8f}秒')
        return result

    return warpper


def fac(num):
    if num in (0,1):
        return 1
    return num*fac(num-1)

time_fac=time_record(fac)
print(time_fac(9))

from functools import cache

@cache
def fib1(n):
    if n in (1,2):
        return 1
    return fib1(n-1)+fib1(n-2)

time_fib1=time_record(fib1)

print(time_fib1(125))