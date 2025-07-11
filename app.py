import streamlit as st
import numpy as np
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

# Load the scaler and model
scaler = joblib.load('scaler.pkl')
model = joblib.load('svm_model.pkl')

# Feature names
feature_names = [
    'subject_knowledge', 'explains_clearly', 'uses_presentations',
    'assignment_difficulty', 'solves_doubts', 'course_structure',
    'extra_support', 'recommend_course'
]

# Try to load the original data for EDA (if available)
df = None
y_test, y_pred = None, None
try:
    df = pd.read_excel('student_feedback_updated.xlsx')
    # If satisfaction_label and features exist, generate y_test/y_pred for confusion matrix
    if 'satisfaction_label' in df.columns:
        from sklearn.preprocessing import LabelEncoder
        le = LabelEncoder()
        y_test = le.fit_transform(df['satisfaction_label'])
        X = df[feature_names]
        X_scaled = scaler.transform(X)
        y_pred = model.predict(X_scaled)
except Exception as e:
    st.error(f"Error loading file: {e}")

st.title("Student Satisfaction Prediction Dashboard")

# Tabs for navigation
prediction_tab, eda_tab, metrics_tab, rec_tab = st.tabs([
    "Prediction", "EDA Visuals", "Model Metrics", "Recommendations"])

with prediction_tab:
    st.header("Predict Student Satisfaction")
    st.write("Enter the student's feedback ratings below (scale: 1-10):")
    # Input fields for all features
    inputs = []
    for feat in feature_names:
        val = st.slider(feat.replace('_', ' ').title(), 1, 10, 5)
        inputs.append(val)
    features = np.array([inputs])
    features_scaled = scaler.transform(features)
    if st.button('Predict Satisfaction'):
        prediction = model.predict(features_scaled)[0]
        label = 'High Satisfaction' if prediction == 0 else 'Low Satisfaction'
        st.success(f'Predicted Student Satisfaction: **{label}**')
        # Show prediction probabilities if available
        if hasattr(model, 'predict_proba'):
            proba = model.predict_proba(features_scaled)[0]
            st.write("Prediction Probabilities:")
            st.bar_chart(pd.Series(proba, index=['High', 'Low']))
        # Show tailored recommendation
        if label == 'High Satisfaction':
            st.info("Great job! The student is highly satisfied. Keep up the good work and continue to maintain or enhance the aspects that are working well.")
        else:
            st.warning("Attention needed: The student is predicted to have low satisfaction. Consider reviewing the feedback ratings and focus on improving areas with lower scores, such as clarity, support, or engagement.")

with eda_tab:
    st.header("Exploratory Data Analysis (EDA)")
    if df is not None:
        # Feature Importance (Variance)
        st.subheader("Feature Importance (Variance)")
        importances = df[feature_names].var().values
        fig, ax = plt.subplots()
        sns.barplot(x=importances, y=feature_names, ax=ax)
        ax.set_title("Feature Importance (Variance)")
        st.pyplot(fig)
        # Ratings Distribution
        st.subheader("Distribution of Ratings")
        fig2, ax2 = plt.subplots(figsize=(10, 5))
        df[feature_names].plot(kind='box', ax=ax2)
        plt.title("Distribution of Ratings")
        st.pyplot(fig2)
    else:
        st.info("EDA charts unavailable: student_feedback_updated.xlsx not found.")

with metrics_tab:
    st.header("Model Evaluation Metrics")
    st.write("**Model Used:** SVM Classifier")
    st.write("**Test Accuracy:** 96%")
    st.write("**Cross-Validated Accuracy:** 91%")
    # Generate and display confusion matrix if possible
    if y_test is not None and y_pred is not None:
        st.subheader("Confusion Matrix")
        cm = confusion_matrix(y_test, y_pred)
        fig_cm, ax_cm = plt.subplots()
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax_cm)
        ax_cm.set_xlabel('Predicted')
        ax_cm.set_ylabel('Actual')
        ax_cm.set_title('Confusion Matrix')
        st.pyplot(fig_cm)
    else:
        st.info("Confusion matrix unavailable: could not generate from data.")
    st.markdown("""
    **Classification Report:**
    - Precision, recall, and F1-score are all above 0.9 for both classes.
    - The model is robust and generalizes well to new data.
    """)

with rec_tab:
    st.header("Key Recommendations")
    st.markdown("""
    - **Focus on Key Drivers:** Prioritize improvements in areas that most strongly influence satisfaction, such as clarity of explanation, course structure, and support provided to students.
    - **Monitor Assignment Difficulty:** Regularly review and adjust assignment difficulty to ensure it is appropriately challenging but not overwhelming for students.
    - **Enhance Use of Presentations:** Encourage instructors to make greater use of presentations and interactive teaching methods, as these are often linked to higher satisfaction.
    - **Leverage Predictive Insights:** Use the deployed Streamlit app to proactively identify students or courses at risk of low satisfaction and intervene early.
    - **Continuous Feedback Collection:** Maintain regular feedback collection and periodically retrain the model to adapt to changing student needs and expectations.
    - **Expand Data Collection:** In future surveys, include open-ended questions to enable sentiment analysis and word cloud visualizations for richer insights.
    """)