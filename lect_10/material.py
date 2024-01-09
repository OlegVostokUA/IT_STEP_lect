### higher order functions
### CASE 1
lst_origin = [2, 4, 6, 8]


def calculate(list_digits, func_calc):
    lst_change = []
    for i in list_digits:
        change_chr = func_calc(i)
        # print(change_chr)
        lst_change.append(change_chr)

    return lst_change


def double(n):
    return n + n


def mult(n):
    return n * n

print('###')
calculate(lst_origin, double)
print('###')
calculate(lst_origin, mult)

print('###')
print(calculate(lst_origin, double))
print('###')
print(calculate(lst_origin, mult))
##### CASE 2
def nameUpper(name):
    return 'user'+name.upper()

def nameLower(name):
    return 'user'+name.lower()

def makeLog(userName, maker):
    return maker(userName)

user = input("Input your name: ")
userAnsw = input("Select login-maker: 1-lower case; 2 -upper case ")


if userAnsw == '1':
    print(makeLog(user, nameLower))
elif userAnsw == '2':
    print(makeLog(user, nameUpper))
else:
    print("Wrong input!")

## CASE 3
adminPassw='111'
studentPassw='222'

def userLogIn(userLog, userPass):
    if (userLog.lower() == 'admin') and (userPass == adminPassw):
        print("Welcome, admin")
    elif (userLog.lower() == 'student') and (userPass == studentPassw):
        print("Welcome, student")
    else:
        print("Wrong data")

def changePass(userLog, userPass):
    global adminPassw
    global studentPassw
    if (userLog.lower() == 'admin') and (userPass == adminPassw):
        adminPassw = input("Input new password for admin:")
    elif (userLog.lower() == 'student') and (userPass == studentPassw):
        studentPassw = input("Input new password for student:")
    else:
        print("Wrong data")

def userAction(login, passw, action):
    return action(login, passw)

userL=input("Login: ")
userP=input("Password: ")
userAnsw=input("1: LogIn; 2: Change password ")

if userAnsw == '1':
    userAction(userL, userP, userLogIn)
elif userAnsw == '2':
    userAction(userL, userP, changePass)
else:
    print("Wrong data")

### enclosing
### CASE 1
def sayUserHello(user):
    msg="Hello, "+ user
    def showMsf():
        print(msg+"! Let's start...")

    showMsf()

sayUserHello('admin') #Hello, admin! Let's start...
# ### CASE 2
def sayUserHello(user):
    msg="Hello, "+ user
    def showMsf():
        msg="Student"
        print(msg+"! Let's start...")
    showMsf()
    print(msg)

sayUserHello('admin')
### CASE 3
def sayUserHello(user):
    msg = "Hello, " + user
    print(msg)
    def showMsf():
        nonlocal msg
        msg = "Student"
        print(msg + "! Let's start...")
    showMsf()
    print(msg)

sayUserHello('admin')

##### carring
## CASE 1
def sendMsg(userTo, msgTxt):
    print(f"Dear {userTo}, welcome to Python world! {msgTxt}")

sendMsg('admin', 'Have a nice day!')
sendMsg('admin', 'See you!')
sendMsg('admin', 'Good luck!')
sendMsg('student', 'Good luck!')

## CASE 2
def sendMsg(userTo):
    def setMsg(msgTxt):
        print(f"Dear {userTo}, welcome to Python world! {msgTxt}")

    return setMsg

user_admin = sendMsg('Admin')
user_admin('Have a nice day')
user_admin('See you')
user_admin('Good luck1')
sendMsg('Student')('Hello')

## CASE 3
def sendMsg(userTo):
    def setMsg(msgTxt):
        def setUserFrom(userFrom):
            def setLang(lang):
                print(f'Dear {userTo}, Hello from {userFrom}.'
                      f'Welcome to {lang} world! {msgTxt}')

            return setLang
        return setUserFrom
    return setMsg

case1 = sendMsg('Admin')('Hello')('superuser')
case2 = sendMsg('Student')('Good luck!!!')

case1('C++')
case2('Teacher')('Python')

#### decorators
## CASE 1
def string_print():
    print('Hello. Happy new year!!!')

var = 'Hello. Happy new year!!!'

print('case 1')
string_print()

### CASE 2
print('case 2')
print('*   *   *   *   *')
print('  *   *   *   *')
string_print()
print('  *   *   *   *')
print('*   *   *   *   *')

### CASE 3
print('case 3')
print('* * * * * * * * * *')
print(' * * * * * * * * *')
string_print()
print(' * * * * * * * * *')
print('* * * * * * * * * *')

###CASE 4
def decorator_1(my_function):
    print('Im decorator #1')
    def wrapper():
        print('*   *   *   *   *')
        print('  *   *   *   *')
        my_function()
        print('  *   *   *   *')
        print('*   *   *   *   *')
    return wrapper

def decorator_2(my_function):
    print('Im decorator #2')
    def wrapper():
        print('* * * * * * * * * *')
        print(' * * * * * * * * *')
        my_function()
        print(' * * * * * * * * *')
        print('* * * * * * * * * *')
    return wrapper

@decorator_2
@decorator_1
def string_print():
    print('Hello. Happy new year!!!')

string_print()

def decorator_1(my_function):
    # Створюємо нову функцію
    def decorated_function(*args, **kwargs):
        print('decorator 1 start')
        my_function(*args, **kwargs) # Виклик функції
        print('decorator 1 finish')
    # Повертаємо декоровану функцію
    return decorated_function

def decorator_2(my_function):
    # Створюємо нову функцію
    def decorated_function(*args, **kwargs):
        print('     decorator 2 start')
        my_function(*args, **kwargs) # Виклик функції
        print('     decorator 2 finish')
    # Повертаємо декоровану функцію
    return decorated_function

@decorator_1
@decorator_2
def seyHello():
    print('             SAY HELLO FUNC')

seyHello()
### CASE 5
def decorator_1(my_function):
    print('Im decorator #1')
    def wrapper(var_in_f):
        print('*   *   *   *   *')
        print('  *   *   *   *')
        my_function(var_in_f)
        print('  *   *   *   *')
        print('*   *   *   *   *')
    return wrapper

def decorator_2(my_function):
    print('Im decorator #2')
    def wrapper(var_in_f):
        print('* * * * * * * * * *')
        print(' * * * * * * * * *')
        my_function(var_in_f)
        print(' * * * * * * * * *')
        print('* * * * * * * * * *')
    return wrapper


@decorator_1
def string_print(var_in_f):
    print(var_in_f)

var = 'Hello. Happy new year!!!'

string_print(var)
### CASE 6
def decorator_1(my_function):
    print('Im decorator #1')
    def wrapper(var_in_f):
        print('*   *   *   *   *')
        print('  *   *   *   *')
        a = my_function(var_in_f)
        print('#' * a)
        print('  *   *   *   *')
        print('*   *   *   *   *')
    return wrapper

@decorator_1
def string_print(var_in_f):
    return var_in_f * 2

var = 22

# print(string_print(var))
string_print(var)
### CASE 7
import time

def decorator_1(my_function):
    def wrapper(*args):
        current_time = time.time()
        rez = my_function(*args)
        delta_time = time.time() - current_time
        print(f'Час виконання: {delta_time}')
        # print(rez)
        # return rez
    return wrapper

@decorator_1
def list_gen(a, b):
    lst = []
    for i in range(a, b):
        i += 1
        lst.append(i)
    print('DONE')
    return lst

list_gen(0, 30000000)
### CASE 8
def num_decorator(n):
    def decorator_1(function):
        def wrapper(*args):
            stars = (n * "*")
            result = function(*args)
            result = stars, result, stars
            return result

        return wrapper
    return decorator_1


@num_decorator(25)
def calculate(a, b):
    return (a+b) * 2

calculate(2, 25)




## functools
### CASE 9
from functools import partial

def myltipleText(myStr, n):
    return myStr*n

doubleMyltipleText = partial(myltipleText, 2)
tripleMyltipleText = partial(myltipleText, 3)
print(doubleMyltipleText("Python")) #PythonPython
print(tripleMyltipleText("Python")) #PythonPythonPython

## CASE 10
from functools import reduce

numbers = [1, 2, 3, 4, 5]

def mySum(x, y):
    return x+y


result1 = reduce(mySum, numbers)
print(f"sum is {result1}") #15
result2 = reduce(mySum, numbers, 10)
print(f"sum is {result2}") #15
