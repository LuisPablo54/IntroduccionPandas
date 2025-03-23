import pandas as pd
df = pd.read_csv('Iris.csv')

# View data

a = df.head(2)
print(a) # Show the first 2 rows

b = df.tail(2)
print(b) # Show the last 2 rows

c = df.sample(2)
print(c) # Show 2 random rows

d = df.shape
print(d) # Show the number of rows and columns

c = df.columns
print(c) # Show the columns

e = df.Species.unique()
print(e) # Show the unique values of the column Species