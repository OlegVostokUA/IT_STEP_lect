our_stack = []

def s_push(x):
    our_stack.append(x)

def s_pop():
    x = our_stack.pop()
    return x

def clear_s():
    our_stack.clear()

def s_is_empty():
    return len(our_stack) == 0

def s_top(): #
    x = our_stack[-1]
    return x
