from abc import ABC, abstractmethod


# class Man:
#     def __init__(self, name):
#         self.name = name
#
#     def say(self):
#         print(f'Hello. My nameis {self.name}')
#
#
# class JetPack:
#     def __init__(self, man):
#         self.man = man
#
#     def fly(self):
#         print(f'{self.man.name} fly')
#
#
# man1 = Man('Petro')
# man1.say()
# print()
# man_jp = JetPack(man1)
#
# man_jp.fly()

# class AWorcker(ABC):
#     @abstractmethod
#     def set_next_worcker(self, worcker):
#         pass
#
#     @abstractmethod
#     def execute(self, command):
#         pass
#
#
# class Worcker(AWorcker):
#     def __init__(self):
#         self.next_worcker = None
#
#     def set_next_worcker(self, worcker):
#         self.next_worcker = worcker
#         return worcker
#
#     def execute(self, command):
#         if self.next_worcker is not None:
#             return self.next_worcker.execute(command)
#         return ''
#
#
# class Designer(Worcker):
#     def execute(self, command):
#         if command == 'house project':
#             return 'Designer ' + command
#         else:
#             return super().execute(command)
#
#
# class Carpen(Worcker):
#     def execute(self, command):
#         if command == 'build house':
#             return 'Carpen ' + command
#         else:
#             return super().execute(command)
#
#
# class FinishW(Worcker):
#     def execute(self, command):
#         if command == 'finish house':
#             return 'FinishW ' + command
#         else:
#             return super().execute(command)
#
#
# def give_command(worcker, command):
#     comm = worcker.execute(command)
#     if comm == '':
#         print(command, '-nobody')
#     else:
#         print(comm)
#
#
# des = Designer()
# carp = Carpen()
# fw = FinishW()
#
#
# des.set_next_worcker(carp).set_next_worcker(fw)
#
# # give_command(des, 'house project')
# # print()
# # give_command(des, 'build house')
# # print()
# # give_command(des, 'finish house')
# print()
# print()
# give_command(des, 'clean house')

# class AMemento(ABC):
#     @abstractmethod
#     def get_dollar(self):
#         pass
#
#     @abstractmethod
#     def get_euro(self):
#         pass
#
# class ExchangeMemento(AMemento):
#     def __init__(self, d, e):
#         self.dollar = d
#         self.euro = e
#
#     def get_dollar(self):
#         return self.dollar
#
#     def get_euro(self):
#         return self.euro
#
#
# class Exchange:
#     def __init__(self, d, e):
#         self.dollar = d
#         self.euro = e
#
#     def get_dollar(self):
#         print(f'Dollars: {self.dollar}')
#
#     def get_euro(self):
#         print(f'EURO: {self.euro}')
#
#     def sell(self):
#         if self.dollar > 0:
#             self.dollar -= 1
#
#     def buy(self):
#         self.euro += 1
#
#     def save(self):
#         return ExchangeMemento(self.dollar, self.euro)
#
#     def restore(self, ex_memento):
#         self.dollar = ex_memento.get_dollar()
#         self.euro = ex_memento.get_euro()
#
#
# class Memory:
#     def __init__(self, exchange):
#         self.exchange = exchange
#         self.hist = []
#
#     def backup(self):
#         self.hist.append(self.exchange.save())
#
#     def undo(self):
#         if len(self.hist) == 0:
#             return 'Hist is empty'
#         else:
#             self.exchange.restore(self.hist.pop())
#
#
# exch1 = Exchange(d=10, e=10)
#
# mem1 = Memory(exch1)
#
# exch1.sell()
# exch1.buy()
# exch1.get_dollar()
# exch1.get_euro()
#
# mem1.backup()
# print('SAVE')
# exch1.sell()
# exch1.buy()
# exch1.get_dollar()
# exch1.get_euro()
# print()
# mem1.undo()
# exch1.get_dollar()
# exch1.get_euro()
#
# print(mem1.undo())

# class AObserver(ABC):
#     @abstractmethod
#     def update(self, obj):
#         pass
#
# class AObservObj(ABC):
#     @abstractmethod
#     def add_observ(self, obs):
#         pass
#
#     @abstractmethod
#     def remove_observ(self, obs):
#         pass
#
#     @abstractmethod
#     def notify(self):
#         pass
#
#
# class Product(AObservObj):
#     def __init__(self, price):
#         self.price = price
#         self.observers = []
#
#     def change_price(self, price):
#         self.price = price
#         self.notify()
#
#     def add_observ(self, obs):
#         self.observers.append(obs)
#
#     def remove_observ(self, obs):
#         self.observers.remove(obs)
#
#     def notify(self):
#         for o in self.observers:
#             o.update(self.price)
#
#
# class MassBuyer(AObserver):
#     def __init__(self, obj):
#         self.product = obj
#         obj.add_observ(self)
#
#     def update(self, obj):
#         if obj < 300:
#             print('MassBuyer buy product', obj)
#             self.product.remove_observ(self)
#
#
# class Buyer(AObserver):
#     def __init__(self, obj):
#         self.product = obj
#         obj.add_observ(self)
#
#     def update(self, obj):
#         if obj < 350:
#             print('Buyer buy product', obj)
#             self.product.remove_observ(self)
#
#
# prod1 = Product(400)
#
#
# mb1 = MassBuyer(prod1)
#
# b1 = Buyer(prod1)
#
# prod1.change_price(380)
# print('380')
# #prod1.change_price(340)
# print('340')
# prod1.change_price(290)
# print('290')
#
# print(len(prod1.observers))

# class AVisitor(ABC):
#     @abstractmethod
#     def visit(self, place):
#         pass
#
# class APlace(ABC):
#     @abstractmethod
#     def accept(self, visitor):
#         pass
#
#
# class Zoo(APlace):
#     def accept(self, visitor):
#         visitor.visit(self)
#
# class Cinema(APlace):
#     def accept(self, visitor):
#         visitor.visit(self)
#
# class Shop(APlace):
#     def accept(self, visitor):
#         visitor.visit(self)
#
#
# class Visitor(AVisitor):
#     def __init__(self):
#         self.val = ''
#
#     def visit(self, place):
#         if isinstance(place, Zoo):
#             self.val = 'Bear'
#         elif isinstance(place, Cinema):
#             self.val = 'Movie'
#         elif isinstance(place, Shop):
#             self.val = 'Shopping'
#
#
# places = [Zoo(), Cinema(), Shop()]
#
# visitor = Visitor()
#
# for p in places:
#     p.accept(visitor)
#     print(visitor.val)

# class State(ABC):
#     def __init__(self):
#         self.traf_light = None
#
#     @abstractmethod
#     def next_state(self):
#         pass
#
#     @abstractmethod
#     def prev_state(self):
#         pass
#
#
# class TrafficLight:
#     def __init__(self, state):
#         self.set_state(state)
#
#     def set_state(self, state):
#         self.state = state
#         self.state.traf_light = self
#
#     def next_state(self):
#         self.state.next_state()
#
#     def prev_state(self):
#         self.state.prev_state()
#
#
# class GreenState(State):
#     def next_state(self):
#         print('Green >>> Yellow')
#         self.traf_light.set_state(YellowState())
#
#     def prev_state(self):
#         print('Green')
#
# class YellowState(State):
#     def next_state(self):
#         print('Yellow >>> Red')
#         self.traf_light.set_state(RedState())
#
#     def prev_state(self):
#         print('Green <<< Yellow')
#         self.traf_light.set_state(GreenState())
#
# class RedState(State):
#     def next_state(self):
#         print('Red')
#
#     def prev_state(self):
#         print('Yellow <<< Red')
#         self.traf_light.set_state(YellowState())
#
#
# tr_light1 = TrafficLight(GreenState())
#
# tr_light1.next_state()
# tr_light1.next_state()
# tr_light1.next_state()
# tr_light1.next_state()
# tr_light1.prev_state()
# tr_light1.prev_state()
# tr_light1.prev_state()
# tr_light1.prev_state()
#
