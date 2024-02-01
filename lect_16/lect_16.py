# class People:
#     def __init__(self, name):
#         self.name = name
#
#     def say_hello(self):
#         print('Hello')
#
#
# p1 = People('Jack')
#
# p1.say_hello()
#
# class Vector2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     # def plus(self, other):
#     #     return self.x + other.x, self.y + other.y
#
#     def __add__(self, other):
#         return self.x + other.x, self.y + other.y
#
#     def __sub__(self, other):
#         return self.x - other.x, self.y - other.y
#
#     def __mul__(self, other):
#         return self.x * other.x, self.y * other.y
#
#     def __divmod__(self, other):
#         return self.x / other.x, self.y / other.y
#
#     def __eq__(self, other):
#         return self.x == other.x, self.y == other.y
#
#     def __neg__(self):
#         return Vector2D(-self.x, -self.y)
#
#     def __str__(self):
#         return f'{self.x}, {self.y}'
#
#     def __int__(self):
#         return self.x
#
#     def __float__(self):
#         return self.y
#
# v1 = Vector2D(6, 4)
# v2 = Vector2D(6, 2)
#
# # v3 = Vector2D(v1 + v2)
# # v3 = Vector2D(v1.x + v2.x, v1.y + v2.y)
# # v3 = Vector2D.plus(v1, v2)
#
# print(v1)
# print(float(v1.x))

# class Collection:
#     def __init__(self):
#         self.elements = []
#
#     def __setitem__(self, key, value):
#         try:
#             self.elements[key] = value
#         except IndexError:
#             self.elements.append(value)
#
#     def __getitem__(self, key):
#         try:
#             return self.elements[key]
#         except IndexError:
#             return None
#
#     def __delitem__(self, key):
#         try:
#             self.elements.pop(key)
#         except IndexError:
#             pass
#
#     def __str__(self):
#         return str(self.elements)
#
#
# c = Collection()
# c[0] = 78
# c[1] = 'abc'
# c[100] = 3456.0
# print('Collection: ', c)
# del c[0]
# del c[100]
#
# print('Collection: ', c)
# print(c[0])
#
# class CallCounter:
#     def __init__(self, n = 0):
#         self.__n = n
#
#     def __call__(self):
#         self.__n += 1
#         return self.__n
#
#
# class Game:
#     def __init__(self, player_game):
#         self.player_game = player_game
#         self.__game_counter = CallCounter()
#         self.__n_calls = self.__game_counter()
#
#     def start_game(self):
#         self.__n_calls = self.__game_counter()
#
#     def info(self):
#         print(f'User {self.player_game} has l-ed the game {self.__n_calls}')
#
#
# user1 = Game('Bob')
# for i in range(5):
#     user1.start_game()
#     user1.info()

from datetime import datetime, timedelta

class DateDelta:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __lt__(self, other):
        date1 = datetime(self.year, self.month, self.day)
        date2 = datetime(other.year, other.month, other.day)
        return date1 < date2

    def __gt__(self, other):
        date1 = datetime(self.year, self.month, self.day)
        date2 = datetime(other.year, other.month, other.day)
        return date1 > date2

    def __sub__(self, other):
        date1 = datetime(self.year, self.month, self.day)
        date2 = datetime(other.year, other.month, other.day)
        return date1 - date2

    def __add__(self, other):
        date1 = datetime(self.year, self.month, self.day)
        return date1 + timedelta(other)


date_1 = DateDelta(2024, 2, 27)
date_2 = DateDelta(2021, 5, 25)

# print(date_1 > date_2)
# print(date_1 < date_2)
# print(date_1 - date_2)
print(date_1 + 2)

