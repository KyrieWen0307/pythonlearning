''''
字符串的定义
'''
s1='hello world'
s2='你好，世界'
s3='hello,' \
'wonderful' \
'world'
print(s1)
print(s2)
print(s3)

s1='\'hello world!\''
s2='\\hello world!\\'
print(s1)
print(s2)

'''
原始字符串
'''
s1='\it \is \time \to \read \now'
s2=r'\it \is \time \to \read \now'
print(s1)
print(s2)

'''
字符的特殊表示
'''
s1='\u28201\142\143\144\x61\x62\x63'
s2='\u661a'
print(s1)
print(s2)

'''
字符串的运算
'''

s1='hello'+', '+'world'
print(s1)
s2='!'*3
print(s2)
s1+=s2
print(s1)
s1*=2
print(s1)

'''
比较运算
使用ord()获取对应编码
'''
print(ord('李'))

s1='hello, world'
print('wo' in s1)
print(len(s1))

s='hello'
for i in s:
    print(i)

'''
字符串的方法
由于字符串是不可变类型，使用字符串的方法对字符串进行操作会产生新的字符串，但是原来变量的值并没有发生变化。
'''

'''
大小写相关方法
'''
s1='hello world'
print(s1.capitalize())
print(s1.title())
print(s1.upper())
print(s1.lower())
print(s1)

'''
查找操作
rfind/findex:逆向查找
'''
print(s1.find('rld'))
print(s1.find('ll',-1))
print(s1.index('or'))

'''
性质判断
'''
print(s1.startswith('hello'))
print(s1.endswith('world'))
print(s1.endswith('hello'))
print(s1.isalpha())
print(s1.isdigit())
print(s1.isalnum())

'''
格式化
'''
print(s1.center(20,'閞'))
print(s1.rjust(20))
print(s.ljust(20,'獱'))
print('33'.zfill(5))
print('-33'.zfill(5))
a=321
b=123
print(f'{a}*{b}={a*b:.2f}')

'''
修剪操作
'''
s1='   student@example.com'
print(s1.strip())
s2='---hello, world---'
print(s2.lstrip('-'))
print(s2.rstrip('-'))
print(s1.replace('s','李'))
print(s1.replace('o','shit'))
print(s1.replace('o','shit',1))

'''
拆分与合并
'''
s='i1love1u'
words=s.split('1',1)
print(words)
print('~'.join(words))

'''
编码与解码
'''
a='李小明'
b=a.encode('utf-8')
c=a.encode('gbk')
print(b)
print(c)
print(b.decode('utf-8'))
print(c.decode('gbk'))