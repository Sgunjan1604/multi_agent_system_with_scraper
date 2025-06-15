import requests
from bs4 import BeautifulSoup

def scrape_hacker_news_headlines():
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    headlines = []
    for tag in soup.select(".titleline a"):  # ✅ updated selector
        headlines.append(tag.text.strip())

    return headlines[:5]  # Return top 5 headlines
