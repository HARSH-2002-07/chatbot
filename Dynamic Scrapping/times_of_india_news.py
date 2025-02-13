from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in the background
options.add_argument("--ignore-certificate-errors")
options.add_argument("--allow-running-insecure-content")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36")


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://timesofindia.indiatimes.com/india")

# Inspect and find a more appropriate class or use XPATH/CSS_SELECTOR
articles = driver.find_elements(By.CSS_SELECTOR, "h2 a")  # Adjust the selector as needed

print("Latest News from Times of India:")
for article in articles[:10]:  # Fetch top 10 articles
    title = article.text.strip()
    link = article.get_attribute("href")
    print(f"{title} - {link}")

driver.quit()
