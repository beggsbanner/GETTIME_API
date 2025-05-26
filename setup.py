#!/bin/bash
import venv
from xml.sax import _Source


import subprocess
import os

# Create a virtual environment
subprocess.run(["python3", "-m", "venv", "my_env"])

# Activate the virtual environment
activate_script = os.path.join("my_env", "bin", "activate")
subprocess.run(["source", activate_script], shell=True, executable="/bin/bash")

# Install required packages
subprocess.run(["pip", "install", "-r", "requirements.txt"])

# Run the GUI application
subprocess.run(["python", "GETTIMEAPIGUI.py"])

# Make the install script executable
subprocess.run(["chmod", "+x", "install.sh"])
# This script creates a virtual environment, activates it, installs the required packages from requirements.txt, and runs the GUI application.
# It also makes the script executable.
# Make sure to run this script in the same directory as the GETTIMEAPIGUI.py and requirements.txt files.
# The script assumes that you have Python 3 and pip installed on your system.
# The script is designed to be run in a Unix-like environment (Linux or macOS).
# If you're using Windows, you may need to adjust the script accordingly.
# The script is intended to be run in a terminal or command line interface.
# It creates a virtual environment named "my_env", activates it, installs the required packages, and runs the GUI application.