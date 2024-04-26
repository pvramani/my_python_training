"""
About print function
"""


print("print function PART-1")
print("-"*20)
# -----------

a = 100
b = 200
c = 300
d = 400

print(a, b, c, d)
# By Default sep=" ", which means print each value separated by SPACE

print(a, b, c, d, sep=",")
# sep=",", which means print each value separated by COMMA

print(a, b, c, d, sep="XYZ")
# sep="XYZ", which means print each value separated by XYZ

print(a, b, c, d, sep="\t\t")
# sep="\t\t", which means print each value separated by \t\t

print("#"*40, end="\n\n")
# ###############################

print("print function PART-2")
print("-"*20)
# -----------

a = 100
b = 200
c = 300
d = 400

print(a, b, c, d)
# by default end="\n", which means put \n at the end after printing all the values

print(a, b, c, d)
# by default end="\n", which means put \n at the end after printing all the values

print(a, b, c, d)
# by default end="\n", which means put \n at the end after printing all the values

print(a, b, c, d, end=".")
# end=".", which means put DOT at the end after printing all the values

print(a, b, c, d, end="XYZ")
# end="XYZ", which means put XYZ at the end after printing all the values

print(a, b, c, d, end="ABC\n")
# end="ABC\n", which means put ABC\n at the end after printing all the values

# similarly
# we can also pass 'file' and 'flush' arguments to print function
# We will discuss 'file' and 'flush' during file operations

print("#"*40, end="\n\n")
# ###############################