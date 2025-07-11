import streamlit as st
import numpy as np
import joblib

# Load the scaler and model
scaler = joblib.load('scaler.pkl')
model = joblib.load('svm_model.pkl')

st.title("Student Satisfaction Prediction")

st.write("""
Enter the student's feedback ratings below (scale: 1-10):
""")

# Input fields for all features
subject_knowledge = st.slider('Subject Knowledge', 1, 10, 5)
explains_clearly = st.slider('Explains Clearly', 1, 10, 5)
uses_presentations = st.slider('Uses Presentations', 1, 10, 5)
assignment_difficulty = st.slider('Assignment Difficulty', 1, 10, 5)
solves_doubts = st.slider('Solves Doubts', 1, 10, 5)
course_structure = st.slider('Course Structure', 1, 10, 5)
extra_support = st.slider('Extra Support', 1, 10, 5)
recommend_course = st.slider('Recommend Course', 1, 10, 5)

# Collect input into a numpy array
features = np.array([[subject_knowledge, explains_clearly, uses_presentations,
                      assignment_difficulty, solves_doubts, course_structure,
                      extra_support, recommend_course]])

# Scale the input
features_scaled = scaler.transform(features)

if st.button('Predict Satisfaction'):
    prediction = model.predict(features_scaled)[0]
    label = 'High Satisfaction' if prediction == 1 else 'Low Satisfaction'
    st.success(f'Predicted Student Satisfaction: **{label}**')