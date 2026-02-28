# Job-Acceptance-Prediction-System
HR Analytics Project using Machine Learning to Predict Job Offer Acceptance
🎯 Job Acceptance Prediction System
📌 Project Overview

Recruitment teams often face uncertainty in predicting whether a candidate will accept a job offer.
This project builds a Machine Learning model to predict job acceptance using candidate academic, skill, experience, and interview data.

🏢 Domain

HR Analytics | Predictive Modeling | Recruitment Analytics

📊 Dataset

50,000 candidate records

Includes:

Academic performance

Skills match percentage

Work experience

Interview scores

Company tier

Placement status (Target)

🔍 Project Workflow
1️⃣ Data Cleaning

Missing value handling

Duplicate removal

Categorical encoding

Feature scaling

2️⃣ Exploratory Data Analysis

Interview score vs acceptance

Skills match impact

Experience vs placement

Correlation analysis

3️⃣ Feature Engineering

Experience category

Skills level bands

Academic performance bands

4️⃣ Machine Learning Models

Logistic Regression

Random Forest

Model evaluation using:

Accuracy

Precision

Recall

F1 Score

📈 Key Insights

Interview score strongly influences acceptance

High skills match increases placement probability

Company tier impacts offer acceptance rate

Experience level affects success probability

📊 Streamlit Dashboard

Includes KPIs:

Total Candidates

Placement Rate

Job Acceptance Rate

Offer Dropout Rate

Average Interview Score

🛠 Tech Stack

Python

Pandas

NumPy

Matplotlib / Seaborn

Scikit-Learn

MySQL

Streamlit

🚀 How to Run
pip install -r requirements.txt
streamlit run dashboard2.py
