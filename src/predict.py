import pandas as pd
import joblib

# Load saved model
model = joblib.load("models/employee_performance_model.pkl")

# New employee data for prediction
new_employee = pd.DataFrame({
    "employee_id": [1001],
    "age": [30],
    "experience_years": [5],
    "department": ["IT"],
    "salary": [60000],
    "training_hours": [70],
    "attendance_percent": [92],
    "projects_completed": [10],
    "manager_feedback": [5],
    "overtime_hours": [8],
    "previous_rating": [4]
})

# Predict performance
prediction = model.predict(new_employee)

print("Employee Details:")
print(new_employee)

print("\nPredicted Employee Performance:")
print(prediction[0])