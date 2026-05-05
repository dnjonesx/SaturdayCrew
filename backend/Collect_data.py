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

print(f"Latitude: ", {ran_lat}, "Longitude: ", {ran_long})

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": ran_lat,
    "longitude": ran_long,
    "current": "temperature_2m",
    "forecast_days": 1,
    "temperature_unit": "fahrenheit",
}

responses = openmeteo.weather_api(url, params = params)
response = responses[0]

current = response.Current()
current_temperature_2m = round(current.Variables(0).Value(), 2)

print(f"Current Temperature: {current_temperature_2m}")