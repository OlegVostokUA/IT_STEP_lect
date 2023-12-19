# RECURSION!!!
# CASE 1
def func_1():
    print('Func 1')

def func_2():
    func_1()
    #print('Func 2')

def func_3():
    func_2()
    #print('Func 3')

def main():
    func_3()

main()
## CASE 2
def func_1(n):
    if n == 0:
        return 0
    else:
        return func_1(n-1) + int(input())

print(func_1(int(input())))
# CASE 3
def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n-1)

print(power(3, 3))