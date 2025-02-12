import requests
from dotenv import load_dotenv
import os

load_dotenv()

Weather_api = os.getenv("WEATHER_API_KEY")

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()

        # Extract relevant information
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        city_name = weather_data["name"]
        #print((f"Weather in {city_name}: {description.capitalize()}, Temperature: {temperature}°C"))
        return (f"Weather in {city_name}: {description.capitalize()}, Temperature: {temperature}°C")
    else:
        return (f"Failed to fetch weather. Status code: {response.status_code}")

