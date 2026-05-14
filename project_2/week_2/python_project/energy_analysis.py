import pandas as pd
import numpy as np

# Load CSV
df = pd.read_csv("energy_usage.csv")

# Convert timestamp
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Convert energy values
df['energy_kwh'] = df['energy_kwh'].astype(float)

# Remove missing values
df = df.dropna()

# Room-wise summary
room_summary = df.groupby(
    'room_id'
)['energy_kwh'].sum()

print("\nRoom Summary:")
print(room_summary)

# NumPy calculations
total_energy = np.sum(df['energy_kwh'])
average_energy = np.mean(df['energy_kwh'])

print("\nTotal Energy:", total_energy)
print("Average Energy:", average_energy)

# Device-wise summary
device_summary = df.groupby(
    'device_name'
)['energy_kwh'].sum()

print("\nDevice Summary:")
print(device_summary)

# Save cleaned data
df.to_csv(
    "cleaned_energy_usage.csv",
    index=False
)

print("\nCleaned dataset saved.")