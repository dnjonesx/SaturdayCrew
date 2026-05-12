#I am thinking of using Open Meteo's free API for the weather. They also have a historical API which includes weather data from 1940-now. Violet might find this useful for his data processing.

#I need to use flask for this to get it set up and see how to receive/send http requests for the lat and long information and then the actual weather data. 

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

print(f"Latitude:, {ran_lat}")
print(f"Longitude:, {ran_long}")

#here i would like to have it use those coordinates to reference Violet's sql to give the name of the location instead
#print(f"Location:, {location}")

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
    elif wind < 19:
        air = "Light"
    elif wind < 39:
        air = "Breezy"
    elif wind < 49:
        air = "Strong Breeze"
    elif wind < 61:
        air = "Very Windy"
    elif wind < 88:
        air = "Gale"
    elif wind < 117:
        air = "Bad Storm"
    else:
        air = "Hurricane"
    return air

air = convert_kmh_to_word(wind)

def convert_mm_to_word(rain):
    if rain == 0:
        water = "None"
    elif rain < 3:
        water = "Light"
    elif rain < 8:
        water = "Moderate"
    elif rain < 50:
        water = "Heavy"
    else:
        water = "Violent"
    return water

water = convert_mm_to_word(rain)

print(f"Current Temperature: {current_temperature_2m} °C")
print(f"Current Precipitation: {water}")
print(f"Wind Speed: {air}")