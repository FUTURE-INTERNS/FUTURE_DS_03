# 🎓 Student Feedback Analysis

## Project Overview
This project leverages data science and machine learning to analyze student feedback collected from college events, courses, or instructors. By examining quantitative ratings and engineered features, we aim to uncover actionable insights and predict overall student satisfaction. The final deliverable includes a predictive model deployed via a user-friendly Streamlit web app, enabling stakeholders to assess satisfaction levels and identify areas for improvement in real time.

## Problem Statement
Colleges and universities regularly collect feedback from students to evaluate the effectiveness of their courses, instructors, and events. However, this feedback is often underutilized, with limited actionable insights extracted from the data. The challenge is to transform raw feedback into meaningful information that can guide improvements in teaching quality and event organization, and to develop a predictive system that can estimate student satisfaction based on their responses.

## Business Objectives
- Analyze student feedback data to identify key factors influencing satisfaction.
- Develop a predictive model that accurately classifies students as “High” or “Low” satisfaction based on their feedback ratings.
- Deploy the model in a Streamlit web app for easy, real-time predictions by stakeholders.
- Provide actionable recommendations to improve courses, events, and overall student experience.
- Enable data-driven decision making for academic and event planning committees.

## Evaluation of Metrics
- **Accuracy:** The primary metric for evaluating the classification model, aiming for at least 95% accuracy.
- **Precision & Recall:** To assess the model’s ability to correctly identify both high and low satisfaction students.
- **F1-Score:** To balance precision and recall, especially if the classes are imbalanced.
- **Confusion Matrix:** To visualize true/false positives and negatives for model predictions.
- **Cross-Validation Accuracy:** To ensure the model generalizes well to unseen data.

## Data Understanding
The dataset consists of student feedback collected via Google Forms or similar surveys. Each record represents a student’s ratings on various aspects of a course or event, such as subject knowledge, clarity of explanation, use of presentations, assignment difficulty, support provided, and overall course recommendation. The data is numeric, with ratings typically on a scale from 1 to 10. Additional engineered features, such as overall satisfaction score and satisfaction label, are created to facilitate analysis and modeling. No free-text comments are present in this dataset.

## Conclusion
This project successfully demonstrates how data science techniques can transform raw student feedback into actionable insights for educational improvement. By analyzing quantitative ratings from students, we identified key factors that influence overall satisfaction with courses and events. Through feature engineering and advanced machine learning models, we achieved high predictive accuracy in classifying student satisfaction levels. The deployment of the predictive model via a Streamlit web app enables real-time, user-friendly access for stakeholders, empowering them to make informed, data-driven decisions. Overall, this approach provides a scalable and effective solution for continuous enhancement of the student experience.

## Recommendations
- **Focus on Key Drivers:** Prioritize improvements in areas that most strongly influence satisfaction, such as clarity of explanation, course structure, and support provided to students.
- **Monitor Assignment Difficulty:** Regularly review and adjust assignment difficulty to ensure it is appropriately challenging but not overwhelming for students.
- **Enhance Use of Presentations:** Encourage instructors to make greater use of presentations and interactive teaching methods, as these are often linked to higher satisfaction.
- **Leverage Predictive Insights:** Use the deployed Streamlit app to proactively identify students or courses at risk of low satisfaction and intervene early.
- **Continuous Feedback Collection:** Maintain regular feedback collection and periodically retrain the model to adapt to changing student needs and expectations.
- **Expand Data Collection:** In future surveys, consider including open-ended questions to capture qualitative feedback, enabling sentiment analysis and deeper insights.

---

# 🎓 Student Feedback Analysis – MINI REPORT
## Graphs of Ratings

## Summary:

We analyzed student feedback across multiple aspects, including subject knowledge, clarity of explanation, use of presentations, assignment difficulty, support provided, course structure, and overall course recommendation.

## Key Visuals:

Bar Charts: Most students rated “Subject Knowledge” and “Recommend Course” highly, indicating general satisfaction.
Boxplots: Showed that while most ratings are high, there is some variability, especially in “Assignment Difficulty” and “Uses Presentations.”
Correlation Heatmap: Revealed strong positive relationships between “Explains Clearly,” “Subject Knowledge,” and “Recommend Course.”

## Sentiment Analysis Summary

Note: No open-ended comments were present in this dataset, so sentiment analysis and word clouds were not performed. If future surveys include text feedback, these analyses can provide deeper insights into student opinions and common themes.

## Key Recommendations for Event Organizers

### 1. Focus on Clarity and Engagement:

Improve clarity of explanations and encourage the use of presentations and interactive teaching methods, as these are closely linked to higher satisfaction.

### 2. Monitor Assignment Difficulty:

Regularly review assignment difficulty to ensure it is challenging but not overwhelming.

### 3. Enhance Support:

Continue to provide and improve extra support for students, as this positively impacts satisfaction.

### 4. Leverage Predictive Insights:

Use the deployed Streamlit app to identify students or courses at risk of low satisfaction and intervene early.

### 5. Continuous Feedback Collection:

Maintain regular feedback collection and periodically retrain the model to adapt to changing student needs.

### 6. Expand Data Collection:

In future surveys, include open-ended questions to enable sentiment analysis and word cloud visualizations for richer insights.

## Model Performance

- Best Model: SVM Classifier
- Test Accuracy: 96%
- Cross-Validated Accuracy: 91%
- Confusion Matrix: High precision and recall for both “High” and “Low” satisfaction classes.

## Conclusion

This project demonstrates the value of data-driven analysis in understanding and improving student satisfaction. By focusing on the most influential factors and leveraging predictive modeling, event and course organizers can make informed decisions to enhance the student experience.