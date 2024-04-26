"""
static method
"""

print("Static Method")
print("-"*20)
# -----------

class Salary:
    def store_salary(self, salary):
        self.salary = salary
    def get_salary(self):
        return self.salary

    # REQUIREMENT: Compuete avg salary,
    # in simple term, if we pass 2 nos then it should return average

    # Since we are not using instance object inside method, no need of passing
    # instance object to 'self'
    # def compute_avg_salary(self, sal1, sal2):
    #     return (sal1+sal2)/2

    # Since we are not using class object inside method, no need of passing
    # class object to 'cls'
    # @classmethod
    # def compute_avg_salary(cls, sal1, sal2):
    #     return (sal1+sal2)/2

    # Here instance/class object WILL NOT BE PASSED as 1st argument
    @staticmethod
    def compute_avg_salary(sal1, sal2):
        return (sal1 + sal2) / 2


e1 = Salary()
e2 = Salary()

e1.store_salary(20000)
e2.store_salary(22000)

s1 = e1.get_salary()
s2 = e2.get_salary()

avg = Salary.compute_avg_salary(s1, s2) # We call using instance/class object
print("avg:", avg)

print("#"*40, end="\n\n")
# ###############################