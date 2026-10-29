"""
for-in循环
每隔一秒输出一次“hello world”，
author：温宇豪
version：1.1
"""
import time

for _ in range(1):
    print("hello world")
    time.sleep(1)
"""
从1到100的整数求和
author：温宇豪
version：1.0
"""
total=0
for i in range(1,101):
    total+=i
print(total)
"""
从1到100的偶数求和
author：温宇豪
version：1.2
"""
print(sum(range(2,101,2)))

"""
while循环
从1到100的整数求和
author：温宇豪
version：1.4
"""
total=0
for i in range(1,101):
    if i%2!=0:
        continue
    total+=i
print(total)

"""
打印乘法口诀表
author：温宇豪
version：1.0
"""
for i in range(1,10):
    for j in range(1,i+1):
        print('%d×%d=%d'%(i,j,i*j),end='\t')
    print()

"""
判断素数
author：温宇豪
version：1.0
"""
num=int(input('请输入一个正整数：'))
end = int(num**0.5)
is_prime = True
for i in range(2,end+1):
    if num%i==0:
        is_prime = False
        break   
if is_prime:
    print('%d是素数'%num)
else:
    print('%d不是素数'%num)

"""
最大公约数
author：温宇豪
version：1.1
"""
x=int(input('x='))
y=int(input('y='))
while y%x!=0:
    x,y=y%x,x
print('最大公约数%d'%x)
"""
猜数字游戏
author：温宇豪
version：1.0
"""
import random
answer=random.randrange(1,101)
counter=0
while True:
    counter+=1
    num=int(input('请输入1-100之间的整数：'))
    if num>answer:
        print('大了')
    elif num<answer:
        print('小了')
    else:
        print('恭喜你猜对了！')
        break
print('你一共猜了%d次'%counter)