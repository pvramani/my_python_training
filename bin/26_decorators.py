"""
Decorators: If we want to write more than one function where
in each function few code/logics are common
then
we can make use of decorator design pattern
"""

print("Without using Decorator")
print("-"*20)
# -----------

def add(a, b):
    print("Result is")
    print(a+b)
    print("End of the result")


def sub(a, b):
    print("Result is")
    print(a-b)
    print("End of the result")


add(10, 20)
sub(10, 20)

# Requirement: How to design/write function to reuse below code
# 1) print("Result is")
# 2) print("End of the result")
# We can think write sone common function for this
# OR decorator design pattern is already provided procedure to write such function

print("#"*40, end="\n\n")
# ###############################
print("Decorator: PARTIALLY IMPLEMENTED")
print("-"*20)
# -----------

# Functions as per decorator design pattern
def my_decorator(my_func): # my_func=sub
    def decorated_func(x, y): # We can make use this decorator for 2 arguments functions
        print("Result is")
        my_func(x,y) # sub(10,20)
        print("End of the result")
    return decorated_func


def add(a, b):
    print(a+b)

inner_func_ref = my_decorator(add)
inner_func_ref(10, 20)


def sub(a, b):
    print(a-b)

inner_func_ref = my_decorator(sub)
inner_func_ref(10, 20)

print("This is PARTIAL IMPLEMENTED DECORATOR")

print("#"*40, end="\n\n")
# ###############################
print("FINAL Decorator")
print("-"*20)
# -----------

# Functions as per decorator design pattern
def my_decorator(my_func): # my_func=add
    def decorated_func(x, y): # We can make use this decorator for 2 arguments functions
        print("Result is")
        my_func(x,y) # add(10,20)
        print("End of the result")
    return decorated_func


@my_decorator
def add(a, b):
    print(a+b)

add(10, 20)

# @my_decorator will take care of doing below 2 steps
# inner_func_ref = my_decorator(add)
# inner_func_ref(10, 20)


@my_decorator
def sub(a, b):
    print(a-b)

sub(10, 20)

# @my_decorator will take care of doing below 2 steps
# inner_func_ref = my_decorator(sub)
# inner_func_ref(10, 20)

print("This is FINAL DECORATOR")

print("#"*40, end="\n\n")
# ###############################