# def mean_d(*args):
#     a = 0
#     b = 0
#     print(args, type(args))
#     for i in args:
#         a = i + a
#         b += 1
#
#     return a / b
#
# # print(mean_d(1,2,3))
# # print(mean_d(1,2,3,4,5,6))
# # print(mean_d(3,3,3))
# A = [1,2,3,4,5,6]
# print(mean_d(*A))

# users = [
#     ['user1', '111'],
#     ['user2', '222'],
#     ['user3', '333']
# ]
#
# def user_info(*clients):
#
#     for i in range(len(clients)):
#         if i == 0:
#             print(f'Login: {clients[i]}')
#         elif i == 1:
#             print(f'Password: {clients[i]}')
#
# for user in users:
#     user_info(*user)

# user1 = 'Aleks'


# def user_log():
#     global user1
#     user1 = 'Vlad'
#     print(user1)
#     print(id(user1))
#
# user_log()
#
# print(user1)
# print(id(user1))
#
# us_log = user_log()

# def factorial_n(n): # 3
#     if n <= 0:
#         return 1
#     else:
#         return n * factorial_n(n-1)
#
# print(factorial_n(5))

# def func_1():
#     print('FUNC 1')
#
# def func_2():
#     func_1()
#     print('FUNC 2')
#
# def func_3():
#     func_2()
#     print('FUNC 3')
#
#
# def main():
#     func_3()
#
#
# main() ###
#
# print(';fggdfgf')


#
#
#
# def add10(x):
#     return x+100
#
# var_f = add10
#
# for i in numb:
#     print(var_f(i))
#
#
# var_l = lambda x: x+100
#
# for i in numb:
#     print(var_l(i))
numb = [2, 50, 35, 12]
numb2 = ['W', 'G', 'L', 'X']


for s, n in zip(numb, numb2):
    if s == 'L' or n == 'L':
        print(';find')
#
# numb2 = list(filter(lambda x:x>25, numb))
# print(numb2)