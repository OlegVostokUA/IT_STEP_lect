###
# example_list = [4, -2, 1, -5, 8]
#
# example_list.sort()
# print(example_list) # [-5, -2, 1, 4, 8]
# example_list.sort(reverse=True)
# print(example_list) # [8, 4, 1, -2, -5]
###
# |NOT SORT!!!
# no change collection - (3, 4, 1) - Tuple
# no indexing collection - {3, 4, 1} - set
# op types in structure - [1, 2, 'Hello']
###
# BUBBLE SORT
unsort_list = [5, 2, 4, 7, 6] # [5,4,3,1,2] = 1


# for i in range(len(unsort_list)-1):
#     for j in range(len(unsort_list)-i-1):
#         if unsort_list[j] < unsort_list[j+1]:
#             temp = unsort_list[j]
#             unsort_list[j] = unsort_list[j+1]
#             unsort_list[j+1] = temp
#
# for index, elem in enumerate(unsort_list):
#     print(f"element {index + 1}: {elem}")

# upgrade method
# count_sort = 0
#
# for i in range(len(unsort_list)-1):
#     sort_flag = True
#     for j in range(len(unsort_list)-i-1):
#         if unsort_list[j] < unsort_list[j+1]:
#             temp = unsort_list[j]
#             unsort_list[j] = unsort_list[j+1]
#             unsort_list[j+1] = temp
#             sort_flag = False
#             count_sort += 1
#
#     if sort_flag:
#         break
#
# for index, elem in enumerate(unsort_list):
#     print(f"element {index + 1}: {elem}")
#
# print(count_sort)

####
# shell sort alg.
# unsorted = [33, 31, 40, 8, 12, 17, 25, 42]
#
# # итерация по неотсортированным массивам
# for i in range(len(unsorted)):
#     # получаем значение элемента
#     val = unsorted[i]
#     # записываем в hole индекс i
#     hole = i
#     # проходим по массиву в обратную сторону, пока не найдём элемент больше текущего
#     while hole > 0 and unsorted[hole - 1] > val:
#         # переставляем элементы местами , чтобы получить правильную позицию
#         unsorted[hole] = unsorted[hole - 1]
#         # делаем шаг назад
#         hole -= 1
#     # вставляем значение на верную позицию
#     unsorted[hole] = val
#
# print(unsorted)

###
# merge sort
# unsorted = [33, 31, 40, 8, 12, 17, 25, 42]

