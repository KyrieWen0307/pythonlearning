'''
创建和使用字典
'''
xinhua={
    '李':'李小明的姓',
    '小明':'李小明的名'
}
print(xinhua)
personinfo={
    'name':'Alex Li',
    'age':'22',
    'height':'170',
    'weight':'60.0',
    'tel':'00000000000',
    'email':'student@example.com'
}
print(personinfo)
person=dict(name='李小明',age='二十二',university='示例大学',major='示例专业')
print(person)

items1=dict(zip('ABCDE','12345'))
print(items1)
items2=dict(zip('ABCDE',range(1,10)))
print(items2)
items3={x:x**3 for x in range(1,6)}
print(items3)

print(len(personinfo))
for key in personinfo:
    print(key)

'''
字典的运算
'''
person={
    'name':'李小明',
    'age':'22',
    'height':'170',
    'weight':'60.0',
    'car':{
        'brand':'示例品牌',
        'type':'示例车型'
    }
}
print(person)
print('name'in person)
print('tel'in person)
print(person['name'])
print(person['car'])
for key in person:
    print(f'{key}:\t{person[key]}')

'''
字典的方法
'''
print(person.get('name'))
print(person.get('sex'))
print(person.get('sex','没有这个选项你扎啤吗'))
print(person.keys())
print(person.values())
print(person.items())
for i,j in person.items():
    print(f'{i}:\t{j}')

person2=dict(sex='male',IP='US')
person|=person2
print(person)

print(person.pop('age'))
print(person)
print(person.popitem())
print(person)
del person['name']
print(person)
person.clear()
print(person)

sentence=input('请输入一个句子:')
counter={}
for char in sentence:
    if 'A'<=char<='Z'or'a'<=char<='z':
        counter[char]=counter.get(char,0)+1
sorted_keys=sorted(counter,key=counter.get,reverse=False)
for key in sorted_keys:
    print(f'{key}出现了{counter[key]}次')

stocks={
    'apple':191.88,
    'google':1186.96,
    'orcle':48.44,
    'symc':21.29
}
stocks2={key:value for key,value in stocks.items()if value>100}
print(stocks2)