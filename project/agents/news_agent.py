# agents/news_agent.py

import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

def run(context, user_goal):
    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        return "News API key missing"

    query = "SpaceX" if "spacex" in user_goal.lower() else "technology"
    from_date = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')

    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={query}&"
        f"from={from_date}&"
        f"sortBy=publishedAt&"
        f"language=en&"
        f"apiKey={api_key}"
    )

    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"[News Agent] Error: {response.status_code}, {response.text}")
            return "News: Failed to fetch"

        data = response.json()
        articles = data.get("articles", [])
        if not articles:
            return "No recent news found."

        top_headlines = [f"- {a['title']}" for a in articles[:3]]
        return "\n".join(top_headlines)

    except Exception as e:
        print(f"[News Agent] Exception: {e}")
        return "News: Error occurred while fetching"
