# GETTIME API

GETTIME API is a Flask-based API with an integrated Tkinter GUI that allows users to retrieve real-time time zone data across the United States. This project provides current time information through an intuitive desktop interface.

## 📝 Overview
This project combines a robust Flask backend with a user-friendly Tkinter GUI to deliver live time zone data. Whether you want to integrate it into another project or use it as a standalone desktop app, GETTIME API makes it simple and accessible.

## 🚀 Installation

### 1. Clone the Repository
Open your terminal and run:
```bash
git clone <repository-url>
cd GETTIME_API

2. Set Up the Virtual Environment
Create and activate a virtual environment if you haven't already):
python3 -m venv my_env
source my_env/bin/activate

3. Install Dependencies
Install the required packages:
pip install -r requirements.txt

▶️ Usage
Run the Flask API
Start the API with:
python GETTIMEAPI.py

Run the Tkinter GUI
Launch the GUI with:
python GETTIMEAPIGUI.py

⚡ Features
Real-Time Data: Retrieve current time for various US time zones.

User-Friendly Interface: Easy-to-use Tkinter GUI.

Flexible Integration: Flask-based API suitable for integration with other applications.

📌 Contributing
If you'd like to contribute to GETTIME API, follow these steps:

Fork the Repository: Use the GitHub interface to fork.

Create a New Branch:
git checkout -b feature-branch
Make Your Changes: Commit with a descriptive message:
git commit -m "Added new feature"
Then, open a pull request on GitHub.

📜 License
This project is licensed under the MIT License 
 Copyright (c) 2025 [beggsbanner]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

📧 Contact
For questions or suggestions, please contact: beggsbanner@gmail.com

## 📌 How to Install & Create a Desktop Shortcut (Linux)

### 🏗️ Step 1: Run the Application
After generating the executable, navigate to the `dist/` folder and run:
```bash
./timezone_app

Step 2: Create a Desktop Shortcut
Open a terminal and create a .desktop file:
nano ~/.local/share/applications/timezone_app.desktop

[Desktop Entry]
Name=Time Zone Widget
Exec=/home/YOUR_USERNAME/GETTIME_API/dist/timezone_app
Icon=/home/YOUR_USERNAME/GETTIME_API/icon.png
Type=Application
Terminal=false
Categories=Utility;
(Replace YOUR_USERNAME with your actual Linux username.)

3. Make it executable:
chmod +x ~/.local/share/applications/timezone_app.desktop

4. Copy it to the Desktop for easy access:
cp ~/.local/share/applications/timezone_app.desktop ~/Desktop/

Right-click the shortcut → "Allow Launching" (if needed).
✅ Done!
