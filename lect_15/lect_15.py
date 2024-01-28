# from random import randint
#
#
# class Dragon:
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health
#
#     def get_damage(self, damage):
#         if damage >= self.health:
#             self.health = 0
#             self.is_dead()
#         else:
#             self.health -= damage
#             print(f'{self.name} get {damage} and have {self.health}')
#         return self.health
#
#     def kick(self, other, damage):
#         crit = randint(1,4)
#         if crit == 3:
#             damage *= 2
#             print(f'{self.name} use CRIT')
#         other.get_damage(damage)
#
#     def is_dead(self):
#         print(f'Dragon {self.name} is dead')
#
#
# d1 = Dragon('Smog', 100)
# d2 = Dragon('Rog', 100)
#
# d1.kick(d2, 10)
# d1.kick(d2, 10)
# d1.kick(d2, 10)
# d1.kick(d2, 10)
# d1.kick(d2, 10)
# d1.kick(d2, 10)
# d1.kick(d2, 10)
# d1.kick(d2, 10)
# d1.kick(d2, 10)
# d1.kick(d2, 10)

# class Person:
#     field = 58
#
#     def __init__(self, f_name, l_name):
#         self.f_name = f_name
#         self.l_name = l_name
#
#     def get_info(self):
#         return f'{self.f_name}, {self.l_name}'
#
#     def hello(self, msg):
#         print(self.get_info())
#         return f'{msg}'
#
#     @staticmethod
#     def say_greeting():
#         print("Nice to meet you")
#
#
# p1 = Person('Jack', 'Dill')
# print(p1.hello('Hello))))'))
# p1.say_greeting()
# import re
#
# class MyOperator:
#     @staticmethod
#     def incrementer(string):
#         numbers = [float(s) for s in re.findall(r'-?\d+\.?\d*', string)]
#         # result = []
#         # for num in numbers:
#         #     result.append(num - 1)
#         # return result
#         return numbers
#
# user_str = 'Extra 100 , hugo 65.0 read 90.3 great'
#
# print(MyOperator.incrementer(user_str))

from datetime import date

# class Person:
#     def __init__(self, f_name, l_name, age):
#         self.f_name = f_name
#         self.l_name = l_name
#         self._age = age
#
#     def get_info(self):
#         return f'{self.f_name}, {self.l_name}, {self._age}'
#
#     def hello(self, msg):
#         print(self.get_info())
#         return f'{msg}'
#
#
# class Student(Person):
#     def __init__(self, f_name, l_name, age, spec, score):
#         super().__init__(f_name, l_name, age)
#         self.spec = spec
#         self.score = score
#
#     def is_successful(self):
#         return True if self.score > 51 else False
#
#     def get_info(self):
#         return super().get_info() + f', {self.spec}, {self.score}'
#
#
# p2 = Person('Joe', 'Diltre', 65)
# print(p2.get_info())
# p3 = Person('Dav', 'Volll', 33)
#
# st1 = Student('Joe', 'Black', 22, 'CV', 78)
# print(st1.get_info())
# #print(st1.hello('Good evening'))
# # print(st1.is_successful())
# # print(st1.spec)
# print(st1._age)
# st1._age = 99
# print(st1._age)
#

class Animal:
    def __init__(self, live, country):
        self.live = live
        self.country = country

    def eat(self):
        return 'Eating'


class Tiger(Animal):
    def __init__(self, live, country, poroda):
        super().__init__(live, country)
        self.poroda = poroda

    def meow(self):
        return 'Meow'


class Crocodile(Animal):
    def __init__(self, live, country, type_cr):
        super().__init__(live, country)

    def swimming(self):
        return 'Sloooooowww swiiiiimiiiiinggg'

class Alligator(Crocodile):
    def __init__(self, live, country, type_cr, porod):
        super().__init__(live, country, type_cr)
        self.porod = porod

    def fast_swimming(self):
        return 'fast swimming'


allig = Alligator('whild', 'australia', 'Alligator', 'Mallian')

print(allig.swimming())
print(allig.fast_swimming())
