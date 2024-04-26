"""
Operator Overloading: We can support for any operators like +, - etc

For all operators, we have system defined names that we need to implement
in our class

For example:
+ -> __add__

"""

print("Supported + operator")
print("-"*20)
# -----------

class Employee:
    def __init__(self, name):
        self.name = name
    def __add__(self, other): # self=e1, other=e2
        concat_result = self.name + other.name
        return concat_result


e1 = Employee("emp-1")
e2 = Employee("emp-2")
result = e1 + e2 # Internally it will call e1.__add__(e2)
print("result:", result)

print("#"*40, end="\n\n")
# ###############################
print("Supported Iteration")
print("-"*20)
# -----------

class Employee:
    def __init__(self, name):
        self.name = name
    def __add__(self, other): # self=e1, other=e2
        concat_result = self.name + other.name
        return concat_result
    def __iter__(self):
        self.start_index = 0
        return self

    def __next__(self):
        current_index = self.start_index
        if current_index < len(self.name):
            self.start_index += 1
            return self.name[current_index]
        else:
            raise StopIteration

e1 = Employee("emp-1")
e2 = Employee("emp-2")
result = e1 + e2 # Internally it will call e1.__add__(e2)
print("'+' result:", result, end="\n\n")

# We implementation for 2 methods
# 1) __iter__() # This will be called 1st before starting the iteration
# 2) __next__() # This will be called every iteration

for i in e1:
    print("Each Char in e1:", i)

for i in e2:
    print("Each Char in e2:", i)

print("#"*40, end="\n\n")
# ###############################