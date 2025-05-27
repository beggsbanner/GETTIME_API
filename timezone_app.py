import tkinter as tk
import requests

# API URL (Make sure your Flask server is running)
API_URL = "http://localhost:5000/timezones"

# Function to fetch live time from API
def update_time():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            data = response.json()
            time_str = "\n".join([f"{zone}: {time}" for zone, time in data.items()])
        else:
            time_str = "Error fetching timezones"
    except Exception as e:
        time_str = f"Error: {str(e)}"

    label.config(text=time_str)
    root.after(1000, update_time)  # Refresh every second

# Create the Tkinter app window
root = tk.Tk()
root.title("Time Zone Widget")
root.geometry("400x250")

# Create label to display time zones
label = tk.Label(root, font=("Arial", 14), justify="left")
label.pack(pady=20)

# Start updating time from API
update_time()

# Run the Tkinter event loop
root.mainloop()
# This script creates a simple Tkinter GUI that fetches and displays the current time in various US time zones
# using the Flask API created in GETTIMEAPI.py.
# It uses the requests library to make HTTP GET requests to the API and updates the GUI every second.
# Ensure you have the requests library installed:
# pip install requests
# Ensure you have the Tkinter library installed (usually included with Python installations)