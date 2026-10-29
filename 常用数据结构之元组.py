'''
元组的定义和运算
'''
t1=(35,12,98)
t2=('李小明',45,True,'示例城市A')
print(type(t1))
print(type(t2))
print(len(t1))
print(len(t2))
print(t2[-1])
print(t2[::3])

for elem in t2:
    print(elem)

t3=t1+t2
print(t3)
a=()
print(type(a))
b=('hello')
print(type(b))
b=('hello',)
print(type(b))
c=(100)
print(type(c))
d=(100,)
print(type(d))

'''
打包和解包操作
'''
a=1,10,100
print(type(a))
print(a)
i,j,k=a
print(i,j,k)

a=1,10,100,1000
i,j,*k=a
print(i,j,k)
i,*j,k=a
print(i,j,k)
*i,j=a
print(i,j)
i,j,k,l,*m=a
print(i,j,k,l,m)

a,b,*c=range(1,10)
print(a,b,c)
a,b,c=[1,10,100]
print(a,b,c)
a,*b,c='hello'
print(a,b,c)

a,b,c=1,2,3
print(a,b,c)
a,b,c=c,b,a
print(a,b,c)

import timeit

print('%.3f 秒' % timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]', number=10000000))
print('%.3f 秒' % timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)', number=10000000))

infos=('user','示例城市A','示例城市B','示例城市C')
print(list(infos))
frts=['apple','banana','orange']
print(tuple(frts))

'''
列表和元组都是容器型的数据类型，即一个变量可以保存多个数据，而且它们都是按一定顺序组织元素的有序容器。
列表是可变数据类型，元组是不可变数据类型，所以列表可以添加元素、删除元素、清空元素、排序反转，但这些操作对元组来说是不成立的。
列表和元组都可以支持拼接运算、成员运算、索引运算、切片运算等操作，后面我们要讲到的字符串类型也支持这些运算，因为字符串就是字符按一定顺序构成的序列，在这一点上三者并没有什么区别。
我们推荐大家使用列表的生成式语法来创建列表，它不仅好用而且效率很高，是 Python 语言中非常有特色的语法。
'''