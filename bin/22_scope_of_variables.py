"""
Variable Scope:
1) Local Scope
2) Enclosed Scope
3) Global Scope
4) Builtins Scope
"""

print("1. Local Scope")
print("-"*20)
# -----------

def f1():
    x = 10 # Local Scope, we can't access outside the function
    print("x:", x)
f1()

print("#"*40, end="\n\n")
# ###############################
print("2. Enclosed Scope")
print("-"*20)
# -----------

def f1():
    x = 10 # Enclosed Scope: We can access inside inner function but we can't access outside the function
    def f2():
        print("Value of x in f2:", x)
    f2()
f1()

print("#"*40, end="\n\n")
# ###############################
print("2. Enclosed Scope Example-2")
print("-"*20)
# -----------

def f1():
    x = 10 # Enclosed Scope: We can access inside inner function but we can't access outside the function
    def f2():
        # x = 100 This will create local variable
        nonlocal x # It refers enclosed scope variable 'x'
        x = 100
        print("Value of x in f2:", x) # 100
    f2()
    print("Value of x in f1:", x) # 100
f1()

print("#"*40, end="\n\n")
# ###############################
print("3. Global Scope Example-1")
print("-"*20)
# -----------

y = 100 # Global scope, we can access anywhere
def f1():
    print("y in f1:", y)
    def f2():
        print("y in f2:", y)
    f2()
f1()
print("Global y:", y)

print("#"*40, end="\n\n")
# ###############################
print("3. Global Scope Example-2")
print("-"*20)
# -----------

z = 100
def f1():
    # z = 20000 # It will create local variable
    global z
    z = 2000
    print("Value of z in f1:", z)
f1()
print("Value of z in global:", z)

print("#"*40, end="\n\n")
# ###############################

# 4) Builtins Scope
# 1st check for the variable in local scope
# if not present in local scope
# then
# check for the variable in enclosed scope
# if not present in enclosed scope
# then
# check for the variable in global scope
# if not present in global scope
# then
# check for the variable in builtins
# if not present in builtins
# then
# thorow NameError