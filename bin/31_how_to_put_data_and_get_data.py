"""
How to put data and get data

3-way to put data and get data

In this section, we should get 100% clarity on,
1) CONSTRUCTOR: __new__() # Has logic to construct object
2) Initializer: __init__()
When we create object both __new__() and __init__() will execute
"""

print("3-way to put data and get data")
print("-"*20)
# -----------

class Employee:

    def __init__(self, en): # self=e1/e2
        self.name = en

    @classmethod
    def store_company_name(cls, cn): # cls="Employee"
        cls.company_name = cn

    @classmethod # @classmethod will make usre to pass CLASS OBJECT even if we call this method using INSTANCE object e1/e2
    def get_company_name(cls):
        return cls.company_name

    def get_employee_name(self):
        return self.name


# create 2 objects
e1 = Employee("emp-1")
e2 = Employee("emp-2")

# Store the values in all 3 objects
Employee.store_company_name("XYZ Company")


# print all the values
print("DATA: company name:", Employee.get_company_name())
print("DATA: employee 1 name :", e1.get_employee_name())
print("DATA: employee 2 name :", e2.get_employee_name())

print("METHODS/VARIABLES inside BRAND NEW Class object 'Employee':", dir(Employee), sep="\n", end="\n\n")
print("METHODS/VARIABLES inside BRAND NEW Instance object 'e1':", dir(e1), sep="\n", end="\n\n")
print("METHODS/VARIABLES inside BRAND NEW Instance object 'e2':", dir(e2), sep="\n", end="\n\n")

print("#"*40, end="\n\n")
# ###############################