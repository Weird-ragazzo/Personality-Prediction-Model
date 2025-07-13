import streamlit as st
import joblib
import numpy as np

# Load the trained SVM model using joblib
model = joblib.load('PersonalityPredictionSVM.pkl')

# Streamlit UI
st.title("Personality Prediction App (SVM)")
st.write("This model was made using a **Support Vector Machine (SVM)** classifier.")
st.write("Predict whether a person is an Introvert or Extrovert based on their social behaviour.")

# Input fields
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
if st.button("Predict Personality"):
    result = model.predict(input_data)
    personality = "Extrovert" if result[0] == 1 else "Introvert"
    st.session_state.result = f"The predicted personality is: **{personality}**"

# Display result
if st.session_state.result:
    st.success(st.session_state.result)

    # Try Again button
    if st.button("Try Again"):
        st.session_state.result = None
        st.experimental_rerun()
