"""
100以内的素数
author：温宇豪
version:1.0
"""
for i in range(2,101):
    is_prime=False
    for j in range(2,i):
        if i%j==0:
            is_prime=True
            break
    if is_prime:
        print('%d不是素数'%i)
    else:
        print('%d是素数'%i)

"""
斐波那契数列
author:温宇豪
version:1.0
"""
x=1
y=1
num=1
for i in range(1,21):
    if i > 2:
        num=x+y
        y=x
        x=num
    print(num,end='\t')
print()
"""
寻找水仙花数
author：温宇豪
version：1.0
"""
for i in range(100,1000):
    a=i//100
    b=i%100//10
    c=i%10
    if i==a**3+b**3+c**3:
        print('%d是水仙花数'%i)

"""
正常数的反转
author：温宇豪
version:1.0
"""
num=int(input('请输入数字：'))
reverse_num=0
while num >0:
    reverse_num=reverse_num*10+num%10
    num//=10
print(reverse_num)

"""
百钱百鸡问题
author：温宇豪
version:1.0
"""
a=5
b=3
c=1/3
for x in range(0,21):
    for y in range (0,33):
        z=(100-x*a-y*b)/c
        if x+y+z==100 and x*a+y*b+z*c==100:
            print('公鸡%d只，母鸡%d只，小鸡%d只'%(x,y,z))

"""
CRAPS赌博游戏
author：温宇豪
version：1.0
"""
import random
asset=1000
while asset>0:
    debt=int(input('输入本次下注金额：'))
    num1=random.randrange(1,7)
    num2=random.randrange(1,7)
    sum1=num1+num2
    print('第一次点数为%d'%sum1)
    if sum1==7 or sum1==11:
        asset+=debt
        print('你摇出了%d点,获胜！目前你有%d资产'%(sum1,asset))
        continue
    elif sum1==2 or sum1==3 or sum1==12:
        asset-=debt
        print('你摇出了%d点，失败，目前你有%d资产'%(sum1,asset))
        continue
    else:
        while True:
            num1=random.randrange(1,7)
            num2=random.randrange(1,7)
            sum2=num1+num2
            if sum2==7:
                asset-=debt
                print('第二次掷骰子你摇出了%d点，失败，目前你有%d资产'%(sum2,asset))
                break
            elif sum2==sum1:
                asset+=debt
                print('第二次掷骰子你摇出了%d点，和上一轮相同，获胜!目前你有%d资产'%(sum2,asset))
                break
