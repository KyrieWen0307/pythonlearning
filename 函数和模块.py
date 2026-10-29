'''
输入m和n，计算C(m,n)
author:kyrie
version:1.2
'''
from math import factorial as f

m=int(input('m='))
n=int(input('n='))
print(f'C({m},{n})={f(m)/f(n)/f(m-n):.0f}')
'''
定义函数
'''

'''
函数的参数
'''

def judg(a,b,c):
    return a+b>c and a+c>b and b+c>a
a,b,c=map(float,input('请输入三条边长').split())
print(judg(a,b,c))

from random import randrange

def roll(n=2):
    total=0
    for _ in range(n):
        total+=randrange(1,7)
    return total

print(roll())

'''
求和相加
注意：带默认值的参数必须放在不带默认值的参数之后
'''

'''
def add(a,b=0,c=0):
    return a+b+c

a,b,c=map(float,input('请输入a,b,c：').split())
print(add(a,b,c))
'''

'''
可变参数
'''
def add(*args):
    total=0
    for char in args:
        if type(char) in (int,float):
            total+=char
    return total

args=list(map(float,input('请输入任意数:').split()))
print(add(*args))

def foo(*args,**kwargs):
    print(args)
    print(kwargs)

foo(3,2.1,True,name='李小明',age='22',gpa='3.50')

def test():
    print('hello world')

def test():
    print('goodbye world')

print(test())