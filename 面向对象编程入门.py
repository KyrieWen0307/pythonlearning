'''
类和对象
'''
class Student:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def study(self,course_name):
        print(f'{self.name}正在学习{course_name}.')

    def play(self):
        print(f'{self.name}正在玩游戏.')

'''
创建和使用对象
'''
stu1=Student('wyh',20)
stu2=Student('ksm',19)
print(stu1)
print(stu2)
print(hex(id(stu1)),hex(id(stu2)))

Student.study(stu1,'Python程序设计')
Student.play(stu2)
stu2.study('Git控制版本')
'''
初始化方法
'''
'''
面向对象的支柱
面向对象编程有三大支柱，就是我们之前给大家划重点的时候圈出的三个词：封装、继承和多态。
对封装的理解是：隐藏一切可以隐藏的实现细节，只向外界暴露简单的调用接口。
'''

'''
面向对象案例
例1：时钟
'''

import time

class Clock:

    def __init__(self,hour=0,minute=0,second=0):

        self.hour=hour
        self.min=minute
        self.sec=second

    def run(self):
        self.sec+=1
        if self.sec==60:
            self.sec=0
            self.min+=1
            if self.min==60:
                self.min=0
                self.hour+=1
                if self.hour==24:
                    self.hour=0

    def show(self):
        return f'{self.hour:0>2d}:{self.min:0>2d}:{self.sec:0>2d}'

class Point:

    def __init__(self,x=0,y=0):
        self.x,self.y=x,y

    def distance_to(self,other):
        dx=self.x-other.x
        dy=self.y-other.y
        return(dx**2+dy**2)**0.5

    def __str__(self):
        return f'({self.x},{self.y})'
    
clock=Clock(23,59,58)
while False:
    print(clock.show())
    time.sleep(1)
    clock.run()

p1=Point(3,5)
p2=Point(6,9)
print(p1)
print(p2)
print(p1.distance_to(p2))

