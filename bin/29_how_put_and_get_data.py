print("1-way to put data and get data")
print("-"*20)
# -----------

class Employee:
    pass
# use pass to keep empty block

# create 2 objects
e1 = Employee()
e2 = Employee()

# Store the data inside brandnew objects
Employee.company_name = "XYZ Company"
e1.name = "emp-1"
e2.name = "emp-2"

# print all the values
print("DATA: company name:", Employee.company_name)
print("DATA: employee 1 name :", e1.name)
print("DATA: employee 2 name :", e2.name)

print("METHODS/VARIABLES inside BRAND NEW Class object 'Employee':", dir(Employee), sep="\n", end="\n\n")
print("METHODS/VARIABLES inside BRAND NEW Instance object 'e1':", dir(e1), sep="\n", end="\n\n")
print("METHODS/VARIABLES inside BRAND NEW Instance object 'e2':", dir(e2), sep="\n", end="\n\n")

# CLASS OBJECT is common space for all instance objects,
# data which is common for all instance objects, those
# data we can keep it inside class object to save memory

print("#"*40, end="\n\n")
# ###############################