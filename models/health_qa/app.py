from flask import Flask, request, jsonify, render_template ,Blueprint
import pickle
import numpy as np
import os
#


healthqa_bp = Blueprint('healthqa', __name__, template_folder='templates')


module_dir = os.path.dirname(__file__)
model_path = os.path.join(module_dir, "model.pkl")
if not os.path.exists(model_path):
    raise FileNotFoundError("models/health_qa/model.pkl file not found. Ensure it exists in the repository.")

with open(model_path, "rb") as file:
    model = pickle.load(file)

@healthqa_bp.route('/')
def index():
    module_dir = os.path.dirname(__file__)
    if os.path.exists(os.path.join(module_dir, 'templates', 'health_qa_index.html')):
        return render_template('health_qa_index.html')
    return render_template('index.html')

# Explicit route for the button in case root collides
@healthqa_bp.route('/home')
def healthqa_home():
    return render_template('index.html')

@healthqa_bp.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        # Convert input data to a list of feature values
        features = [
            int(data.get("fever", "no") == "yes"),
            int(data.get("cough", "no") == "yes"),
            int(data.get("fatigue", "no") == "yes"),
            int(data.get("difficulty-breathing", "no") == "yes"),
            int(data.get("blood-pressure", "no") == "yes"),
            int(data.get("cold", "no") == "yes"),
            int(data.get("dizziness", "no") == "yes"),
            int(data.get("body-pain", "no") == "yes"),
            int(data.get("headache", "no") == "yes"),
            int(data.get("days", 0))
        ]
        
        # Convert to NumPy array and reshape for prediction
        input_array = np.array([features])
        prediction = model.predict(input_array)[0]
        
        return jsonify({"prediction": str(prediction)})
    except Exception as e:
        return jsonify({"error": str(e)})