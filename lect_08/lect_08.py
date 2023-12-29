# student_1 = ['Jack', 25, 125]
# student_2 = ['John', 22, 195]
#
# print(f'Name: {student_1[0]}')
# print(f'Age: {student_1[1]}')
# print(f'Score: {student_1[2]}')
import time


# def print_cons(x, y):
#     result = x * y
#     result_2 = x ** y
#     return result, x, y, result_2
#
#
# a = 15
# b = 18
#
# q,w,e,r = print_cons(a, b)
# print(q,w,e,r)

# def check(customer, customers):
#     result = 0
#
#     for i in range(len(customers)):
#         if customers[i] == customer:
#             result += 1
#
#     discount = result * 0.589
#     print(discount)
#
#     return discount
#
# customers_list = ['Bob', 'Anna', 'Joe', 'Bob']
#
# my_customer = 'Bob'
#
# print('Customer', my_customer, 'will get discount', check(my_customer, customers_list))

def mean_d(*args): # 1 2 3
    a = 0 # 1 # 3
    b = 0 # 1 # 2
    # print(args, type(args))
    for i in args:
        a = i + a
        b += 1

    return a / b

# print(mean_d(1,2,3))
# print(mean_d(1,2,3,4,5,6))
# print(mean_d(3,3,3))
A = [1, 2]
print(mean_d(*A))
