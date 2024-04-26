"""
Numbers: We have option to store numbers like int, float etc
"""

print("How to store the values")
print("-"*20)
# -----------

a = 10
# Internally it will create object of builtin-class 'int' and store the values

# OR we can also use class name
b = int(10)
# If we call class name then it will create object and store it in 'b'

c = 12.5
# Internally it will create object of builtin-class 'float' and store the values

# OR we can also use class name
d = float(12.5)

print(a, b, c, d, sep="\n")

# All operators supported like +, -, * etc

e = 10
f = 2
div_result = e/f
print("div_result:", div_result)

floor_div_result = e//f
print("floor_div_result:", div_result)

power_of_2 = e ** f
print("power_of_2:", power_of_2)

print("#"*40, end="\n\n")
# ###############################