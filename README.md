 BlinkIT Grocery Sales Analytics + Machine Learning + Power BI Dashboard Project
📌 Project Overview

This project combines Business Intelligence (Power BI) with Machine Learning (Python + Scikit-learn) to transform BlinkIT grocery sales data into both descriptive analytics and predictive insights.

The objective was not just to analyze historical sales trends, but to answer deeper business questions:

Key Questions Solved:
What factors truly drive BlinkIT sales?
Can future sales be predicted using Machine Learning?
Which model performs better for this dataset?
How can predictive insights be integrated into Power BI dashboards?
What happens to sales if product visibility changes?

Project Goals
Phase 1: Business Intelligence (Power BI)

Built an interactive dashboard to analyze:

Total Sales
Average Sales
Ratings
Outlet Type Performance
Outlet Size
Outlet Location
Item Type Trends
Fat Content Analysis
Phase 2: Machine Learning (Python + Scikit-learn)

Developed predictive models to:

✔ Predict product sales
✔ Compare model performance
✔ Identify top sales drivers
✔ Simulate hypothetical product scenarios
📂 Dataset Details
Dataset:

BlinkIT Grocery Dataset

Total Records:

8,523 rows

Features:
Item Fat Content
Item Identifier
Item Type
Outlet Establishment Year
Outlet Identifier
Outlet Location Type
Outlet Size
Outlet Type
Item Visibility
Item Weight
Sales (Target Variable)
Rating

Data Preprocessing Workflow
✔ Missing Value Handling
Item Weight had missing values
Filled using:
fillna(0)
✔ Feature Selection

Removed:

Sales → Target variable
Item Identifier → Non-predictive unique identifier
✔ Categorical Encoding

Used:

pd.get_dummies(drop_first=True)
Purpose:

Convert categorical business columns into machine-readable numerical format.

🤖 Machine Learning Models Used
1️⃣ Linear Regression (Baseline Model)
Objective:

Establish a simple benchmark.

Performance:
R² Score: ~0.014
RMSE: ~62
Key Learning:

Linear Regression significantly underperformed because BlinkIT sales patterns are non-linear.

2️⃣ Random Forest Regressor (Advanced Model)
Objective:

Capture complex decision patterns using multiple decision trees.

Performance:
R² Score: ~0.51
RMSE: ~44
Improvement:
✔ Better predictive power
✔ Lower error
✔ Better business applicability
📊 Model Evaluation Metrics Learned
R² Score

Measures how much better the model performs compared to simply predicting average sales.

MSE (Mean Squared Error)

Measures squared prediction error.

RMSE (Root Mean Squared Error)

Measures average prediction error in real sales units.

🔍 Feature Importance Analysis

Using:

model.feature_importances_
Top Sales Drivers:
🥇 Item Visibility
🥈 Item Weight
🥉 Rating
💡 Business Insight:

Product visibility is the strongest driver of expected sales.

🧪 Scenario Simulation (What-If Analysis)

Created hypothetical BlinkIT product scenarios to test prediction behavior.

Example Scenario:
High Visibility Product:

Predicted Sales ≈ ₹127.69

Low Visibility Product:

Predicted Sales ≈ ₹105.45

📈 Key Insight:

Reducing visibility significantly lowered predicted sales.

Business Conclusion:
✔ Shelf placement matters
✔ Product discoverability impacts performance
📊 Power BI + Python Integration

This project also integrated Python scripts directly into Power BI to create an AI / ML Insights Dashboard.

ML Modules Built:
feature_importance.py

Outputs:

Top business drivers of sales
model_comparison.py

Outputs:

Linear Regression vs Random Forest performance comparison
scenario_simulation.py

Outputs:

Hypothetical product sales predictions
🖥️ Power BI Dashboard Structure
Page 1:
Traditional BlinkIT Business Dashboard
Sales KPIs
Outlet Analysis
Product Category Insights
Page 2:
AI / ML Insights Dashboard
Model Comparison
Feature Importance
Scenario Simulation
🛠️ Tech Stack Used
Python:
Pandas
NumPy
Scikit-learn
OpenPyXL
Power BI:
Dashboard Design
Python Script Integration
Predictive Visuals
📁 Project Files Included
Core Files:
main_project.py

Complete ML workflow

BlinkIT_ML_Notebook.ipynb

Step-by-step experimentation + learning journey

feature_importance.py

Feature ranking module

model_comparison.py

Model benchmarking module

scenario_simulation.py

What-if prediction module

BlinkIT Power BI Dashboard.pbix

Interactive dashboard

🚀 Key Skills Demonstrated
Data Analytics:
✔ Data Cleaning
✔ Feature Engineering
✔ EDA
Machine Learning:
✔ Regression
✔ Random Forest
✔ Model Evaluation
✔ Feature Importance
✔ Scenario Testing
Business Intelligence:
✔ Power BI Dashboarding
✔ Python + Power BI Integration
✔ Strategic Visualization
🌟 Project Outcome

This project successfully evolved from:

Descriptive Analytics:
“What happened?”
Predictive Analytics:
“What is likely to happen?”
Strategic Analytics:
“What should we do next?”
📌 Real Business Recommendations
Based on findings:
✔ Improve product visibility
✔ Prioritize high-impact sales drivers
✔ Use ML before product launches
✔ Combine BI dashboards with predictive systems
🔮 Future Enhancements
Planned:
K-Fold Cross Validation
Hyperparameter Tuning
Classification Models
Streamlit / Power Apps for live prediction
Advanced Ensemble Models
🏆 Final Takeaway

This project demonstrates how Power BI + Python + Machine Learning can move beyond dashboards into decision intelligence systems.

It is not just a sales dashboard —
it is a retail predictive analytics framework.

👨‍💻 Author
Bibhanshu Swain
Aspiring Data Analyst | Power BI | SQL | Python | Scikit-learn
