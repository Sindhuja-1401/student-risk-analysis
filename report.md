# 📊 Student Risk Analysis Report

## 1. Introduction

This project aims to analyze student performance data and identify individuals who are at risk of poor academic outcomes. The system uses machine learning techniques to classify students based on their engagement and performance metrics.

---

## 2. Dataset Description

A synthetic dataset of 300 students was generated. The dataset includes:

* Attendance percentage
* Quiz scores
* Missed sessions
* Late submissions
* Technical ratings
* Progress percentage

These features represent both academic performance and behavioral engagement.

---

## 3. Feature Engineering

Two important variables were created:

* **risk_label**: Binary classification (0 = low risk, 1 = high risk)
* **risk_score**: A continuous score indicating severity of risk

The risk score is computed using attendance, quiz performance, and engagement factors.

---

## 4. Exploratory Data Analysis

Key observations:

* Students with attendance below 60% are more likely to be high-risk
* Low quiz scores (<50) are strongly associated with poor outcomes
* High missed sessions correlate with disengagement
* Combined factors provide better risk identification than individual features

---

## 5. Model Development

Two models were used:

* Logistic Regression
* Random Forest Classifier

Random Forest performed better due to its ability to handle complex relationships between variables.

---

## 6. Model Evaluation

The models were evaluated using classification metrics such as precision, recall, and F1-score.

Random Forest showed improved performance in identifying high-risk students compared to Logistic Regression.

---

## 7. System Implementation

A simple web interface was built using Streamlit.

The application allows users to:

* Input student details
* Predict risk level
* View risk score
* Receive recommendations

---

## 8. Key Insights

* Student risk is influenced by both performance and engagement
* Early indicators (attendance, activity) can predict future decline
* Multi-factor analysis improves prediction accuracy

---

## 9. Conclusion

The project demonstrates how machine learning can be used to identify at-risk students and support early intervention strategies.

Such systems can help educational institutions improve student outcomes and reduce dropout rates.

---

## 10. Future Improvements

* Use real-world datasets
* Add more behavioral features
* Improve model accuracy with advanced algorithms
* Deploy the system for real-time use
