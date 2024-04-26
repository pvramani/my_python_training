"""
Conditional Statement 'if': Based on the condition, we can execute block of code

In some languages, we will write 'if-block' like

if some_condition
{
s1
    s2
        s3
    s4
s5
}
s6

In Python, we won't use {} to make block, INSTEAD we use INDENTATION

if some_condition
    s1
    s2
    s3
    s4
    s5
s6
"""

print("Only 'if'")
print("-"*20)
# -----------

x = 10
if x == 10:
    print("Value of x is eq to 10")
    print("Value of x is eq to 10")

if x > 10:
    print("Value of x is gt 10")
    print("Value of x is gt 10")

if x < 10:
    print("Value of x is lt 10")
    print("Value of x is lt 10")

print("#"*40, end="\n\n")
# ###############################
print("Only 'if-elif'")
print("-"*20)
# -----------

x = 10
if x == 10:
    print("Value of x is eq to 10")
    print("Value of x is eq to 10")

elif x > 10:
    print("Value of x is gt 10")
    print("Value of x is gt 10")

elif x < 10:
    print("Value of x is lt 10")
    print("Value of x is lt 10")

print("#"*40, end="\n\n")
# ###############################

print("Only 'if-elif-else'")
print("-"*20)
# -----------

x = 10
if x == 10:
    print("Value of x is eq to 10")
    print("Value of x is eq to 10")

elif x > 10:
    print("Value of x is gt 10")
    print("Value of x is gt 10")

else:
    print("Value of x is lt 10")
    print("Value of x is lt 10")

print("#"*40, end="\n\n")
# ###############################
print("if-with-strings")
print("-"*20)
# -----------

my_string = "Python"
print("my_string:", my_string, end="\n\n")

if "tho" in my_string:
    print("Substring 'tho' found")

if my_string != "Java" or my_string != "C++":
    print("Not Java/C++")

print("#"*40, end="\n\n")
# ###############################
print("if-with-list/tuple/set/any-other-collection")
print("-"*20)
# -----------

my_list = ["C++", "Java-1", "Perl", "Java-2", "Shell"]
print("my_list:", my_list, end="\n\n")

if "Java-1" in my_list:
    print("Value 'Java-1' found")

print("#"*40, end="\n\n")
# ###############################
print("if-with-Dictionary")
print("-"*20)
# -----------

my_dictionary = {"course": "python", "duration": 10, "mode": "online"}
print("my_dictionary:", my_dictionary, end="\n\n")

# >>> my_dictionary.keys()
# ['course', 'duration', 'mode']
if 'course' in my_dictionary.keys():
    print("Key Found")

# >>> my_dictionary.values()
# ['python', 10, 'online']
if 'python' in my_dictionary.values():
    print("Value 'python' found")

# >>> my_dictionary.items()
# [('course', 'python'), ('duration', 10), ('mode', 'online')]
if ('mode', 'online') in my_dictionary.items():
    print("Value ('mode', 'online') Found")

print("#"*40, end="\n\n")
# ###############################