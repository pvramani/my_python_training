"""
In this section,
Case-2: How to pass values to variables present inside the function

There are 2 ways to pass values
1st-way: We can directly pass only values
2nd-way: We can pass values using key=value format

In this section, we will discuss
1st-way: We can directly pass only values
called POSITIONAL ARGUMENTS
"""

print("Function with positional arguments")
print("-"*20)
# -----------


def employee(name, company):
    print("Name:", name)
    print("Company:", company)
    return [name, company]


received_value = employee("emp-1", "comp-1")
print("received_value:", received_value)

print("#"*40, end="\n\n")
# ###############################
print("Function with variable positional arguments")
print("-"*20)
# -----------

# *prev_companies called variable positional arguments
def employee(name, company, *prev_companies):
    print("Name:", name)
    print("Company:", company)
    print("prev_companies:", prev_companies)
    return [name, company, prev_companies]


received_value = employee("emp-1", "comp-1")
# prev_companies=()
print("received_value:", received_value)

received_value = employee("emp-2", "comp-1", "prev_comp_1")
# prev_companies=("prev_comp_1",)
print("received_value:", received_value)

received_value = employee("emp-3", "comp-1", "prev_comp_1", "prev_comp_2", "prev_comp_3")
# prev_companies=("prev_comp_1", "prev_comp_2", "prev_comp_3")
print("received_value:", received_value)

print("#"*40, end="\n\n")
# ###############################