# This script creates a simple Flask web application that provides the current time in various US time zones.
# It uses the pytz library to handle time zone conversions and Flask to create the web server.
# Import necessary libraries
from flask import Flask, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

# List of US time zones
us_time_zones = [
    "America/New_York", "America/Chicago", "America/Denver", "America/Los_Angeles",
    "America/Anchorage", "Pacific/Honolulu"
]

@app.route('/')
def home():
    return "Welcome to GETTIME API! Use `/timezones` to get time zone data."

@app.route('/timezones', methods=['GET'])
def get_timezones():
    print("Fetching timezones...")  # Debugging line
    time_data = {}
    for zone in us_time_zones:
        tz = pytz.timezone(zone)
        time_data[zone] = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S %Z')

    return jsonify(time_data)

if __name__ == '__main__':
    app.run(debug=True)

    

