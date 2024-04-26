# pip install seaborn
"""
seaborn: Plotting
"""

print("iris data")
print("-"*20)
# -----------

import pandas as pd

iris_data = pd.read_csv("Iris.csv")
print(iris_data.head(5)) # top 5 rows

print("#"*40, end="\n\n")
# ###############################
print("Inside Seaborn library")
print("-"*20)
# -----------

import seaborn as sns
print(dir(sns))

print("#"*40, end="\n\n")
# ###############################
print("Line Plot")
print("-"*20)
# -----------

import matplotlib.pyplot as plt

sns.lineplot(x="Species", y="SepalWidthCm", data=iris_data)

plt.show()

print("#"*40, end="\n\n")
# ###############################
print("relplot")
print("-"*20)
# -----------

import matplotlib.pyplot as plt

sns.relplot(x="Species", y="SepalWidthCm", data=iris_data)

plt.show()

print("#"*40, end="\n\n")
# ###############################

print("scatterplot")
print("-"*20)
# -----------

import matplotlib.pyplot as plt

sns.scatterplot(x="SepalLengthCm", y="SepalWidthCm",   data=iris_data)

plt.show()

print("#"*40, end="\n\n")
# ###############################

print("violinplot")
print("-"*20)
# -----------

import matplotlib.pyplot as plt

sns.violinplot(x="SepalLengthCm", y="SepalWidthCm",   data=iris_data)

plt.show()

print("#"*40, end="\n\n")
# ###############################