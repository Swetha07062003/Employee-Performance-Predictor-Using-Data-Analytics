import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("models/employee_performance_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Employee Performance Predictor",
    layout="wide"
)

# Attractive title
st.markdown(
    """
    <h1 style='text-align: center; color: #1f77b4;'>
        Employee Performance Predictor
    </h1>
    <h4 style='text-align: center; color: gray;'>
        Predict whether an employee is a High, Medium, or Low Performer
    </h4>
    <hr>
    """,
    unsafe_allow_html=True
)

# Layout: left for inputs, right for result
left_col, right_col = st.columns([2, 1])

with left_col:
    st.subheader("Enter Employee Details")

    employee_id = st.number_input(
        "Employee ID",
        min_value=1,
        value=1001,
        step=1
    )

    age = st.number_input(
        "Age",
        min_value=22,
        max_value=60,
        value=30
    )

    experience_years = st.number_input(
        "Experience (Years)",
        min_value=0,
        max_value=20,
        value=5
    )

    department = st.selectbox(
        "Department",
        ["IT", "HR", "Finance", "Sales", "Marketing"]
    )

    salary = st.number_input(
        "Salary",
        min_value=25000,
        max_value=120000,
        value=60000,
        step=1000
    )

    training_hours = st.number_input(
        "Training Hours",
        min_value=0,
        max_value=100,
        value=40
    )

    attendance_percent = st.number_input(
        "Attendance Percentage",
        min_value=60,
        max_value=100,
        value=85
    )

    projects_completed = st.number_input(
        "Projects Completed",
        min_value=1,
        max_value=20,
        value=5
    )

    manager_feedback = st.number_input(
        "Manager Feedback (1 to 5)",
        min_value=1,
        max_value=5,
        value=3
    )

    overtime_hours = st.number_input(
        "Overtime Hours",
        min_value=0,
        max_value=50,
        value=10
    )

    previous_rating = st.number_input(
        "Previous Rating (1 to 5)",
        min_value=1,
        max_value=5,
        value=3
    )

    predict_button = st.button("Predict Performance")

with right_col:
    st.subheader("Prediction Result")

    if predict_button:
        employee_data = pd.DataFrame({
            "employee_id": [employee_id],
            "age": [age],
            "experience_years": [experience_years],
            "department": [department],
            "salary": [salary],
            "training_hours": [training_hours],
            "attendance_percent": [attendance_percent],
            "projects_completed": [projects_completed],
            "manager_feedback": [manager_feedback],
            "overtime_hours": [overtime_hours],
            "previous_rating": [previous_rating]
        })

        prediction = model.predict(employee_data)[0]

        if prediction == "High":
            st.success("High Performer")
            st.markdown(
                """
                This employee is likely to perform very well and may be suitable for:
                - Promotion
                - Leadership opportunities
                - Reward and recognition
                """
            )

        elif prediction == "Medium":
            st.warning("Medium Performer")
            st.markdown(
                """
                This employee is performing adequately but may benefit from:
                - Additional training
                - Skill improvement
                - Manager guidance
                """
            )

        else:
            st.error("Low Performer")
            st.markdown(
                """
                This employee may need:
                - Immediate support
                - Performance improvement plan
                - Additional mentoring and supervision
                """
            )

        st.markdown("### Employee Details Entered")
        st.dataframe(employee_data, use_container_width=True)