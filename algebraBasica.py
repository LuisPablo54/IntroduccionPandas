import pandas as pd
df = pd.read_csv('Iris1.csv')


# plus
df['add_sepal_Petal'] = df['SepalLengthCm'] + df['PetalLengthCm']

# Subtraction
df['sub_sepal_Petal'] = df['SepalLengthCm'] - df['PetalLengthCm']

# Multiplication
df['mul_sepal_Petal'] = df['SepalLengthCm'] * df['PetalLengthCm']

# Division
df['div_sepal_Petal'] = df['SepalLengthCm'] / df['PetalLengthCm']

print(df.head(4)) # Show the first 4 rows

# How to drop columns
df1 = df.drop(['add_sepal_Petal', 'sub_sepal_Petal', 'mul_sepal_Petal', 'div_sepal_Petal'], axis=1)
#print(df1.head(4)) # Show the first 4 rows

#print(df.head(4)) # Show the first 4 rows

# How to drop columns in place
df.drop(['add_sepal_Petal', 'sub_sepal_Petal', 'mul_sepal_Petal', 'div_sepal_Petal','SepalLengthCm'], axis=1, inplace=True)
print(df.head(4)) # Show the first 4 rows
