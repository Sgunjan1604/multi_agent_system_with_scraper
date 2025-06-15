# agents/spacex_agent.py

import requests

def get_next_launch():
    url = "https://api.spacexdata.com/v4/launches/next"
    res = requests.get(url)
    if res.status_code != 200:
        return {}

    data = res.json()
    return {
        "name": data.get("name", "Unknown Mission"),
        "date_utc": data.get("date_utc", "Unknown Date"),
        "location": "Cape Canaveral"  # optional for weather
    }
