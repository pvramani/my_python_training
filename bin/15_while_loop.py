"""
While-loop: Based on the condition, we can execute loop
"""
print("While loop example")
print("-"*20)
# -----------

x = 0
while x < 5:
    print("Value of x:", x)
    x = x + 1 # x += 1

print("#"*40, end="\n\n")
# ###############################
print("# Case-1: 'break' - We can end while loop in-between")
print("-"*20)
# -----------

my_list = ["C++", "Java-1", "Perl", "Java-2", "Shell"]
print("my_list:", my_list, end="\n\n")

# REQUIREMENT: Check are there any value starting with Java,
# If one value found then no need to verify other values

index_no = 0
while index_no < len(my_list):
    if my_list[index_no].startswith("Java"):
        print("Course Found")
        break
    index_no += 1

# for each_value in my_list:
#     if each_value.startswith("Java"):
#         print("Course Found")
#         break

print("#"*40, end="\n\n")
# ###############################
print("# Case-2: 'continue' - We can skip current iteration & jump to next iteration")
print("-"*20)
# -----------

my_list = ["C++", "Java-1", "Perl", "Java-2", "Shell"]
print("my_list:", my_list, end="\n\n")

index_no = 0
while index_no < len(my_list):
    if not my_list[index_no].startswith("Java"):
        index_no += 1
        continue
    # Below code is applicable only for JAVA courses,
    # other courses are not required
    print("This JAVA course name is:", my_list[index_no])
    print("This is one version of 'JAVA'")
    print("This JAVA course duration is 10 days")
    index_no += 1


# for each_value in my_list:
#     if not each_value.startswith("Java"):
#         continue
#     # Below code is applicable only for JAVA courses,
#     # other courses are not required
#     print("This JAVA course name is:", each_value)
#     print("This is one version of 'JAVA'")
#     print("This JAVA course duration is 10 days")

print("#"*40, end="\n\n")
# ###############################
print("We have 'while-else' like 'if-else'")
print("-"*20)
# -----------

my_list = ["C++", "Java-1", "Perl", "Java-2", "Shell"]
print("my_list:", my_list, end="\n\n")

index_no = 0
while index_no < len(my_list):
    print("Each Value:", my_list[index_no])
    index_no += 1
else:
    print("All Iteration Completed, so deleting my_list")
    my_list.clear()
    # OR
    # del my_list

# After completing while-loop, else block will execute
# After completing while-loop, if we want to cleanup something then we can make use of 'while-else'
# Now, if use 'break' then 'break' will make sure to end-while-loop & 'else' block as well


# for each_value in my_list:
#     print("Each Value:", each_value)
# else:
#     print("All Iteration Completed, so deleting my_list")
#     my_list.clear()
#     # OR
#     # del my_list


print("#"*40, end="\n\n")
# ###############################