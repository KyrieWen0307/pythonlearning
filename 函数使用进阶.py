'''
高阶函数
'''
def add(x,y):
    return x+y

def mul(x,y):
    return x*y

def cal(init_value,op_func,*arg,**kwargs):
    items=list(arg)+list(kwargs.values())
    result=init_value
    for item in items:
        if type(item)in (int,float):
            result=op_func(result,item)
    return result

arg=list(map(float,input('请输入任意数：').split()))
op_func=input('请输入方法:')
if op_func =='add':
    op_func=add
elif op_func=='mul':
    op_func=mul
init_value=int(input('请输入初始值:'))
print(cal(init_value,op_func,*arg))

import random

def is_even(num):
    return num%2==0

def square(num):
    return num**2

old_nums=[random.randint(1,100) for _ in range(10)]
print(old_nums)
new_nums=list(map(square,filter(is_even,old_nums)))
print(new_nums)

'''
.sort()和sorted()的区别
'''

'''
lambda函数
'''

old_nums=[random.randint(1,100)for _ in range(10)]
print(old_nums)
new_nums=list(map(lambda x:x**2,filter(lambda x:x%2==0,old_nums)))
print(new_nums)

import functools
import operator

fac=lambda n:functools.reduce(operator.mul,range(2,n+1),1)

is_prime=lambda x:all(map(lambda f:x%f,range(2,int(x**0.5)+1)))

print(fac(6))
print(is_prime(37))

'''
偏函数
'''

int2=functools.partial(int,base=2)
int8=functools.partial(int,base=8)
int16=functools.partial(int,base=16)
print(int2('1000'))
print(int8('1000'))
print(int16('1000'))