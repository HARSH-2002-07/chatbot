import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("INDIAN_NEWS_GOOGLE_API_KEY")

def get_google_news(api_key, query):
    url = f"https://www.googleapis.com/customsearch/v1"
    params = {
        "key": api_key,
        "cx": "84bff9dc0fb2e41e2",  # Replace with your Search Engine ID
        "q": query,
        "siteSearch": "timesofindia.indiatimes.com",  # Restrict to Indian site
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        results = response.json().get("items", [])
        for result in results:
            print(f"Title: {result['title']}\nLink: {result['link']}\n")
    else:
        print("Failed to fetch results.")

get_google_news(api_key, "addverb trending news")