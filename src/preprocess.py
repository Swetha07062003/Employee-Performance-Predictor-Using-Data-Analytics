import pandas as pd
import os

# Load dataset
df = pd.read_csv("data/raw/employee_data.csv")

print("Original Dataset Shape:", df.shape)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows if any
duplicates = df.duplicated().sum()
print("\nDuplicate Rows:", duplicates)

df = df.drop_duplicates()

# Final shape after cleaning
print("\nCleaned Dataset Shape:", df.shape)

# Create processed folder if not present
os.makedirs("data/processed", exist_ok=True)

# Save cleaned dataset
output_path = "data/processed/cleaned_employee_data.csv"
df.to_csv(output_path, index=False)

print(f"\nCleaned dataset saved at: {output_path}")
print("\nFirst 5 cleaned rows:")
print(df.head())