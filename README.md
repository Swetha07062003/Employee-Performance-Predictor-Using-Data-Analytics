# Employee Performance Predictor Using Data Analytics

## Project Overview

Employee Performance Predictor is a machine learning project that predicts whether an employee is likely to be a High, Medium, or Low performer using HR-related data.

The project uses synthetic employee data because real company HR data is confidential and not publicly available. The system simulates a real company HR analytics environment and helps HR teams make better decisions about promotions, training, and employee improvement.

This project includes:

* Synthetic HR dataset generation
* Data preprocessing and cleaning
* Data visualization and analysis
* Machine learning model training
* Employee performance prediction
* Streamlit dashboard for interactive predictions

---

## Problem Statement

Companies often struggle to identify:

* Which employees are performing well
* Which employees need support or training
* Which employees may be suitable for promotion

Traditional performance reviews are manual and time-consuming. This project solves that problem by using machine learning to predict employee performance automatically.

The prediction classes are:

* High Performer
* Medium Performer
* Low Performer

---

## Business Value

This project can help HR teams and managers:

* Identify top-performing employees
* Detect employees who may need improvement
* Support promotion and reward decisions
* Plan training programs
* Improve employee retention
* Reduce manual work in performance evaluation

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Streamlit

---

## Project Structure

```text
Employee-Performance-Predictor-Using-Data-Analytics/
│
├── data/
│   ├── raw/
│   │   └── employee_data.csv
│   └── processed/
│       └── cleaned_employee_data.csv
│
├── images/
│   ├── Dashboard1.png
│   ├── Dashboard2.png
│   ├── Dashboard3.png
│   ├── performance_distribution.png
│   ├── department_performance.png
│   └── correlation_heatmap.png
│
├── models/
│   └── employee_performance_model.pkl
│
├── outputs/
│   ├── performance_distribution.png
│   ├── department_performance.png
│   └── correlation_heatmap.png
│
├── src/
│   ├── generate_data.py
│   ├── preprocess.py
│   ├── visualize.py
│   ├── train_model.py
│   ├── predict.py
│   └── app.py
│
├── requirements.txt
├── README.md
└── main.py
```

---

## Dataset Features

The synthetic dataset contains the following employee-related features:

* employee_id
* age
* experience_years
* department
* salary
* training_hours
* attendance_percent
* projects_completed
* manager_feedback
* overtime_hours
* previous_rating
* performance_label

The target variable is:

```text
performance_label
```

Possible values:

* High
* Medium
* Low

---

## Workflow

```text
Generate Dataset → Clean Data → Visualize Data → Train Model → Save Model → Predict Performance → Show Dashboard
```

---

## Machine Learning Model

The project uses a Random Forest Classifier.

Why Random Forest?

* Works well with mixed numerical and categorical data
* Gives high accuracy
* Handles non-linear relationships
* Suitable for beginner and industry-level projects

Model used:

```python
RandomForestClassifier(n_estimators=200, random_state=42)
```

---

## Model Accuracy

The trained model achieved approximately:

```text
Accuracy: 78%
```

Sample classification result:

```text
              precision    recall    f1-score
High             0.82      0.96       0.88
Medium           0.60      0.54       0.57
Low              0.94      0.55       0.69
```

The model predicts High performers most accurately.

---

## Visualizations Generated

The project generates the following graphs:

1. Performance Distribution Graph
2. Department vs Performance Graph
3. Correlation Heatmap

These graphs are stored inside the `outputs/` and `images/` folders.

---

## Streamlit Dashboard

The project also includes an interactive Streamlit dashboard.

Dashboard features:

* Enter employee details manually
* Predict employee performance instantly
* View employee summary
* User-friendly interface

Run the dashboard using:

```bash
streamlit run src/app.py
```

---

## How to Run the Project

Step 1: Install dependencies

```bash
pip install -r requirements.txt
```

Step 2: Generate synthetic employee dataset

```bash
python src/generate_data.py
```

Step 3: Preprocess and clean the dataset

```bash
python src/preprocess.py
```

Step 4: Generate visualizations

```bash
python src/visualize.py
```

Step 5: Train the machine learning model

```bash
python src/train_model.py
```

Step 6: Predict employee performance

```bash
python src/predict.py
```

Step 7: Run the Streamlit dashboard

```bash
streamlit run src/app.py
```

---

## Sample Prediction

Example employee input:

```text
Age: 30
Experience: 5 years
Department: IT
Training Hours: 40
Attendance: 85%
Projects Completed: 5
Manager Feedback: 3
Previous Rating: 3
```

Predicted Result:

```text
Medium Performer
```

---

```markdown


### Dashboard Preview

![Dashboard 1](images/Dashboard1.png)

![Dashboard 2](images/Dashboard2.png)

![Dashboard 3](images/Dashboard3.png)

### Performance Distribution

![Performance Distribution](images/performance_distribution.png)

### Department vs Performance

![Department vs Performance](images/department_performance.png)

### Correlation Heatmap

![Correlation Heatmap](images/correlation_heatmap.png)
```

---

## Future Improvements

This project can be improved further by:

* Using a real HR dataset
* Adding more employee-related features
* Using advanced algorithms like XGBoost
* Building a web application with login system
* Adding employee attrition prediction
* Creating a real-time HR analytics dashboard
* Deploying the project online

---


