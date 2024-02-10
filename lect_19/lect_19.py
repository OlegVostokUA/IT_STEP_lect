# our_stack = []
#
# def s_push(x):
#     our_stack.append(x)
#
# def s_pop():
#     x = our_stack.pop()
#     return x
#
# def clear_s():
#     our_stack.clear()
#
# def s_is_empty():
#     return len(our_stack) == 0
#
# def s_top(): #
#     x = our_stack[-1]
#     return x


# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def empty(self):
#         return len(self.items) == 0
#
#     def push(self, x):
#         self.items.append(x)
#
#     def pop(self):
#         x = self.items.pop()
#         return x
#
#     def top(self):
#         if self.empty():
#             raise Exception('Stack is empty')
#         return self.items[-1]
#
#     def __len__(self):
#         return len(self.items)


# def bracket_checker(brackets):
#
#     s = Stack()
#     for bracket in brackets:
#         if bracket == '(':
#             s.push(bracket)
#         else:
#             if s.empty():
#                 return False
#             else:
#                 s.pop()
#
#     # if s.empty():
#     #     return True
#     # else:
#     #     return False
#     return s.empty()

# def bracket_checker(brackets):
#
#     s = Stack()
#
#     for bracket in brackets:
#         if bracket not in '()[]':
#             continue
#         if bracket in '([':
#             s.push(bracket)
#         else:
#             if s.empty():
#                 return False
#             left = s.pop()
#             if left == '(':
#                 right = ')'
#             elif left == '[':
#                 right = ']'
#
#             if right != bracket:
#                 return False
#
#     return s.empty()
#
#
#
# print(bracket_checker('[()]'))
# print(bracket_checker('([([(())])])'))
# print(bracket_checker('(([3])([cx])([])([,j]))'))
# print(bracket_checker('[)([>>])(]'))
# print(bracket_checker('(([(5+8)]90))'))

# class Queue:
#     def __init__(self):
#         self.items = []
#
#     def empty(self):
#         return len(self.items) == 0
#
#     def enqueue(self, x):
#         self.items.append(x)
#
#     def dequeue(self):
#         if self.empty():
#             raise Exception('Queue is empty!')
#         return self.items.pop(0)
#
#     def __len__(self):
#         return len(self.items)

# from collections import deque
#
# q = deque()
#
# #print(help(q))
#
# q.append(11)
# q.append(12)
# q.append(13)
# print(q, type(q))
#
# print(q.popleft())
# print(q.popleft())
# print(q.popleft())
# print(q.popleft())
# from queue import Queue
#
# q = Queue()
#
# print(help(q))
# print()
# q.put(21)
# q.put(22)
# q.put(23)
#
# print(q)
# print(q.qsize())
# print(q.get())
# print(q.get())
# print(q.get())
# #print(q.get())
#
# from multiprocessing import Queue
#
# q = Queue()
#
# print()
# q.put(21)
# q.put(22)
# q.put(23)
#
# print(q)
# print(q.qsize())
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.qsize())
# print(q.get())

class PriorQueue:
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def insert(self, item, priority):
        self.items.append((item, priority))

    def extract(self):
        if self.empty():
            raise Exception('Queue is empty')

        minpos = 0
        for i in range(1, len(self.items)):
            if self.items[minpos][1] > self.items[i][1]:
                minpos = i

        return self.items.pop(minpos)[0]

prq = PriorQueue()

prq.insert(5,2)
prq.insert(12,1)
prq.insert(5656,3)
prq.insert(21,3)
prq.insert(51,2)

print(prq.extract())
print(prq.extract())
print(prq.extract())
print(prq.extract())
print(prq.extract())

