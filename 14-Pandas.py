import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
}

df = pd.DataFrame(data)
print(df)

# Example inspection
print(df.info())
print(df.describe())

# Selecting a single column (returns a Series)
names = df['Name']

# Selecting multiple columns (returns a DataFrame)
subset = df[['Name', 'City']]

# Add a new column
df['Salary'] = [70000, 85000, 92000]

# Update values based on a condition
df.loc[df['Name'] == 'Alice', 'Age'] = 26