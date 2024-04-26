"""
IMMUTABLE
- Tuple: We have option to store collection of values like list of names, list of email-ids etc
    - We can store duplicate values
    - automatically index number will be assigned to each value
"""
print("Tuple PART-1")
print("Store the values")
print("-"*20)
# -----------

my_tuple_1 = (10, 12.5, "python", (100, 200))
# it will create tuple class object and store the values

print("Tuple PART-2")
print("Indexes ARE similar to strings")
print("-"*20)
# -----------

my_tuple = (10, 12.5, "python", (100, 200))
print("my_tuple:", my_tuple, end="\n\n")

print("Course Name:", my_tuple[2]) # "python"
print("2nd character in Course Name:", my_tuple[2][1], end="\n\n") # "y"

# x = my_tuple[3]
# x = (100, 200)
# value = x[0]
print("Inner tuple:", my_tuple[3]) # (100, 200)
print("1st Value in Inner tuple:", my_tuple[3][0]) # 100

print("#"*40, end="\n\n")
# ###############################