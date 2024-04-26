"""
Functions: If we want to rewrite/copy-paste same code
more than one time then instead of rewrite/copy-paste same code
more than one time, we can keep that code in a block and reuse it
"""

print("Without using function: copy-paste/rewrite")
print("-"*20)
# -----------

a = 10
b = 20
c = a + b
print("Value of c:", c)

a = 10
b = 20
c = a + b
print("Value of c:", c)

a = 10
b = 20
c = a + b
print("Value of c:", c)

a = 10
b = 20
c = a + b
print("Value of c:", c)

print("#"*40, end="\n\n")
# ###############################

print("Using function: code reusability")
print("-"*20)
# -----------


# Function Definition
def my_func():
    a = 10
    b = 20
    c = a + b
    print("Value of c:", c)


# Function Call
my_func()
my_func()
my_func()
my_func()

print("#"*40, end="\n\n")
# ###############################