import time

# for i in 1, 2, 3, 4, 5: # TITLE OF CYCLE
#     # print(i) # BODY OF CYCLE
#     print(i, end='')
#     print(i ** 3)


# word = 'alligator'
#
# for i in word: # TITLE OF CYCLE
#     # print(i) # BODY OF CYCLE
#     time.sleep(1)
#     print(i, end='')

# word = 'alligator'
#
# for number, i in enumerate(word): # TITLE OF CYCLE
#     # print(i) # BODY OF CYCLE
#     print(number+1, i)

# 1 to 100
# range (start, stop, step)
# var = range(1, 101, 1)
#
# for i in var:
#     print(i)

# for i in range(1, 101, 1):
#     print(i)
#
# for i in range(101):
#     print(i)


# running man
### 1 CASE
# health = 5
# weather = 'sun'
#
# for i in range(1, health+1):
#     time.sleep(1)
#     print('run 0.25l')
#     time.sleep(1)
#     print('run 0.50l')
#     time.sleep(1)
#     print('run 0.75l')
#     time.sleep(1)
#     print('run', i, 'lap')


# ### 2 CASE
# health = 5
# weather = 'sun'
#
# for i in range(1, health+1):
#     if weather == 'sun':
#         # print('run 0.25l')
#         # print('run 0.50l')
#         # print('run 0.75l')
#         print('run', i, 'lap')


# ### 3 CASE
# health = 5
# laps = 0
# weather = 'sun'
#
# for i in range(1, health + 1):
#     if weather == 'sun':
#         # print('run 0.25l')
#         # print('run 0.50l')
#         # print('run 0.75l')
#         print('run', i, 'lap')
#         laps += 1
#
# print('we run', laps, 'today')

# ### 4 CASE
# health = 5
# laps = 0
# weather = 'sun'
#
#
# for i in range(1, health + 1):
#     if weather == 'sun':
#         # print('run 0.25l')
#         # print('run 0.50l')
#         # print('run 0.75l')
#         print('run', i, 'lap')
#         laps += 1
#         if laps == 3:
#             break
#
# print('we run', laps, 'today')

# ############################
# # ### 5 CASE
# health = 5
# r_laps = 0
# weather = 'sun'
#
#
# while health != 0:
#     r_laps += 1
#     print('run', r_laps, 'lap')
#     health -= 1
#
# print('we run', r_laps, 'laps today')
#
# # ### 6 CASE # LOOOOOOOOOOOOOOOOOOOOP
# health = -5
# r_laps = 0
# weather = 'sun'
#
#
# while health != 0:
#     r_laps += 1
#     print('run', r_laps, 'lap')
#     health -= 1
#
# print('we run', r_laps, 'laps today')
#
# # ### 7 CASE #
# health = 5
# r_laps = 0
# weather = 'sun'
#
#
# while health > 0:
#     r_laps += 1
#     print('run', r_laps, 'lap')
#     health -= 1
#
# print('we run', r_laps, 'laps today')
#
# # ### 8 CASE #
# health = 5
# r_laps = 0
# weather = 'sun'
#
#
# while health > 0 and weather == 'sun':
#     r_laps += 1
#     print('run', r_laps, 'lap')
#     health -= 1
#     if health < 2:
#         break
#
# print('we run', r_laps, 'laps today')
#
#
#
# # ## 8 CASE #
# health = 5
# r_laps = 0
# weather = 'sun'
#
#
# while health > 0 and weather == 'sun':
#     r_laps += 1
#     print('run', r_laps, 'lap')
#     # DOPING ON 3 LAP
#     if r_laps == 3:
#         continue
#
#     health -= 1
#
#
# print('we run', r_laps, 'laps today')
#
# ### OR
#
# number = 0
# count = 0
# while count < 5:
#     number += 1
#     if (number % 2) == 1:
#         continue
#     print(number)
#     count += 1

### OR

# number = 0
# while number < 300:
#     number += 1
#     if number % 3 != 0:
#         continue
#     elif number % 5 != 0:
#         print(number, "divides by 3")
#     elif number % 7 != 0:
#         print(number, "divides by 3 and 5")
#     else:
#         print(number, "divides by 3 and 5 and 7")

# ## 9 CASE #
# health = 5
# r_laps = 0
# weather = 'sun'
#
#
# while health > 0 and weather == 'sun':
#     r_laps += 1
#     health -= 1
#     print('run', r_laps, 'lap')
#     if r_laps > 3:
#         weather = 'rain'
#
#
# print('we run', r_laps, 'laps today')

## 10 CASE #
#
# health = 5
# r_laps = 0
# weather = 'sun'
#
# while health > 0 and weather == 'sun':
#     r_laps += 1
#     health -= 1
#     print('run', r_laps, 'lap')
#     time.sleep(1)
#     if r_laps == 3:
#         weather = 'rain'
#         print('stop running. Rain')
#         time.sleep(5)
#     weather = 'sun'
#
#
# print('we run', r_laps, 'laps today')
# print('we have', health, 'health')


## 11 CASE #
# health = 5
# r_laps = 0
# weather = 'sun'
#
# while health > 0 and weather == 'sun':
#     r_laps += 1
#     health -= 1
#     print('run', r_laps, 'lap')
#     # time.sleep(1)
#     # if r_laps == 7:
#     #     weather = 'rain'
#     #     print('stop running. Rain')
#     #     # time.sleep(5)
#     # weather = 'sun'
# else:
#     print('Shower')
#
# print()
# print('we run', r_laps, 'laps today')
# print('we have', health, 'health')


## 12 CASE #
#
# health = 5
# r_laps = 0
# weather = 'sun'
#
# while health > 0 and weather == 'sun':
#     r_laps += 1
#     health -= 1
#     print('run', r_laps, 'lap')
#
#
#
#
# print()
# print('we run', r_laps, 'laps today')
# print('we have', health, 'health')

## 13 CASE #
#
# health = 85
# r_laps = 0
#
#
# while r_laps != 5:
#     step = 0
#     while step != 200:
#         step += 1
#         if step % 10 == 0:
#             health -= 1
#
#         if health == 0:
#             print('Im tired, I will rest a little')
#             health += 75
#
#     r_laps += 1
#     print('run', r_laps, 'lap')
#
#
# print()
# print('we run', r_laps, 'laps today')
# print('we have', health, 'health')
## 14 CASE #

# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j, end="\t")
#     print("\n")


# try:
#     a = input("Введите первое число: ")
#     b = input("Введите второе число: ")
#     print("Результат: ", int(a)/int(b))
# except ValueError:
#     print("Пожалуйста, вводите только числа")
# except ZeroDivisionError:
#     print("На ноль делить нельзя")


# try:
#     a = input("Введите первое число: ")
#     b = input("Введите второе число: ")
#     result = int(a)/int(b)
# except (ValueError, ZeroDivisionError):
#     print("Что-то пошло не так...")
# else:
#     print("Результат в квадрате: ", result**2)


# -*- coding: utf-8 -*-

# try:
#     a = input("Введите первое число: ")
#     b = input("Введите второе число: ")
#     result = int(a)/int(b)
# except (ValueError, ZeroDivisionError):
#     print("Что-то пошло не так...")
# else:
#     print("Результат в квадрате: ", result**2)
# finally:
#     print("Вот и сказочке конец, а кто слушал - молодец.")


# while True:
#     a = input("Введите число: ")
#     b = input("Введите второе число: ")
#     try:
#         result = int(a)/int(b)
#     except ValueError:
#         print("Поддерживаются только числа")
#     except ZeroDivisionError:
#         print("На ноль делить нельзя")
#     else:
#         print(result)
#         break

# try:
#     apples = int(input("Enter the amount of apples you have: "))
#     if apples < 0:
#         raise Exception
#     print("You have", apples, "apples")
# except Exception:
#     print("You can’t have", apples, "apples")

# try:
#     raise ValueError
# except ValueError:
#     print("Improper value was obtained")
# except Exception:
#     print("Hmm... Something went wrong")


# try:
#     v1 = int(input("Enter the amount of received items: "))
#     # items_type = input("Specify the type of received items: ")
#     v2 = int(input("Enter the number of parts: "))
#     v3 = v1 / v2
#     print("Supply of", v3, "saved")
#     print("Each of", v1, "parts consists of", v2)
# except (ValueError, ZeroDivisionError):
#     print("Improper value was obtained")

# for i in range(1, 10):
#     print('1')
#     for j in range(1, 10):
#         print('\t2')
#         for j in range(1, 10):
#             print('\t\t3')
    #print()


# A = [[20, 4, 9],
#      [1, 9, 87],
#      [22, 56, 0]]
#
# for row in A:
#     for elen in row:
#         print(elen, end='\t|')
#     print()


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


my_lst = list(map(int,input().split()))
# 3 4 5 2 3 4 5 6 1 2 8	
print(my_lst)
# [3, 4, 5, 2, 3, 4, 5, 6, 1, 2, 8]

my_lst = list(range(5))
print(my_lst)
# [0, 1, 2, 3, 4]
my_lst = list(range(1, 25, 2))
print(my_lst)
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]

my_lst = []

for i in range(1, 21):
	if i % 2 == 0:
		my_lst.append(i)
print(my_lst)

my_lst = [i for i in range(1, 21) if i % 2 == 0]
print(my_lst)
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]

lst_1 = [1, 2, 2, 3]
print(2 in lst_1)
print(4 in lst_1)
lst_2 =[]

for i in lst_1:
	if i not in lst_2:
		lst_2.append(i)
		
print(lst_2)

my_str = '6emds83mmsad99342n42ld9xm37vn4820'
my_lst2 = [i for i in my_str if i.isnumeric()]
print(my_lst2)
#['6', '8', '3', '9', '9', '3', '4', '2', '4', '2', '9', '3', '7', '4', '8', '2', '0']
# unpacking list

lst = [1, 2, 3, 4, 5]
lst2 = ['a', 'b', 'c', 'd', 'e']

print(*lst)
print(*lst2)
###
lst = [7, 6, 0, 9, 5, 3, 2, 8, 1]
lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)

my_lst = ['яблоко', 'ананас', 'груша']
my_lst.sort()
print(my_lst)

my_lst.sort(reverse=True)
print(my_lst)
###
# 3,4,2,7,8,9,1,11,2,56,2,6,81

#st = [int(i) for i in input().split(',')]
#lst_odd = [i for i in st if i % 2 != 0]
#lst_even = [i for i in st if i % 2 == 0]
#print(*lst_odd)
#print(*lst_even)

###
# кіт осел пес авто
vowels = 'аиеоуієюя'
st = input().split()

#lst1 = [i for i in st if i[0] in vowels]
#lst2 = [i for i in st if i not in lst1]
# АБО
lst1 = []
lst2 = []

for i in st:
	if i[0] in vowels:
		lst1.append(i)
	else:
		lst2.append(i)


print(*lst1)
print(*lst2)

