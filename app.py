from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

RAPIDAPI_KEY = "21a09c8617msh9824fc42e884973p1ef091jsn7c5eafa3f211"  # Change this!

@app.route("/location", methods=["POST"])
def search_location():
    data = request.json
    city = data.get("query")
    url = "https://booking-com15.p.rapidapi.com/api/v1/flights/searchDestination"
    params = {"query": city}
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "booking-com15.p.rapidapi.com"
    }
    resp = requests.get(url, headers=headers, params=params)
    try:
        resp.raise_for_status()
        locations = resp.json()
        return jsonify(locations)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
