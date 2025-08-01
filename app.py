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

def proxy_get(url, params):
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def home():
    return jsonify({"status": "Travel Automation Backend is live!"})

# ------------ HOTELS ---------------
@app.route("/hotel/search-destination", methods=["GET"])
def hotel_search_destination():
    return proxy_get(f"{BASE_URL}/hotels/searchDestination", request.args)

@app.route("/hotel/get-filter", methods=["GET"])
def hotel_get_filter():
    return proxy_get(f"{BASE_URL}/hotels/getFilter", request.args)

@app.route("/hotel/get-sort-by", methods=["GET"])
def hotel_get_sort_by():
    return proxy_get(f"{BASE_URL}/hotels/getSortBy", request.args)

@app.route("/hotel/search-hotels", methods=["GET"])
def hotel_search_hotels():
    return proxy_get(f"{BASE_URL}/hotels/searchHotels", request.args)

@app.route("/hotel/search-hotels-by-coordinates", methods=["GET"])
def hotel_search_hotels_by_coordinates():
    return proxy_get(f"{BASE_URL}/hotels/searchHotelsByCoordinates", request.args)

@app.route("/hotel/get-hotel-details", methods=["GET"])
def hotel_get_hotel_details():
    return proxy_get(f"{BASE_URL}/hotels/getHotelDetails", request.args)

@app.route("/hotel/get-room-availability", methods=["GET"])
def hotel_get_room_availability():
    return proxy_get(f"{BASE_URL}/hotels/getRoomAvailability", request.args)

@app.route("/hotel/get-description-info", methods=["GET"])
def hotel_get_description_info():
    return proxy_get(f"{BASE_URL}/hotels/getDescriptionAndInfo", request.args)

@app.route("/hotel/get-room-list", methods=["GET"])
def hotel_get_room_list():
    return proxy_get(f"{BASE_URL}/hotels/getRoomList", request.args)

@app.route("/hotel/get-payment-features", methods=["GET"])
def hotel_get_payment_features():
    return proxy_get(f"{BASE_URL}/hotels/getPaymentFeatures", request.args)

@app.route("/hotel/get-hotel-policies", methods=["GET"])
def hotel_get_hotel_policies():
    return proxy_get(f"{BASE_URL}/hotels/getHotelPolicies", request.args)

@app.route("/hotel/property-children-policies", methods=["GET"])
def hotel_property_children_policies():
    return proxy_get(f"{BASE_URL}/hotels/propertyChildrenPolicies", request.args)

@app.route("/hotel/get-hotel-reviews-filter-metadata", methods=["GET"])
def hotel_get_hotel_reviews_filter_metadata():
    return proxy_get(f"{BASE_URL}/hotels/getHotelReviewsFilterMetadata", request.args)

@app.route("/hotel/get-hotel-review-scores", methods=["GET"])
def hotel_get_hotel_review_scores():
    return proxy_get(f"{BASE_URL}/hotels/getHotelReviewScores", request.args)

@app.route("/hotel/get-hotel-reviews-tips-sort-option", methods=["GET"])
def hotel_get_hotel_reviews_tips_sort_option():
    return proxy_get(f"{BASE_URL}/hotels/getHotelReviewsTipsSortOption", request.args)

@app.route("/hotel/get-hotel-reviews-tips", methods=["GET"])
def hotel_get_hotel_reviews_tips():
    return proxy_get(f"{BASE_URL}/hotels/getHotelReviewsTips", request.args)

@app.route("/hotel/get-question-answer", methods=["GET"])
def hotel_get_question_answer():
    return proxy_get(f"{BASE_URL}/hotels/getQuestionAndAnswer", request.args)

@app.route("/hotel/get-nearby-cities", methods=["GET"])
def hotel_get_nearby_cities():
    return proxy_get(f"{BASE_URL}/hotels/getNearbyCities", request.args)

@app.route("/hotel/get-popular-attraction-nearby", methods=["GET"])
def hotel_get_popular_attraction_nearby():
    return proxy_get(f"{BASE_URL}/hotels/getPopularAttractionNearby", request.args)

@app.route("/hotel/get-room-list-with-availability", methods=["GET"])
def hotel_get_room_list_with_availability():
    return proxy_get(f"{BASE_URL}/hotels/getRoomListWithAvailability", request.args)

@app.route("/hotel/get-hotel-photos", methods=["GET"])
def hotel_get_hotel_photos():
    return proxy_get(f"{BASE_URL}/hotels/getHotelPhotos", request.args)

@app.route("/hotel/get-hotel-facilities", methods=["GET"])
def hotel_get_hotel_facilities():
    return proxy_get(f"{BASE_URL}/hotels/getHotelFacilities", request.args)

# ------------ FLIGHTS ---------------
@app.route("/flight/search-location", methods=["GET"])
def flight_search_location():
    return proxy_get(f"{BASE_URL}/flights/searchDestination", request.args)

@app.route("/flight/search-flights", methods=["GET"])
def flight_search_flights():
    return proxy_get(f"{BASE_URL}/flights/searchFlights", request.args)

@app.route("/flight/search-flights-multi-stops", methods=["GET"])
def flight_search_flights_multi_stops():
    return proxy_get(f"{BASE_URL}/flights/searchFlightsMultiStops", request.args)

@app.route("/flight/get-flight-details", methods=["GET"])
def flight_get_flight_details():
    return proxy_get(f"{BASE_URL}/flights/getFlightDetails", request.args)

@app.route("/flight/get-min-price", methods=["GET"])
def flight_get_min_price():
    return proxy_get(f"{BASE_URL}/flights/getMinPrice", request.args)

@app.route("/flight/get-min-price-multi-stops", methods=["GET"])
def flight_get_min_price_multi_stops():
    return proxy_get(f"{BASE_URL}/flights/getMinPriceMultiStops", request.args)

@app.route("/flight/get-seat-map", methods=["GET"])
def flight_get_seat_map():
    return proxy_get(f"{BASE_URL}/flights/getSeatMap", request.args)

# ------------ ATTRACTIONS ---------------
@app.route("/attraction/search-location", methods=["GET"])
def attraction_search_location():
    return proxy_get(f"{BASE_URL}/attractions/searchDestination", request.args)

@app.route("/attraction/search-attractions", methods=["GET"])
def attraction_search_attractions():
    return proxy_get(f"{BASE_URL}/attractions/searchAttractions", request.args)

@app.route("/attraction/get-availability-calendar", methods=["GET"])
def attraction_get_availability_calendar():
    return proxy_get(f"{BASE_URL}/attractions/getAvailabilityCalendar", request.args)

@app.route("/attraction/get-availability", methods=["GET"])
def attraction_get_availability():
    return proxy_get(f"{BASE_URL}/attractions/getAvailability", request.args)

@app.route("/attraction/get-attraction-details", methods=["GET"])
def attraction_get_attraction_details():
    return proxy_get(f"{BASE_URL}/attractions/getAttractionDetails", request.args)

@app.route("/attraction/get-attraction-review", methods=["GET"])
def attraction_get_attraction_review():
    return proxy_get(f"{BASE_URL}/attractions/getAttractionReview", request.args)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
