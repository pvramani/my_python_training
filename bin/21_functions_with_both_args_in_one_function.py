"""
We can combine both positional and keyword argument in one function
"""

print("Function with positional & keyword arguments")
print("-"*20)
# -----------

# before *, all args are positional
# after *, all args are keyword
def add(a, b, *, c, d):
    return a + b + c + d

add_result = add(10, 20, c=30, d=40)
print("add_result:", add_result)

print("#"*40, end="\n\n")
# ###############################