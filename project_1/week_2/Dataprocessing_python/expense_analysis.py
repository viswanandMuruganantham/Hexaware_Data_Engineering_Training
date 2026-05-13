import pandas as pd
import numpy as np

# Load CSV
df = pd.read_csv("expenses.csv")

# Clean amount column
df['amount'] = (
    df['amount']
    .replace('[\$,]', '', regex=True)
    .astype(float)
)

# Convert date
df['date'] = pd.to_datetime(df['date'])

# Create month column
df['month'] = df['date'].dt.to_period('M')

# Monthly summary
monthly_expense = (
    df.groupby(['month', 'category'])['amount']
    .sum()
    .unstack()
    .fillna(0)
)

print("\nMonthly Expense Summary:")
print(monthly_expense)

# NumPy calculations
total_expense = np.sum(df['amount'])
average_expense = np.mean(df['amount'])

print("\nTotal Expense:", total_expense)
print("Average Expense:", average_expense)

# Save cleaned data
df.to_csv("cleaned_expenses.csv", index=False)

print("\nCleaned dataset saved.")