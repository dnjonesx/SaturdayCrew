#I am thinking of using Open Meteo's free API for the weather. They also have a historical API which includes weather data from 1940-now. Violet might find this useful for his data processing.

import openmeteo_requests
import requests_cache
from retry_requests import retry
import pandas as pd
import numpy as np

#Setting up API client with cache and retry
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

def generate_latitude():
    ran_lat = np.random.uniform(-90.0, 90.0)
    return round(ran_lat, 5)
ran_lat = generate_latitude()

def generate_longitude():
    ran_long = np.random.uniform(-180.0, 180.0)
    return round(ran_long, 5)
ran_long = generate_longitude()

print(f"Latitude:", {ran_lat})
print(f"Longitude:", {ran_long})

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": ran_lat,
    "longitude": ran_long,
    "current": ["temperature_2m", "precipitation", "wind_speed_10m"],
    "temperature_unit": "celsius",
}

responses = openmeteo.weather_api(url, params = params)
response = responses[0]

current = response.Current()
current_temperature_2m = round(current.Variables(0).Value(), 2)
current_precipitation = current.Variables(1).Value()
current_wind_speed_10m = current.Variables(2).Value()

wind = round(current_wind_speed_10m, None)
rain = round(current_precipitation, None)

def convert_kmh_to_word(wind):
    if wind == 0:
        air = "None"
    elif wind in range(0, 19):
        air = "Light"
    elif wind in range(20, 38):
        air = "Breezy"
    elif wind in range(39, 49):
        air = "Strong Breeze"
    elif wind in range(50, 61):
        air = "Very Windy"
    elif wind in range(62, 88):
        air = "Gale"
    elif wind in range(89, 117):
        air = "Bad Storm"
    else:
        air = "Hurricane"
    return air

air = convert_kmh_to_word(wind)

def convert_mm_to_word(rain):
    if rain == 0:
        water = "None"
    elif rain in range(0, 3):
        water = "Light"
    elif rain in range(3, 8):
        water = "Moderate"
    elif rain in range(8, 50):
        water = "Heavy"
    else:
        water = "Violent"
    return water

water = convert_mm_to_word(rain)

print(f"Current Temperature: {current_temperature_2m} °C")
print(f"Current Precipitation: {water}")
print(f"Wind Speed: {air}")