"""
- Strings: We have option to store collection of characters like name, email-id etc
    - automatically index number will be assigned to each character
"""

print("Strings PART-1")
print("-"*20)
# -----------

a = 'PERSON'
# Internally it will create object of builtin-class 'str' and store the values

# OR
b = str('PERSON')

print(a, b, sep="\n")

print("#"*40, end="\n\n")
# ###############################

print("Strings PART-2")
print("-"*20)
# -----------

a = 'PERSON'
b = "PERSON'S"
c = '''PERSON'S HEIGHT IS XYZ" (" represents inches)'''
d = """PERSON'S HEIGHT IS XYZ" (" represents inches)"""

# multi line comments are strings only but not assigned to any variable

print(a, b, c, d, sep="\n")

print("#"*40, end="\n\n")
# ###############################

print("Strings PART-3")
print("-"*20)
# -----------

a = 'C:\newfolder\test.py'
# by default \n will get replaced with new line & \t will get replaced with tab space

b = r'C:\newfolder\test.py'
# r-> raw string It will not replace \n\t etc with newline/tab space

print("Value of a:", a)
print("Value of b:", b)
print("Convert 'a' to raw format:", repr(a))

print("#"*40, end="\n\n")
# ###############################

print("Strings PART-4")
print("-"*20)
# -----------

x = 10
y = 20
z = x + y

result = f'add of {x} and {y} is {z}'
# f-> format
# f-> replaces {var_name} with value

print("x + y result is:", result)

print("#"*40, end="\n\n")
# ###############################


print("Strings PART-5")
print("Indexes: We can access each character using index")
print("-"*20)
# -----------

# Refer 7_strings.xlsx, Section-1

my_string = "WEL COME"
print('my_string:', my_string, end="\n\n")

print("Access 0th character using +ve index no:", my_string[0])
print("Access 0th character using -ve index no:", my_string[-8])

# print("Access 100th character using +ve index no:", my_string[100]) # IndexError

print("#"*40, end="\n\n")
# ###############################

print("Strings PART-6")
print("Slicing: We can get substring")
print("-"*20)
# -----------

# Refer 7_strings.xlsx, Section-2

my_string = "WEL COME"
print('my_string:', my_string, end="\n\n")

print("Substring b/n index-1 to 6 using +ve index no:", my_string[1:6])
print("Substring b/n index-1 to 6 using -ve index no:", my_string[-7:-2], end="\n\n")
# character at end index will not come, this is default behavior

print("Substring from index-1 to END using +ve index no:", my_string[1:])
print("Substring from index-1 to END using -ve index no:", my_string[-7:], end="\n\n")

print("Substring from BEGINNING to 6 using +ve index no:", my_string[:6])
print("Substring from BEGINNING to 6 using -ve index no:", my_string[:-2], end="\n\n")

print("my_string[:] we will get same string:", my_string[:])

print("#"*40, end="\n\n")
# ###############################

print("Strings PART-7")
print("Step Value: We can skip characters in b/n ")
print("-"*20)
# -----------

# Refer 7_strings.xlsx, Section-3

my_string = "WEL COME"
print('my_string:', my_string, end="\n\n")

print("substring from index-1 to 6 using +ve index no & default step=1:", my_string[1:6])
print("substring from index-1 to 6 using -ve index no & default step=1:", my_string[-7:-2], end="\n\n")
# Default step value=1, which means from index-1 to 6 give me every character

print("substring from index-1 to 6 using +ve index no & step=1:", my_string[1:6:1])
print("substring from index-1 to 6 using -ve index no & step=1:", my_string[-7:-2:1], end="\n\n")
# step value=1, which means from index-1 to 6 give me every character

print("substring from index-1 to 6 using +ve index no & step=2:", my_string[1:6:2])
print("substring from index-1 to 6 using -ve index no & step=2:", my_string[-7:-2:2], end="\n\n")
# step value=2, which means from index-1 to 6 give me every 2nd character

print("substring from index-1 to 6 using +ve index no & step=3:", my_string[1:6:3])
print("substring from index-1 to 6 using -ve index no & step=3:", my_string[-7:-2:3], end="\n\n")
# step value=3, which means from index-1 to 6 give me every 3rd character


print("#"*40, end="\n\n")
# ###############################

print("Strings PART-9")
print("Methods inside 'str' class")
print("-"*20)
# -----------

my_string = "WEL COME"

print(dir(my_string))

# OR we can also pass class name
# print(dir(str))

print("#"*40, end="\n\n")
# ###############################


print("Strings PART-10")
print("'split' method")
print("-"*20)
# -----------

my_string = "WEL COME"
print('my_string:', my_string, end="\n\n")

split_1_result = my_string.split() # split by SPACE, returns splited values in LIST
print("split_1_result:", split_1_result) # ['WEL', 'COME']

split_2_result = my_string.split('E')
print("split_2_result:", split_2_result) # ['W', 'L COM', '']

print("#"*40, end="\n\n")
# ###############################