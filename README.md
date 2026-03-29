# 🎓 Student Risk Analysis & Prediction System

This project focuses on identifying students who are at risk based on their academic performance and engagement metrics such as attendance, quiz scores, and activity patterns.

The goal is to build a simple machine learning system that can help in early detection of struggling students and provide basic recommendations.

---

## 🚀 Features

* 📊 Data analysis using pandas and seaborn
* 📈 Visualization of student performance trends
* 🤖 Machine learning model (Random Forest & Logistic Regression)
* ⚠️ Risk classification (Low Risk / High Risk)
* 🧠 Risk score calculation
* 🌐 Streamlit web app for real-time prediction

---

## 📂 Project Structure

```
student-risk-analysis/
│── data/
│── notebooks/
│   └── analysis.ipynb
│── app.py
│── report.md
│── README.md
```

---

## 📊 Dataset

A synthetic dataset is generated with the following features:

* Attendance percentage
* Quiz average score
* Missed sessions
* Late submissions
* Technical rating
* Progress percentage

A target variable `risk_label` is created based on performance conditions.

---

## 🧠 Approach

1. Data Generation
2. Feature Engineering (risk_label, risk_score)
3. Exploratory Data Analysis
4. Model Training
5. Model Evaluation
6. Deployment using Streamlit

---

## 🤖 Models Used

* Logistic Regression
* Random Forest Classifier

Random Forest performed better as it captured non-linear relationships between features.

---

## 🌐 Streamlit App

The project includes a simple web interface where users can:

* Enter student details
* Get risk prediction instantly
* View risk score
* Receive basic suggestions

To run the app:

```
streamlit run app.py
```

---

## 📌 Key Insights

* Low attendance is strongly linked to high risk
* Poor quiz performance indicates learning gaps
* Missed sessions significantly affect outcomes
* Risk is influenced by multiple combined factors

---

## 🌍 Real-World Use

This system can be used as an early warning tool in:

* Schools and colleges
* Online learning platforms
* Training academies

It helps identify students who need support before performance drops further.

---

## 👩‍💻 Author

Sindhuja R
B.Tech CSE (AI)



