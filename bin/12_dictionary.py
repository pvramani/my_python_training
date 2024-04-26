"""
- Dictionary: We have option to store collection of values like list of names, list of email-ids etc
    - We can store duplicate values
    - automatically index number will NOT be assigned to each value
        instead we can provide index to each value called KEY. or KEY/VALUE Pair.

For KEY: We should use any IMMUTABLE VALUES like numbers, strings, tuples etc
For VALUE: We can store any value. It can be IMMUTABLE/MUTABLE/User-Defined-Class-Object etc
"""


print("Dictionary PART-1")
print("Store the values")
print("-"*20)
# -----------

my_dictionary_1 = {0:"python", 1:10, 2:"online"}
# It will create object of 'dict' class and store the values

# OR
my_dictionary_2 = dict({0:"python", 1:10, 2:"online"})

# For KEY: We should use any IMMUTABLE VALUES like numbers, strings, tuples etc
my_dictionary_3 = {"course":"python", "duration":10, "mode":"online"}

# For VALUE: We can store any value. It can be IMMUTABLE/MUTABLE/User-Defined-Class-Object etc
my_dictionary_4 = {
    "duration":10,
    "course":"python",
    "mode":["online", "class room"],
    "trainer": {"fname": "abc", "lname": "xyz"}
}

print("my_dictionary_1:", my_dictionary_1, sep="\n", end="\n\n")
print("my_dictionary_2:", my_dictionary_2, sep="\n", end="\n\n")
print("my_dictionary_3:", my_dictionary_3, sep="\n", end="\n\n")
print("my_dictionary_4:", my_dictionary_4, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
# ###############################
print("Dictionary PART-2")
print("We can access each VALUE using KEY")
print("-"*20)
# -----------

# Dictionary example with tuple as KEY
# my_dictionary_5 = {
#     ("emp-1", "emp-id"): {"phone": "", "email": ""},
#     ("emp-2", "emp-id"): {"phone": "", "email": ""},
#     ("emp-3", "emp-id"): {"phone": "", "email": ""},
# }

my_dictionary = {
    "duration":10,
    "course":"python",
    "mode":["online", "class room"],
    "trainer": {"fname": "abc", "lname": "xyz"}
}

print("my_dictionary:", my_dictionary, sep="\n", end="\n\n")

print("duration:", my_dictionary["duration"], sep="\n", end="\n\n")

# x = my_dictionary["course"] # python
# value = x[1] # y
print("course:", my_dictionary["course"]) # "Python"
print("2nd char in course:", my_dictionary["course"][1], sep="\n", end="\n\n") # 'y'

# x = my_dictionary["mode"] # ["online", "class room"]
# y = x[1] # "class room"
# value = y[3] # 's'
print("mode:", my_dictionary["mode"]) # ["online", "class room"]
print("2nd mode:", my_dictionary["mode"][1]) # "class room"
print("4th char in 2nd mode:", my_dictionary["mode"][1][3], sep="\n", end="\n\n") # "s"

# x = my_dictionary["trainer"] # {"fname": "abc", "lname": "xyz"}
# y = x["lname"] # "xyz"
# value = y[1]
print("Trainer:", my_dictionary["trainer"])# {"fname": "abc", "lname": "xyz"}
print("Trainer Last Name:", my_dictionary["trainer"]["lname"]) # "xyz"
print("2nd char in Trainer Last Name:", my_dictionary["trainer"]["lname"][1]) # "y"

print("#"*40, end="\n\n")
# ###############################
print("Dictionary PART-4")
print("length of my_dictionary")
print("-"*20)
# -----------

print(len(my_dictionary))
# Internally it calls __len__ present in dict class
# inside __len__ there is logic to find length

print("#"*40, end="\n\n")
# ###############################