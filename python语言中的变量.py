"""
整型（int）是Python中最常用的数据类型之一，用于表示整数。
整型可以是正数、负数或零，并且没有大小限制，取决于计算机的内存。
在Python中，整型可以使用十进制、二进制、八进制
"""
print(0b100)
print(0o100)
print(100)
print(0x100)
"""
浮点型（float）用于表示实数，即带有小数部分的数字。
浮点数在Python中通常使用双精度表示，具有较高的精度和范围。
"""
print(123.456)
print(1.23456e2)
"""
字符串（str）是Python中用于表示文本的数据类型。
字符串可以包含字母、数字、符号和空格，并且可以使用单引号或双引号括起来。
"""
print('hello')
print("hello")
"""
布尔型（bool）是Python中用于表示逻辑值的数据类型。
布尔型只有两个取值：True（真）和False（假）。
"""
print(True)
print(False)

"""
变量命名规则：
1. 变量名只能包含字母、数字和下划线，且不能以数字开头。
2. 变量名不能使用Python的关键字。
惯例：
1. 变量名通常使用小写字母，多个单词之间使用下划线分隔（例如：my_variable）。
2. 常量名通常使用大写字母，多个单词之间使用下划线分隔（例如：MY_CONSTANT）。
3. 类名通常使用首字母大写的驼峰命名法（例如：MyClass）。
4. 函数名通常使用小写字母，多个单词之间使用下划线分隔（例如：my_function）。
5. 模块名通常使用小写字母，多个单词之间使用下划线分隔（例如：my_module）。
6. 包名通常使用小写字母，多个单词之间使用下划线分隔（例如：my_package）。
7. 变量名、函数名、模块名和包名应该具有描述性，能够清楚地表达其用途。
8. 避免使用过于简短或模糊的名称，以提高代码的可读性。
9. 在命名时，尽量避免使用拼音或其他非英语单词，以便于国际化和团队协作。
10. 在命名时，尽量避免使用缩写，除非是非常常见的缩写，以提高代码的可读性。
11. 在命名时，尽量避免使用与内置函数或模块同名的名称，以避免潜在的冲突。
12.受保护的变量用单个下划线开头。
13.私有变量用双下划线开头。
"""
"""
使用变量保存数据并进行加减乘除运算
version：1.0
author：温宇豪
"""
a = 45
b = 12
print(a,b)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
"""
使用type函数检查变量的类型
version：1.0
author：温宇豪
"""
a = 100
b = 123.45
c = 'hello world'
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
"""
类型转换函数：
int()：将其他类型转换为整型。
float()：将其他类型转换为浮点型。
str()：将其他类型转换为字符串。
bool()：将其他类型转换为布尔型。
chr()：将整数转换为对应的Unicode字符。
ord()：将Unicode字符转换为对应的整数。
"""
a=100
b=123.45
c='123'
d='100'
e='123.45'
f='hello, world!'
g=True
print(float(a))
print(int(b))
print(int(c))
print(int(c,base=16))
print(int(d,base=2))
print(float(e))
print(bool(f))
print(int(g))
print(chr(a))
print(ord('d'))