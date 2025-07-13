import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load all trained models and their accuracies
models = {
    "Logistic Regression": {
        "model": joblib.load("PersonalityPredictionLogReg.pkl"),
        "accuracy": 0.99  # replace with actual accuracy if different
    },
    "Decision Tree": {
        "model": joblib.load("PersonalityPredictionDT.pkl"),
        "accuracy": 0.99  # replace with actual accuracy if different
    },
    "SVM": {
        "model": joblib.load("PersonalityPredictionSVM.pkl"),
        "accuracy": 0.99  # replace with actual accuracy if different
    }
}

# Sidebar with project info
st.sidebar.title("About")
st.sidebar.info("""
**🔮 Personality Prediction App**

Made by: Dhruv Raghav 
Project: Personality Classification  
Models: Logistic Regression, Decision Tree, SVM  
""")

# App title and description
st.markdown("# 🔮 Personality Prediction App")
st.markdown("Predict whether a person is an Introvert or Extrovert based on their social behaviour using different ML models.")

# Show model accuracies in a table
st.subheader("📊 Model Performance Comparison")
model_metrics = {
    "Model": list(models.keys()),
    "Accuracy (%)": [models[m]["accuracy"]*100 for m in models]
}
metrics_df = pd.DataFrame(model_metrics)
st.table(metrics_df)

# Model selection
st.subheader("🔧 Choose Your Model")
model_choice = st.selectbox("Select a model for prediction:", list(models.keys()))
selected_model = models[model_choice]["model"]
model_accuracy = models[model_choice]["accuracy"]

# Model description
st.markdown("### 📌 Model Description")
if model_choice == "Logistic Regression":
    st.write("**Logistic Regression:** A linear model useful for binary classification tasks based on probabilities.")
elif model_choice == "Decision Tree":
    st.write("**Decision Tree:** A tree-structured model that splits data based on feature thresholds for decision-making.")
elif model_choice == "SVM":
    st.write("**SVM:** Classifies data by finding the optimal hyperplane separating classes for maximum margin.")

# Input fields
st.subheader("📝 Enter Your Details")
time_spent_alone = st.number_input("Time spent alone (hours per day)", min_value=0, step=1)
stage_fear = st.selectbox("Do you have stage fear?", ["Yes", "No"])
social_event_attendance = st.number_input("Number of social events attended per month", min_value=0, step=1)
going_outside_count = st.number_input("How many times do you go outside in a week?", min_value=0, step=1)

# Just for display (not used in prediction)
going_outside_preference = st.selectbox("Do you like going outside?", ["Yes", "No"])

drained_after_socializing = st.selectbox("Do you feel drained after socializing?", ["Yes", "No"])
friends_circle_size = st.number_input("Number of close friends", min_value=0, step=1)
post_frequency = st.number_input("Frequency of posting on social media (posts per week)", min_value=0, step=1)

# Convert categorical inputs to numeric
stage_fear_num = 1 if stage_fear == "Yes" else 0
drained_after_socializing_num = 1 if drained_after_socializing == "Yes" else 0

# Prepare input for model prediction
input_data = np.array([[time_spent_alone, stage_fear_num, social_event_attendance,
                        going_outside_count, drained_after_socializing_num,
                        friends_circle_size, post_frequency]])

# Session state for result
if 'result' not in st.session_state:
    st.session_state.result = None

# Prediction button
if st.button("🔮 Predict Personality"):
    result = selected_model.predict(input_data)
    personality = "Extrovert" if result[0] == 1 else "Introvert"
    st.session_state.result = f"The predicted personality using **{model_choice}** is: **{personality}**"
    st.balloons()

# Display result
if st.session_state.result:
    st.success(st.session_state.result)

    # Try Again button
    if st.button("🔁 Try Again"):
        st.session_state.result = None
        st.experimental_rerun()
