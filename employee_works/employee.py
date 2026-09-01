import pandas as pd

data = pd.read_csv("C:/Users/aswat/OneDrive/Desktop/EDA/employee_works/sample.csv")

# read the data from csv file

df = pd.DataFrame(data)

# convert into data structure

print(df)

print(df.describe())

