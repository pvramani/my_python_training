"""
pip install pandas   - run this command in terminal

about pandas library
- pandas is one library
- Inside pandas, we have many functions & classes
- one of the main class is 'DataFrame'
- inside 'DataFrame' class we have methods related to tabular-data/csv/xlsx/db data
"""

print("Inside pandas")
print("-"*20)
# -----------

import pandas as pd
print(dir(pd))

print("#"*40, end="\n\n")
# ###############################

print("Inside DataFrame class")
print("-"*20)
# -----------

import pandas as pd
print(dir(pd.DataFrame))

print("#"*40, end="\n\n")
# ###############################


print("DataFrame Example-1")
print("-"*20)
# -----------

import pandas as pd
my_df = pd.DataFrame([[10, 20, 30], [100, 200, 300]])
print(my_df)

print("#"*40, end="\n\n")
# ###############################

print("DataFrame Example-2")
print("-"*20)
# -----------

import pandas as pd
my_df = pd.DataFrame([[10, 20, 30], [100, 200, 300]], index=["r1", "r2"], columns=["c1", "c2", "c3"])
print(my_df)

print("#"*40, end="\n\n")
# ###############################
print("minimum value in entire dataframe")
print("-"*20)
# -----------

import pandas as pd
my_df = pd.DataFrame([[10, 20, 30], [100, 200, 300]], index=["r1", "r2"], columns=["c1", "c2", "c3"])
print(my_df.min())

print("#"*40, end="\n\n")
# ###############################

print("minimum value in 2nd column")
print("-"*20)
# -----------

import pandas as pd
my_df = pd.DataFrame([[10, 20, 30], [100, 200, 300]], index=["r1", "r2"], columns=["c1", "c2", "c3"])
print(my_df["c2"].min())
print(my_df.iloc[:,1].min())
# iloc -> slice using index
# iloc[rows,columns]
# iloc[:,1] all rows & column 1

# iloc[1:3:2, 1:5:3 ]
# 1 to 3 rows step by 2
# 1 to 5 columns step by 3

print("#"*40, end="\n\n")
# ###############################