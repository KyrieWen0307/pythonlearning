'''
可见性和属性装饰器
'''
class Student:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def study(self,subject):
        print(f'{self.name}正在学习{subject}')

stu=Student('wyh',20)
stu.study('Python程序设计')
'''
动态属性
'''
stu.sex='男'
print(stu.sex)

'''
静态方法和类方法
'''
class Triangle(object):

    def __init__(self,a,b,c):

        self.a=a
        self.b=b
        self.c=c

    @staticmethod
    def is_valid(a,b,c):
        return a+b>c and a+c>b and b+c>a

    @property
    def perimeter(self):
        return self.a+self.b+self.c

    @property
    def area(self):
        p=self.perimeter/2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

if Triangle.is_valid(3,4,5):
    t=Triangle(3,4,5)
    print(t.perimeter)
    print(t.area)
else:
    print('无效边长')

'''
继承和多态
'''

class Human:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eat(self):
        print(f'{self.name}正在吃饭')

    def sleep(self):
        print(f'{self.name}正在睡觉')

class Student(Human):

    def __init__(self, name, age):
        super().__init__(name, age)

    def study(self,subject):
        print(f'{self.name}正在学习{subject}')

class Teacher(Human):

    def __init__(self, name, age, title):
        super().__init__(name,age)
        self.title=title

    def teach(self,subject):
        print(f'{self.name}{self.title}正在讲授{subject}')

stu1 = Student('白元芳', 21)
stu2 = Student('狄仁杰', 22)
tea1 = Teacher('武则天', 35, '副教授')
stu1.eat()
stu2.sleep()
tea1.eat()
stu1.study('Python程序设计')
tea1.teach('Python程序设计')
stu2.study('数据科学导论')