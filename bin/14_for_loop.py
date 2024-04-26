"""
for-loop: Iterate any collection
"""

print("for-with-strings")
print("-"*20)
# -----------

my_string = "Python"
print("my_string:", my_string, end="\n\n")

# syntax: for some_variable in some_collection

for each_char in my_string:
    print("Each Char:", each_char)

print("#"*40, end="\n\n")
# ###############################
print("for-with-list/tuple/set/any-other-collection")
print("-"*20)
# -----------

my_list = ["C++", "Java-1", "Perl", "Java-2", "Shell"]
print("my_list:", my_list, end="\n\n")

for each_value in my_list:
    print("Each Value:", each_value)

print("#"*40, end="\n\n")
# ###############################
print("for-with-Dictionary.Keys()")
print("-"*20)
# -----------

my_dictionary = {"course": "python", "duration": 10, "mode": "online"}
print("my_dictionary:", my_dictionary, end="\n\n")

# >>> my_dictionary.keys()
# ['course', 'duration', 'mode']
for each_key in my_dictionary.keys():
    print("Key:", each_key)
    print("Value:", my_dictionary[each_key])


print("#"*40, end="\n\n")
# ###############################
print("for-collection-of-collections")
print("-"*20)
# -----------

my_list = [(10, 20), (100,200), (1000, 2000)]
print("my_list:", my_list, end="\n\n")

for i in my_list:
    print("i:", i)
    print("0th Value:", i[0])
    print("1st Value:", i[1])

print("\n\n")

for m, n in my_list:
    print("m:", m)
    print("n:", n)

print("#"*40, end="\n\n")
# ###############################
# 2 Cases
# -----------
# Case-1: 'break' - We can end for loop in-between
# Case-2: 'continue' - We can skip current iteration & jump to next iteration
# ###############################

print("# Case-1: 'break' - We can end for loop in-between")
print("-"*20)
# -----------

my_list = ["C++", "Java-1", "Perl", "Java-2", "Shell"]
print("my_list:", my_list, end="\n\n")

# REQUIREMENT: Check are there any value starting with Java,
# If one value found then no need to verify other values

for each_value in my_list:
    if each_value.startswith("Java"):
        print("Course Found")
        break

print("#"*40, end="\n\n")
# ###############################
print("# Case-2: 'continue' - We can skip current iteration & jump to next iteration")
print("-"*20)
# -----------

my_list = ["C++", "Java-1", "Perl", "Java-2", "Shell"]
print("my_list:", my_list, end="\n\n")


for each_value in my_list:
    if not each_value.startswith("Java"):
        continue
    # Below code is applicable only for JAVA courses,
    # other courses are not required
    print("This JAVA course name is:", each_value)
    print("This is one version of 'JAVA'")
    print("This JAVA course duration is 10 days")

print("#"*40, end="\n\n")
# ###############################
print("We have 'for-else' like 'if-else'")
print("-"*20)
# -----------

my_list = ["C++", "Java-1", "Perl", "Java-2", "Shell"]
print("my_list:", my_list, end="\n\n")

for each_value in my_list:
    print("Each Value:", each_value)
else:
    print("All Iteration Completed, so deleting my_list")
    my_list.clear()
    # OR
    # del my_list

# After completing for-loop, else block will execute
# After completing for-loop, if we want cleanup something then we can make use of 'for-else'
# Now, if use 'break' then 'break' will make sure to end-for-loop & 'else' block as well

print("#"*40, end="\n\n")
# ###############################