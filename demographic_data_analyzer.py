import pandas as pd

df=pd.read_csv('e:/mernweak3/freecodecamp/data.csv')
df.head()
print(df.head())

# How many people of each race are represented in this dataset? 
# This should be a Pandas series with race names as the index labels. (race column)
race_count = df['race'].value_counts()
print(race_count)

