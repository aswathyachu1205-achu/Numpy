# pandas
# =============

# pandas is a library used for data manipulation and analysis which is also called data handling
# pandas is built on top of numpy
# and it is used to handle data in tabular form (rows and column)

# series,dataframe

# use cases
# ==========
# reading and storing data
# ========================
# load data from csv,excel,from databases transform into dataframe or series
# clean and transform the data
# ============================
# handle missing values,remove duplicate ,change column values
# analyzing and summarizing the data
# ==================================
# filter the data,group the data,calculate the average....

# Data structure of pandas
# ========================
# series
# 1 - dimensional  data structure
# stores only one single column of data


# Dataframe
# ===========
# 2-dimensional  data structure
# stores the data in rows and columns(table format)
# Equivalent of excel sheet or sql table


import pandas as pd

# pd.Series(data)

data = [1,2,3,4,5,6,7]

result = pd.Series(data)
print(result)

# list/tuple,dictonary

# creating series using a dictonary

data = {"a":10,"b":20,"c":30,"d":40,"e":50,"f":60,"g":70}

result = pd.Series(data)

# keys become the index of the series and the values becomes the data
print(result.ndim)
print(result.shape) # (7,)






