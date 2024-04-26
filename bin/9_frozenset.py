"""
- Frozenset: We have option to store collection of values like list of names, list of email-ids etc
    - We can store unique values
    - No index for each value
    - Unordered: It will not maintain the order of the values
    - Inside frozenset we can store only IMMUTABLE values like numbers, string, frozenset etc
"""
print("Frozenset PART-1")
print("Store the values")
print("-"*20)
# -----------

my_fset_1 = frozenset([10, 10, 10, "Python", "Python", "Python", "Java", "Java"])
print(my_fset_1)

print("#"*40, end="\n\n")
# ###############################
print("Frozenset PART-2")
print("Methods inside 'frozenset' class")
print("-"*20)
# -----------

my_fset_1 = frozenset([10, 10, 10, "Python", "Python", "Python", "Java", "Java"])
print(dir(my_fset_1))

print("#"*40, end="\n\n")
# ###############################