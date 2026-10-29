"""
[] 索引
[:] 切片
** 幂
~ 按位取反
* / % // 乘、除、模、整除
>> << 按位右移、按位左移
& 按位与
^ 按位异或
in not in 成员运算符
not or and 逻辑运算符


"""
a = 10
b = 3
a += b
a *= a+2
print(a)
"""
:= 海象运算符（walrus operator）是Python 3.8引入的一种新的赋值运算符，用于在表达式中进行变量赋值。它的语法是：variable := expression，其中variable是要赋值的变量名，expression是要计算的表达式。海象运算符可以在表达式中直接进行赋值，从而减少代码行数，提高代码的可读性。
"""
print((c := 10))

"""
比较运算符
"""
flag0 = 1 == 1
flag1 =3 > 2
flag2 =2 < 1
flag3= flag1 and flag2
flag4= flag1 or flag2
flag5= not flag0
print(flag0,flag1,flag2,flag3,flag4,flag5)
print(flag1 and not flag2)
print(1 > 2 or 2 == 3)
"""
将华氏温度转换为摄氏温度
author: 温宇豪
version: 1.0
"""
f = float(input('请输入华氏温度：'))
c=(f-32)/1.8
print('%.1f华氏度=%.1f℃'%(f,c))
"""
输入半径计算圆的周长和面积
author: 温宇豪
version: 1.2
"""
import math
r = float(input('radius:'))
p = 2*math.pi*r
s = math.pi*r**2
print(f'{p=:.2f}')
print('面积为：%.2f'%s)
"""
判断闰年
author: 温宇豪
version: 1.0
"""
year = int(input('请输入年份：'))
is_leap = year % 4 == 0 and year % 100 !=0 or year % 400 == 0
print(f'{is_leap=}')