# class BaseClass1:
#     pass
#
# class BaseClass2:
#     pass
#
# class DerivedClass(BaseClass1, BaseClass2):
#     pass
#
# class Vehicle:
#     def __init__(self, wheels, engine):
#         self.wheels = wheels
#         self.engine = engine
#
# class Car(Vehicle):
#     def __init__(self, wheels, engine, gas_type):
#         super().__init__(wheels, engine)
#         self.gas_type = gas_type
#
# class Supercar(Car):
#     def __init__(self, wheels, engine, gas_type):
#         super().__init__(wheels, engine, gas_type)
#
#
# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def show_info(self):
#         print(f'Title {self.title}')
#         print(f'Author {self.author}')
#         print(f'Pages {self.pages}')
#
# class File:
#     def __init__(self, size, src):
#         self.size = size
#         self.src = src
#
#     def show_info(self):
#         print(f'Size {self.size}')
#         print(f'Src {self.src}')
#
# class ElBook(Book, File):
#     def __init__(self, title, author, pages, size, src, website):
#         Book.__init__(self, title, author, pages)
#         File.__init__(self, size, src)
#         self.website = website
#
#
# book1 = ElBook('Harry Potter', 'J.R', 874, '653Kb', 'C:/Books', 'www.google.com')
# book1.show_info()
#
# print(ElBook.mro())

# class MyClass1:
#     def say(self):
#         print('Hi from Class - 1')
#
# class MyClass2(MyClass1):
#     def say1(self):
#         print('Hi from Class - 2')
#
# class MyClass3(MyClass1):
#     def say1(self):
#         print('Hi from Class - 3')
#
# class MyClass4(MyClass2, MyClass3):
#     pass
#     # def say(self):
#     #     print('Hi from Class - 4')
#
#
# obj_1 = MyClass4()
# obj_1.say()
# print(MyClass4.mro())
#
# class Class1:
#     pass
#
# class Class2:
#     pass
#
# class Class3:
#     pass
#
# class Class4(Class3):
#     pass
#
# class Class5(Class1, Class2):
#     pass
#
# class Class6(Class4, Class5):
#     pass
#
# print(Class6.mro())
#
# class A:
#     def method(self):
#         print('Called method to class A')
#
# class B(A):
#     pass
#     # def method(self):
#     #     print('Called method to class B')
#
# class C:
#     def method(self):
#         print('Called method to class C')
#
# class D(B, C):
#     def method(self):
#         C.method(self)
#
# obj_1 = D()
# obj_1.method()

# class Transport:
#     def __init__(self, type):
#         self.type = type
#
# class Auto:
#     def __init__(self, factory, model):
#         self.factory = factory
#         self.model = model
#
# class Engine(Transport, Auto):
#     def __init__(self, type, factory, model, horsepower):
#         Transport.__init__(self, type)
#         Auto.__init__(self, factory, model)
#         self.horsepower = horsepower
#
# eng1 = Engine('W', 'MB', '300Sl', '168')
# print(eng1.horsepower)
#
# class Human:
#     def __init__(self, f_name, l_name):
#         self.f_name = f_name
#         self.l_name = l_name
#
#     def walking(self):
#         print(f'{self.f_name} walking')
#
#
# class Employer:
#     def __init__(self, name_emp, salary):
#         self.name_emp = name_emp
#         self.salary = salary
#
#     def working(self):
#         print(f'{self.name_emp} working')
#
#
#
# class Person(Human, Employer):
#     def __init__(self, f_name, l_name, name_emp, salary, exp):
#         Human.__init__(self, f_name, l_name)
#         Employer.__init__(self, name_emp, salary)
#         self.exp = exp
#
#     def __str__(self):
#         return f'{self.f_name}, {self.l_name}, {self.name_emp}, {self.salary}, {self.exp}'
#
#
# person_1 = Person('Jack', 'Green', 'Builder', 5600, 3)
#
# print(person_1)
# person_1.walking()
# person_1.working()
# import time
#

#
# @timer
# class Rectangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     @property
#     def area(self):
#         return self.a * self.b
#
#
#
#
# rect_1 = Rectangle(4, 6)
# # print(rect_1.a)
# # # print(rect_1.area())
# # print(rect_1.area)

class MyDecorator:
    def __init__(self, func):
        self.func = func
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.func(*args, **kwargs)
        self.counter += 1
        print(f'Called {self.counter} times')



@MyDecorator
def some_func():
    return 45


some_func()
some_func()
some_func()
some_func()
