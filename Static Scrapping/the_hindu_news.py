import requests
from bs4 import BeautifulSoup

url = "https://www.thehindu.com/news/national/"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

articles = soup.find_all("h3", class_="title")

print("Latest News from The Hindu:")
for article in articles[:10]:  # Fetch top 10 articles
    title = article.text.strip()
    link = article.a["href"] if article.a else "No link available"
    print(f"{title} - {link}")
