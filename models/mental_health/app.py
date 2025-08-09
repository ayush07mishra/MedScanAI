import pickle , os
import numpy as np
from flask import Flask
from flask import request, jsonify, render_template , Blueprint


module_dir = os.path.dirname(__file__)
model_path = os.path.join(module_dir, "model.pkl")
model = pickle.load(open(model_path, "rb"))



mental_bp = Blueprint('mental', __name__, template_folder='templates')

@mental_bp.route('/')
def mental_health():
    # Use a unique template name to avoid any cross-blueprint index.html collisions
    return render_template('mental_health_full.html')

@mental_bp.route('/home')
def mental_health_home():
    return render_template('mental_health_full.html')









@mental_bp.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json["answers"]
        mapping = {
            "Not At All": 0,
            "Several Days": 1,
            "More Than Half The Days": 2,
            "Very Difficult": 3,
            "Somewhat Difficult": 2,
            "Not Difficult At All": 1
        }
        numerical_input = [mapping.get(answer, 0) for answer in data]
        input_array = np.array(numerical_input).reshape(1, -1)
        prediction = model.predict(input_array)[0]

        return jsonify({"prediction": int(prediction)})

    except Exception as e:
        return jsonify({"error": str(e)})
