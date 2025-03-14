import streamlit as st
import pickle
import numpy as np

# Load your pre-trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Title and Header
st.set_page_config(page_title="Depression Test", layout="centered")
st.title("Depression Test")
st.write("Over the last 2 weeks, how often have you been bothered by any of the following problems? Please answer all questions.")

# Questions and options
questions = [
    "1. Little interest or pleasure in doing things",
    "2. Feeling down, depressed, or hopeless",
    "3. Trouble falling or staying asleep, or sleeping too much",
    "4. Feeling tired or having little energy",
    "5. Poor appetite or overeating",
    "6. Feeling bad about yourself - or that you are a failure or have let yourself or your family down",
    "7. Trouble concentrating on things, such as reading the newspaper or watching television",
    "8. Moving or speaking so slowly that other people could have noticed, or the opposite - being so fidgety or restless that you have been moving around a lot more than usual",
    "9. Thoughts that you would be better off dead, or of hurting yourself",
    "10. If you checked off any problems, how difficult have these problems made it for you at work, home, or with other people?"
]

options = ["Not At All", "Several Days", "More Than Half The Days", "Nearly Every Day"]

# Store user responses
responses = []

# Create a form for user inputs
with st.form("depression_test_form"):
    for i, question in enumerate(questions, 1):
        st.write(question)
        response = st.radio(
            label=f"Select your response for question {i}",
            options=options,
            key=f"question_{i}"
        )
        responses.append(response)

    # Submit button
    submitted = st.form_submit_button("Submit")

if submitted:
    # Map user responses to numerical values
    response_mapping = {
        "Not At All": 0,
        "Several Days": 1,
        "More Than Half The Days": 2,
        "Nearly Every Day": 3
    }
    
    # Convert responses to numerical format
    numerical_responses = [response_mapping[resp] for resp in responses]

    # Reshape input for prediction
    input_data = np.array(numerical_responses).reshape(1, -1)

    # Make a prediction
    try:
        prediction = model.predict(input_data)
        st.success(f"Your result: {'Positive' if prediction[0] == 1 else 'Negative'}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
