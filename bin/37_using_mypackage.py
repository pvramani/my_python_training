"""
PACKAGES
We can keep/organize modules in folders & sub-folders,
these folders are called PACKAGES
"""

print("1-way to import")
print("-"*20)
# -----------

import mypackage.db.mymodule

print("course:", mypackage.db.mymodule.course, end="\n\n")

add_result = mypackage.db.mymodule.add(10, 20)
print("add_result:", add_result, end="\n\n")

e = mypackage.db.mymodule.EmployeeClass()
e.store_name("emp-1")
print("Emp name:", e.get_name(), end="\n\n")

print("#"*40, end="\n\n")
# ###############################

print("2-way to import")
print("-"*20)
# -----------

import mypackage.db.mymodule as mm

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
from mypackage.db.mymodule import course, add, EmployeeClass

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

from mypackage.db.mymodule import course as c, add as a, EmployeeClass as EC

print("course:", c, end="\n\n")

add_result = a(10, 20)
print("add_result:", add_result, end="\n\n")

e = EC()
e.store_name("emp-1")
print("Emp name:", e.get_name(), end="\n\n")

print("#"*40, end="\n\n")
# ###############################
# Environment Variable
# -----------
# - If we are keeping mymodule.py/mypackage in some other
#   drive/directory then we need to add that directory path in
#   enviroment variables
#   VARIABLE NAME: PYTHONPATH
#   VARIABLE VALUE: directory path where mymodule.py/mypackage present
# ###############################