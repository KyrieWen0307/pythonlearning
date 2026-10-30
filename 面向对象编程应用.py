'''
例1：扑克游戏
类和类之间的关系可以粗略的分为 is-a关系（继承）、**has-a关系（关联）**和 use-a关系（依赖）
'''
from enum import Enum

class Suite(Enum):

    SPADE,HEART,CLUB,DIAMOND = range(4)

for elem in Suite:
    print(f'{elem}:{elem.value}')

class Card:

    def __init__(self,suite,face):
        self.suite=suite
        self.face=face

    def __repr__(self):
        suites='♠♥♣♦'
        faces=['','A','2','3','4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'

    def __lt__(self,other):
        if self.suite==other.suite:
            return self.face<other.face
        return self.suite.value<other.suite.value

card1=Card(Suite.SPADE,5)
card2=Card(Suite.HEART,13)
print(card1)
print(card2)

import random

class Poker:

    def __init__(self):
        self.cards=[Card(suite,face)
                   for suite in Suite
                   for face in range(1,14)]
        self.current=0

    def shuffle(self):
        self.current=0
        random.shuffle(self.cards)

    def deal(self):
        card=self.cards[self.current]
        self.current+=1
        return card

    @property
    def has_next(self):
        return self.current<len(self.cards)

poker=Poker()
print(poker.cards)
poker.shuffle()
print(poker.cards)

class Player:

    def __init__(self,name):
        self.name=name
        self.cards=[]

    def get_one(self,card):
        self.cards.append(card)

    def arrange(self):
        self.cards.sort()

players=[Player('青龙'),Player('白虎'),Player('朱雀'),Player('玄武')]
for _ in range(13):
    for player in players:
        player.get_one(poker.deal())

for player in players:
    player.arrange()
    print(f'{player.name}的手牌为{player.cards}')

'''
工资结算系统
'''

from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):

    def __init__(self,name):
        self.name=name

    @abstractmethod
    def get_salary(self):
        pass

class Manager(Employee):    
    def get_salary(self):
        return 15000.0

class Programmer(Employee):

    def __init__(self,name,working_hour=0):
        super().__init__(name)
        self.working_our=working_hour

    def get_salary(self):
        return 200*self.working_our

class Sales(Employee):

    def __init__(self, name,sales=0):
        super().__init__(name)
        self.sales=sales

    def get_salary(self):
        return 1800+self.sales*0.05

'''
isintance函数
'''
emps=[Manager('WYH'),Programmer('logo'),Sales('yz')]
for emp in emps:
    if isinstance(emp,Programmer):
        emp.working_our=int(input(f'请输入{emp.name}本月工作时间:'))
    elif isinstance(emp,Sales):
        emp.sales=float(input(f'请输入{emp.name}本月销售额:'))
    print(f'{emp.name}本月工资为：{emp.get_salary():.2f}￥')