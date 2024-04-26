"""
How to create objects?
- using class we can create n number of objects

In this section, we should get 100% clarity on,
1) CLASS OBJECT
2) INSTANCE OBJECTS
"""

print("CLASS object and INSTANCE objects")
print("-"*20)
# -----------

class Employee:
    pass
# use pass to keep empty block

# create 2 objects
e1 = Employee()
e2 = Employee()

# Total 3 objects
# CLASS OBJECT: 'Employee', automatically getting created
# INSTANCE OBJECTS: 'e1' & 'e2' which we are creating

print("DATA inside BRAND NEW Class object 'Employee':", Employee)
print("DATA inside BRAND NEW Instance object 'e1':", e1)
print("DATA inside BRAND NEW Instance object 'e2':", e2)


print("METHODS/VARIABLES inside BRAND NEW Class object 'Employee':", dir(Employee), sep="\n", end="\n\n")
print("METHODS/VARIABLES inside BRAND NEW Instance object 'e1':", dir(e1), sep="\n", end="\n\n")
print("METHODS/VARIABLES inside BRAND NEW Instance object 'e2':", dir(e2), sep="\n", end="\n\n")

print("#"*40, end="\n\n")
# ###############################