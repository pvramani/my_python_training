print("Handling exceptions Using exception classes")
print("-"*20)
# -----------

# - For exception handling, we need to have exception classes
# - Few exception classes are present in builtins
# - we can also write user defined exception class
# - For all the exception classes super class is 'Exception'

try:
    a = 10
    b = 0
    result = a/x # NameError
    print("result:", result)
except ZeroDivisionError:
    print("This is ZDE")
except NameError as ne:
    print("This is Name Error and value of ne:", ne)
except (KeyError, IndexError):
    print("It can be KE or IE")

print("#"*40, end="\n\n")
# ###############################
print("try-except-else")
print("-"*20)
# -----------

try:
    my_file_handle = open("xyzsdsds.txt", "r")
except:
    print("Handling Only File Not Found Error")
else:
    print("In Else block")
    print("We do read/write operations")

# If "try" success then execute "else" block and skip "except" block
# If "try" failed then execute "except" block and skip "else" block

print("#"*40, end="\n\n")
# ###############################
print("try-except-else-finally")
print("-"*20)
# -----------

try:
    my_file_handle = open("xyz.txt", "w")
except:
    print("In Except")
    print("Handling Only File Not Found Error")
else:
    print("In else, writing 10 to file")
    my_file_handle.write('10')
finally:
    print("Reached Finally, closing file connection")
    my_file_handle.close()

# if "try" success/failed, "finally" will execute
# if "except" success/failed, "finally" will execute
# if "else" success/failed, "finally" will execute
# "Finally" will execute always
# so we use this block for closing/cleanup activity


print("#"*40, end="\n\n")
# ###############################
print("About 'assert' statement")
print("-"*20)
# -----------

a = 10
assert a == 10
# If condition fails then throw AssertionError

print("#"*40, end="\n\n")
# ###############################

print("We can catch even assertion error")
print("-"*20)
# -----------

try:
    a = 10
    assert a != 10
    # If condition fails then throw AssertionError
except AssertionError:
    print("This is AssertionError")

print("#"*40, end="\n\n")
# ###############################
print("About 'raise' statement")
print("-"*20)
# -----------

# Using 'assert', we can throw only AssertionError
# BUT using 'raise' we can throw any type of Error

x = 10

if x < 10:
    raise MemoryError
if x > 10:
    raise FileNotFoundError
if x != 10:
    raise ArithmeticError

print("#"*40, end="\n\n")
# ###############################


print("We can catch exception raised by 'raise' statement")
print("-"*20)
# -----------


try:
    x = 10

    if x < 10:
        raise MemoryError
    if x > 10:
        raise FileNotFoundError
    if x == 10:
        raise ArithmeticError

except Exception as e: # Exception is super class and receive any type of error
    print("Error in try and error type is:", type(e))

print("#"*40, end="\n\n")
# ###############################
print("User defined exception class example -1")
print("-"*20)
# -----------

# Mandatory Step: It should be subclass of 'Exception' class

class MyError(Exception):
    pass
# It is valid exception

try:
    x = 10

    if x < 10:
        raise MyError
    if x > 10:
        raise MyError
    if x == 10:
        raise MyError

except MyError:
    print("This MyError")

print("#"*40, end="\n\n")
# ###############################

print("User defined exception class example -2")
print("-"*20)
# -----------

# Requirement: Pass some message while raising exception

class MyError(Exception):
    def __init__(self, msg):
        self.error_message = msg


try:
    x = 10

    if x < 10:
        raise MyError("Here value of x is less than 10")
    if x > 10:
        raise MyError("Here value of x is greater than 10")
    if x == 10:
        raise MyError("Here value of x is equal to 10")

except MyError as me:
    print("This MyError Detail:", me.error_message)

print("#"*40, end="\n\n")
# ###############################