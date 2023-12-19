#'5 6 9 2'

#temp_lst = inp.split()

# s = map(int, ['5', '6', '9', '2'])
# print(s)

#my_lst = list(map(int, input().split()))

# my_lst = [i for i in range(21) if i % 2 == 0]
#
# my_lst2 = []
# for i in range(21):
#     if i % 2 == 0:
#         my_lst2.append(i)
#
# print(my_lst)
# print(my_lst2)

# lst1 = [1, 2, 2, 3, 3, 4]
# print(2 in lst1)
# print(4 in lst1)
# str1 = 'n4k3kn43n5kl4n535nk4nkl5n43ln5lk43n5'
#
# lst2 = [i for i in str1 if i.isnumeric()]
# print(lst2)
# 1,2,2,3,3,4
# st = [int(i) for i in input().split(',')]
# lst1 = [i for i in st if i % 2 != 0]
# lst2 = [i for i in st if i % 2 == 0]
# print(lst1)
# print(lst2)

# volv = 'аоеи'
#
# st = input().split()
# lst1 = [i for i in st if i[0] in volv]
# lst2 = [i for i in st if i not in lst1]
# print(lst1)
# print(lst2)

# keys = ['марка', 'модель', 'ціна', 'знижка']
# values = ['тойота', 'РАВ4', 45488, '12%']
#
# result = [key+': '+str(value) for key, value in zip(keys, values)]
#
# print(*result, sep='\n')

A = [[20, 5, 9],
     [1, 6, 18],
     [33, 65, 2]]

for row in A:
    for elem in row:
        print(elem, end='\t|')
    print()
