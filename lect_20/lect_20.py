# class LincList:
#     head = None
#     length = 0
#
#     class Node:
#         element = None
#         next_node = None
#
#         def __init__(self, element, next_node=None):
#             self.element = element
#             self.next_node = next_node
#
#     def __str__(self):
#         try:
#             node = self.head
#             line = '['
#             while node.next_node:
#                 line += str(node.element) + ', '
#                 node = node.next_node
#             line += str(node.element) + ']'
#         except:
#             line = '[]'
#         return line
#
#     def empty(self):
#         return self.head is None
#
#     def append(self, element):
#         if not self.head:
#             self.head = self.Node(element)
#             self.length += 1
#             return element
#         node = self.head # [ 1 2 3 4 ]
#         while node.next_node:
#             node = node.next_node
#         node.next_node = self.Node(element)
#         self.length += 1
#         return element
#
#     def __getitem__(self, item):
#         ind = 0
#         node = self.head
#         while ind < item:
#             node = node.next_node
#             ind += 1
#         return node.element
#
#     def insert(self, key, value):
#         ind = 0
#         node = self.head
#         prev_node = self.head
#
#         if key == 0:
#             old_head = self.head
#             self.head = self.Node(element=value, next_node=old_head)
#             self.length += 1
#             return value
#         while ind < key:
#             prev_node = node
#             node = node.next_node # [ 22  '000'  777]
#             ind += 1
#         prev_node.next_node = self.Node(element=value, next_node=node)
#         self.length += 1
#         return value
#
#     def __delitem__(self, key):
#         ind = 0
#         node = self.head
#         prev_node = node
#         if key == 0:
#             old_head = self.head
#             element = self.head.element
#             self.head = self.head.next_node
#             self.length -= 1
#             del old_head
#             return element
#         while ind < key:
#             prev_node = node
#             node = node.next_node
#             ind += 1
#         prev_node.next_node = node.next_node
#         element = node.element
#         self.length -= 1
#         del node
#         return element
#
#
# lst = LincList()
# print(lst.empty())
# print(lst)
# print(lst.append(234))
# print(lst.empty())
# print(lst)
# lst.append(98)
# lst.append(67)
# print(lst)
# lst.insert(1, '000')
# print(lst)
# print(lst.length)
# print(lst[2])
# del (lst[0])
# print(lst)
# print(lst.length)
# del (lst[1])
# print(lst)
# print(lst.length)

### TREE

class Node:
    def __init__(self, key):
        self.t_key = key

    def set_key(self, key):
        self.t_key = key

    def key(self):
        return self.t_key

    def __str__(self):
        return str(self.t_key)


class Tree(Node):
    def __init__(self, key):
        super().__init__(key)
        self.t_children = []

    def add_child(self, child):
        self.t_children.append(child)
