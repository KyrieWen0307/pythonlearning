'''
创建集合
'''
set1={1,2,3,3,3,2,2}
print(set1)
set2={'user','李小明','user','李小明'}
print(set2)
set3=set('hello')
print(set3)
set4=set([1,2,3,4,3,2,1])
print(set4)
set5={num for num in range(1,20)if num%3==0 or num%7==0}
print(set5)
for elem in set5:
    print(elem)
'''
集合的运算
'''
print(7 in set5)
print(10 in set5)
print('user'in set2)

set1={1,2,3,4,5,6,7}
set2={2,4,6,8,10}

print(set1&set2)
print(set1.intersection(set2))
print(set1|set2)
print(set1.union(set2))
print(set1-set2)
print(set1.difference(set2))
print(set1^set2)
print(set1.symmetric_difference(set2))
set1.update(set2)
print(set1)
set2.difference_update(set1)
print(set2)

set1={1,3,5}
set2={1,2,3,4,5}
print(set1.issubset(set2))
print(set2.issuperset(set1))

''''
集合的方法
'''
set1={1,10,100}
set1.add(1000)
set1.add(10000)
print(set1)
set1.discard(10)
if 100 in set1:
    set1.remove(100)
print(set1)
set1.clear()
print(set1)
set1={'user','user_b'}
set1={'user'}
print(set1.isdisjoint(set2))

'''
不可变集合
'''
fset1=frozenset({1,3,5,7})
fset2=frozenset({1,2,3,4,5})
print(fset1)
print(fset2)