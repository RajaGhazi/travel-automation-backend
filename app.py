from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

RAPIDAPI_KEY = "21a09c8617msh9824fc42e884973p1ef091jsn7c5eafa3f211"
RAPIDAPI_HOST = "booking-com15.p.rapidapi.com"
BASE_URL = f"https://{RAPIDAPI_HOST}/api/v1"

HEADERS = {
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": RAPIDAPI_HOST
}

@app.route("/")
def home():
    return jsonify({"status": "Travel Automation Backend is live!"})

# ----------------- HOTEL ENDPOINTS -----------------

@app.route("/hotel/search-destination", methods=["POST"])
def hotel_search_destination():
    data = request.json
    url = f"{BASE_URL}/hotels/searchDestination"
    params = {"query": data.get("query")}
    return proxy_get(url, params)

@app.route("/hotel/get-filter", methods=["POST"])
def hotel_get_filter():
    data = request.json
    url = f"{BASE_URL}/hotels/getFilter"
    return proxy_post(url, data)

@app.route("/hotel/get-sort-by", methods=["POST"])
def hotel_get_sort_by():
    data = request.json
    url = f"{BASE_URL}/hotels/getSortBy"
    return proxy_post(url, data)

@app.route("/hotel/search-hotels", methods=["POST"])
def hotel_search_hotels():
    data = request.json
    url = f"{BASE_URL}/hotels/searchHotels"
    return proxy_post(url, data)

@app.route("/hotel/search-hotels-by-coordinates", methods=["POST"])
def hotel_search_hotels_by_coordinates():
    data = request.json
    url = f"{BASE_URL}/hotels/searchHotelsByCoordinates"
    return proxy_post(url, data)

@app.route("/hotel/get-hotel-details", methods=["POST"])
def hotel_get_hotel_details():
    data = request.json
    url = f"{BASE_URL}/hotels/getHotelDetails"
    return proxy_post(url, data)

@app.route("/hotel/get-room-availability", methods=["POST"])
def hotel_get_room_availability():
    data = request.json
    url = f"{BASE_URL}/hotels/getRoomAvailability"
    return proxy_post(url, data)

@app.route("/hotel/get-description-info", methods=["POST"])
def hotel_get_description_info():
    data = request.json
    url = f"{BASE_URL}/hotels/getDescriptionAndInfo"
    return proxy_post(url, data)

@app.route("/hotel/get-room-list", methods=["POST"])
def hotel_get_room_list():
    data = request.json
    url = f"{BASE_URL}/hotels/getRoomList"
    return proxy_post(url, data)

@app.route("/hotel/get-payment-features", methods=["POST"])
def hotel_get_payment_features():
    data = request.json
    url = f"{BASE_URL}/hotels/getPaymentFeatures"
    return proxy_post(url, data)

@app.route("/hotel/get-hotel-policies", methods=["POST"])
def hotel_get_hotel_policies():
    data = request.json
    url = f"{BASE_URL}/hotels/getHotelPolicies"
    return proxy_post(url, data)

@app.route("/hotel/property-children-policies", methods=["POST"])
def hotel_property_children_policies():
    data = request.json
    url = f"{BASE_URL}/hotels/propertyChildrenPolicies"
    return proxy_post(url, data)

@app.route("/hotel/get-hotel-reviews-filter-metadata", methods=["POST"])
def hotel_get_hotel_reviews_filter_metadata():
    data = request.json
    url = f"{BASE_URL}/hotels/getHotelReviewsFilterMetadata"
    return proxy_post(url, data)

@app.route("/hotel/get-hotel-review-scores", methods=["POST"])
def hotel_get_hotel_review_scores():
    data = request.json
    url = f"{BASE_URL}/hotels/getHotelReviewScores"
    return proxy_post(url, data)

@app.route("/hotel/get-hotel-reviews-tips-sort-option", methods=["POST"])
def hotel_get_hotel_reviews_tips_sort_option():
    data = request.json
    url = f"{BASE_URL}/hotels/getHotelReviewsTipsSortOption"
    return proxy_post(url, data)

@app.route("/hotel/get-hotel-reviews-tips", methods=["POST"])
def hotel_get_hotel_reviews_tips():
    data = request.json
    url = f"{BASE_URL}/hotels/getHotelReviewsTips"
    return proxy_post(url, data)

@app.route("/hotel/get-question-answer", methods=["POST"])
def hotel_get_question_answer():
    data = request.json
    url = f"{BASE_URL}/hotels/getQuestionAndAnswer"
    return proxy_post(url, data)

@app.route("/hotel/get-nearby-cities", methods=["POST"])
def hotel_get_nearby_cities():
    data = request.json
    url = f"{BASE_URL}/hotels/getNearbyCities"
    return proxy_post(url, data)

@app.route("/hotel/get-popular-attraction-nearby", methods=["POST"])
def hotel_get_popular_attraction_nearby():
    data = request.json
    url = f"{BASE_URL}/hotels/getPopularAttractionNearby"
    return proxy_post(url, data)

@app.route("/hotel/get-room-list-with-availability", methods=["POST"])
def hotel_get_room_list_with_availability():
    data = request.json
    url = f"{BASE_URL}/hotels/getRoomListWithAvailability"
    return proxy_post(url, data)

@app.route("/hotel/get-hotel-photos", methods=["POST"])
def hotel_get_hotel_photos():
    data = request.json
    url = f"{BASE_URL}/hotels/getHotelPhotos"
    return proxy_post(url, data)

@app.route("/hotel/get-hotel-facilities", methods=["POST"])
def hotel_get_hotel_facilities():
    data = request.json
    url = f"{BASE_URL}/hotels/getHotelFacilities"
    return proxy_post(url, data)

# ----------------- FLIGHT ENDPOINTS -----------------

@app.route("/flight/search-location", methods=["POST"])
def flight_search_location():
    data = request.json
    url = f"{BASE_URL}/flights/searchDestination"
    params = {"query": data.get("query")}
    return proxy_get(url, params)

@app.route("/flight/search-flights", methods=["POST"])
def flight_search_flights():
    data = request.json
    url = f"{BASE_URL}/flights/searchFlights"
    return proxy_post(url, data)

@app.route("/flight/search-flights-multi-stops", methods=["POST"])
def flight_search_flights_multi_stops():
    data = request.json
    url = f"{BASE_URL}/flights/searchFlightsMultiStops"
    return proxy_post(url, data)

@app.route("/flight/get-flight-details", methods=["POST"])
def flight_get_flight_details():
    data = request.json
    url = f"{BASE_URL}/flights/getFlightDetails"
    return proxy_post(url, data)

@app.route("/flight/get-min-price", methods=["POST"])
def flight_get_min_price():
    data = request.json
    url = f"{BASE_URL}/flights/getMinPrice"
    return proxy_post(url, data)

@app.route("/flight/get-min-price-multi-stops", methods=["POST"])
def flight_get_min_price_multi_stops():
    data = request.json
    url = f"{BASE_URL}/flights/getMinPriceMultiStops"
    return proxy_post(url, data)

@app.route("/flight/get-seat-map", methods=["POST"])
def flight_get_seat_map():
    data = request.json
    url = f"{BASE_URL}/flights/getSeatMap"
    return proxy_post(url, data)

# ----------------- ATTRACTION ENDPOINTS -----------------

@app.route("/attraction/search-location", methods=["POST"])
def attraction_search_location():
    data = request.json
    url = f"{BASE_URL}/attractions/searchDestination"
    params = {"query": data.get("query")}
    return proxy_get(url, params)

@app.route("/attraction/search-attractions", methods=["POST"])
def attraction_search_attractions():
    data = request.json
    url = f"{BASE_URL}/attractions/searchAttractions"
    return proxy_post(url, data)

@app.route("/attraction/get-availability-calendar", methods=["POST"])
def attraction_get_availability_calendar():
    data = request.json
    url = f"{BASE_URL}/attractions/getAvailabilityCalendar"
    return proxy_post(url, data)

@app.route("/attraction/get-availability", methods=["POST"])
def attraction_get_availability():
    data = request.json
    url = f"{BASE_URL}/attractions/getAvailability"
    return proxy_post(url, data)

@app.route("/attraction/get-attraction-details", methods=["POST"])
def attraction_get_attraction_details():
    data = request.json
    url = f"{BASE_URL}/attractions/getAttractionDetails"
    return proxy_post(url, data)

@app.route("/attraction/get-attraction-review", methods=["POST"])
def attraction_get_attraction_review():
    data = request.json
    url = f"{BASE_URL}/attractions/getAttractionReview"
    return proxy_post(url, data)

# ----------------- HELPER FUNCTIONS -----------------

def proxy_get(url, params):
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def proxy_post(url, data):
    try:
        response = requests.post(url, headers=HEADERS, json=data)
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
