import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# -------------------------
# Creating sample dataset
# -------------------------
np.random.seed(42)

data_size = 300

data = pd.DataFrame({
    "attendance": np.random.randint(40, 100, data_size),
    "quiz_score": np.random.randint(30, 100, data_size),
    "missed_classes": np.random.randint(0, 10, data_size),
    "late_submissions": np.random.randint(0, 8, data_size),
    "technical_rating": np.random.randint(1, 5, data_size),
    "progress": np.random.randint(20, 100, data_size)
})

# -------------------------
# Creating target column
# -------------------------
data["risk"] = (
    (data["attendance"] < 60) |
    (data["quiz_score"] < 50) |
    (data["missed_classes"] > 5)
).astype(int)

# -------------------------
# Train model
# -------------------------
X = data.drop("risk", axis=1)
y = data["risk"]

model = RandomForestClassifier()
model.fit(X, y)

# -------------------------
# Streamlit UI
# -------------------------
st.title("Student Risk Checker")

st.write("Enter student details below to check if the student is at risk.")

attendance = st.slider("Attendance (%)", 0, 100, 70)
quiz = st.slider("Quiz Score", 0, 100, 60)
missed = st.slider("Missed Classes", 0, 10, 2)
late = st.slider("Late Submissions", 0, 10, 1)
tech = st.slider("Technical Rating (1-5)", 1, 5, 3)
progress = st.slider("Progress (%)", 0, 100, 60)

# -------------------------
# Prediction
# -------------------------
if st.button("Check Risk"):

    input_values = np.array([[attendance, quiz, missed, late, tech, progress]])
    result = model.predict(input_values)[0]

    # simple risk score
    score = (
        0.3 * (100 - attendance) +
        0.3 * (100 - quiz) +
        0.2 * missed * 10 +
        0.2 * late * 10
    )

    score = int(score)

    st.subheader("Result")

    if result == 1:
        st.error("Student is at HIGH risk")
    else:
        st.success("Student is at LOW risk")

    st.write("Risk Score:", score)

    # suggestions
    st.subheader("Suggestions")

    if attendance < 60:
        st.write("- Improve attendance")

    if quiz < 50:
        st.write("- Focus more on studies")

    if missed > 5:
        st.write("- Avoid missing classes")

    if late > 3:
        st.write("- Submit work on time")

    if result == 0:
        st.write("- Keep maintaining current performance")

# optional preview
if st.checkbox("Show sample dataset"):
    st.write(data.head())