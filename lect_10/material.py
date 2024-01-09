# higher order functions
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


# print('###')
# calculate(lst_origin, double)
# print('###')
# calculate(lst_origin, mult)

# print('###')
# print(calculate(lst_origin, double))
# print('###')
# print(calculate(lst_origin, mult))
###### CASE 2

# def nameUpper(name):
#     return 'user'+name.upper()
#
# def nameLower(name):
#     return 'user'+name.lower()
#
# def makeLog(userName, maker):
#     return maker(userName)
#
# user = input("Input your name: ")
# userAnsw = input("Select login-maker: 1-lower case; 2 -upper case ")
#
#
# if userAnsw == '1':
#     print(makeLog(user, nameLower))
# elif userAnsw == '2':
#     print(makeLog(user, nameUpper))
# else:
#     print("Wrong input!")

### CASE 3
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
