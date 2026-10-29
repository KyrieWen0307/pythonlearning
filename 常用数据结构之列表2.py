'''
添加和删除元素
append:追加元素至列表末尾
insert(x,'xxx'):插入元素至指定位置
remove("):删除指定元素
pop():默认删除列表中最后一个元素
clear():清空列表
del
'''
languages=['python','java','c++']
languages.append('javascript')
print(languages)
languages.insert(1,'SQL')
print(languages)

languages=['python','java','c++','javascript','SQL']
if 'java' in languages:
    languages.remove('java')
print(languages)
languages.pop()
temp=languages.pop(1)
print(languages)
languages.append(temp)
print(languages)
languages.clear()
print(languages)

'''
Q:若有多个相同元素？
'''
languages=['python','python']
print(languages)
languages.remove('python')
print(languages)
del languages[0]
print(languages)

'''
元素位置和频次
.index('xxx',number)
.count('xxx')
'''
languages=['Python', 'Java', 'Java', 'C++', 'Kotlin', 'Python']
print(languages.index('Python',2))
print(languages.count('Python'))

'''
元素排序和反转
.sort()：排序
.reverse():反转
'''
numbers=['2','1','3','4']
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

numbers = ['2', '10', '1', '3']
numbers.sort(key=int)
print(numbers)  # ['1', '2', '3', '10']

numbers = [2, 10, 1, 3]
numbers.sort(key=str)
print(numbers)

'''
列表生成式
'''

items=[]
for i in range(1,100):
    if i%3==0 or i%5==0:
        items.append(i)
print(items)

items1=[i for i in range(1,100) if i%10==0]
print(items1)

nums1=[1,2,3,4]
nums2=[]
for i in nums1:
    nums2.append(i**2)
print(nums2)

nums1=[12,14,17,19]
nums3=[i**3 for i in nums1]
print(nums3)

'''
强烈建议用生成式语法来创建列表
'''

'''
嵌套列表
'''

scores=[[95,83,92],[80,75,82],[92,97,90]]
print(scores[0])
print(scores[0][1])

scores.clear()
scores=[]
for _ in range(3):
    temp=[]
    for _ in range(3):
        score=int(input('请输入：'))
        temp.append(score)
    scores.append(temp)
print(scores)

import random

scores=[[random.randrange(60,101)for _ in range(3)]for _ in range(5)]
print(scores)

'''
双色球随机选号程序
author:温宇豪
version:1.2
'''
n=int(input('生成几注号码：'))
red_balls=[i for i in range(1,34)]
blue_balls=[i for i in range(1,17)]
for _ in range(n):
    selected_balls=random.sample(red_balls,6)
    selected_balls.sort()
    for ball in selected_balls:
        print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
    blue_ball=random.choice(blue_balls)
    print(f'\033[034m{blue_ball:0>2d}\033[0m')

"""
双色球随机选号程序

Author: 骆昊
Version: 1.3
"""
import random

from rich.console import Console
from rich.table import Table

# 创建控制台
console = Console()

n = int(input('生成几注号码: '))
red_balls = [i for i in range(1, 34)]
blue_balls = [i for i in range(1, 17)]

# 创建表格并添加表头
table = Table(show_header=True)
for col_name in ('序号', '红球', '蓝球'):
    table.add_column(col_name, justify='center')

for i in range(n):
    selected_balls = random.sample(red_balls, 6)
    selected_balls.sort()
    blue_ball = random.choice(blue_balls)
    # 向表格中添加行（序号，红色球，蓝色球）
    table.add_row(
        str(i + 1),
        f'[red]{" ".join([f"{ball:0>2d}" for ball in selected_balls])}[/red]',
        f'[blue]{blue_ball:0>2d}[/blue]'
    )

# 通过控制台输出表格
console.print(table)
