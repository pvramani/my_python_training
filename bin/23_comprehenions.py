"""
Comprehensions: We can write expression in list/tuple/dict/set
"""

print("List Comprehensions")
print("-"*20)
# -----------

my_list = [10, 20, 30, 40]
print("my_list:", my_list)

my_squared_list = [i*i for i in my_list]
print("my_squared_list:", my_squared_list)

my_even_squared_list = [i*i for i in my_list if i%2 == 0]
print("my_even_squared_list:", my_even_squared_list)

print("#"*40, end="\n\n")
# ###############################
print("Tuple Comprehensions: It is not tuple, it is generator")
print("-"*20)
# -----------

my_list = [10, 20, 30, 40]
print("my_list:", my_list)

my_squared_generator = (i*i for i in my_list)
print("my_squared_generator:", my_squared_generator)
print("my_squared_generator to list:", list(my_squared_generator))

print("#"*40, end="\n\n")
# ###############################
print("Dictionary Comprehension")
print("-"*20)
# -----------

my_list = [10, 20, 30, 40]
print("my_list:", my_list)

my_dictionary = {i:j for i, j in enumerate(my_list)}
print("my_dictionary:", my_dictionary)

# Example
# >>> my_list = [10, 20, 30, 40]
# >>> my_list = [(0, 10), (1,20), (2,30), (4,40)]
# >>> # We can use builtin function enumerate() ti make index/value pair
# >>> my_list = [10, 20, 30, 40]
# >>> e = enumerate(my_list)
# >>> list(e)
# [(0, 10), (1, 20), (2, 30), (3, 40)]

print("#"*40, end="\n\n")
# ###############################
print("Set Comprehensions")
print("-"*20)
# -----------

my_list = [10, 20, 30, 40]
print("my_list:", my_list)

my_set = {i*i for i in my_list}
print("my_set:", my_set)

print("#"*40, end="\n\n")
# ###############################