"""
Generators: We can create objects whenever it is required
"""

print("Without using generator")
print("-"*20)
# -----------

def my_squares(my_list):
    my_square_result = []
    for i in my_list:
        my_square_result.append(i*i)
    return my_square_result


# Calling function
L = [10, 20, 30, 40]
square_result = my_squares(L)
for i in square_result:
    print("Value of i:", i)

# FINAL requirement is, print each squared value one by one

print("#"*40, end="\n\n")
# ###############################
print("Using generator")
print("-"*20)
# -----------

def gen_my_squares(my_list):
    for i in my_list:
        yield i * i

# Calling function
L = [10, 20, 30, 40]
gen_square_result = gen_my_squares(L)
print("gen_square_result:", gen_square_result)

# FINAL requirement is, print each squared value one by one
for i in gen_square_result:
    print("Value of i:", i*i)

print("#"*40, end="\n\n")
# ###############################