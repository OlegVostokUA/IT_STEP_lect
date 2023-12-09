# try:
#     print(5)
#     print(5)
# except:

# try:
#     a = input()
#     b = input()
#     result = int(a) / int(b)
#
# except (ValueError, ZeroDivisionError):
#     print('Please, enter digits')
# except Exception:
#     print('Its exp-n block')
# else:
#     print('Result:', result ** 2)
# finally:
#     print('Program END')

# try:
#     apples = int(input())
#     if apples < 0:
#         raise Exception
#     # gfdggfd
#     print('You have', apples, 'apples')
#
# except Exception:
#     print('you cant have', apples)

# 1, 2, 3, 4, 5
# for
import time

# word = 'alligator'
#
# print(word[7])
#
# for numb, i in enumerate(word):
#     print(numb, i)

# running man

# health = 5
# weather = 'sun'
# laps = 0
#
# for i in range(1, health+1):
#     if weather == 'sun':
#         print('run', i, 'lap')
#         laps += 1
#         if laps == 3:
#             break

health = 5
weather = 'sun'
laps = 0

while health != 0:
    health -= 1
    laps += 1
    print('run', laps)


print()
print(laps)



