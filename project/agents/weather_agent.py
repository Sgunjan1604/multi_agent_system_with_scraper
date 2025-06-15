# agents/weather_agent.py

import requests, os
from dotenv import load_dotenv

load_dotenv()

def get_weather(launch_data):
    # Try to get a real location from launch data
    location = launch_data.get("location", "Cape Canaveral")

    print(f"[Weather Agent] Fetching weather for location: {location}")

    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return "Missing API key"

    # API call
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    res = requests.get(url)

    if res.status_code != 200:
        print(f"[Weather Agent] Error: {res.status_code}, {res.text}")
        return "Weather: Unknown"

    data = res.json()

    # Parse key info
    temp = data["main"]["temp"]
    weather = data["weather"][0]["main"]
    description = data["weather"][0]["description"]

    return f"{weather} ({description}), {temp}°C"
