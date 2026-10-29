"""
课前任务：记录6000次掷骰子
author:温宇豪
version:1.0
"""
import random
num=0
num1=0
num2=0
num3=0
num4=0
num5=0
num6=0
for _ in range(6000):
    num=random.randrange(1,7)
    if num == 1:
        num1+=1
    elif num==2:
        num2+=1
    elif num==3:
        num3+=1
    elif num==4:
        num4+=1
    elif num==5:
        num5+=1
    elif num==6:
        num6+=1
print('点数1、2、3、4、5、6各出现%d、%d、%d、%d、%d、%d次' %(num1,num2,num3,num4,num5,num6))

'''
创建列表
'''
items1=[35,12,99,68,55,35,87]
items2=['python','java','go','kotlin']
items3=[100,12.3,'python',True]
print(type(items1))
print(items2)
print(items3)
items4=list(range(1,10))
items5=list('hello')
print(items4)
print(items5)

"""
列表的运算
"""
items5=[35,12,99,45,66]
items6=[45,58,29]
items7=['python','java','javascript']
print(items5+items6)
print(items6+items7)
items5+=items6
print(items5)
print(items6*3)
print(items7*2)
print(29 in items6)
print(99 in items6)
print('C++'not in items7)
print('python'not in items7)
items8=['apple','waxberry','durian','peach','watermelon']
print(items8[0])
print(items8[-1])
print(items8[-5])
print(items8[1:3:1])
print(items8[0:5:2])
items8[1:3]=['x','o']
print(items8)
num1=[1,2,3,4]
num2=list(range(1,5))
num3=[3,2,1]
print(num1==num2)
print(num3>num1)
'''
元素的遍历
'''
languages=['python','java','c++','kotlin']
for index in range(len(languages)):
    print(languages[index])

for i in languages:
    print(i)

"""
记录掷骰子
author:温宇豪
version:2.0
"""
counter=[0]*6
for _ in range(6000):
    result=random.randrange(1,7)
    if result == 1:
        counter[0]+=1
    elif result ==2:
        counter[1]+=1
    elif result ==3:
        counter[2]+=1
    elif result ==4:
        counter[3]+=1
    elif result ==5:
        counter[4]+=1
    elif result ==6:
        counter[5]+=1
print(counter)