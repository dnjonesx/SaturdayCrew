#I am thinking of using Open Meteo's free API for the weather. They also have a historical API which includes weather data from 1940-now. Violet might find this useful for his data processing.

#I need to use flask for this to get it set up and see how to receive/send http requests for the lat and long information and then the actual weather data. 

import openmeteo_requests
import requests_cache
from retry_requests import retry
import pandas as pd
import numpy as np
import os
from flask import Flask

url = "https://api.open-meteo.com/v1/forecast"

#set up Flask
app = Flask(__name__)

#Setting up API client with cache and retry
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

def generate_location(min: int, max: int):
    result = np.random.uniform(min, max)
    return round(result, 5)

def convert_kmh_to_word(current_wind):
    if current_wind == 0:
        air = "None"
    elif current_wind < 19:
        air = "Light"
    elif current_wind < 39:
        air = "Breezy"
    elif current_wind < 49:
        air = "Strong Breeze"
    elif current_wind < 61:
        air = "Very Windy"
    elif current_wind < 88:
        air = "Gale"
    elif current_wind < 117:
        air = "Bad Storm"
    else:
        air = "Hurricane"
    return air

def convert_mm_to_word(current_water):
    if current_water == 0:
        water = "None"
    elif current_water < 3:
        water = "Light"
    elif current_water < 8:
        water = "Moderate"
    elif current_water < 50:
        water = "Heavy"
    else:
        water = "Violent"
    return water

ran_lat = generate_location(-90.0, 90.0)
ran_long = generate_location(-180.0, 180.0)


ran_params = {
        "latitude": ran_lat,
        "longitude": ran_long,
        "current": ["temperature_2m", "precipitation", "wind_speed_10m"],
        "temperature_unit": "celsius",
    }
responses = openmeteo.weather_api(url, params = ran_params)
response = responses[0]
current = response.Current()
current_temp = round(current.Variables(0).Value(), 2)
current_water = current.Variables(1).Value()
current_wind = current.Variables(2).Value()
air = convert_kmh_to_word(round(current_wind, None))
water = convert_mm_to_word(round(current_water, None))

@app.route('/location/<id>', methods=['GET'])
def location():
    return None #temporarily

@app.route('/random')
def random_weather():
    random_data = {
        "latitude": ran_lat,
        "longitude": ran_long,
        "location": None,#i need to get location name from violet
        "timezone": None,#i need to get location name from violet
        "timezone_abbreviation": None,#i need to get location name from violet
        "temperature_2m": current_temp,
        "wind": air,
        "precipitation": water
    }
    return random_data  

app.run(host="0.0.0.0", port=9000)