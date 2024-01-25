# class ClassName:
#     <class statement 1>
#     ...
#     def func_class(self):
#         <BODY>

# class Student:
#     SPEC = 'Python developer'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show_info(self):
#         return f'Student {self.name} is {self.age} years old'
#
#     def show_msg(self, msg_text):
#         return f'{self.name} says {msg_text}'
#
#
#
# st_1 = Student('Jane', 26)
# st_2 = Student('Bob', 23)
#
# print('Student 1')
# print(st_1.show_info())
# print(st_1.show_msg('Hello'))
# print('Student 2')
# print(st_2.show_info())
# print(st_2.show_msg('How are you?'))

# class Film:
#     def __init__(self, title, director, genre):
#         self.title = title
#         self.director = director
#         self.genre = genre
#
#     def show_info(self):
#         print(f'Film: {self.title}, Director: {self.director}, Genre: {self.genre}')
#
#
# class Book:
#     def __init__(self, title, autor, pages):
#         self.title = title
#         self.autor = autor
#         self.pages = pages
#
#     def show_info(self):
#         print(f'Book: {self.title}, Autor: {self.autor}, Pages: {self.pages}')
#
# film_1 = Film('Goodfather', 'F.F. Coppola', 'Crime')
# book_1 = Book('Python crash course', 'Eric Matthes', 876)
#
# for i in (film_1, book_1):
#     i.show_info()
#
# print(4 + 3)
# print(len('Student'))
# print(len(['Student', 'Prof']))
# print(len({'f_name': 'Jane', 'l_name': 'Bons'}))

# class Fraction:
#     def __init__(self, num_1, num_2):
#         self.num_1 = num_1
#         self.num_2 = num_2
#
#     def show(self):
#         return f'{self.num_1}, {self.num_2}'
#
#     def summ(self):
#         return self.num_1 + self.num_2
#
#     def diff(self):
#         return self.num_1 - self.num_2
#
#     def mult(self):
#         return self.num_1 * self.num_2
#
#     def div(self):
#         return self.num_1 / self.num_2
#
#
# fr_1 = Fraction(50, 25)
#
# print(fr_1.show())
# print(fr_1.summ())
# print(fr_1.diff())
# print(fr_1.mult())
# print(fr_1.div())

# class Person:
#     def __init__(self, f_name, l_name, age):
#         # public
#         self.f_name = f_name
#         self.l_name = l_name
#         self.age = age
#
#     # public method
#     def get_info(self):
#         return f'{self.f_name}, {self.l_name}, {self.age}'
#
#     def get_hi(self, msg):
#         person_inf = self.get_info()
#         return f'{person_inf} say {msg}'
#
# from random import randint
#
# class Person:
#     def __init__(self, f_name, l_name, age):
#         # public
#         self.f_name = f_name
#         self.l_name = l_name
#         self.age = age
#
#         self.__personID = randint(10000, 99999)
#
#
#     def __get_id(self):
#         # self.__personID = 12333
#         return f'{self.__personID}'
#
#     # public method
#     def get_info(self):
#         self.__personID = 33312
#         return f'{self.f_name}, {self.l_name}, {self.age}, {self.__get_id()}'
#
#     def get_hi(self, msg):
#         person_inf = self.get_info()
#         return f'{person_inf} say {msg}'
#
# pers_1 = Person('Jack', 'Sparrow', 45)
# # print(pers_1.get_info())
# pers_1.age = 35
# print(pers_1.get_info())
# pers_1.__personID = 99999
# print(pers_1.get_info())
# # print(pers_1.f_name)
# # print(pers_1.__personID)

# import turtle
#
#
# class Rectangle:
#     def __init__(self, color, dist):
#         self.color = color
#         self.dist = dist
#
#
#     def draw(self):
#         turtle.pencolor(self.color)
#         for i in range(4):
#             turtle.forward(self.dist)
#             turtle.right(90)
#         turtle.exitonclick()
#
#
# r1 = Rectangle('Red', 150)
#
#
# r2 = Rectangle('Green', 250)
#
# # r2.COLOR = 'Black'
# # r2.DISTANCE = 250
#
# # r1.draw()
# r2.draw()

class Dragon:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def get_damage(self, damage):
        pass

    def kick(self, other, damage):
        pass

    def is_dead(self):
        pass
