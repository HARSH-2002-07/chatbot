import requests
from dotenv import load_dotenv
import os

load_dotenv()

News_api = os.getenv("GLOBAL_NEWS_GOOGLE_API_KEY")

def get_latest_news(api_key):
    base_url = "https://newsapi.org/v2/top-headlines"
    params = {
        "apiKey": api_key,
        "country": "in",  # Replace with your country code, e.g., 'us' for the United States
        "category": "technology",
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        news_data = response.json()
        print(news_data)
        articles = news_data.get("articles", [])
        News = []
        print("test")
        print(articles)

        for index, article in enumerate(articles, start=1):
            print("test2")
            title = article.get("title", "No Title")
            description = article.get("description", "No Description")
            News.append(title)
            print(f"{index}. {title}\n   {description}\n")
        return News
    else:
        return "failed to get latest news"

  # Replace with your News API key
print(get_latest_news(News_api))

