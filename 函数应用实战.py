'''
随机验证码
'''

import random
import string

all_char=string.digits+string.ascii_letters

def generate_code(*,code_len=4):
    return ''.join(random.choices(all_char,k=code_len))

for _ in range(5):
    print(generate_code(code_len=6))

'''
判断素数
'''

def judg_prime(num:int):
    is_prime=1
    for i in range(2,int(pow(num,0.5))+1):
        if num%i==0:
            is_prime=0
            break
    if is_prime==0:
        print(f'{num}不是素数，{i}是他的因数')
    else:
        print(f'{num}是素数')


for _ in range(1):
    i=random.randrange(1,1000)
    judg_prime(i)

'''
最大公约数&最小公倍数
'''

def gcd(x:int,y:int)->int:
    while y%x!=0:
        x,y=y%x,x
    return x

def lcm(x:int,y:int)->int:
    return x*y//gcd(x,y)

print(lcm(41341,31231))

'''
数据统计
'''
def ptp(data):
    return max(data)-min(data)

def mean(data):
    return sum(data)/len(data)

def median(data):
    temp,size=sorted(data),len(data)
    if size%2!=0:
        return temp[size//2]
    else:
        return mean(temp[size//2-1:size//2+1])

def var(data,ddof=1):
    x_bar = mean(data)
    temp = [(num - x_bar) ** 2 for num in data]
    return sum(temp) / (len(temp) - ddof)

def std(data,ddof=1):
    return var(data,ddof)**0.5

def cv(data,ddof=1):
    return std(data,ddof)/mean(data)

def describe(data):
    """输出描述性统计信息"""
    print(f'均值: {mean(data)}')
    print(f'中位数: {median(data)}')
    print(f'极差: {ptp(data)}')
    print(f'方差: {var(data)}')
    print(f'标准差: {std(data)}')
    print(f'变异系数: {cv(data)}')

data=[1,2,3,525,234,534,6363,24245,363,354,345,353]
describe(data)

'''
双色球随机选号
autho:wyh
version:1.3
'''

import random

RED_BALLS=[i for i in range(1,34)]
BULE_BALLS=[i for i in range(1,17)]

def choose():
    selected_balls=random.sample(RED_BALLS,6)
    sorted(selected_balls)
    selected_balls.append(random.choice(BULE_BALLS))
    return selected_balls

def display(balls):
    for ball in balls[:-1]:
        print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
    print(f'\033[034m{balls[-1]:0>2d}\033[0m')

n=int(input('生成几注号码：'))
for _ in range(n):
    display(choose())