#this will be used to install dependencies when needed as it shouldn't need to be run everytime.

import subprocess
import sys

def install_dependencies():
    packages = ["openmeteo-requests", "requests-cache", "retry-requests", "pandas", "numpy", "ipykernel"]
    for package in packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            print(f"Importing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install_dependencies()