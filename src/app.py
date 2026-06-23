# Streamlit uygulaması

import streamlit as st
import pandas as pd
import joblib
from catboost import CatBoostRegressor

st.set_page_config(
    page_title="Student Test Score Predictor",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Test Score Predictor")
st.write(
    "This application predicts a student's exam score using study habits, "
    "attendance, sleep patterns, and educational factors."
)
st.write(
    "Bu uygulama; çalışma alışkanlıkları, ders devamı, uyku düzeni ve eğitim koşullarına göre öğrencinin sınav puanını tahmin eder."
)

model = CatBoostRegressor()
model.load_model("student_score_model.cbm")

feature_columns = joblib.load("feature_columns.pkl")

age = st.number_input("Age / Yaş", min_value=15, max_value=30, value=21)
gender = st.selectbox("Gender / Cinsiyet", ["male", "female"])
course = st.selectbox("Course / Bölüm", ["bsc", "bca", "engineering", "arts", "commerce"])
study_hours = st.number_input("Study Hours / Çalışma Saati", min_value=0.0, max_value=12.0, value=5.0)
class_attendance = st.number_input("Class Attendance (%) / Devam Oranı", min_value=0.0, max_value=100.0, value=75.0)
internet_access = st.selectbox("Internet Access / İnternet Erişimi", ["yes", "no"])
sleep_hours = st.number_input("Sleep Hours / Uyku Süresi", min_value=0.0, max_value=12.0, value=7.0)
sleep_quality = st.selectbox("Sleep Quality / Uyku Kalitesi", ["poor", "average", "good"])
study_method = st.selectbox("Study Method / Çalışma Yöntemi", ["self-study", "online videos", "coaching", "group study"])
facility_rating = st.selectbox("Facility Rating / Eğitim Olanakları", ["low", "medium", "high"])
exam_difficulty = st.selectbox("Exam Difficulty / Sınav Zorluğu", ["easy", "moderate", "hard"])

sleep_quality_map = {
    "poor": 1,
    "average": 2,
    "good": 3
}

sleep_quality_num = sleep_quality_map[sleep_quality]

study_efficiency = study_hours * class_attendance
sleep_score = sleep_hours * sleep_quality_num
academic_engagement = study_hours + (class_attendance / 10)
study_sleep_ratio = study_hours / (sleep_hours + 1)

input_df = pd.DataFrame({
    "age": [age],
    "gender": [gender],
    "course": [course],
    "study_hours": [study_hours],
    "class_attendance": [class_attendance],
    "internet_access": [internet_access],
    "sleep_hours": [sleep_hours],
    "sleep_quality": [sleep_quality],
    "study_method": [study_method],
    "facility_rating": [facility_rating],
    "exam_difficulty": [exam_difficulty],
    "study_efficiency": [study_efficiency],
    "sleep_quality_num": [sleep_quality_num],
    "sleep_score": [sleep_score],
    "academic_engagement": [academic_engagement],
    "study_sleep_ratio": [study_sleep_ratio]
})

input_df = input_df[feature_columns]

if st.button("Predict Exam Score / Sınav Puanını Tahmin Et"):
    prediction = model.predict(input_df)[0]
    prediction = max(0, min(100, prediction))

    st.success(f"Predicted Exam Score: {prediction:.2f}")
    st.success(f"Tahmini Sınav Puanı: {prediction:.2f}")