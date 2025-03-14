import streamlit as st
import pickle

# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Set page configuration
st.set_page_config(page_title="Health Questionnaire", page_icon="🏥", layout="centered")

# Header Section
st.title("Health Questionnaire")
st.markdown(
    "This brief questionnaire can help you get a better understanding of your current health status."
)
st.image(
    "https://file.forms.app/sitefile/35+essential-questions-to-ask-in-a-health-history-questionnaire.jpg",
    caption="Health History Questions",
    use_column_width=True
)

# Questionnaire Section
responses = {}

responses["fever"] = st.radio("Do you have a fever?", ["Yes", "No"], index=1)
responses["cough"] = st.radio("Do you have a cough?", ["Yes", "No"], index=1)
responses["fatigue"] = st.radio("Are you feeling fatigued?", ["Yes", "No"], index=1)
responses["difficulty_breathing"] = st.radio(
    "Are you experiencing difficulty breathing?", ["Yes", "No"], index=1
)
responses["blood_pressure"] = st.radio("Do you have blood pressure issues?", ["Yes", "No"], index=1)
responses["cold"] = st.radio("Are you feeling cold?", ["Yes", "No"], index=1)
responses["dizziness"] = st.radio("Are you feeling dizzy?", ["Yes", "No"], index=1)
responses["body_pain"] = st.radio("Do you have body pain?", ["Yes", "No"], index=1)
responses["headache"] = st.radio("Do you have a headache?", ["Yes", "No"], index=1)
responses["days"] = st.number_input(
    "For how many days have you had symptoms?", min_value=0, step=1
)

# Footer Section
if st.button("Submit"):
    try:
        st.write("Analyzing your responses...")

        # Convert responses to input features for the model
        input_features = [
            1 if responses["fever"] == "Yes" else 0,
            1 if responses["cough"] == "Yes" else 0,
            1 if responses["fatigue"] == "Yes" else 0,
            1 if responses["difficulty_breathing"] == "Yes" else 0,
            1 if responses["blood_pressure"] == "Yes" else 0,
            1 if responses["cold"] == "Yes" else 0,
            1 if responses["dizziness"] == "Yes" else 0,
            1 if responses["body_pain"] == "Yes" else 0,
            1 if responses["headache"] == "Yes" else 0,
            responses["days"]
        ]

        # Make prediction
        prediction = model.predict([input_features])[0]

        # Display result
        st.success(f"Prediction: {prediction}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Thank You Section
st.markdown(
    "---\n\nThank you for participating in the Health Questionnaire!"
)
