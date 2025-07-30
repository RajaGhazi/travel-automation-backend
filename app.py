from flask import Flask, request, jsonify
from flask_cors import CORS
import asyncio
from flight_scraper import fetch_flight_price

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Hello from your travel backend!"

@app.route("/quote", methods=["POST"])
def quote():
    data = request.json
    from_location = data.get("from")
    to_location = data.get("to")
    date = data.get("date")  # Format: yymmdd

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    price = loop.run_until_complete(fetch_flight_price(from_location, to_location, date))

    if price is None:
        return jsonify({"error": "No price found, try again later."}), 404

    price_with_markup = round(price * 1.15, 2)
    return jsonify({
        "from": from_location,
        "to": to_location,
        "date": date,
        "price_with_markup": price_with_markup
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)