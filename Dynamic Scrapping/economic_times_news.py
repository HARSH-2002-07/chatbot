from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://economictimes.indiatimes.com/news/economy")

articles = driver.find_elements(By.TAG_NAME, "h3")  # Update tag if needed

print("Latest News from Economic Times:")
for article in articles[:10]:  # Fetch top 10 articles
    print(article.text.strip())

driver.quit()
