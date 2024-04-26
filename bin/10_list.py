"""
MUTABLE
- List: We have option to store collection of values like list of names, list of email-ids etc
    - We can store duplicate values
    - automatically index number will be assigned to each value
"""
print("list PART-1")
print("Store the values")
print("-"*20)
# -----------

my_list_1 = [10, 12.5, "python", (100, 200)]
# it will create list class object and store the values

# OR we can make use of classname
my_list_2 = list((10, 12.5, "python", (100, 200)))

print(my_list_1, my_list_2, sep="\n")

print("#"*40, end="\n\n")
# ###############################

print("list PART-2")
print("Indexes ARE similar to strings")
print("-"*20)
# -----------

my_list = [10, 12.5, "python", (100, 200)]
print("my_list:", my_list, end="\n\n")

print("Course Name:", my_list[2]) # "python"
print("2nd character in Course Name:", my_list[2][1], end="\n\n") # "y"

# x = my_list[3]
# x = (100, 200)
# value = x[0]
print("Inner list:", my_list[3]) # (100, 200)
print("1st Value in Inner list:", my_list[3][0]) # 100

print("#"*40, end="\n\n")
# ###############################


print("list PART-3")
print("Methods inside 'list' class")
print("-"*20)
# -----------

my_list = [10, 12.5, "python", (100, 200)]

print(dir(my_list))
# OR
# print(dir(list))

print("#"*40, end="\n\n")
# ###############################