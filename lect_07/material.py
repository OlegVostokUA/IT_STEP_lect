#
# # for i in range(1, 10):
# #     print('1')
# #     for j in range(1, 10):
# #         print('\t2')
# #         for j in range(1, 10):
# #             print('\t\t3')
#     #print()
# ####
# # change element
# # cycles list
# # list.append(x) list.clear(i) list.count(x) list.extend(iterable) list.index(x, #start, #end)
# # list.insert(i, x) list.pop(i) list.remove(x) list.reverse() list.sort(key=None, reverse=False)
# # min - max
# A = [1, 3, 2, 5, 9, 6]
# m = A[0]
# for elem in A:
# 	if elem > m: # <
# 		m = elem
# print(m)
# ####
# # sum
# m = 0
# for i in A:
# 	m += i
# print(m)
# ###
#
# # list from keyboard
# my_lst = list(map(int, input().split()))
# # 3 4 5 2 3 4 5 6 1 2 8
# print(my_lst)
# # [3, 4, 5, 2, 3, 4, 5, 6, 1, 2, 8]
#
# # generators lists
# my_lst = list(range(5))
# print(my_lst)
# # [0, 1, 2, 3, 4]
# my_lst = list(range(1, 25, 2))
# print(my_lst)
# # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
#
# my_lst = []
# for i in range(1, 21):
# 	if i % 2 == 0:
# 		my_lst.append(i)
# print(my_lst)
#
# my_lst = [i for i in range(1, 21) if i % 2 == 0]
# print(my_lst)
# # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
#
# # 'in' operator
# lst_1 = [1, 2, 2, 3]
# print(2 in lst_1)
# print(4 in lst_1)
# # examples
# # unice elem list
# lst_2 =[]
# for i in lst_1:
# 	if i not in lst_2:
# 		lst_2.append(i)
# print(lst_2)
#
# # numeric list
# my_str = '6emds83mmsad99342n42ld9xm37vn4820'
# my_lst2 = [i for i in my_str if i.isnumeric()]
# print(my_lst2)
# #['6', '8', '3', '9', '9', '3', '4', '2', '4', '2', '9', '3', '7', '4', '8', '2', '0']
#
# # unpacking list
# lst = [1, 2, 3, 4, 5]
# lst2 = ['a', 'b', 'c', 'd', 'e']
# print(*lst)
# print(*lst2)
# ###
# lst = [7, 6, 0, 9, 5, 3, 2, 8, 1]
# lst.sort()
# print(lst)
#
# lst.sort(reverse=True)
# print(lst)
#
# my_lst = ['яблоко', 'ананас', 'груша']
# my_lst.sort()
# print(my_lst)
#
# my_lst.sort(reverse=True)
# print(my_lst)
# ###
# # 3,4,2,7,8,9,1,11,2,56,2,6,81
#
# # 2 lists
# st = [int(i) for i in input().split(',')]
# lst_odd = [i for i in st if i % 2 != 0]
# lst_even = [i for i in st if i % 2 == 0]
# print(*lst_odd)
# print(*lst_even)
#
# ###
# # 2 lists
# # кіт осел пес авто
# vowels = 'аиеоуієюя'
# st = input().split()
#
# #lst1 = [i for i in st if i[0] in vowels]
# #lst2 = [i for i in st if i not in lst1]
# # АБО
# lst1 = []
# lst2 = []
#
# for i in st:
# 	if i[0] in vowels:
# 		lst1.append(i)
# 	else:
# 		lst2.append(i)
#
#
# print(*lst1)
# print(*lst2)
#
# ###
# # zip 2 lists in 1
# keys = ['модель', 'цена', 'количество', 'размер', 'цвет', 'скидка']
# values = ['XXLDude', 5678.00, 57, 'XXL', 'черный', '12%']
#
# res = [key + ': ' + str(value) for key, value in zip(keys, values)]
#
# print(*res, sep='\n')
#
# # doble massives
# A = [[20, 4, 9],
#      [1, 9, 87],
#      [22, 56, 0]]
#
# for row in A:
# 	for elen in row:
# 		print(elen, end='\t|')
# 	print()


a = [1, 2, 3]
b = a
b[0] = 5
print(a, b)

a = [1, 2, 3]
b = a.copy()
b[0] = 5
print(a, b)

# CASE 1
a = [1, 2, [3, 4, 5]]
b = a.copy()
b[2][0] = 10
print(a, b)


from copy import deepcopy

a = [1, 2, [3, 4, 5]]
b = deepcopy(a)
b[2][0] = 10
print(a, b)



A = [1, 2]
B = [3, 4]

C = []
C.append(A)
C.append(B)

E = deepcopy(C)
D = C.copy()
A[0] = 500

print(C)
print(D)
print(E)
# D = C



