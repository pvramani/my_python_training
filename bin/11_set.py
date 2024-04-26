"""
- set: We have option to store collection of values like list of names, list of email-ids etc
    - We can store unique values
    - No index for each value
    - Unordered: It will not maintain the order of the values
    - Inside set we can store only IMMUTABLE values like numbers, string, set etc
"""
print("set PART-1")
print("Store the values")
print("-"*20)
# -----------

my_set_1 = {10, 10, 10, "Python", "Python", "Python", "Java", "Java"}
# it will create object of 'set' and store the values

my_set_2 = set([10, 10, 10, "Python", "Python", "Python", "Java", "Java"])
print(my_set_1, my_set_2, sep="\n")

print("#"*40, end="\n\n")
# ###############################

print("set PART-2")
print("Methods inside 'set' class")
print("-"*20)
# -----------

my_set_1 = set([10, 10, 10, "Python", "Python", "Python", "Java", "Java"])
print(dir(my_set_1))

print("#"*40, end="\n\n")
# ###############################