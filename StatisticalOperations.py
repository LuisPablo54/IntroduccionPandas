import pandas as pd

df = pd.read_csv('train.csv')   
#dprint(df.head(4)) 

# Drop string columns
df.drop(['Name', 'Cabin', 'Ticket'], axis=1, inplace=True)
print(df.head(4))

# Saw sum of the columns to see what is our data
#print(df.sum(numeric_only=True)) 
x = df.sum(numeric_only=True)
print(x)
# promed the age
#df['Age'].mean()
print(x['Age'].mean())



