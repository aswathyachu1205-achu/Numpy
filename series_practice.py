import pandas as pd

s_1 = pd.Series([1,2,3,4,5,6])
s_2 = pd.Series([7,8,9,10,11,12])

print(s_1.add(s_2)) # returns the sum of elements from each series
print(s_1.multiply(s_2))
print(pd.concat([s_1,s_2])) # join more than one series into a single series