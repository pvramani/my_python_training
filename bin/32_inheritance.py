"""
Inheritance:
1) Multi level inheritance
2) multiple inheritance
"""

print("1) Multi level inheritance")
print("-"*20)
# -----------

# Assume below class is already present
class Salary:
    def store_salary(self, salary):
        self.salary = salary
    def get_salary(self):
        return self.salary

# REQUIREMENT:
# Extend above class and add below functionalities
# 1) store/get tax
# 2) modify 'get_salary' to return (salary-tax)

# Employee -> sub/child class
# Salary -> super/parent class
class Employee(Salary):
    # 1) store/get tax
    def store_tax(self, tax):
        self.tax = tax
    def get_tax(self):
        return self.tax
    # 2) modify 'get_salary' to return (salary-tax)
    # POLYMORPHISM: We can reuse same name as super class
    def get_salary(self):
        return self.salary - self.tax


e1 = Employee()
e1.store_salary(20000)
e1.store_tax(2000)
print("Salary:", e1.get_salary())
print("Tax:", e1. get_tax())

print("#"*40, end="\n\n")
# ###############################
print("2) Multiple inheritance")
print("-"*20)
# -----------

# Assume Below class is already present
class Salary:
    def store_salary(self, salary):
        self.salary = salary
    def get_salary(self):
        return self.salary

# Assume Below class also already present
class Tax:
    def store_tax(self, tax):
        self.tax = tax
    def get_tax(self):
        return self.tax

# New Requirement: Create class 'Employee' with below functionality
# 1) store/get salary
# 2) store/get tax
# 3) store/get employee names

# For 1) & 2) , we can make use of existing class
class Employee(Salary, Tax):
    def store_employee_name(self, name):
        self.name = name
    def get_employee_name(self):
        return self.name

e1 = Employee()
e1.store_employee_name("emp-1")
e1.store_salary(20000)
e1.store_tax(2000)


print("Name:", e1.get_employee_name())
print("Salary:", e1.get_salary())
print("tax:", e1.get_tax())

print("#"*40, end="\n\n")
# ###############################