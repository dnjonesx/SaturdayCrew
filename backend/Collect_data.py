#I am thinking of using Open Meteo's free API for the weather. They also have a historical API which includes weather data from 1940-now. Violet might find this useful for his data processing.

#First I want to have the program itself run the necessary commands to download the imported packages.
import subprocess
import sys

def install_dependencies():
    packages = ["openmeteo-requests", "requests-cache", "retry-requests"]
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

print("all dependencies are ready")