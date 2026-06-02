#I am thinking of using Open Meteo's free API for the weather. They also have a historical API which includes weather data from 1940-now. Violet might find this useful for his data processing.

#I need to use flask for this to get it set up and see how to receive/send http requests for the lat and long information and then the actual weather data.

#You can access random information via /random and local information via /local?lat=##.##&long=##.##

import openmeteo_requests
import requests_cache
from retry_requests import retry
import pandas as pd
import numpy as np
from flask import Flask, request

url = "https://api.open-meteo.com/v1/forecast"

#set up Flask
app = Flask(__name__)

#Setting up API client with cache and retry
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

def generate_location(min, max):
    result = np.random.uniform(min, max)
    return round(result, 5)

def convert_kmh_to_word(kmh):
    if kmh == 0:
        result = "None"
    elif kmh < 19:
        result = "Light"
    elif kmh < 39:
        result = "Breezy"
    elif kmh < 49:
        result = "Strong Breeze"
    elif kmh < 61:
        result = "Very Windy"
    elif kmh < 88:
        result = "Gale"
    elif kmh < 117:
        result = "Bad Storm"
    else:
        result = "Hurricane"
    return result

def convert_mm_to_word(mm):
    if mm == 0:
        result = "None"
    elif mm < 3:
        result = "Light"
    elif mm < 8:
        result = "Moderate"
    elif mm < 50:
        result = "Heavy"
    else:
        result = "Violent"
    return result

@app.route('/')
def home():
    return "This is the home page"

@app.route('/local')
def local():
    lat = request.args.get('lat')
    long = request.args.get('long')

    local_params = {
            "latitude": lat,
            "longitude": long,
            "current": ["temperature_2m", "precipitation", "wind_speed_10m"],
            "hourly": ["temperature_2m", "precipitation", "wind_speed_10m"],
            "daily": ["temperature_2m_max", "temperature_2m_min"]
        }

    responses = openmeteo.weather_api(url, params = local_params)
    response = responses[0]
    
    current = response.Current()
    current_temp = round(current.Variables(0).Value(), 1)
    current_water = current.Variables(1).Value()
    current_wind = current.Variables(2).Value()
    air = convert_kmh_to_word(round(current_wind, None))
    water = convert_mm_to_word(round(current_water, None))

    #Hourly temperature and date information
    hourly = response.Hourly()
    hourly_temp = hourly.Variables(0).ValuesAsNumpy()
    hourly_water = hourly.Variables(1).ValuesAsNumpy()
    hourly_wind = hourly.Variables(2).ValuesAsNumpy()

    hourly_temp = hourly_temp[:24]
    hourly_water = hourly_water[:24]
    hourly_wind = hourly_wind[:24]

    start_time = pd.to_datetime(hourly.Time(), unit = "s", utc = True)

    hourly_data = {
        "date": pd.date_range(
            start = start_time,
            end = start_time + pd.Timedelta(hours = 24),
            freq = pd.Timedelta(seconds = hourly.Interval()),
            inclusive = "left"
        )
    }

    hourly_data["temperature_2m"] = hourly_temp
    hourly_data["precipitation"] = hourly_water
    hourly_data["wind_speed_10m"] = hourly_wind
    hourly_dataframe = pd.DataFrame(data = hourly_data)
    hourly_dataframe['date'] = hourly_dataframe['date'].dt.strftime('%Y-%m-%d %H:%M')
    hourly_dataframe['temperature_2m'] = hourly_dataframe['temperature_2m'].round(1)
    hourly_dataframe['precipitation'] = hourly_dataframe['precipitation'].round(0).astype(int)
    hourly_dataframe['wind_speed_10m'] = hourly_dataframe['wind_speed_10m'].round(0).astype(int)
    local_date = hourly_dataframe['date'].tolist()
    local_temp = [round(float(t), 1) for t in hourly_dataframe['temperature_2m'].tolist()]
    local_water = hourly_dataframe['precipitation'].tolist()
    local_wind = hourly_dataframe['wind_speed_10m'].tolist()

    local_water_word = []
    for i in local_water:
        result = convert_mm_to_word(i)
        local_water_word.append(result)

    local_wind_word = []
    for i in local_wind:
        result = convert_kmh_to_word(i)
        local_wind_word.append(result)

    #Daily min and max temperatures
    daily = response.Daily()
    daily_max = daily.Variables(0).ValuesAsNumpy().tolist()
    daily_min = daily.Variables(1).ValuesAsNumpy().tolist()

    daily_max = [round(t, 1) for t in daily_max]
    daily_min = [round(t, 1) for t in daily_min]

    daily_data = {
        "date": pd.date_range(
            start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
            end =  pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
            freq = pd.Timedelta(seconds = daily.Interval()),
            inclusive = "left"
        )
    }

    daily_data["temperature_2m_max"] = daily_max
    daily_data["temperature_2m_min"] = daily_min

    local_data = {
        "latitude": lat,
        "longitude": long,
        "location": None,#i need to get location name from violet
        "timezone": None,#i need to get location name from violet
        "timezone_abbreviation": None,#i need to get location name from violet
        "current_temp": current_temp,
        "current_wind": air,
        "current_water": water,
        "hours": local_date,
        "hourly_temp": local_temp,
        "hourly_water": local_water_word,
        "hourly_wind": local_wind_word,
        "daily_max": daily_max,
        "daily_min": daily_min
    }
    return local_data

@app.route('/random')
def random_weather():
    random_lat = generate_location(-90.0, 90.0)
    random_long = generate_location(-180.0, 180.0)

    random_params = {
            "latitude": random_lat,
            "longitude": random_long,
            "current": ["temperature_2m", "precipitation", "wind_speed_10m"]
        }
    responses = openmeteo.weather_api(url, params = random_params)
    response = responses[0]
    current = response.Current()
    current_temp = round(current.Variables(0).Value(), 1)
    current_water = current.Variables(1).Value()
    current_wind = current.Variables(2).Value()
    air = convert_kmh_to_word(round(current_wind, None))
    water = convert_mm_to_word(round(current_water, None))

    random_data = {
        "latitude": random_lat,
        "longitude": random_long,
        "location": None,#i need to get location name from violet
        "timezone": None,#i need to get location name from violet
        "timezone_abbreviation": None,#i need to get location name from violet
        "temp": current_temp,
        "wind": air,
        "water": water
    }
    return random_data  

app.run(host="0.0.0.0", port=9000)