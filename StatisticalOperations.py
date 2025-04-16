import pandas as pd

df = pd.read_csv('train.csv')   
#dprint(df.head(4)) 

# Drop string columns
df.drop(['PassengerId', 'Name', 'SibSp', 'Embarked'], axis=True, inplace=True)
print(df.columns)

# Saw sum of the columns to see what is our data
#print(df.sum(numeric_only=True)) 
# x = df.sum(numeric_only=True)
# print(x)

# promed the age (round to 0 decimal places to get an integer)
# print('Promed of the age\n')
# print(df.median(numeric_only=True, axis="index"))
# print(df['Age'].median().round(0))
# The variance of the all columns
# print('Variance\n')
# print(df.var(numeric_only=True))

# Mode
# print(df.columns)

# Minmun
# print(df.min(numeric_only=True))

# Maximum
# print(df.max(numeric_only=True))

# Count
# print(df.count(numeric_only=True))

# Correlation

print(df.corr(numeric_only=True))



