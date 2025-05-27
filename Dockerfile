# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Set environment variables (optional)
ENV FLASK_APP=GETTIMEAPI.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the Flask port
EXPOSE 5000

# Start Flask using Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "GETTIMEAPI:app"]
