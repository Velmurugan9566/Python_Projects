'''import matplotlib.pyplot as plt
#plt.figure(figsize=(10,5))
h=[121.9,124.5,129.5,134.5,139.7,147.3,152.4,157.5,162.6]
w=[19.7,21.3,23.5,25.9,28.5,32.1,35.7,39.6,43.5]
plt.plot(w,'r.-',label='height')
plt.plot(h,'k.-',label='weight')
plt.xlabel('height')
plt.ylabel('weight')
plt.grid(linestyle=':')
plt.show()
plt.legend()'''
import pandas as pd

# Sample dataset
data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 1],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Charlie'],
    'Age': [25, None, 30, 35, 28, 22, 30],
    'Email': ['alice@email.com', 'bob@email.com', 'charlie@', 'david@email.com', None, 'frank@email.com', 'charlie@']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Step 1: Handling Missing Values
# Identify missing values
missing_values = df.isnull()
print("Missing Values:")
print(missing_values)

# Drop rows with missing values
df.dropna(inplace=True)
print("\nDataFrame after dropping rows with missing values:")
print(df)

# Step 2: Handling Duplicates
# Identify duplicate rows
duplicates = df.duplicated()
print("\nDuplicate Rows:")
print(duplicates)

# Remove duplicate rows
df.drop_duplicates(inplace=True)
print("\nDataFrame after removing duplicate rows:")
print(df)

# Step 3: Data Type Conversion (if needed)
# In this example, no type conversion is needed.

# Step 4: Text Data Cleaning (if needed)
# In this example, email validation can be performed, but we'll skip it for brevity.

# Step 5: Handling Inconsistent Data (if needed)
# In this example, we'll correct the inconsistent email address.
df['Email'] = df['Email'].str.replace('@', '@example.com')

# Print the cleaned DataFrame
print("\nCleaned DataFrame:")
print(df)

