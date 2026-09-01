import pandas as pd

data = {
    "names":["arun","meera","rahul","sukumar"],
    "age":[20,23,25,28],
    "dept":["hr","it","testing","hr"],
    "salary":[10000,15000,20000,19000]
}

df = pd.DataFrame(data)
print(df)

#df[columnname] = [values]
df["place"] = ["ekm","tvm","allepy","chennai"]
print(df["place"])
df.head() # return first few rows from the df
df.tail()
print(df.shape) #(4,5)
print(df.size) # return total no of elements

print(df.describe())
# returns the statistical summry of columns having numerical values
# df.sort_values(by="age")
print(df.sort_values(by="age"))
# arrange the column age in ascending order

print(df.sort_values(by="age",ascending=False))
# arrange the column age in descending order

print(df.columns)#(['names','age','dept','salary','place']
print(df.sample())
print(df.dtypes)



