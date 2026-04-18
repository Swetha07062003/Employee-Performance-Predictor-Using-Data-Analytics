import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load cleaned dataset
df = pd.read_csv("data/processed/cleaned_employee_data.csv")

# Create outputs folder if not exists
os.makedirs("outputs", exist_ok=True)

# -------------------------------
# Graph 1: Performance Distribution
# -------------------------------
plt.figure(figsize=(8, 5))
sns.countplot(x="performance_label", data=df)

plt.title("Employee Performance Distribution")
plt.xlabel("Performance Label")
plt.ylabel("Number of Employees")

plt.savefig("outputs/performance_distribution.png")
plt.show()

# -------------------------------
# Graph 2: Department vs Performance
# -------------------------------
plt.figure(figsize=(10, 6))
sns.countplot(x="department", hue="performance_label", data=df)

plt.title("Department vs Employee Performance")
plt.xlabel("Department")
plt.ylabel("Employee Count")

plt.savefig("outputs/department_performance.png")
plt.show()

# -------------------------------
# Graph 3: Correlation Heatmap
# -------------------------------
plt.figure(figsize=(16, 10))

numeric_df = df.select_dtypes(include=["int64", "float64"])

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    annot_kws={"size": 8}
)

plt.title("Correlation Heatmap", fontsize=18, pad=20)

plt.xticks(rotation=35, ha="right", fontsize=11)
plt.yticks(rotation=0, fontsize=11)

plt.subplots_adjust(bottom=0.30, left=0.25)

plt.savefig("outputs/correlation_heatmap.png", bbox_inches="tight")
plt.show()