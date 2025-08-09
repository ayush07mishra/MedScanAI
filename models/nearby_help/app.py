# import requests
# from flask import Flask, render_template, request, jsonify
# from geopy.distance import geodesic

# app = Flask(__name__)

# @app.route('/nearby', methods=['GET'])
# def get_nearby_places():
#     lat = request.args.get('lat')
#     lng = request.args.get('lng')
#     place_type = request.args.get('type')

#     if not lat or not lng:
#         return jsonify({"error": "Latitude and longitude are required"}), 400

#     user_location = (float(lat), float(lng))
    
#     # ✅ Fix category issue (Medical Stores are actually "Pharmacy")
#     category = "pharmacy" if place_type == "medical_store" else "doctor"

#     # ✅ Use Overpass API for better results
#     url = f"https://overpass-api.de/api/interpreter?data=[out:json];node[amenity={category}](around:5000,{lat},{lng});out;"
    
#     headers = {"User-Agent": "MedScanAI/1.0 (ayush@example.com)"}
#     response = requests.get(url, headers=headers)

#     # ✅ Check if API is working
#     if response.status_code != 200:
#         return jsonify({"error": "API request failed", "status": response.status_code, "text": response.text}), 500
    
#     try:
#         data = response.json()
#     except requests.exceptions.JSONDecodeError:
#         return jsonify({"error": "Invalid JSON response from API"}), 500

#     nearby_places = []
#     for element in data.get("elements", []):
#         place_lat = element.get("lat")
#         place_lng = element.get("lon")
#         place_name = element.get("tags", {}).get("name", "Unknown Place")

#         if place_lat and place_lng:
#             distance = geodesic(user_location, (place_lat, place_lng)).km
#             if distance <= 5:
#                 nearby_places.append({
#                     "name": place_name,
#                     "latitude": place_lat,
#                     "longitude": place_lng,
#                     "distance": round(distance, 5)
#                 })

#     if nearby_places:
#         return jsonify(nearby_places)
#     else:
#         return jsonify({"error": "No places found within 5 km."}), 404

# @app.route('/')
# def index():
#     return render_template('index1.html')

# if __name__ == '__main__':
#     app.run(debug=True)



import requests
from flask import Blueprint, Flask, render_template, request, jsonify
from geopy.distance import geodesic
import os
module2_bp = Blueprint('model2_8', __name__) 














nearby_bp = Blueprint('nearby', __name__, template_folder='templates')

@nearby_bp.route('/')
def nearby_home():
    module_dir = os.path.dirname(__file__)
    if os.path.exists(os.path.join(module_dir, 'templates', 'nearby_help_index.html')):
        return render_template('nearby_help_index.html')
    return render_template('index.html')

# Explicit helper route
@nearby_bp.route('/home')
def nearby_home_alias():
    return render_template('index.html')










# Replace with your new Geoapify API key
GEOAPIFY_API_KEY = '19b13fb3d72044bab53370cb9fa462c7'

@nearby_bp.route('/nearby', methods=['GET'])
def get_nearby_places():
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    place_type = request.args.get('type')

    if not lat or not lng:
        return jsonify({"error": "Latitude and longitude are required"}), 400

    user_location = (float(lat), float(lng))

    # Fix categories for Geoapify API
    category = "healthcare.pharmacy" if place_type == "medical_store" else "healthcare.doctor"

    # Geoapify API URL
    url = (
        f"https://api.geoapify.com/v2/places?categories={category}"
        f"&filter=circle:{lng},{lat},5000&limit=50&apiKey={GEOAPIFY_API_KEY}"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "API request failed", "status": response.status_code, "text": response.text}), 500

    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        return jsonify({"error": "Invalid JSON response from API"}), 500

    nearby_places = []
    for feature in data.get("features", []):
        properties = feature.get("properties", {})
        place_name = properties.get("name", "Unknown Place")
        # Prefer properties lat/lon, else fallback to geometry coordinates
        place_lat = properties.get("lat")
        place_lng = properties.get("lon")
        if place_lat is None or place_lng is None:
            coords = feature.get("geometry", {}).get("coordinates")
            if isinstance(coords, (list, tuple)) and len(coords) >= 2:
                place_lng, place_lat = coords[0], coords[1]

        if place_lat is not None and place_lng is not None:
            distance = geodesic(user_location, (float(place_lat), float(place_lng))).km
            if distance <= 10:
                nearby_places.append({
                    "name": place_name,
                    "latitude": float(place_lat),
                    "longitude": float(place_lng),
                    "distance": round(distance, 3)
                })

    if nearby_places:
        return jsonify(nearby_places)
    else:
        return jsonify({"error": "No places found within 5 km."}), 404

 
