import requests
import pandas as pd
import datetime
import logging
import os
from config import API_KEY, CITY, BASE_URL

# Setup logging
logging.basicConfig(filename='logs/pipeline.log', level=logging.INFO)

def fetch_weather():
    params = {'q': CITY, 'appid': API_KEY, 'units': 'metric'}
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()

        weather = {
            'city': CITY,
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description'],
            'wind_speed': data['wind']['speed'],
            'timestamp': datetime.datetime.now()
        }

        df = pd.DataFrame([weather])

        # Ensure 'data' directory exists
        os.makedirs("data", exist_ok=True)
        output_file = "data/weather_log.csv"

        # Check if file exists before deciding to write header
        write_header = not os.path.isfile(output_file)
        df.to_csv(output_file, mode='a', index=False, header=write_header)

        logging.info(f"✅ Weather data logged at {weather['timestamp']}")

    except Exception as e:
        logging.error(f"❌ Error fetching weather: {str(e)}")

if __name__ == "__main__":
    fetch_weather()
