#I am thinking of using Open Meteo's free API for the weather. They also have a historical API which includes weather data from 1940-now. Violet might find this useful for his data processing.

#First I want to have the program itself run the necessary commands to download the imported packages.
import subprocess
import sys

def install_dependencies():
    packages = ["openmeteo-requests", "requests-cache", "retry-requests", "pandas"]
    for package in packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            print(f"Importing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install_dependencies()

import openmeteo_requests
import requests_cache
from retry_requests import retry
import pandas as pd

#Setting up API client with cache and retry
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

locations = [52.52, 13.41, 40.69, -80.12]

user_location = input("What location would you like to know the temperature for? Cranberry or Berlin? ")

if user_location == "Berlin":
    user_location1 = locations[0]
    user_location2 = locations[1]
if user_location == "Cranberry":
    user_location1 = locations[2]
    user_location2 = locations[3]

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": user_location1,
    "longitude": user_location2,
    "hourly": "temperature_2m",
    "forecast_days": 1,
    "temperature_unit": "fahrenheit",
}

responses = openmeteo.weather_api(url, params = params)
response = responses[0]

hourly = response.Hourly()
hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

hourly_data = {"date": pd.date_range(
	start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
	end =  pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
	freq = pd.Timedelta(seconds = hourly.Interval()),
	inclusive = "left"
)}

hourly_data["temperature_2m"] = hourly_temperature_2m

hourly_dataframe = pd.DataFrame(data = hourly_data)
print("\nHourly data\n", hourly_dataframe)