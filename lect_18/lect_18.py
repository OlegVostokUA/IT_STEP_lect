#
# """
# >>> s_is_empty()
# True
# >>> s_push(1)
# >>> s_push(2)
# >>> s_push(3)
# >>> s_is_empty()
# False
# >>> s_pop()
# 3
# >>> s_pop()
# 2
# >>> s_pop()
# 1
# >>> s_is_empty()
# True
# """
#
# our_stack = []
#
# def s_push(x):
#     our_stack.append(x)
#
# def s_pop():
#     x = our_stack.pop()
#     return x
#
# def clear_s():
#     our_stack.clear()
#
# def s_is_empty():
#     return len(our_stack) == 0
#
# def s_top(): #
#     x = our_stack[-1]
#     return x
#
#
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()

# def factorial(n):
#     """
#     >>> [factorial(n) for n in range(6)]
#     [1, 1, 2, 6, 24, 120]
#     >>> factorial(10)
#     3628800
#
#     >>> factorial(-1)
#     Traceback (most recent call last):
#     ...
#     ValueError: n must be > 0
#     >>> factorial(1e100)
#     Traceback (most recent call last):
#     ...
#     OverflowError: too large
#     """
#
#     if not n >= 0:
#         raise ValueError('n must be > 0')
#     if n+1 == n:
#         raise OverflowError('too large')
#     result = 1
#     factor = 2
#     while factor <= n:
#         result *= factor
#         factor += 1
#     return result
#
#
# #factorial(1e100)

class Calculator:
    def __init__(self):
        pass

    def add(self, x1, x2):
        return x1 + x2

    def mult(self, x1, x2):
        return x1 * x2

    def sub(self, x1, x2):
        return x1 - x2

    def divide(self, x1, x2):
        if x1 != 0 and x2 != 0:
            return x1 / x2
        else:
            return 'Zero !!!'




