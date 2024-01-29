import pandas as pd

# Replace 'stats.csv' with the actual file name
# Specify the delimiter as ';'
# Specify the header row as the second row (index 1)
df = pd.read_csv('stats.csv', encoding='latin-1', delimiter=';', header=1)

# Explore the data
print(df.head())
print(df.info())
print(df.describe())
