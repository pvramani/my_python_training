"""
In this program we are accessing variables, functions & classes
defined in mymodule.py
"""

print("1-way to import")
print("-"*20)
# -----------

import mymodule

print("course:", mymodule.course, end="\n\n")

add_result = mymodule.add(10, 20)
print("add_result:", add_result, end="\n\n")

e = mymodule.EmployeeClass()
e.store_name("emp-1")
print("Emp name:", e.get_name(), end="\n\n")

print("#"*40, end="\n\n")
# ###############################

print("2-way to import")
print("-"*20)
# -----------

import mymodule as mm

print("course:", mm.course, end="\n\n")

add_result = mm.add(10, 20)
print("add_result:", add_result, end="\n\n")

e = mm.EmployeeClass()
e.store_name("emp-1")
print("Emp name:", e.get_name(), end="\n\n")

print("#"*40, end="\n\n")
# ###############################
print("3-way to import")
print("-"*20)
# -----------

# from mymodule import *
# OR
from mymodule import course, add, EmployeeClass

print("course:", course, end="\n\n")

add_result = add(10, 20)
print("add_result:", add_result, end="\n\n")

e = EmployeeClass()
e.store_name("emp-1")
print("Emp name:", e.get_name(), end="\n\n")

print("#"*40, end="\n\n")
# ###############################

print("4-way to import")
print("-"*20)
# -----------

from mymodule import course as c, add as a, EmployeeClass as EC

print("course:", c, end="\n\n")

add_result = a(10, 20)
print("add_result:", add_result, end="\n\n")

e = EC()
e.store_name("emp-1")
print("Emp name:", e.get_name(), end="\n\n")

print("#"*40, end="\n\n")
# ###############################