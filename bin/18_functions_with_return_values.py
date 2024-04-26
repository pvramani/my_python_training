"""
2 Cases
Case-1: How to access values outside the function
Case-2: How to pass values to variables present inside the function

In this section, we will discuss
Case-1: How to access values outside the function
"""
print("Function with 1 return value")
print("-"*20)
# -----------

# 2 steps
# step-1: inside the function use 'return' statement to send values to outside
# Step-2: Assign function call to any variable so that returned value will be stored

def employee():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company)
    # step-1: inside the function use 'return' statement to send values to outside
    return name

# Step-2: Assign function call to any variable so that returned value will be stored
received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
# ###############################

print("Function with more than 1 return value: IN TUPLE")
print("-"*20)
# -----------

# 2 steps
# step-1: inside the function use 'return' statement to send values to outside
# Step-2: Assign function call to any variable so that returned value will be stored

def employee():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company)
    # step-1: inside the function use 'return' statement to send values to outside
    return name, company # It will return in tuple

# Step-2: Assign function call to any variable so that returned value will be stored
received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
# ###############################

print("Function with more than 1 return value: IN LIST")
print("-"*20)
# -----------

# 2 steps
# step-1: inside the function use 'return' statement to send values to outside
# Step-2: Assign function call to any variable so that returned value will be stored

def employee():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company)
    # step-1: inside the function use 'return' statement to send values to outside
    return [name, company]

# Step-2: Assign function call to any variable so that returned value will be stored
received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
# ###############################

print("Function with more than 1 return value: IN Dictionary")
print("-"*20)
# -----------

# 2 steps
# step-1: inside the function use 'return' statement to send values to outside
# Step-2: Assign function call to any variable so that returned value will be stored

def employee():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company)
    # step-1: inside the function use 'return' statement to send values to outside
    return {"name": name, "company": company}

# Step-2: Assign function call to any variable so that returned value will be stored
received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
# ###############################