import pandas as pd
import numpy as np
import os

# Reproducible random values
np.random.seed(42)

# Number of employees
num_employees = 1000

# Create employee data
employee_data = {
    "employee_id": range(1, num_employees + 1),

    "age": np.random.randint(22, 60, num_employees),

    "experience_years": np.random.randint(0, 20, num_employees),

    "department": np.random.choice(
        ["IT", "HR", "Finance", "Sales", "Marketing"],
        num_employees
    ),

    "salary": np.random.randint(25000, 120000, num_employees),

    "training_hours": np.random.randint(0, 100, num_employees),

    "attendance_percent": np.random.randint(60, 100, num_employees),

    "projects_completed": np.random.randint(1, 20, num_employees),

    "manager_feedback": np.random.randint(1, 6, num_employees),

    "overtime_hours": np.random.randint(0, 50, num_employees),

    "previous_rating": np.random.randint(1, 6, num_employees)
}

# Convert to DataFrame
df = pd.DataFrame(employee_data)

# Generate performance score
performance_score = (
    df["training_hours"] * 0.20 +
    df["attendance_percent"] * 0.30 +
    df["projects_completed"] * 2 +
    df["manager_feedback"] * 10 +
    df["previous_rating"] * 8 -
    df["overtime_hours"] * 0.50
)

# Convert score into categories
performance_label = []

for score in performance_score:
    if score >= 120:
        performance_label.append("High")
    elif score >= 85:
        performance_label.append("Medium")
    else:
        performance_label.append("Low")

# Add target column
df["performance_label"] = performance_label

# Ensure output folder exists
os.makedirs("data/raw", exist_ok=True)

# Save dataset
output_path = "data/raw/employee_data.csv"
df.to_csv(output_path, index=False)

print("Synthetic employee dataset created successfully!")
print(f"Dataset saved at: {output_path}")
print("\nFirst 5 rows:")
print(df.head())