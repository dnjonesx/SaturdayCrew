#this will be used to install dependencies when needed as it shouldn't need to be run everytime.
import subprocess
import sys
import importlib

def install_dependencies():
    # These are the names you use in 'import' statements
    packages = {
        "openmeteo_requests": "openmeteo-requests",
        "requests_cache": "requests-cache",
        "retry_requests": "retry-requests",
        "pandas": "pandas",
        "numpy": "numpy"
    }

    for module, install_name in packages.items():
        try:
            importlib.import_module(module)
        except ImportError:
            print(f"--- {install_name} not found. Installing... ---")
            
            # The Command: 
            # 1. sys.executable ensures we use the same Python VSCodium is using
            # 2. --break-system-packages bypasses the 'externally managed' error on Fedora/Mac
            # 3. --user installs it to your home folder instead of system folders
            cmd = [
                sys.executable, "-m", "pip", "install", 
                install_name, 
                "--user", 
                "--break-system-packages"
            ]
            
            try:
                subprocess.check_call(cmd)
            except subprocess.CalledProcessError:
                print(f"Failed to install {install_name}. You may need to install it manually.")

if __name__ == "__main__":
    install_dependencies()
    print("Dependencies check complete!")