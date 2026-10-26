import pandas as pd

# Create employee DataFrame
data = {
    'Employee': ['Raja', 'Sahil', 'Adiya', 'Suryansh', 'Swarup', 'Yash'],
    'Department': ['Sales', 'IT', 'Sales', 'HR', 'Sales', 'Sales'],
    'Salary': [100000, 150000, None, 100000, 50000, None]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Fill missing Salary values with median
median_salary = df['Salary'].median()
df['Salary'] = df['Salary'].fillna(median_salary)

# Filter employees from Sales department
sales_df = df[df['Department'] == 'Sales']

# Calculate average salary of Sales department
average_salary = sales_df['Salary'].mean()

print("\nSales Department:")
print(sales_df)

print("\nAverage Salary of Sales Department:", average_salary)