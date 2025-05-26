import tkinter as tk
import requests

API_URL = "http://127.0.0.1:5000/timezones"

def fetch_timezones():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            time_data = response.json()
            result_text.set("\n".join(f"{tz}: {time}" for tz, time in time_data.items()))
        else:
            result_text.set("Error fetching data")
    except Exception as e:
        result_text.set(f"Error: {e}")

# Create the main window
root = tk.Tk()
root.geometry("800x600")  # Adjust size as needed
root.title("US Time Zones")

# Add a button to fetch data
fetch_button = tk.Button(root, text="Get Time", command=fetch_timezones)
fetch_button.pack()

# Add a label to display results
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left")
result_label.pack()

# Start the GUI event loop
root.mainloop()
# This script creates a simple GUI application using Tkinter that fetches and displays the current time in various US time zones.
# It uses the requests library to make HTTP requests to the Flask API created in GETTIMEAPI.py.
# The GUI consists of a button to fetch the time and a label to display the results.
# The application runs a local server on port 5000, so make sure to run the Flask app before running this GUI script.
# The GUI will display the current time in the specified US time zones when the button is clicked.
# Make sure to have the Flask app running before executing this GUI script.
