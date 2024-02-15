# ### TREE
#
# class Node:
#     def __init__(self, key):
#         self.t_key = key
#
#     def set_key(self, key):
#         self.t_key = key
#
#     def key(self):
#         return self.t_key
#
#     def __str__(self):
#         return str(self.t_key)
#
#
# class Tree(Node):
#     def __init__(self, key):
#         super().__init__(key)
#         self.t_children = []
#
#     def add_child(self, child):
#         self.t_children.append(child)
#
#     def remove_child(self, key):
#         for child in self.t_children:
#             if child.key() == key:
#                 self.t_children.remove(child)
#                 return True
#         return False
#
#     def get_child(self, key):
#         for child in self.t_children:
#             if child.key() == key:
#                 return child
#         return None
#
#     def get_children(self):
#         return self.t_children
#
#
# def constr_tree():
#     node7 = Tree(7)
#     node9 = Tree(9)
#     node10 = Tree(10)
#     node11 = Tree(11)
#     node12 = Tree(12)
#     node13 = Tree(13)
#     node14 = Tree(14)
#     node15 = Tree(15)
#     #
#     node8 = Tree(8)
#     node8.add_child(node14)
#     node8.add_child(node15)
#
#     node4 = Tree(4)
#     node4.add_child(node8)
#     node4.add_child(node9)
#
#     node5 = Tree(5)
#     node5.add_child(node10)
#     node5.add_child(node11)
#
#     node6 = Tree(6)
#     node6.add_child(node12)
#     node6.add_child(node13)
#
#     node2 = Tree(2)
#     node2.add_child(node4)
#     node2.add_child(node5)
#
#     node3 = Tree(3)
#     node3.add_child(node6)
#     node3.add_child(node7)
#
#     root = Tree(1)
#     root.add_child(node2)
#     root.add_child(node3)
#
#     return root
#
# tree = constr_tree()
#
# # nd11 = tree.get_child(2).get_child(5).get_child(11)
# # print(nd11)
#
# def DFS(root):
#     print(root.key(), end=' => ')
#     for child in root.get_children(): # 2 3
#         DFS(child)
#
#
# DFS(tree)
#
# from queue import Queue
#
# def BFS(root):
#     q = Queue()
#     q.put(root)
#
#     while not q.empty():
#         node = q.get()
#         print(node.key(), end=' => ')
#
#         for child in node.get_children():
#             q.put(child)
#
# print()
# BFS(tree)
###
# class Document:
#     def show(self):
#         pass
#
# class PDFDocument(Document):
#     def show(self):
#         print('Open PDF document')
#
# class WordDocument(Document):
#     def show(self):
#         print('Open Word document')
#
# class Application:
#     def create_document(self, type_d):
#         pass
#
# class MyApp(Application):
#     def create_document(self, type_d):
#         if type_d == 'pdf':
#             return PDFDocument()
#         elif type_d == 'doc':
#             return WordDocument()
#
# app = MyApp()
# app.create_document('doc').show()
# app.create_document('pdf').show()
#
# class Phone:
#     def __init__(self):
#         self.os = None
#         self.camera = None
#         self.battery = None
#         self.screen = None
#
#
# class PhoneBuilder:
#     def __init__(self):
#         self.phone = Phone()
#
#     def set_os(self, os):
#         self.phone.os = os
#         return self
#
#     def set_camera(self, camera):
#         self.phone.camera = camera
#         return self
#
#     def set_battery(self, battery):
#         self.phone.battery = battery
#         return self
#
#     def set_screen(self, screen):
#         self.phone.screen = screen
#         return self
#
#     def get(self):
#         return self.phone
#
# builder = PhoneBuilder()
#
# phone1 = builder.set_os('IOS').set_camera('48MP').set_screen('5.5"').set_battery('3400mAh').get()
# print(phone1.battery)
import copy

class Sheep:
    name = ''
    params = {'w': 25, 'h':55}

    def __init__(self, donor = None):
        if donor is not None:
            self.name = donor.get_name()
            self.params = copy.deepcopy(donor.get_params())

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_params(self):
        return self.params

    def set_weight(self, w):
        self.params['w'] = w

    def clone(self):
        return Sheep(self)

sheep_d = Sheep()
sheep_d.set_name('A')

sheep_clone = sheep_d.clone()

sheep_clone.set_name('B')
sheep_clone.set_weight('90')

print('Donor', sheep_d.get_name(), sheep_d.get_params(), id(sheep_d))
print('Clone', sheep_clone.get_name(), sheep_clone.get_params(), id(sheep_clone))
