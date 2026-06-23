# Student Test Score Predictor

## Overview

Student Test Score Predictor is a machine learning project that estimates student exam scores using academic, behavioral, and lifestyle factors. The objective is to understand how study habits, attendance, sleep patterns, and educational conditions influence academic performance and to build a regression model capable of predicting exam results accurately.

The project was developed using the **CatBoost Regressor** algorithm and achieved a **Kaggle Public Score of 8.75421 RMSE**.

## Dataset

The dataset contains information related to student demographics, academic habits, and learning conditions.

### Features

- Age
- Gender
- Course
- Study Hours
- Class Attendance
- Internet Access
- Sleep Hours
- Sleep Quality
- Study Method
- Facility Rating
- Exam Difficulty

### Target Variable

**exam_score**

The goal is to predict a student's final exam score.

## Feature Engineering

Several new variables were created to capture relationships between study habits and academic performance:

- **study_efficiency** = study_hours × class_attendance
- **sleep_score** = sleep_hours × sleep_quality
- **academic_engagement** = study_hours + attendance contribution
- **study_sleep_ratio** = study_hours ÷ sleep_hours

These features helped represent learning efficiency, engagement level, and study-life balance more effectively.

## Model Development

A **CatBoost Regressor** was selected because it performs exceptionally well on tabular datasets containing both numerical and categorical variables.

### Validation Strategy

- Train/Validation Split
- RMSE Evaluation
- Feature Engineering
- Kaggle Submission Testing

## Results

| Metric | Score |
|----------|----------|
| Validation RMSE | 8.766 |
| Kaggle Public Score | 8.75421 |

The model successfully captured the relationship between study behavior and academic achievement while maintaining strong leaderboard performance.

## Streamlit Application

A Streamlit web application was developed to allow users to enter student information and instantly receive a predicted exam score.

The application uses the trained CatBoost model and automatically generates the engineered features used during training.

## Live Demo

🔗 **[Hugging Face Demo](https://huggingface.co/spaces/MSK34/student-test-score-predictor)**

## Kaggle Notebook

🔗 **[Kaggle Notebook](https://www.kaggle.com/code/mhskaya/predict-student-test-scores)**

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- CatBoost
- Matplotlib
- Seaborn
- Streamlit
- Hugging Face Spaces

## Project Structure

```text
student-test-score-predictor
│
├── src
│   ├── app.py
│   ├── student_score_model.cbm
│   ├── feature_columns.pkl
│   └── categorical_features.pkl
│
├── README.md
├── requirements.txt
└── predict_student_test_scores.ipynb
```

## Conclusion

This project demonstrates how machine learning can be applied to educational analytics by predicting student exam scores from academic and behavioral data. The results show that study habits, attendance, sleep quality, and overall academic engagement have a significant impact on student performance. The combination of feature engineering and CatBoost regression produced a competitive Kaggle score and an interactive deployment for real-world use.
