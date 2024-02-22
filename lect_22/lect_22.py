# class DBHelper:
#     database_conn = None
#     data = ''
#
#     def __new__(cls):
#         if cls.database_conn is None:
#             cls.database_conn: DBHelper = object.__new__(cls)
#             print('Connection to DB')
#         return cls.database_conn
#
#     def select_data(self):
#         return self.data
#
#     def insert_data(self, new_data):
#         self.data = new_data
#
#
# conn1 = DBHelper()
# conn1.insert_data('12345')
#
# conn2 = DBHelper()
# print(conn2.select_data())
#
# print(id(conn1))
# print(id(conn2))
# print(conn1 is conn2)

from abc import ABC, abstractmethod

#
# class AScale(ABC):
#     @abstractmethod
#     def get_weight(self):
#         pass
#
# class UAScale(AScale):
#     def __init__(self, curr_w):
#         self.curr_w = curr_w
#
#     def get_weight(self):
#         return self.curr_w
#
#
# class GBScale(AScale):
#     def __init__(self, curr_w):
#         self.curr_w = curr_w
#
#     def get_weight(self):
#         return self.curr_w
#
# class Adapter(AScale):
#     def __init__(self, gb_scale):
#         self.gb_scale = gb_scale
#
#     def get_weight(self):
#         return self.gb_scale.get_weight() * 0.453
#
#
#
# item1 = 35
# item2 = 35
#
# u_sc = UAScale(item1)
# # gb_sc = GBScale(item2)
#
# gb_sc = Adapter(GBScale(item2))
#
#
# print(u_sc.get_weight())
# print(gb_sc.get_weight())


# class ADataReader(ABC):
#     @abstractmethod
#     def read(self):
#         pass
#
#
# class DBReader(ADataReader):
#     def read(self):
#         print('data from Database')
#
#
# class FileReader(ADataReader):
#     def read(self):
#         print('data from File')
#
#
# class ASender(ABC):
#     def __init__(self, data_r):
#         self.reader = data_r
#
#     def set_data_reader(self, data_r):
#         self.reader = data_r
#
#     @abstractmethod
#     def send(self):
#         pass
#
#
# class EmailSender(ASender):
#     def __init__(self, data_r):
#         super().__init__(data_r)
#
#     def send(self):
#         self.reader.read()
#         print('Send on Email')
#
#
# class TGBotSender(ASender):
#     def __init__(self, data_r):
#         super().__init__(data_r)
#
#     def send(self):
#         self.reader.read()
#         print('Send on Telegram')
#
#
# sender = EmailSender(DBReader())
# sender.send()
# print()
# sender.set_data_reader(FileReader())
# sender.send()
# print()
# sender = TGBotSender(DBReader())
# sender.send()

# class Graphic:
#     def draw(self):
#         pass
#
#     def add(self, obj):
#         pass
#
#     def remove(self, obj):
#         pass
#
#     def get_child(self, index):
#         pass
#
#
# class Line(Graphic):
#     def draw(self):
#         print('Line')
#
# class Rectangle(Graphic):
#     def draw(self):
#         print('Rectangle')
#
# class Text(Graphic):
#     def draw(self):
#         print('Text')
#
# class Text2():
#     def draw(self):
#         print('Text2')
#
# class Picture(Graphic):
#     def __init__(self):
#         self.children = []
#
#     def draw(self):
#         print('Picture:')
#         for i in self.children:
#             i.draw()
#
#     def add(self, obj):
#         if isinstance(obj, Graphic) and not obj in self.children:
#             self.children.append(obj)
#
#     def remove(self, obj):
#         index = self.children.index(obj)
#         del self.children[index]
#
#     def get_child(self, index):
#         return self.children[index]
#
#
# pic1 = Picture()
# pic1.add(Line())
# pic1.add(Rectangle())
# pic1.add(Text())
#
# pic1.draw()
# print()
# line = pic1.get_child(0)
# pic1.remove(line)
# pic1.draw()

# class Paper:
#     def __init__(self, count):
#         self.count = count
#
#     def get_count(self):
#         return self.count
#
#     def draw(self, text):
#         if self.count > 0:
#             self.count -= 1
#             print(text)
#
# class Printer:
#     def error(self, msg):
#         print(f'ERROR: {msg}')
#
#     def print_(self, paper, text):
#         if paper.get_count() > 0:
#             paper.draw(text)
#         else:
#             self.error('no paper')
#
# class Facade:
#     def __init__(self):
#         self.printer = Printer()
#         self.paper = Paper(5)
#
#     def write(self, text):
#         self.printer.print_(self.paper, text)
#
# f = Facade()
# f.write('Hello')
# f.write('Hello')
# f.write('Hello')
# f.write('Hello')
# f.write('Hello')
# f.write('Hello')
# f.write('Hello')
# f.write('Hello')

# class ASite(ABC):
#     @abstractmethod
#     def get_page(self, num):
#         pass
#
# class Site(ASite):
#     def get_page(self, num):
#         return f'This page {num}'
#
# class SiteProxy(ASite):
#     def __init__(self, site):
#         self.site = site
#         self.cache = {}
#
#     def get_page(self, num):
#         page = ''
#         if self.cache.get(num) is not None:
#             page = self.cache[num]
#             page = 'from cache: ' + page
#         else:
#             page = self.site.get_page(num)
#             self.cache[num] = page
#         return page
#
# my_site = SiteProxy(Site())
#
# print(my_site.get_page(1))
# print(my_site.get_page(2))
# print(my_site.get_page(3))
# print(my_site.get_page(1))
# print(my_site.get_page(3))
# print(my_site.get_page(4))

class ACommand(ABC):
    @abstractmethod
    def posit(self):
        pass

    @abstractmethod
    def negat(self):
        pass

class Conveyor:
    def on(self):
        print('Conv start working')

    def off(self):
        print('Conv stop working')

    def speed_up(self):
        print('Conv speed up')

    def speed_low(self):
        print('Conv speed low')

class ConvWorkCommand(ACommand):
    def __init__(self, conv):
        self.conv = conv

    def posit(self):
        self.conv.on()

    def negat(self):
        self.conv.off()

class ConvAdjustCommand(ACommand):
    def __init__(self, conv):
        self.conv = conv

    def posit(self):
        self.conv.speed_up()

    def negat(self):
        self.conv.speed_low()

class Multipult:
    def __init__(self):
        self.commands = [None, None]
        self.history = []

    def set_command(self, button, command):
        self.commands[button] = command

    def press_on(self, button):
        self.commands[button].posit()
        self.history.append(self.commands[button])

    def press_cancel(self):
        if len(self.history) != 0:
            self.history.pop().negat()

conv1 = Conveyor()

mp = Multipult()
mp.set_command(0, ConvWorkCommand(conv1))
mp.set_command(1, ConvAdjustCommand(conv1))

mp.press_on(0)
mp.press_on(1)
mp.press_on(1)
mp.press_cancel()
mp.press_cancel()
mp.press_cancel()
